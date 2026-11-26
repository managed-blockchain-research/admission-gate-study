#!/usr/bin/env python3.11
"""11aab job-start self-check (exit 0 = pass, 5 = refused). Block table: M (Besu G1 512 MB, mixed burst), Z (Besu ZGC 512 MB), N (Nethermind 2048 MiB), TS (sustained attack A0=0 A1=240), TP (short pulse A0=60 A1=90).
Checks: hardware class node-05, manifest pins of the frozen service/detector/workload files (except launcher-family files), 11aab pins (launcher, wrapper, self-check, mixed modules, sticky service), build (Besu r6 jars + JDK 21.0.12, or NM dll sha256), exports, token grammar, arm/seed/burst/profile per block, single-use run ids."""
import os, re, sys, json, hashlib, subprocess, glob
P = '<path>'
def sha(p):
    try: return hashlib.sha256(open(p, 'rb').read()).hexdigest()
    except Exception: return None
errs = []; info = []
def refuse(m): errs.append(m)
M = json.load(open(P + '/calibration_manifest.json')); rc = M['raac']; hw = M['registered_hardware']; L = json.load(open(P + '/acc/ACC_PINS_11aab.json'))
host = subprocess.run(['hostname', '-s'], stdout=subprocess.PIPE, universal_newlines=True).stdout.strip()
mdl = subprocess.run(['bash', '-c', "lscpu | grep 'Model name' | sed 's/.*: *//'"], stdout=subprocess.PIPE, universal_newlines=True).stdout.strip()
ncpu = int(subprocess.run(['nproc', '--all'], stdout=subprocess.PIPE, universal_newlines=True).stdout.strip())
if not re.match(r'^cpu(0[1-9]|10)$', host) or hw['model_substr'] not in mdl or ncpu != hw['ncpu']: refuse('R2 hardware: %s %s %s' % (host, mdl, ncpu))
else: info.append('hardware ok %s %s' % (host, ncpu))
SKIP = {'run_raac_11az.sbatch', 'run_raac_checked.sbatch', 'stage1_run_dispatch.sh', 'stage1_run_hook_raac.sh'}
for f, h in rc['pins'].items():
    if os.path.basename(f) in SKIP: continue
    if sha(f) != h: refuse('R3 pinned file %s differs' % os.path.basename(f))
for f, h in L['files'].items():
    if sha(f) != h: refuse('R3 11aab file %s differs' % f.split('/acc/')[-1])
env = os.environ; blk = env.get('BLOCK', ''); B = L['blocks'].get(blk)
if not B: refuse('R6 unknown BLOCK %r' % blk); B = None
arm, burst, rid = env.get('RAAC_ARM'), env.get('RAAC_BURST'), env.get('RUN_ID', '')
for k, v in rc['profile'].items():
    exp = v
    if B and k == 'A0': exp = str(B['A0'])
    if B and k == 'A1': exp = str(B['A1'])
    if env.get(k) != exp: refuse('R3 %s=%r differs from the block profile (%s)' % (k, env.get(k), exp))
toks = [t for t in env.get('TOKENS', '').split('+') if t]
if len(toks) != 1: refuse('R6 exactly one token required')
if B:
    if B['kind'] == 'besu':
        if env.get('PROBE') != '1': refuse('R3 PROBE must be 1 (Besu)')
        bh = env.get('BESU_HOME', '')
        if bh != P + '/besu-25.1.0-[other study]-r6': refuse('R3 BESU_HOME must be the r6 build')
        else:
            es = glob.glob(bh + '/lib/besu-eth-26.10-develop-*.jar'); ms = glob.glob(bh + '/lib/besu-26.10-develop-*.jar')
            if not es or sha(es[0]) not in M['allowed_eth_jar_sha256']: refuse('R3 besu-eth jar not in the registered build list')
            if not ms or sha(ms[0]) != L['besu_main_jar_sha256']: refuse('R3 besu main jar sha differs')
        try:
            jv = subprocess.run(['<path>', '-version'], stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).stderr
            if '21.0.12' not in jv.split('\n')[0]: refuse('R3 JDK %r' % jv.split('\n')[0])
        except Exception as e: refuse('R3 JDK: %s' % e)
    else:
        if env.get('PROBE') != '0': refuse('R3 PROBE must be 0 (Nethermind)')
        nb = env.get('NM_BIN') or './impl/nm/bin'
        if nb != L['nm_bin'] or sha(nb + '/nethermind.dll') != L['nm_dll_sha256'] or sha(nb + '/Nethermind.TxPool.dll') != L['nm_txpool_sha256']: refuse('R3 NM build differs from the pins')
        if env.get('BESU_HOME'): refuse('R3 BESU_HOME must not be set for Nethermind')
    m = re.match(B['token_re'], toks[0] if toks else '')
    if not m: refuse('R6 token grammar for block %s' % blk)
    else:
        seed = int(m.group(m.lastindex)); smoke = env.get('SMOKE') == '1'
        if smoke and seed != B['smoke_seed']: refuse('R7 smoke seed %d != %d' % (seed, B['smoke_seed']))
        if not smoke and not (B['seeds'][0] <= seed <= B['seeds'][1]): refuse('R7 seed %d outside %s' % (seed, B['seeds']))
    if arm not in B['arms']: refuse('R6 arm %r not registered for block %s' % (arm, blk))
    if burst != B['burst']: refuse('R6 burst %r != %r' % (burst, B['burst']))
    if not re.match(r'^TWONODE_%s_[A-Za-z0-9_]+$' % blk, rid): refuse('R6 RUN_ID grammar')
for ek,bk in (('FAIL_CLOSED','fc'),('SVC_STOP_AT','ss'),('SVC_STOP_S','sd'),('LAT_T','lt'),('ATTACK_BYTES','ab'),('ATTACK_STAGGER','stg'),('ATTACK_EVERY_M_END','mend'),('ATTACK_STEP_AT','stp'),('ARRIVAL_WINDOW','aw'),('MULTI','mn'),('ATTACK_VIA_B','avb')):
    if B and env.get(ek, '') != B.get(bk, ''): refuse('R3 %s %r != block value %r' % (ek, env.get(ek, ''), B.get(bk, '')))
if B and env.get('ATTACK_EVERY_M', '') != B.get('em', ''): refuse('R3 ATTACK_EVERY_M %r != block value %r' % (env.get('ATTACK_EVERY_M', ''), B.get('em', '')))
if B and env.get('REAL_MIX', '') != B.get('rm', ''): refuse('R3 REAL_MIX %r != block value %r' % (env.get('REAL_MIX', ''), B.get('rm', '')))
if B and env.get('ATTACK_FRACTION', '') != B.get('af', ''): refuse('R3 ATTACK_FRACTION %r != block value %r' % (env.get('ATTACK_FRACTION', ''), B.get('af', '')))
if os.path.exists('%s/runs/%s' % (P, rid)) and any(f for f in os.listdir('%s/runs/%s' % (P, rid)) if f not in ('job_start_selfcheck.txt',)): refuse('R6 run dir already has content (run ids are single-use)')
if env.get('GOVENV') or env.get('GOV_MODE'): refuse('R4 GOVENV/GOV_MODE must not be set')
if not os.path.exists('/usr/bin/python3.11'): refuse('R3 python3.11 missing')
if errs:
    print('SELFCHECK REFUSED (%d):' % len(errs)); [print('  - ' + e) for e in errs]; sys.exit(5)
for i in info: print('SELFCHECK info: ' + i)
print('SELFCHECK ok: %s arm=%s block=%s' % (rid, arm, blk)); sys.exit(0)
