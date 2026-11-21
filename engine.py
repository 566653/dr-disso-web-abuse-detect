"""Offline defensive event analysis. Standard library only."""
import argparse, hashlib, json, pathlib, sys, datetime
RULES = json.loads((pathlib.Path(__file__).parent / "rules.json").read_text(encoding="utf-8"))
def analyze(records):
    if not isinstance(records,list): raise ValueError("Input must be a JSON array")
    findings=[]
    for index,record in enumerate(records):
        if not isinstance(record,dict): raise ValueError("Each record must be an object")
        for rule in RULES:
            if record.get(rule["field"]) == rule["equals"]:
                findings.append({"record_index":index,"record_id":str(record.get("id",index)),"rule":rule["id"],"severity":rule["score"],"reason":rule["reason"]})
    return {"schema_version":"1.0","records_analyzed":len(records),"findings":findings,"max_risk":max((x["severity"] for x in findings),default=0),"disclaimer":"Indicators are leads, not proof of a crime or identity."}
def main():
    parser=argparse.ArgumentParser(description="Offline defensive cybercrime investigation")
    parser.add_argument("input",help="JSON array of authorized/synthetic observations")
    parser.add_argument("--output",help="Optional JSON report path")
    args=parser.parse_args()
    raw=pathlib.Path(args.input).read_bytes()
    report=analyze(json.loads(raw))
    report["source_sha256"]=hashlib.sha256(raw).hexdigest()
    report["generated_utc"]=datetime.datetime.now(datetime.timezone.utc).isoformat()
    result=json.dumps(report,ensure_ascii=False,indent=2)
    if args.output: pathlib.Path(args.output).write_text(result,encoding="utf-8")
    print(result)
if __name__=="__main__": main()
