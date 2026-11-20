"""detlib: shared pieces of the RAAC2 detector pipeline (feature extraction identical to ml_model.py, record loading, role/seed separation checks, hashing,
scoring, intervals). Python >= 3.8 with numpy/pandas/scikit-learn/joblib (login-node python 3.11; NOT the 3.6 node python)."""
import gzip, hashlib, json, math, os

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL_FEATURES = ["vcr_log", "economic_density_log", "resource_intensity", "gas_price", "gas_limit", "bytecode_size"]
INPUT_FIELDS = ["gas_price", "gas_limit", "wei_value", "bytecode_size", "opcode_count"]
BENIGN_LABELS = ("benign", "lookalike")
ROLES = ("train", "calibration", "holdout")


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def extract_features(df):
    """Same formulas as ~/diss_impl/raac/ml_model.py TransactionModel._extract_features (checked by tests)."""
    d = pd.DataFrame(index=df.index)
    wei = df["wei_value"].astype(float)
    d["vcr_log"] = np.log1p(wei) / (np.log1p(df["opcode_count"].astype(float)) + 1)
    d["economic_density_log"] = np.log1p(wei) / (np.log1p(df["gas_limit"].astype(float)) + 1)
    d["resource_intensity"] = (df["gas_limit"].astype(float) * df["bytecode_size"].astype(float)) / 1e9
    d["gas_price"] = df["gas_price"].astype(float)
    d["gas_limit"] = df["gas_limit"].astype(float)
    d["bytecode_size"] = df["bytecode_size"].astype(float)
    return d[MODEL_FEATURES]


def normalise_score(decision):
    """Service score: 0.5 - 4*decision_function, clipped to [0,1] (ml_model.predict_score)."""
    return np.clip(0.5 - 4.0 * np.asarray(decision, dtype=float), 0.0, 1.0)


def load_collection_manifest(path):
    """collection_manifest.json: {"runs": {run_id: {"role", "label_set", "client", "heap", "seed", "workload", ...}}, "seeds": {...optional}}.
    Validates: role in ROLES; seeds of different roles disjoint (a seed is the workload seed AND the identity of the unit of independence)."""
    cm = json.load(open(path))
    runs = cm["runs"]
    by_role = {r: set() for r in ROLES}
    for rid, m in runs.items():
        if m["role"] not in ROLES:
            raise ValueError("run %s: unknown role %r" % (rid, m["role"]))
        if "seed" not in m:
            raise ValueError("run %s: seed missing" % rid)
        by_role[m["role"]].add((m.get("workload", "v5"), m["seed"]))
    for a in ROLES:
        for b in ROLES:
            if a < b and by_role[a] & by_role[b]:
                raise ValueError("seed overlap between roles %s and %s: %s" % (a, b, sorted(by_role[a] & by_role[b])))
    return cm


def read_records(paths):
    """Read workload label JSONL (type 'tx', header lines skipped) or flat feature JSONL ({run_id,label,features,...}).
    Returns list of dicts: run_id, label, cls, features(dict), plus optional source/subtype/worker/n/seed."""
    out = []
    for p in paths:
        hdr = {}
        with (gzip.open(p, "rt") if p.endswith(".gz") else open(p)) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                j = json.loads(line)
                if j.get("type") == "header":
                    hdr = {k: j.get(k) for k in ("lookalike_profile", "client", "heap_mb", "burst_kind") if k in j}
                    continue
                for k, v in hdr.items():
                    j.setdefault(k, v)
                if "features" not in j or "label" not in j:
                    raise ValueError("%s: record without features/label" % p)
                j.setdefault("cls", j.get("class", "?"))
                j["_file"] = os.path.basename(p)
                out.append(j)
    return out


def subtype_of(r):
    """look-alike profile 'hard' is a diagnostic subtype (never trained/calibrated on)."""
    if r["label"] != "lookalike":
        return r["label"]
    return "lookalike_hard" if r.get("lookalike_profile") == "hard" or r.get("subtype") == "hard" else "lookalike"


def records_frame(recs):
    rows = []
    for r in recs:
        f = r["features"]
        row = {k: f[k] for k in INPUT_FIELDS}
        row.update(run_id=r["run_id"], label=r["label"], subtype=subtype_of(r), cls=r.get("cls", "?"), worker=r.get("worker", -1), n=r.get("n", -1),
                   source=r.get("source", "v5"))
        rows.append(row)
    return pd.DataFrame(rows)


def check_roles(recs, cm, allowed_role, allowed_labels, what):
    """Every record must belong to a run that the collection manifest assigned to allowed_role, and carry an allowed label."""
    runs = cm["runs"]
    bad_run = sorted({r["run_id"] for r in recs if r["run_id"] not in runs})
    if bad_run:
        raise ValueError("%s: runs not in collection manifest: %s" % (what, bad_run[:5]))
    wrong = sorted({r["run_id"] for r in recs if runs[r["run_id"]]["role"] != allowed_role})
    if wrong:
        raise ValueError("%s: runs with role != %s: %s" % (what, allowed_role, wrong[:5]))
    badl = sorted({r["label"] for r in recs if r["label"] not in allowed_labels})
    if badl:
        raise ValueError("%s: labels %s not allowed (allowed %s)" % (what, badl, list(allowed_labels)))


def dataset_sha256(recs):
    """Canonical hash of a record set: sorted (run_id, worker, n, label, cls, features) lines."""
    lines = []
    for r in recs:
        f = r["features"]
        lines.append(json.dumps([r["run_id"], r.get("worker", -1), r.get("n", -1), r["label"], subtype_of(r), r.get("cls", "?")] + [f[k] for k in INPUT_FIELDS],
                                separators=(",", ":")))
    lines.sort()
    return sha256_bytes("\n".join(lines).encode()), len(lines)


def tree_fingerprint(model):
    h = hashlib.sha256()
    for est in model.estimators_:
        t = est.tree_
        for a in (t.feature, t.threshold, t.children_left, t.children_right, t.n_node_samples):
            h.update(np.ascontiguousarray(a).tobytes())
    h.update(np.float64(model.offset_).tobytes())
    return h.hexdigest()


def score_frame(model, df):
    return normalise_score(model.decision_function(extract_features(df)))


def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def load_manifest(path):
    return json.load(open(path)) if os.path.exists(path) else {}


def save_manifest(path, m):
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(m, f, indent=1, sort_keys=True)
    os.replace(tmp, path)


def versions():
    import sklearn, joblib, sys
    return {"python": sys.version.split()[0], "numpy": np.__version__, "pandas": pd.__version__, "sklearn": sklearn.__version__, "joblib": joblib.__version__}
