"""ml_model for 11uu: drop-in for TransactionModel (predict_score(features_dict)) that returns the attack probability of a supervised gradient-boosting classifier (artifact sup_gb.joblib, trained by train_supervised.py on benign 'train' records and 'calibration' attack records; look-alikes never trained on). With AI_MODE=raac and AI_ATTACK_SCORE_REF=0.5 a request is flagged when the probability is at least 0.5; the rest of the decision is unchanged."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import joblib, pandas as pd
import detlib as D

class TransactionModel:
    def __init__(self):
        man = json.load(open(os.path.join(HERE, 'sup_manifest.json')))
        art = os.path.join(HERE, man['artifact'])
        if D.sha256_file(art) != man['artifact_sha256']: raise RuntimeError('supervised artifact sha256 mismatch')
        import sklearn
        if sklearn.__version__ != man['sklearn']: raise RuntimeError('sklearn %s != trained with %s' % (sklearn.__version__, man['sklearn']))
        self.model = joblib.load(art); self._cache = {}
        print('supervised detector loaded: sha256 %s' % man['artifact_sha256'][:12], flush=True)

    def predict_score(self, features_dict):
        key = tuple(features_dict.get(k, 0) for k in D.INPUT_FIELDS)
        if key in self._cache: return self._cache[key]
        df = pd.DataFrame([{k: features_dict.get(k, 0) for k in D.INPUT_FIELDS}])
        s = float(self.model.predict_proba(D.extract_features(df))[0, 1]); self._cache[key] = s
        return s
