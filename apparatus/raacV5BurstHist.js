// 11jj MIXED-BURST COPY of raacV5Burst.js: adds burstKind 'mixed' (effKind per burst worker); behaviour for attack|lookalike|none is unchanged.
'use strict';
// raacV5Burst.js (RAAC2, PREREG 11o): workload v5 (constant offered gas, price independent of class; stateBloatPhase0v5.js is REQUIRED, not copied, so the
// benign stream cannot drift) + RAAC admission call per tx + a 120 s burst window from 10% of workers that is either
//   burstKind='attack'    : 96 KB (98,304-byte payload) PayloadSink.submit transactions, identical on the wire to the v5 burst class A, or
//   burstKind='lookalike' : BENIGN large-calldata look-alike (same size, rate, workers and window; see feature_spec.json "lookalike"), or
//   burstKind='none'      : no burst (benign-only load).
// The two kinds are never mixed in one run. Every attempt is labelled (attack | benign | lookalike) in a per-worker JSONL together with the features sent to the
// AI service, the service answer and the submit outcome. The label is NEVER sent to the service.
//
// Client protocol kept from mixedAttackLOHRaacBurst.js: POST {AI}/predict JSON with the features, 2 s timeout, FAIL-OPEN (any error/timeout/garbled answer => accept;
// now recorded as ai.status != 'ok'), reject => the tx is not sent. Self-pacing on ATTEMPTS (a rejected tx never reaches sendRequests, so Caliper's controller cannot pace
// it), per-worker attempt cap = ceil(1.05 * tps/worker * roundDurationSeconds), the attempt slot is claimed synchronously before the first await (AGENTS item 10).
// Deviation from the old module: the semaphore bounds concurrent AI POSTs only (maxInflightAi, default 8), NOT the send: a send waits for confirmation, and under v5's
// intended backlog a semaphore held across it would serialise the load (5 / confirmation latency per worker) and change the offered load; the send is bounded by the v5
// per-submit guard (40 s) and the attempt cap instead.
//
// round arguments (all optional unless stated): meanPayloadKb, seed, numContracts, contractPrefix, payloadSinkId, attackFraction (0.1), attackStartS, attackEndS,
//   attackPayloadBytes (98304), submitTimeoutMs (40000), tierStatsDir, burstKind ('attack'), lookalikeProfile ('rollup'|'hard'), aiUrl (env RAAC_AI_URL; 'off' = no service
//   call, features are still logged), aiTimeoutMs (2000), maxInflightAi (8), targetTps (env RAAC_TARGET_TPS or 100; must equal the yaml fixed-rate tps), roundDurationSeconds,
//   selfPace (true), labelDir (env RAAC_LABEL_DIR; required to write labels), runId, client, heapMb, defaultGasLimit (feature_spec), featureSpec (path), expectFeatureSpecSha,
//   v5Module (path, default ./stateBloatPhase0v5.js next to this file).

const { WorkloadModuleBase } = require('@hyperledger/caliper-core');
const http = require('http');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { signLegacy } = require('./rawsign.js');

const sha256File = (p) => crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

class Semaphore {
    constructor(max) { this.max = max; this.count = 0; this.queue = []; }
    async acquire() { if (this.count < this.max) { this.count++; return; } await new Promise((r) => this.queue.push(r)); this.count++; }
    release() { this.count--; const n = this.queue.shift(); if (n) n(); }
}

function mulberry32(a) {
    return function () {
        a |= 0; a = (a + 0x6D2B79F5) | 0;
        let t = Math.imul(a ^ (a >>> 15), 1 | a);
        t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
        return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
}

// ---- feature derivation (pure; unit-tested; must match feature_spec.json) ----
const ceil32 = (n) => Math.ceil(n / 32) * 32;
function submitCalldataLen(payloadBytes) { return 4 + 32 + 32 + ceil32(payloadBytes); }   // selector + offset + length + padded data
const BLOAT_CALLDATA_LEN = 4 + 32 + 32;
function featuresFor(spec, d) {
    // d: {cls:'SL'|'SH'|'M'|'L'|'A'|'LA', k, payloadBytes, gasPrice, gasLimit}
    const om = spec.opcode_model;
    let opcode, sstore, bytes;
    if (d.cls === 'SL' || d.cls === 'SH') { const k = d.cls === 'SL' ? 2 : d.k; opcode = om.bloat_base + om.bloat_per_slot * k; sstore = spec.sstore_model.bloat_per_slot * k; bytes = BLOAT_CALLDATA_LEN; }
    else { opcode = om.payload_base + om.payload_per_word * Math.ceil(d.payloadBytes / 32); sstore = spec.sstore_model.payload; bytes = submitCalldataLen(d.payloadBytes); }
    return { gas_price: d.gasPrice, gas_limit: d.gasLimit, wei_value: 0, bytecode_size: bytes, opcode_count: opcode, call_depth: 1, sstore_count: sstore };
}

function httpPostJson(url, body, timeoutMs) {
    // resolves {resp, status, latency_ms}; status: ok | timeout | error | bad-response. Never rejects (fail-open).
    return new Promise((resolve) => {
        const t0 = Date.now(); let done = false;
        const fin = (resp, status) => { if (done) return; done = true; clearTimeout(timer); resolve({ resp, status, latency_ms: Date.now() - t0 }); };
        let req; const timer = setTimeout(() => { try { req && req.destroy(); } catch (e) { /* ignore */ } fin({ action: 'accept' }, 'timeout'); }, timeoutMs);
        try {
            const data = JSON.stringify(body); const u = new URL(url);
            req = http.request({ hostname: u.hostname, port: u.port || 80, path: u.pathname, method: 'POST', agent: false,
                headers: { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(data), Connection: 'close' } }, (res) => {
                let raw = ''; res.on('data', (c) => { raw += c; });
                res.on('end', () => {
                    try { const j = JSON.parse(raw); if (j && (j.action === 'accept' || j.action === 'reject')) fin(j, 'ok'); else fin({ action: 'accept' }, 'bad-response'); }
                    catch (e) { fin({ action: 'accept' }, 'bad-response'); }
                });
            });
            req.on('error', () => fin({ action: 'accept' }, 'error'));
            req.write(data); req.end();
        } catch (e) { fin({ action: 'accept' }, 'error'); }
    });
}

class RaacV5BurstWorkload extends WorkloadModuleBase {
    constructor() {
        super();
        this.txIndex = 0; this.t0 = null; this.pending = new Map(); this.counts = {};
        this.stats = { S: [], SL: [], SH: [], M: [], L: [], A: [], LA: [], R: [] };
    }

    async initializeWorkloadModule(workerIndex, totalWorkers, roundIndex, roundArguments, sutAdapter, sutContext) {
        await super.initializeWorkloadModule(workerIndex, totalWorkers, roundIndex, roundArguments, sutAdapter, sutContext);
        const a = this.roundArguments || {};
        this.args = a;
        const v5Path = a.v5Module || path.join(__dirname, 'stateBloatPhase0v5.js');
        this.v5 = require(path.resolve(v5Path)).__test; this.v5Sha = sha256File(path.resolve(v5Path));
        const specPath = a.featureSpec || process.env.RAAC2_FEATURE_SPEC || path.join(__dirname, 'feature_spec.json');
        this.specSha = sha256File(specPath);
        if (a.expectFeatureSpecSha && a.expectFeatureSpecSha !== this.specSha) throw new Error(`feature_spec sha256 mismatch: ${this.specSha} != expected ${a.expectFeatureSpecSha}`);
        this.spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));
        this.defaultGas = Number(a.defaultGasLimit || this.spec.default_gas_limit);
        this.burstKind = a.burstKind || 'attack';
        if (!['attack', 'lookalike', 'none', 'mixed', 'split', 'hist'].includes(this.burstKind)) throw new Error('burstKind must be attack|lookalike|none|mixed|split|hist');
        this.laProfile = a.lookalikeProfile || 'rollup';
        if (!['rollup', 'hard'].includes(this.laProfile)) throw new Error('lookalikeProfile must be rollup|hard');
        const frac = Number(a.attackFraction === undefined ? 0.1 : a.attackFraction);
        this.nBurst = frac > 0 ? Math.max(1, Math.round(frac * totalWorkers)) : 0;
        this.isBurstWorker = workerIndex >= totalWorkers - this.nBurst;      // same rule as v5
        this.effKind = this.burstKind === 'mixed' ? (workerIndex === totalWorkers - 1 ? 'lookalike' : 'attack') : this.burstKind;   // 11jj: 'mixed' = burst workers 27,28 send attack, worker 29 sends benign look-alike (same window); other kinds unchanged
        this.splitStride = 1;
        if (this.burstKind === 'split' || this.burstKind === 'hist') {   // 11mm/11pp: nA attack senders + nL look-alike senders (last workers); attack senders [T-nL-nA, T-nL), look-alike senders [T-nL, T). A burst worker sends a heavy transaction on every m-th slot (n % m == 0) of the window; the other slots stay ordinary benign traffic. Totals in a 120 s window at 3.33 slots/s per worker (400 slots): attack nA*400/mA = 800 (mA = nA/2), look-alike nL*400/nL = 400.
            this.nA = Number(a.attackSenders || 2); this.nL = Number(a.lookalikeSenders || 1);
            if (!(this.nA >= 2 && this.nL >= 1 && this.nA + this.nL <= totalWorkers)) throw new Error('split: need attackSenders >= 2, lookalikeSenders >= 1, sum <= workers');
            const isLA = workerIndex >= totalWorkers - this.nL; const isA = !isLA && workerIndex >= totalWorkers - this.nL - this.nA;
            this.isBurstWorker = isLA || isA; this.effKind = isLA ? 'lookalike' : 'attack';
            this.splitStride = isLA ? this.nL : Math.max(1, Math.round(this.nA / 2));
            this.role = isLA ? 'LA' : (isA ? 'A' : 'B');
            this.histMode = this.burstKind === 'hist'; this.attackWarmS = Number(a.attackWarmS || 0); this.laFresh = !!(a.lookalikeFresh && Number(a.lookalikeFresh) > 0);   // 11pp: attack accounts send nothing outside the window except an ordinary-traffic warm-up of attackWarmS seconds before it (fresh = no history); look-alike accounts are established (ordinary traffic throughout) unless lookalikeFresh = 1
        }
        this.A0 = Number(a.attackStartS || 0); this.A1 = Number(a.attackEndS || 0);
        this.submitTimeoutMs = Number(a.submitTimeoutMs || 40000);
        this.meanKb = Number(a.meanPayloadKb || a.MEAN_PAYLOAD_KB || 16); this.heavySlots = this.v5.plan(this.meanKb).k;
        this.seed = Number(a.seed || 1);
        this.numContracts = a.numContracts || 30; this.contractPrefix = a.contractPrefix || 'SB'; this.payloadSinkId = a.payloadSinkId || 'PayloadSink';
        this.mPayload = '0x' + '11'.repeat(this.v5.M_BYTES); this.lPayload = '0x' + '22'.repeat(this.v5.L_BYTES);
        this.attackBytes = Number(a.attackPayloadBytes || 98304);
        this.attackPayload = '0x' + 'ab'.repeat(this.attackBytes);
        this.laGas = this.laProfile === 'hard' ? this.defaultGas
            : Math.ceil(1.05 * this.spec.lookalike.profiles.rollup.gross_gas_onchain_A / 1000) * 1000;
        this.laPayloads = [];
        if (this.effKind === 'lookalike' && this.isBurstWorker) {
            const pool = this.spec.lookalike.payload_pool;
            for (let i = 0; i < pool; i++) {
                const rnd = mulberry32((this.seed * 7000003 + workerIndex * 104729 + i * 15485863 + 5) >>> 0); const buf = Buffer.alloc(this.attackBytes);
                for (let j = 0; j < buf.length; j++) buf[j] = 1 + Math.floor(rnd() * 255);      // 1..255: no zero bytes => same calldata gas as the 0xab attack payload
                this.laPayloads.push('0x' + buf.toString('hex'));
            }
        }
        this.aiUrl = a.aiUrl !== undefined ? a.aiUrl : (process.env.RAAC_AI_URL || 'http://127.0.0.1:8000');
        this.aiOn = this.aiUrl && this.aiUrl !== 'off';
        this.aiTimeoutMs = Number(a.aiTimeoutMs || 2000);
        this.sem = new Semaphore(Number(a.maxInflightAi || 8));
        this.targetTps = Number(a.targetTps || process.env.RAAC_TARGET_TPS || 100);
        this.tpsPerWorker = this.targetTps / totalWorkers;
        this.selfPace = a.selfPace === undefined ? true : !!a.selfPace;
        this.noSleep = !!a.noSleep;                                   // offline regeneration only: keep the scheduled offsets, skip the waits
        const dur = Number(a.roundDurationSeconds || 0);
        this.maxAttempts = dur > 0 && this.tpsPerWorker > 0 ? Math.ceil(this.tpsPerWorker * dur * 1.05) : Infinity;
        this.statsDir = a.tierStatsDir || './tierstats';
        this.labelDir = a.labelDir || process.env.RAAC_LABEL_DIR || null;
        this.runId = a.runId || process.env.RUN_TAG || 'run';
        this.out = null;
        if (this.labelDir) {
            fs.mkdirSync(this.labelDir, { recursive: true });
            this.out = fs.createWriteStream(path.join(this.labelDir, `labels_w${workerIndex}.jsonl`), { flags: 'a' });
            this.out.write(JSON.stringify({ type: 'header', run_id: this.runId, worker: workerIndex, total_workers: totalWorkers, seed: this.seed, client: a.client || null,
                heap_mb: a.heapMb || null, mean_payload_kb: this.meanKb, burst_kind: this.burstKind, lookalike_profile: this.laProfile, burst_worker: this.isBurstWorker,
                attack_start_s: this.A0, attack_end_s: this.A1, target_tps: this.targetTps, max_attempts: this.maxAttempts === Infinity ? null : this.maxAttempts,
                ai_url: this.aiOn ? this.aiUrl : 'off', ai_timeout_ms: this.aiTimeoutMs, feature_spec_sha256: this.specSha, v5_module_sha256: this.v5Sha,
                module_sha256: sha256File(__filename), default_gas_limit: this.defaultGas, la_gas_limit: this.laGas }) + '\n');
        }
        console.log(`[RaacV5Burst] worker ${workerIndex}/${totalWorkers} burst=${this.burstKind}${this.isBurstWorker ? '(burst worker)' : ''} mean=${this.meanKb}KB ai=${this.aiOn ? this.aiUrl : 'off'}`);
    }

    _flushStats() {
        try {
            fs.mkdirSync(this.statsDir, { recursive: true });
            fs.writeFileSync(`${this.statsDir}/w${this.workerIndex}.json`, JSON.stringify({ worker: this.workerIndex, seed: this.seed, meanKb: this.meanKb, stats: this.stats }));
        } catch (e) { /* best effort */ }
    }
    _write(rec) { if (this.out) this.out.write(JSON.stringify(rec) + '\n'); }

    async submitTransaction() {
        if (this.txIndex >= this.maxAttempts) { await sleep(200); return; }
        const myIndex = this.txIndex; this.txIndex++;              // claim synchronously (AGENTS item 10)
        const n = myIndex + 1;
        if (this.t0 === null) this.t0 = Date.now();
        const schedMs = myIndex * 1000 / this.tpsPerWorker;
        if (this.histMode && this.role !== 'B') {   // 11pp: silent slots (no transaction, no label): attack accounts are fresh, look-alike accounts may be fresh
            const so = schedMs / 1000; const inWin = so >= this.A0 && so < this.A1;
            if (this.role === 'A') { const inWarm = so >= this.A0 - this.attackWarmS && so < this.A0; if (!inWin && !inWarm) return; if (inWin && (n % this.splitStride !== 0)) return; }
            else if (this.laFresh) { if (!inWin || (n % this.splitStride !== 0)) return; }
        }
        if (this.selfPace && !this.noSleep && this.tpsPerWorker > 0) { const diff = this.t0 + schedMs - Date.now(); if (diff > 0) await sleep(diff); }
        const offsetS = this.selfPace ? schedMs / 1000 : (Date.now() - this.t0) / 1000;   // scheduled offset: label stream is arm-independent
        const inBurst = this.burstKind !== 'none' && this.isBurstWorker && offsetS >= this.A0 && offsetS < this.A1 && (n % this.splitStride === 0);   // 11mm: stride 1 for every other burst kind
        const gasPrice = this.v5.gasPriceOf(this.seed, this.workerIndex, n);
        let cls, label, k = 0, payloadBytes = 0, gasLimit = this.defaultGas, req;
        if (inBurst) {
            cls = this.effKind === 'attack' ? 'A' : 'LA'; label = cls === 'A' ? 'attack' : 'lookalike'; payloadBytes = this.attackBytes;
            if (cls === 'LA') gasLimit = this.laGas;
            const pl = cls === 'A' ? this.attackPayload : this.laPayloads[n % this.laPayloads.length];
            req = { contract: this.payloadSinkId, verb: 'submit', args: [pl], readOnly: false, gasPrice, gas: gasLimit };
        } else {
            const c = this.v5.classOf(this.seed, this.workerIndex, n, this.meanKb); label = 'benign';
            if (c === 0 || c === 1) {
                cls = c === 1 ? 'SH' : 'SL'; k = c === 1 ? this.heavySlots : 2;
                req = { contract: `${this.contractPrefix}${(n - 1) % this.numContracts}`, verb: 'bloat', args: [(this.workerIndex * 1000000) + (n * k), k], readOnly: false, gasPrice, gas: gasLimit };
            } else {
                cls = c === 2 ? 'M' : 'L'; payloadBytes = c === 2 ? this.v5.M_BYTES : this.v5.L_BYTES;
                req = { contract: this.payloadSinkId, verb: 'submit', args: [c === 2 ? this.mPayload : this.lPayload], readOnly: false, gasPrice, gas: gasLimit };
            }
        }
        const features = featuresFor(this.spec, { cls, k, payloadBytes, gasPrice, gasLimit });
        const txHash = `0x${this.workerIndex.toString(16).padStart(4, '0')}${n.toString(16).padStart(8, '0')}`;
        this.counts[label] = (this.counts[label] || 0) + 1;
        const rec = { type: 'tx', run_id: this.runId, worker: this.workerIndex, n, t_sched_ms: Math.round(schedMs), t_wall_ms: Date.now() - this.t0, label, cls, seed: this.seed,
            tx_hash: txHash, features, ai: null, submit: null };
        this.pending.set(n, rec);
        let blocked = false;
        if (this.aiOn) {
            await this.sem.acquire();
            let r;
            try { r = await httpPostJson(`${this.aiUrl}/predict`, { tx_hash: txHash, ...features }, this.aiTimeoutMs); } finally { this.sem.release(); }
            const j = r.resp;
            rec.ai = { status: r.status, action: j.action, score: j.anomaly_score === undefined ? null : j.anomaly_score, reject_prob: j.reject_prob === undefined ? null : j.reject_prob,
                u_t: j.u_t === undefined ? null : j.u_t, stale: j.stale === undefined ? null : j.stale, mode: j.mode === undefined ? null : j.mode, latency_ms: r.latency_ms };
            blocked = j.action === 'reject';
        } else { rec.ai = { status: 'none', action: 'accept' }; }
        const ts = Date.now();
        const viaRaw = cls === 'LA' && this.laProfile === 'rollup';      // tight gas limit cannot be signed by Caliper 0.4.2's signer (see rawsign.js)
        if (blocked) {
            rec.submit = { outcome: 'not-sent', latency_ms: 0 };
            this.stats.R.push([Math.round(ts - this.t0), 0, 0]);
            this._write(rec); this.pending.delete(n); return;
        }
        let timer, outcome = 'ok';
        const guard = new Promise((resolve) => { timer = setTimeout(() => resolve('submit-timeout'), this.submitTimeoutMs); });
        try {
            const r = await Promise.race([Promise.resolve().then(() => (viaRaw ? this._sendRaw(req) : this.sutAdapter.sendRequests(req))).catch((e) => { rec.err = String(e && e.message || e).slice(0, 200); return 'send-error'; }), guard]);
            if (r === 'submit-timeout' || r === 'send-error') outcome = r;
            else { try { const st = Array.isArray(r) ? r[0] : r; if (st && typeof st.GetStatus === 'function' && st.GetStatus() !== 'success') outcome = 'failed'; } catch (e) { /* ignore */ } }
        } finally { clearTimeout(timer); }
        rec.submit = { outcome, latency_ms: Date.now() - ts, via: viaRaw ? 'raw' : 'connector' };
        const sr = [Math.round(ts - this.t0), Date.now() - ts, outcome === 'ok' ? 1 : 0];
        if (cls === 'SL' || cls === 'SH') { this.stats.S.push(sr); this.stats[cls].push(sr); } else this.stats[cls].push(sr);
        this._write(rec); this.pending.delete(n);
        if (n % 100 === 0) this._flushStats();
    }

    async _sendRaw(req) {
        // nonce from the connector's own claim (same sequence as its sendRequests), own signature, same web3 transport and receipt wait; mirrors the connector's nonce reset on pool rejections
        const ad = this.sutAdapter, ctx = ad.context; const info = ctx.contracts[req.contract];
        const nonce = await ad._claimNonce(ctx); if (nonce == null) throw new Error('nonce-unavailable');
        const data = info.contract.methods[req.verb](...req.args).encodeABI();
        const raw = signLegacy(ctx.fromAddressPrivateKey, { nonce, gasPrice: req.gasPrice, gas: req.gas, to: info.contract._address, data, chainId: ctx.chainId || 1337 });
        const pe = ctx.web3.eth.sendSignedTransaction(raw); try { pe.catch(() => {}); } catch (e) { /* not a promise */ }
        try { await new Promise((res, rej) => { pe.on('receipt', res).on('error', rej); }); }
        catch (err) { if (err && err.message && /FeeTooLowToCompete|nonce too low|already known|Internal error|RacePacingRejected/.test(err.message)) ctx.localNonce = null; throw err; }
        return { GetStatus: () => 'success' };
    }

    async cleanupWorkloadModule() {
        for (const rec of this.pending.values()) { if (!rec.submit) rec.submit = { outcome: 'unfinished', latency_ms: null }; this._write(rec); }
        this.pending.clear(); this._flushStats();
        if (this.out) await new Promise((r) => this.out.end(r));
        console.log(`[RaacV5Burst] worker ${this.workerIndex}: attempts=${this.txIndex} ${JSON.stringify(this.counts)}`);
    }
}

module.exports.createWorkloadModule = () => new RaacV5BurstWorkload();
module.exports.__test = { featuresFor, submitCalldataLen, BLOAT_CALLDATA_LEN, httpPostJson, mulberry32 };
