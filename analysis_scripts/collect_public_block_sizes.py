import json,sys,time,urllib.request,random
URL="https://ethereum-rpc.publicnode.com"
def rpc(m,p):
    for i in range(5):
        try:
            r=urllib.request.Request(URL,json.dumps({"jsonrpc":"2.0","method":m,"params":p,"id":1}).encode(),{"content-type":"application/json","user-agent":"trace-study"})
            return json.load(urllib.request.urlopen(r,timeout=30))["result"]
        except Exception as e: time.sleep(1+i)
    return None
head=int(rpc("eth_blockNumber",[]),16)
random.seed(20261120)
# 240 blocks spread uniformly over the last ~90 days (7200 blocks/day)
span=90*7200
nums=sorted(random.sample(range(head-span,head-100),240))
out=open("blocks_sample.jsonl","w")
for n in nums:
    b=rpc("eth_getBlockByNumber",[hex(n),True])
    if not b: continue
    out.write(json.dumps({"n":n,"ts":int(b["timestamp"],16),"gasUsed":int(b["gasUsed"],16),
      "tx":[(int(t["gas"],16),(len(t["input"])-2)//2,int(t.get("gasPrice","0x0"),16)) for t in b["transactions"]]})+"\n")
    time.sleep(0.15)
print("head",head,"blocks",len(nums))
