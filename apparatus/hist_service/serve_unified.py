"""[11pp HISTORY-BUDGET COPY (adds mode hist_budget: per-sender heavy-byte bucket whose rate grows with the sender history)] [11mm SENDER-BUDGET COPY (adds mode sender_budget: per-sender heavy-byte token bucket) of the 11kk budget copy; modes budget/rule_size/... unchanged] [11kk BUDGET COPY (adds mode budget: heavy-byte token bucket) of the 11jj sticky copy; with AI_MODE != budget and AI_HOLD_S unset identical to the frozen service] [11jj STICKY COPY: adds AI_HOLD_S (sliding-max pressure hold); with AI_HOLD_S unset/0 identical to the frozen service] Unified RAAC admission-control service for the [other study] re-run.

Copy of [internal path] (v6) with the changes required by
PREREG_UNIFIED_v1.md 1.5/1.8 and SYMMETRY_AUDIT_EXTRA.md row 9.
Stdlib-only core, Python 3.6 compatible (cluster nodes run 3.6); the Isolation
Forest (ml_model.py: numpy/pandas/sklearn) is imported lazily and only for
AI_MODE=raac.

Pressure source (AI_PRESSURE_SOURCE):
  ut_file (DEFAULT)  u_t = last row, column "u_t", of the [other study] governor's
                     gov_trace.csv (AI_UT_FILE, or $GOV_TRACE_DIR/gov_trace.csv).
                     u_t = post-GC old-gen (gen2+LOH) / ENFORCED heap limit, same
                     definition on Besu and Nethermind, exported in ALL arms
                     including OFF.  FAIL-SAFE: file missing / unreadable / last
                     complete row older than AI_UT_STALE_S (3 s) -> u_t unusable,
                     pressure = 0 (accept), stale counters increment (/stats).
  gclog | rss        legacy v6 sources (Besu G1 GC-log tail / NM VmRSS delta).
                     Kept selectable, NOT default.  rss uses pgrep -f (legacy,
                     AGENTS.md rule 18 caveat); do not use in the unified study.

Arms (AI_MODE; legacy aliases in parentheses):
  raac            IsolationForest score vs FIXED AI_ATTACK_SCORE_REF; only flagged
                  tx are rejected, with probability grad(u_t). Benign never touched.
  pressure_only   (heap_only) ignores features; every tx rejected w.p. grad(u_t).
  circuit_breaker reject ALL when u_t > AI_CB_THRESHOLD (default 0.95), step.
  cpu_ramp        (dagor) ignores features and u_t; reject w.p. = CPU ramp
                  AI_DAGOR_CPU_LOW..HIGH (50..90 %) of the SUT process.
                  SUT located via /proc scan (AI_CPU_PID_FILE, else exec-time env
                  tag RUN_TAG + AI_CPU_TARGET_REGEX); never pgrep -f.
  rule_size       (rule_based) like raac but flag = bytecode_size >=
                  AI_RULE_SIZE_THRESHOLD instead of the model.

COMMON GRADUATION FUNCTION (raac, pressure_only, rule_size):
  grad(u) = clamp((u - AI_GRAD_LOW) / (AI_GRAD_HIGH - AI_GRAD_LOW), 0, 1)
  defaults LOW=0.60 (= [other study] deactivate), HIGH=0.90 (= common emergency tier).
  Memoryless (no hysteresis).  Rejection draw: reject iff rng.random() < p.
  (In v6 reject_prob == pressure after the threshold round-trip; grad() is that
  same linear ramp, now over u_t instead of RSS-delta / GC-log occupancy.)

Every decision is appended to a per-run JSONL (AI_DECISION_LOG) and counters are
written to AI_COUNTERS_FILE periodically, at SIGTERM/SIGINT and at exit
(rule R8: arm counters must move).  GET /stats returns the live counters.

Launcher requirements: `ulimit -n 65536` before starting (AGENTS.md rule 13);
start with exec-time env RUN_TAG=<id>; never `uvicorn --workers`; /predict
is computed inline (rule 6), no thread-pool dispatch.
"""
import asyncio
import atexit
import json
import math
import os
import random
import re
import signal
import sys
import threading
import time
from collections import deque
from concurrent.futures import ThreadPoolExecutor

MODES = ("raac", "pressure_only", "circuit_breaker", "cpu_ramp", "rule_size", "budget", "sender_budget", "hist_budget")
_ALIASES = {"heap_only": "pressure_only", "dagor": "cpu_ramp", "rule_based": "rule_size"}
_SKIP_ARGV0 = {"bash", "sh", "python", "python3", "python3.6", "python3.11", "ssh",
               "srun", "nohup", "setsid", "timeout", "sudo", "tee", "flock"}


def _f(env, key, default):
    return float(env.get(key, default))


class Config(object):
    """All tunables; built from an env mapping so tests can vary them."""

    def __init__(self, env=None):
        env = os.environ if env is None else env
        m = env.get("AI_MODE", "raac")
        self.mode = _ALIASES.get(m, m)
        if self.mode not in MODES:
            raise ValueError("AI_MODE=%r not in %s" % (m, MODES))
        self.mode_raw = m
        self.source = env.get("AI_PRESSURE_SOURCE", "ut_file")
        if self.source not in ("ut_file", "gclog", "rss"):
            raise ValueError("AI_PRESSURE_SOURCE=%r" % self.source)
        tdir = env.get("GOV_TRACE_DIR", "")
        self.ut_file = env.get("AI_UT_FILE", os.path.join(tdir, "gov_trace.csv") if tdir else "")
        self.ut_col = env.get("AI_UT_COLUMN", "u_t")
        self.ut_stale_s = _f(env, "AI_UT_STALE_S", "3.0")
        self.ut_poll_s = _f(env, "AI_UT_POLL_S", "0.2")
        self.grad_lo = _f(env, "AI_GRAD_LOW", "0.60")
        self.grad_hi = _f(env, "AI_GRAD_HIGH", "0.90")
        self.hold_s = _f(env, "AI_HOLD_S", "0")          # 11jj sticky-pressure copy: u_t used for the decision = max of u_t over the last hold_s seconds (0 = off, identical to the frozen service)
        self.budget_tau = _f(env, "AI_BUDGET_TAU", "65604")       # 11kk budget mode: calldata bytes above this are 'heavy' (post-hoc threshold, disclosed)
        self.budget_rate = _f(env, "AI_BUDGET_RATE", "250000")    # heavy-byte refill rate, bytes per second (R0)
        self.budget_cap = _f(env, "AI_BUDGET_CAP", "200000")      # bucket capacity in bytes (about two heavy transactions)
        self.budget_adapt = _f(env, "AI_BUDGET_ADAPT", "0")
        # 11pp hist_budget mode: per-sender heavy-byte bucket whose refill rate depends on the sender history h (ordinary, non-heavy transactions the gate has seen from that sender): r(h) = r0 + (rmax - r0) * min(1, h / H)
        self.hist_r0 = _f(env, "AI_HIST_R0", "10000"); self.hist_rmax = _f(env, "AI_HIST_RMAX", "400000"); self.hist_h = _f(env, "AI_HIST_H", "100")
        # 11mm sender_budget mode: one heavy-byte token bucket PER SENDER (sender id = the 4 hex digits after 0x of tx_hash = the worker index = one signing account); AI_BUDGET_RATE / AI_BUDGET_CAP / AI_BUDGET_TAU apply per sender       # 1 = refill rate R(u) = R0 * (1 - 0.75 * grad(u_t)) (pressure-adaptive), 0 = fixed R0
        if self.grad_hi <= self.grad_lo:
            raise ValueError("AI_GRAD_HIGH must be > AI_GRAD_LOW")
        self.cb_threshold = _f(env, "AI_CB_THRESHOLD", "0.95")
        self.attack_ref = _f(env, "AI_ATTACK_SCORE_REF", "0.80")
        self.rule_size = _f(env, "AI_RULE_SIZE_THRESHOLD", "20000")
        self.thr_base = _f(env, "AI_THRESHOLD_BASE", "0.95")
        self.thr_min = _f(env, "AI_THRESHOLD_MIN", "0.70")   # only for legacy response field
        self.cpu_lo = _f(env, "AI_DAGOR_CPU_LOW", "50.0")
        self.cpu_hi = _f(env, "AI_DAGOR_CPU_HIGH", "90.0")
        self.cpu_poll_s = _f(env, "AI_CPU_POLL_S", "2.0")
        self.cpu_pid_file = env.get("AI_CPU_PID_FILE", "")
        self.cpu_run_id = env.get("AI_CPU_RUN_ID", env.get("RUN_TAG", ""))
        self.cpu_regex = env.get(
            "AI_CPU_TARGET_REGEX",
            r"org\.hyperledger\.besu\.Besu|hyperledger\.besu\.Besu|nethermind\.dll|Nethermind\.Runner")
        self.cpu_normalize = env.get("AI_CPU_NORMALIZE", "none")  # none (v6 semantics: % of ONE core) | cpus
        self.seed = env.get("AI_SEED", "")
        self.host = env.get("AI_HOST", "127.0.0.1")
        self.port = int(env.get("AI_PORT", "8000"))
        self.decision_log = env.get("AI_DECISION_LOG", "")
        self.counters_file = env.get("AI_COUNTERS_FILE", "")
        # legacy source knobs (v6 names kept)
        self.gc_log = env.get("AI_GC_LOG_PATH", "")
        self.gc_lo = _f(env, "AI_GC_OCCU_LOW", "0.30")
        self.gc_hi = _f(env, "AI_GC_OCCU_HIGH", "0.70")
        self.gc_window = _f(env, "AI_GC_WINDOW_SEC", "30.0")
        self.gc_poll = _f(env, "AI_GC_POLL_INTERVAL", "2.0")
        self.rss_pattern = env.get("AI_TARGET_PROCESS_PATTERN", "nethermind.dll")
        self.rss_lo = _f(env, "AI_DELTA_LOW_MB", "100.0")
        self.rss_hi = _f(env, "AI_DELTA_HIGH_MB", "350.0")
        self.rss_abs_lo = _f(env, "AI_RSS_ABS_LOW_MB", "2800.0")
        self.rss_abs_hi = _f(env, "AI_RSS_ABS_HIGH_MB", "3600.0")
        self.rss_stable_delta = _f(env, "AI_RSS_STABLE_DELTA_MB", "15.0")
        self.rss_stable_polls = int(env.get("AI_RSS_STABLE_POLLS", "6"))


def grad(u, lo, hi):
    """Common graduation function (see module docstring). Memoryless ramp."""
    if u is None or u != u:
        return 0.0
    if u <= lo:
        return 0.0
    if u >= hi:
        return 1.0
    return (u - lo) / (hi - lo)


# ---------------------------------------------------------------- u_t file reader
class UtFileReader(object):
    """Reads only the LAST complete row of gov_trace.csv (tail of <=16 KiB)."""
    TAIL = 16384

    def __init__(self, path, col="u_t"):
        self.path = path
        self.col = col
        self._hdr = None
        self._hdr_key = None

    def _header(self, f, st):
        key = (st.st_ino, st.st_dev)
        if self._hdr is not None and self._hdr_key == key:
            return self._hdr
        f.seek(0)
        head = f.read(8192).decode("utf-8", "replace")
        for line in head.split("\n")[:-1]:       # complete lines only
            if line and not line.startswith("#"):
                cols = line.strip().split(",")
                self._hdr = cols
                self._hdr_key = key
                return cols
        return None

    def read(self):
        """-> (state, u_t, ts_ms); state in ok|missing|empty|noheader|norow|error."""
        try:
            with open(self.path, "rb") as f:
                st = os.fstat(f.fileno())
                if st.st_size == 0:
                    return ("empty", None, None)
                hdr = self._header(f, st)
                if not hdr or self.col not in hdr or "ts_ms" not in hdr:
                    return ("noheader", None, None)
                iu, it, n = hdr.index(self.col), hdr.index("ts_ms"), len(hdr)
                start = max(0, st.st_size - self.TAIL)
                f.seek(start)
                data = f.read().decode("utf-8", "replace")
        except (IOError, OSError) as e:
            if getattr(e, "errno", None) == 2:
                return ("missing", None, None)
            return ("error", None, None)
        lines = data.split("\n")
        lines.pop()                      # text after the last "\n" is a partial/empty line
        if start > 0 and lines:
            lines.pop(0)                 # first line may be cut by the tail window
        for line in reversed(lines):
            if not line or line.startswith("#"):
                continue
            p = line.split(",")
            if len(p) != n:
                continue
            try:
                u, ts = float(p[iu]), float(p[it])
            except ValueError:
                continue
            if u != u or math.isinf(u):
                continue
            return ("ok", u, ts)
        return ("norow", None, None)


class PressureState(object):
    """u_t snapshot shared by monitor and handler; freshness evaluated at decision time."""

    def __init__(self, cfg):
        self.cfg = cfg
        self.state = "init"
        self.u = None
        self.ts_ms = None
        self.legacy_p = 0.0              # legacy sources provide pressure directly
        self.stale_polls = 0
        self.stale_decisions = 0
        self.stale_episodes = 0
        self._was_stale = False
        self._last_warn = 0.0
        self.max_u = 0.0
        self.reason = "init"

    def update(self, state, u, ts_ms):
        self.state, self.u, self.ts_ms = state, u, ts_ms
        if state == "ok" and u is not None and u > self.max_u:
            self.max_u = u
        if not self.fresh():
            self.stale_polls += 1
            if not self._was_stale:
                self.stale_episodes += 1
            self._was_stale = True
            self._warn()
        else:
            self._was_stale = False

    def fresh(self, now_ms=None):
        if self.state != "ok" or self.ts_ms is None:
            self.reason = self.state
            return False
        now_ms = time.time() * 1000.0 if now_ms is None else now_ms
        if abs(now_ms - self.ts_ms) > self.cfg.ut_stale_s * 1000.0:
            self.reason = "stale_row(age_s=%.1f)" % ((now_ms - self.ts_ms) / 1000.0)
            return False
        self.reason = "ok"
        return True

    def get(self, now_ms=None):
        """-> (u_t_or_None, is_stale). Stale => u_t None (pressure 0)."""
        if self.fresh(now_ms):
            return self.u, False
        self.stale_decisions += 1
        return None, True

    def _warn(self):
        now = time.time()
        if now - self._last_warn >= 60.0:
            self._last_warn = now
            print("[ut_file] STALE/UNAVAILABLE: %s file=%s -> pressure=0 "
                  "(stale_polls=%d episodes=%d)" % (self.reason, self.cfg.ut_file,
                                                    self.stale_polls, self.stale_episodes), flush=True)


# ---------------------------------------------------------------- decisions
class Counters(object):
    def __init__(self):
        self.total = self.accept = self.reject = 0
        self.flagged = self.rejected_flagged = self.rejected_unflagged = 0
        self.pressure_nonzero = 0        # decisions taken with p > 0
        self.stale = 0
        self.max_p = 0.0
        self.t0 = time.time()

    def add(self, d):
        self.total += 1
        if d["action"] == "reject":
            self.reject += 1
            if d.get("flagged") is True:
                self.rejected_flagged += 1
            else:
                self.rejected_unflagged += 1
        else:
            self.accept += 1
        if d.get("flagged"):
            self.flagged += 1
        if d["p"] > 0:
            self.pressure_nonzero += 1
        if d["p"] > self.max_p:
            self.max_p = d["p"]
        if d.get("stale"):
            self.stale += 1

    def as_dict(self):
        return dict(total=self.total, accept=self.accept, reject=self.reject,
                    flagged=self.flagged, rejected_flagged=self.rejected_flagged,
                    rejected_unflagged=self.rejected_unflagged,
                    decisions_with_p_gt_0=self.pressure_nonzero,
                    decisions_while_stale=self.stale, max_reject_prob=round(self.max_p, 6),
                    uptime_s=round(time.time() - self.t0, 1))


def decide(cfg, features, u_t, stale, rng, score_fn=None, cpu_pressure=0.0):
    """Pure decision function. u_t is None when stale/unavailable (=> pressure 0).
    Returns dict(mode,u_t,stale,score,flagged,p,action)."""
    mode = cfg.mode
    score = None
    flagged = None
    if mode == "circuit_breaker":
        p = 1.0 if (u_t is not None and u_t > cfg.cb_threshold) else 0.0
    elif mode == "cpu_ramp":
        p = cpu_pressure
    elif mode == "pressure_only":
        p = grad(u_t, cfg.grad_lo, cfg.grad_hi)
    else:                                  # raac | rule_size
        if mode == "raac":
            score = float(score_fn(features))      # model may return numpy scalars
            flagged = bool(score >= cfg.attack_ref)
        else:
            bs = features.get("bytecode_size", 0) or 0
            score = 1.0 if bs >= cfg.rule_size else 0.0
            flagged = bool(bs >= cfg.rule_size)
        p = grad(u_t, cfg.grad_lo, cfg.grad_hi) if flagged else 0.0
    action = "reject" if rng.random() < p else "accept"
    return dict(mode=mode, u_t=u_t, stale=bool(stale), score=score, flagged=flagged,
                p=p, action=action)


# ---------------------------------------------------------------- cpu_ramp target discovery
def scan_target_pids(regex, run_id, proc="/proc", self_pid=None):
    """/proc scan (never pgrep -f). Candidates: cmdline matches regex, argv0 not a
    wrapper, and (if run_id) exec-time environ has RUN_TAG=<run_id>."""
    rx = re.compile(regex)
    tag = ("RUN_TAG=%s" % run_id).encode() if run_id else None
    self_pid = os.getpid() if self_pid is None else self_pid
    out = []
    try:
        names = os.listdir(proc)
    except OSError:
        return out
    for n in names:
        if not n.isdigit() or int(n) == self_pid:
            continue
        try:
            with open("%s/%s/cmdline" % (proc, n), "rb") as f:
                raw = f.read()
            argv = [a.decode("utf-8", "replace") for a in raw.split(b"\0") if a]
            if not argv or os.path.basename(argv[0]) in _SKIP_ARGV0:
                continue
            if not rx.search(" ".join(argv)):
                continue
            if tag is not None:
                with open("%s/%s/environ" % (proc, n), "rb") as f:
                    if tag not in f.read().split(b"\0"):
                        continue
            out.append(int(n))
        except (IOError, OSError):
            continue
    return out


def read_cpu_ticks(pid, proc="/proc"):
    with open("%s/%s/stat" % (proc, pid)) as f:
        rest = f.read().rsplit(")", 1)[-1].split()
    return float(rest[11]) + float(rest[12])


class CpuRamp(object):
    def __init__(self, cfg):
        self.cfg = cfg
        self.pressure = 0.0
        self.pid = None
        self.cpu_pct = None
        self.target_missing_polls = 0
        self.polls = 0
        self._prev = None
        self.clk = os.sysconf("SC_CLK_TCK") if hasattr(os, "sysconf") else 100
        self.div = 1.0
        if cfg.cpu_normalize == "cpus" and hasattr(os, "sched_getaffinity"):
            self.div = float(len(os.sched_getaffinity(0)))

    def find_pid(self):
        c = self.cfg
        if c.cpu_pid_file:
            try:
                with open(c.cpu_pid_file) as f:
                    pid = int(f.read().strip().split()[0])
                if os.path.exists("/proc/%d" % pid):
                    return pid
            except (IOError, OSError, ValueError, IndexError):
                pass
            return None
        pids = scan_target_pids(c.cpu_regex, c.cpu_run_id)
        if not pids:
            return None
        best, bt = None, -1.0
        for p in pids:
            try:
                t = read_cpu_ticks(p)
            except (IOError, OSError, IndexError, ValueError):
                continue
            if t > bt:
                best, bt = p, t
        return best

    def poll(self):
        self.polls += 1
        pid = self.find_pid()
        if pid is None:
            self.target_missing_polls += 1
            self.pid = None
            self._prev = None
            self.pressure = 0.0
            return
        if pid != self.pid:
            self.pid = pid
            self._prev = None
            print("[cpu_ramp] target pid=%d" % pid, flush=True)
        try:
            ticks = read_cpu_ticks(pid)
        except (IOError, OSError, IndexError, ValueError):
            self.pressure = 0.0
            return
        now = time.monotonic()
        if self._prev is not None:
            dt = now - self._prev[1]
            if dt > 0:
                self.cpu_pct = 100.0 * ((ticks - self._prev[0]) / self.clk) / dt / self.div
                self.pressure = grad(self.cpu_pct, self.cfg.cpu_lo, self.cfg.cpu_hi)
        self._prev = (ticks, now)


# ---------------------------------------------------------------- legacy sources (v6, unchanged logic)
_GC_EVENT_RE = re.compile(r'\[(\d+\.\d+)s\].*?(\d+)M->(\d+)M\((\d+)M\)')


class LegacySources(object):
    """v6 GC-log tail and NM RSS-delta monitors, folded into one object that
    yields pressure in [0,1] directly (no u_t)."""

    def __init__(self, cfg):
        self.cfg = cfg
        self.pressure = 0.0
        self._pos = 0
        self._win = deque()
        self._pid = ""
        self._t_pid = 0.0
        self._base = 0.0
        self._grace_last = 0.0
        self._prev = 0.0
        self._stable = 0

    def poll_gclog(self):
        c = self.cfg
        if not c.gc_log or not os.path.exists(c.gc_log):
            return
        with open(c.gc_log, "r", errors="replace") as f:
            f.seek(self._pos)
            chunk = f.read(1 << 20)
            self._pos = f.tell()
        for m in _GC_EVENT_RE.finditer(chunk):
            ha, hm = int(m.group(3)), int(m.group(4))
            if hm > 0:
                self._win.append((float(m.group(1)), ha, hm))
        if not self._win:
            return
        cutoff = self._win[-1][0] - c.gc_window
        while self._win and self._win[0][0] < cutoff:
            self._win.popleft()
        mo = max(a / float(b) for (_, a, b) in self._win)
        self.pressure = grad(mo, c.gc_lo, c.gc_hi)

    def poll_rss(self):
        c = self.cfg
        pids = scan_target_pids(c.rss_pattern, c.cpu_run_id)   # /proc scan instead of pgrep -f
        if not pids:
            return
        pid = str(pids[0])
        if pid != self._pid:
            self._pid, self._t_pid = pid, time.monotonic()
            self._base = self._grace_last = self._prev = 0.0
            self._stable = 0
        rss = 0.0
        with open("/proc/%s/status" % pid) as f:
            for line in f:
                if line.startswith("VmRSS:"):
                    rss = int(line.split()[1]) / 1024.0
        if rss <= 0:
            return
        if time.monotonic() - self._t_pid < 90.0:
            self._grace_last, self._prev, self._stable, self.pressure = rss, rss, 0, 0.0
            return
        if self._base <= 0:
            self._base = self._grace_last
        if self._prev > 0 and abs(rss - self._prev) <= c.rss_stable_delta:
            self._stable += 1
        else:
            self._stable = 0
        if self._stable >= c.rss_stable_polls and abs(rss - self._base) > 1.0:
            self._base = rss
        self._prev = rss
        dp = grad(rss - self._base, c.rss_lo, c.rss_hi)
        ap = grad(rss, c.rss_abs_lo, c.rss_abs_hi)
        self.pressure = max(dp, ap)


# ---------------------------------------------------------------- service
class Service(object):
    def __init__(self, cfg, model=None):
        self.cfg = cfg
        self.ps = PressureState(cfg)
        self.reader = UtFileReader(cfg.ut_file, cfg.ut_col) if cfg.ut_file else None
        self.cpu = CpuRamp(cfg) if cfg.mode == "cpu_ramp" else None
        self.legacy = LegacySources(cfg) if cfg.source != "ut_file" else None
        self.counters = Counters()
        self.rng = random.Random(int(cfg.seed)) if cfg.seed else random.Random()
        self._hold = deque()                              # 11jj: monotonic deque (time, u) for the sliding maximum
        self._tok = float(cfg.budget_cap); self._tok_t = None       # 11kk heavy-byte token bucket
        self._stok = {}                                              # 11mm per-sender buckets: sender -> [tokens, last time]
        self._hist = {}                                              # 11pp per-sender state: sender -> [tokens, last time, h]
        self._model = model
        self._buf = []
        self._log = None
        self._cf_last = 0.0
        if cfg.decision_log:
            self._log = open(cfg.decision_log, "a")
            self._log.write(json.dumps({"type": "header", "ts": time.time(), "mode": cfg.mode,
                                        "mode_raw": cfg.mode_raw, "source": cfg.source,
                                        "ut_file": cfg.ut_file, "grad": [cfg.grad_lo, cfg.grad_hi],
                                        "cb_threshold": cfg.cb_threshold, "attack_ref": cfg.attack_ref,
                                        "stale_s": cfg.ut_stale_s,
                                        "run_id": os.environ.get("RUN_TAG", "")}) + "\n")
        if cfg.mode == "circuit_breaker" and cfg.source != "ut_file":
            raise ValueError("circuit_breaker requires AI_PRESSURE_SOURCE=ut_file (needs u_t)")
        if cfg.mode == "cpu_ramp" and not (cfg.cpu_pid_file or cfg.cpu_run_id):
            raise ValueError("cpu_ramp needs AI_CPU_PID_FILE or RUN_TAG/AI_CPU_RUN_ID "
                             "(no pgrep -f fallback)")
        if cfg.source == "ut_file" and cfg.mode != "cpu_ramp" and not cfg.ut_file:
            raise ValueError("AI_PRESSURE_SOURCE=ut_file needs AI_UT_FILE or GOV_TRACE_DIR")

    def score(self, features):
        if self._model is None:
            from ml_model import TransactionModel      # lazy: needs numpy/pandas/sklearn
            self._model = TransactionModel()
        return self._model.predict_score(features)

    def handle(self, features, now_ms=None):
        """Inline decision for one /predict request."""
        c = self.cfg
        if c.mode == "hist_budget":                  # 11pp: history-weighted per-sender heavy-byte bucket; small transactions always pass and add to the sender history; no pressure signal read
            _now = time.time(); _txh = str(features.get("tx_hash", "")); _snd = _txh[2:6]
            _bytes = float(features.get("bytecode_size", 0) or 0); heavy = _bytes > c.budget_tau
            _b = self._hist.get(_snd)
            if _b is None: _b = self._hist[_snd] = [float(c.budget_cap), _now, 0]
            action = "accept"
            if heavy:
                _r = c.hist_r0 + (c.hist_rmax - c.hist_r0) * min(1.0, _b[2] / c.hist_h)
                _b[0] = min(float(c.budget_cap), _b[0] + _r * (_now - _b[1])); _b[1] = _now
                if _b[0] >= _bytes: _b[0] -= _bytes
                else: action = "reject"
            else:
                _b[2] += 1
            d = dict(mode="hist_budget", u_t=None, stale=True, score=None, flagged=bool(heavy), p=(1.0 if action == "reject" else 0.0), action=action)
            d["tx_hash"] = _txh
            d["ts"] = round(time.time(), 3)
            self.counters.add(d)
            if self._log is not None:
                self._buf.append(json.dumps({"type": "decision", "ts": d["ts"], "mode": d["mode"], "u_t": None, "stale": True, "score": None, "flagged": d["flagged"], "p": d["p"], "action": d["action"], "tx": d["tx_hash"]}))
                if len(self._buf) >= 2000: self.flush()
            return d
        if c.mode == "sender_budget":                # 11mm: heavy-byte token bucket per sender; small transactions always pass; no pressure signal read
            _now = time.time(); _txh = str(features.get("tx_hash", "")); _snd = _txh[2:6]
            _b = self._stok.get(_snd)
            if _b is None: _b = self._stok[_snd] = [float(c.budget_cap), _now]
            _b[0] = min(float(c.budget_cap), _b[0] + c.budget_rate * (_now - _b[1])); _b[1] = _now
            _bytes = float(features.get("bytecode_size", 0) or 0); heavy = _bytes > c.budget_tau
            action = "accept"
            if heavy:
                if _b[0] >= _bytes: _b[0] -= _bytes
                else: action = "reject"
            d = dict(mode="sender_budget", u_t=None, stale=True, score=None, flagged=bool(heavy), p=(1.0 if action == "reject" else 0.0), action=action)
            d["tx_hash"] = _txh
            d["ts"] = round(time.time(), 3)
            self.counters.add(d)
            if self._log is not None:
                self._buf.append(json.dumps({"type": "decision", "ts": d["ts"], "mode": d["mode"], "u_t": None, "stale": True, "score": None, "flagged": d["flagged"], "p": d["p"], "action": d["action"], "tx": d["tx_hash"]}))
                if len(self._buf) >= 2000: self.flush()
            return d
        if c.mode == "budget":                       # 11kk: heavy-byte token bucket; small transactions always pass; reads u_t only for the adaptive refill
            u = None; stale = True
            if c.source == "ut_file" and self.reader:
                u, stale = self.ps.get(now_ms)
            _now = time.time()
            if self._tok_t is None: self._tok_t = _now
            _rate = c.budget_rate
            if c.budget_adapt > 0 and u is not None: _rate = c.budget_rate * (1.0 - 0.75 * grad(u, c.grad_lo, c.grad_hi))
            self._tok = min(float(c.budget_cap), self._tok + _rate * (_now - self._tok_t)); self._tok_t = _now
            _bytes = float(features.get("bytecode_size", 0) or 0); heavy = _bytes > c.budget_tau
            action = "accept"
            if heavy:
                if self._tok >= _bytes: self._tok -= _bytes
                else: action = "reject"
            d = dict(mode="budget", u_t=u, stale=bool(stale), score=None, flagged=bool(heavy), p=(1.0 if action == "reject" else 0.0), action=action)
            d["tx_hash"] = features.get("tx_hash", "")
            d["ts"] = round(time.time(), 3)
            self.counters.add(d)
            if self._log is not None:
                self._buf.append(json.dumps({"type": "decision", "ts": d["ts"], "mode": d["mode"], "u_t": d["u_t"], "stale": d["stale"], "score": None, "flagged": d["flagged"], "p": d["p"], "action": d["action"], "tx": d["tx_hash"]}))
                if len(self._buf) >= 2000: self.flush()
            return d
        if c.source == "ut_file":
            u, stale = self.ps.get(now_ms) if self.reader else (None, True)
            if c.hold_s > 0 and u is not None:                # 11jj hysteresis / pressure hold: sliding maximum over the last hold_s seconds
                _t = time.time(); _dq = self._hold
                while _dq and _dq[-1][1] <= u: _dq.pop()
                _dq.append((_t, u))
                while _dq[0][0] < _t - c.hold_s: _dq.popleft()
                u = _dq[0][1]
            d = decide(c, features, u, stale, self.rng, self.score, self.cpu.pressure if self.cpu else 0.0)
        else:                                   # legacy: pressure is given directly
            u, stale = None, False
            d = decide(c, features, None, False, self.rng, self.score, self.cpu.pressure if self.cpu else 0.0)
            if c.mode in ("raac", "pressure_only", "rule_size"):
                p = self.legacy.pressure if (c.mode == "pressure_only" or d["flagged"]) else 0.0
                d["p"] = p
                d["action"] = "reject" if self.rng.random() < p else "accept"
        d["tx_hash"] = features.get("tx_hash", "")
        d["ts"] = round(time.time(), 3)
        self.counters.add(d)
        if self._log is not None:
            self._buf.append(json.dumps(
                {"type": "decision", "ts": d["ts"], "mode": d["mode"], "u_t": d["u_t"],
                 "stale": d["stale"], "score": d["score"], "flagged": d["flagged"],
                 "p": round(d["p"], 6), "action": d["action"], "tx": d["tx_hash"]}))
            if len(self._buf) >= 2000:
                self.flush()
        return d

    def stats(self):
        s = {"mode": self.cfg.mode, "source": self.cfg.source, "counters": self.counters.as_dict(),
             "u_t_last": self.ps.u, "u_t_max_seen": round(self.ps.max_u, 6),
             "u_t_state": self.ps.state, "u_t_reason": self.ps.reason,
             "stale_polls": self.ps.stale_polls, "stale_episodes": self.ps.stale_episodes,
             "stale_decisions": self.ps.stale_decisions}
        if self.cpu:
            s["cpu_ramp"] = {"pid": self.cpu.pid, "cpu_pct": self.cpu.cpu_pct,
                             "pressure": self.cpu.pressure, "polls": self.cpu.polls,
                             "target_missing_polls": self.cpu.target_missing_polls}
        if self.legacy:
            s["legacy_pressure"] = self.legacy.pressure
        return s

    def flush(self):
        if self._log is not None and self._buf:
            self._log.write("\n".join(self._buf) + "\n")
            self._buf = []
            self._log.flush()
        self.write_counters()

    def write_counters(self):
        if not self.cfg.counters_file:
            return
        tmp = self.cfg.counters_file + ".tmp"
        with open(tmp, "w") as f:
            json.dump(self.stats(), f, indent=1)
        os.rename(tmp, self.cfg.counters_file)

    def finalize(self):
        self.flush()
        st = self.stats()
        if self._log is not None:
            self._log.write(json.dumps(dict(st, type="counters_final", ts=time.time())) + "\n")
            self._log.close()
            self._log = None
        c = self.counters
        if c.reject == 0 and self.ps.max_u > self.cfg.grad_lo and self.cfg.mode != "cpu_ramp":
            print("[R8-WARNING] mode=%s saw u_t max %.3f > %.2f but rejected nothing: arm was inert"
                  % (self.cfg.mode, self.ps.max_u, self.cfg.grad_lo), flush=True)
        if c.total and self.ps.stale_decisions > 0.2 * c.total:
            print("[R8-WARNING] %d/%d decisions made while u_t stale" % (self.ps.stale_decisions, c.total),
                  flush=True)
        print("[final] " + json.dumps(st), flush=True)
        self.write_counters()


# ---------------------------------------------------------------- HTTP
_RECV_TIMEOUT = 2.0
_MON = ThreadPoolExecutor(max_workers=2)       # monitors only; /predict never uses it


async def _resp(writer, code, obj):
    body = json.dumps(obj).encode()
    writer.write(("HTTP/1.1 %s\r\nContent-Type: application/json\r\nConnection: close\r\n"
                  "Content-Length: %d\r\n\r\n" % (code, len(body))).encode() + body)
    await writer.drain()


def make_handler(svc):
    cfg = svc.cfg

    async def handle_client(reader, writer):
        try:
            try:
                raw = await asyncio.wait_for(reader.readuntil(b"\r\n\r\n"), timeout=_RECV_TIMEOUT)
            except (asyncio.TimeoutError, asyncio.IncompleteReadError):
                return
            head = raw[:-4].decode(errors="replace")
            parts = head.split("\r\n")[0].split(" ")
            if len(parts) < 2:
                return
            method, path = parts[0], parts[1]
            if method == "GET" and path.startswith("/stats"):
                await _resp(writer, "200 OK", svc.stats())
                return
            if method == "GET":
                p = svc.legacy.pressure if svc.legacy else grad(svc.ps.u, cfg.grad_lo, cfg.grad_hi)
                await _resp(writer, "200 OK", {"status": "ok", "mode": cfg.mode, "gc_pressure": round(p, 4),
                                               "u_t": svc.ps.u, "u_t_state": svc.ps.state})
                return
            if method == "POST" and path == "/predict":
                n = 0
                for line in head.split("\r\n")[1:]:
                    if line.lower().startswith("content-length:"):
                        try:
                            n = int(line.split(":", 1)[1].strip())
                        except ValueError:
                            pass
                if n <= 0 or n > 65536:
                    await _resp(writer, "400 Bad Request", {})
                    return
                try:
                    body = await asyncio.wait_for(reader.readexactly(n), timeout=_RECV_TIMEOUT)
                except (asyncio.TimeoutError, asyncio.IncompleteReadError):
                    return
                try:
                    data = json.loads(body.decode())
                except ValueError:
                    await _resp(writer, "400 Bad Request", {})
                    return
                d = svc.handle(data)                       # INLINE, no executor (AGENTS.md rule 6)
                p = d["p"]
                await _resp(writer, "200 OK", {
                    "tx_hash": d["tx_hash"],
                    "anomaly_score": (round(d["score"], 4) if d["score"] is not None else None),
                    "dynamic_threshold": round(cfg.thr_base - p * (cfg.thr_base - cfg.thr_min), 4),
                    "gc_pressure": round(p, 4), "reject_prob": round(p, 4),
                    "u_t": d["u_t"], "stale": d["stale"],
                    "dagor_cpu_pressure": (round(svc.cpu.pressure, 4) if svc.cpu else None),
                    "action": d["action"], "mode": d["mode"]})
                return
            await _resp(writer, "404 Not Found", {})
        except Exception:
            pass
        finally:
            try:
                writer.close()
                if hasattr(writer, "wait_closed"):
                    await writer.wait_closed()
            except Exception:
                pass
    return handle_client


async def _ut_monitor(svc):
    loop = asyncio.get_event_loop()
    while True:
        try:
            st = await loop.run_in_executor(_MON, svc.reader.read)
        except Exception:
            st = ("error", None, None)
        svc.ps.update(*st)
        await asyncio.sleep(svc.cfg.ut_poll_s)


async def _legacy_monitor(svc):
    loop = asyncio.get_event_loop()
    fn = svc.legacy.poll_gclog if svc.cfg.source == "gclog" else svc.legacy.poll_rss
    while True:
        try:
            await loop.run_in_executor(_MON, fn)
        except Exception:
            pass
        await asyncio.sleep(svc.cfg.gc_poll)


async def _cpu_monitor(svc):
    loop = asyncio.get_event_loop()
    while True:
        try:
            await loop.run_in_executor(_MON, svc.cpu.poll)
        except Exception:
            pass
        await asyncio.sleep(svc.cfg.cpu_poll_s)


async def _flusher(svc):
    while True:
        await asyncio.sleep(1.0)
        try:
            svc.flush()
        except Exception:
            pass


async def amain(svc, stop_evt):
    cfg = svc.cfg
    server = await asyncio.start_server(make_handler(svc), cfg.host, cfg.port, limit=65536, backlog=4096)
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(_flusher(svc))]
    if cfg.source == "ut_file" and svc.reader:
        tasks.append(loop.create_task(_ut_monitor(svc)))
    elif cfg.source != "ut_file":
        tasks.append(loop.create_task(_legacy_monitor(svc)))
    if svc.cpu:
        tasks.append(loop.create_task(_cpu_monitor(svc)))
    print("Serving on %s:%d serve_unified mode=%s (raw=%s) source=%s ut_file=%s grad=[%.2f,%.2f] "
          "cb=%.2f attack_ref=%.2f stale_s=%.1f log=%s" % (
              cfg.host, cfg.port, cfg.mode, cfg.mode_raw, cfg.source, cfg.ut_file, cfg.grad_lo,
              cfg.grad_hi, cfg.cb_threshold, cfg.attack_ref, cfg.ut_stale_s, cfg.decision_log), flush=True)
    await stop_evt.wait()
    server.close()
    for t in tasks:
        t.cancel()


def main():
    cfg = Config()
    svc = Service(cfg)
    if cfg.mode == "raac":
        svc.score({"gas_price": 50, "gas_limit": 21000, "wei_value": 10 ** 18, "bytecode_size": 0,
                   "opcode_count": 10})                   # train + warm before serving
    atexit.register(lambda: svc._log is not None and svc.finalize())
    loop = asyncio.get_event_loop()
    stop_evt = asyncio.Event()

    def _stop():
        stop_evt.set()
    for s in (signal.SIGTERM, signal.SIGINT):
        loop.add_signal_handler(s, _stop)
    try:
        loop.run_until_complete(amain(svc, stop_evt))
    finally:
        svc.finalize()


if __name__ == "__main__":
    main()
