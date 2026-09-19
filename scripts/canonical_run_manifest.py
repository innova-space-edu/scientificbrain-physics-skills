#!/usr/bin/env python3
import argparse,json,platform,sys,uuid
from datetime import datetime,timezone
def main():
 p=argparse.ArgumentParser(); p.add_argument("--solver",required=True); p.add_argument("--model",required=True)
 p.add_argument("--version",required=True); p.add_argument("--geometry",required=True); p.add_argument("--dimension",type=int,choices=[1,2,3],required=True)
 p.add_argument("--out",required=True); p.add_argument("--seed",type=int)
 a=p.parse_args()
 d={"schema_version":"0.2","run_id":str(uuid.uuid4()),"created_utc":datetime.now(timezone.utc).isoformat(),
    "solver":a.solver,"model":a.model,"solver_version":a.version,"geometry":a.geometry,"dimension":a.dimension,
    "seed":a.seed,"host_python":sys.version.split()[0],"platform":platform.platform(),"parameters":{},"artifacts":[],"validation":{}}
 open(a.out,"w",encoding="utf-8").write(json.dumps(d,indent=2)+"\n"); print(a.out)
if __name__=="__main__": main()
