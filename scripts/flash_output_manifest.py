#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path

def sha256(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
 return h.hexdigest()

def main():
 p=argparse.ArgumentParser(); p.add_argument('run_dir'); p.add_argument('--out',default='run_manifest.json'); a=p.parse_args()
 d=Path(a.run_dir).resolve(); files=[]
 for f in sorted(d.iterdir()):
  if f.is_file() and ('hdf5' in f.name.lower() or f.suffix in {'.par','.log'}):
   files.append({'name':f.name,'bytes':f.stat().st_size,'sha256':sha256(f)})
 manifest={'schema_version':'0.1','run_dir':str(d),'files':files}
 for candidate in ['flash.par','setup_call','setup_command.txt']:
  q=d/candidate
  if q.exists(): manifest[candidate]=q.read_text(errors='replace')
 (d/a.out).write_text(json.dumps(manifest,indent=2)+'\n')
 print(d/a.out)
if __name__=='__main__': main()
