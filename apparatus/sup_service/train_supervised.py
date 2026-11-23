#!/usr/bin/env python3.11
"""Train the supervised comparison detector for 11uu (offline, deterministic): gradient boosting on the six model features of the Isolation Forest, benign records of role 'train' (subsample 60,000, seed 20261123) versus attack records of role 'calibration' (all 7,200); look-alike records are never used. Writes sup_gb.joblib and sup_manifest.json (sha256, sizes, sklearn version)."""
import json,sys,os,hashlib
import numpy as np, pandas as pd, joblib, sklearn
from sklearn.ensemble import GradientBoostingClassifier
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import detlib as D
df=pd.read_csv('./impl/raac2/diag/all_scored.csv.gz')
ben=df[(df.role=='train')&(df.label=='benign')].sample(60000,random_state=20261123)
att=df[(df.role=='calibration')&(df.label=='attack')]
tr=pd.concat([ben,att])
X=D.extract_features(tr[D.INPUT_FIELDS].copy()); y=(tr.label=='attack').astype(int).values
m=GradientBoostingClassifier(n_estimators=100,max_depth=3,random_state=20261123).fit(X,y)
joblib.dump(m,H+'/sup_gb.joblib')
man={'artifact':'sup_gb.joblib','artifact_sha256':D.sha256_file(H+'/sup_gb.joblib'),'n_benign':int(len(ben)),'n_attack':int(len(att)),'sklearn':sklearn.__version__,'features':D.MODEL_FEATURES}
json.dump(man,open(H+'/sup_manifest.json','w'),indent=1); print(man)
# sanity on hold-out roles
for role in ('holdout',):
    for lab in ('attack','benign','lookalike'):
        s=df[(df.role==role)&(df.label==lab)].sample(min(20000,((df.role==role)&(df.label==lab)).sum()),random_state=1)
        p=m.predict_proba(D.extract_features(s[D.INPUT_FIELDS].copy()))[:,1]
        print(role,lab,'share flagged at 0.5: %.4f'%(p>=0.5).mean())
