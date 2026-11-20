"""ml_model_frozen: drop-in for ml_model.TransactionModel (same predict_score(features_dict) interface used by serve_unified.py) that loads the FROZEN, hash-checked
detector instead of training on synthetic data at start-up. Install as ml_model.py in a copy of the service directory (make_frozen_service_dir.sh) together with detlib.py.
Env: AI_DETECTOR_MANIFEST (path to detector_manifest.json). Refuses to start if the artifact sha256, the feature-spec sha256 or sklearn's version differ from the manifest."""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import joblib
import pandas as pd
import detlib as D


class TransactionModel:
    def __init__(self):
        mp = os.environ.get("AI_DETECTOR_MANIFEST")
        if not mp:
            raise RuntimeError("AI_DETECTOR_MANIFEST not set")
        man = json.load(open(mp)); d = os.path.dirname(os.path.abspath(mp))
        art = os.path.join(d, man["model"]["artifact"])
        if D.sha256_file(art) != man["model"]["artifact_sha256"]:
            raise RuntimeError("detector artifact sha256 mismatch")
        fs = man["feature_spec"]
        spec_path = os.environ.get("AI_FEATURE_SPEC", fs["path"])
        if D.sha256_file(spec_path) != fs["sha256"]:
            raise RuntimeError("feature spec sha256 mismatch")
        import sklearn
        if sklearn.__version__ != man["model"]["versions"]["sklearn"]:
            raise RuntimeError("sklearn %s != trained with %s" % (sklearn.__version__, man["model"]["versions"]["sklearn"]))
        self.model = joblib.load(art)
        self.manifest = man
        self._cache = {}
        print("frozen detector loaded: sha256 %s ATTACK_SCORE_REF(manifest)=%s" % (man["model"]["artifact_sha256"][:12], man.get("attack_score_ref")), flush=True)

    def predict_score(self, features_dict):
        key = tuple(features_dict.get(k, 0) for k in D.INPUT_FIELDS)
        if key in self._cache:
            return self._cache[key]
        df = pd.DataFrame([{k: features_dict.get(k, 0) for k in D.INPUT_FIELDS}])
        s = float(D.score_frame(self.model, df)[0])
        self._cache[key] = s
        return s
