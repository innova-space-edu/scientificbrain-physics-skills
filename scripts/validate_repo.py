#!/usr/bin/env python3
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]; skills=root/'skills'; errors=[]
for d in sorted(p for p in skills.iterdir() if p.is_dir()):
 s=d/'SKILL.md'; c=d/'skill-card.md'
 if not s.exists(): errors.append(f'{d.name}: missing SKILL.md'); continue
 txt=s.read_text()
 if not txt.startswith('---\n'): errors.append(f'{d.name}: missing YAML frontmatter')
 if f'name: {d.name}' not in txt: errors.append(f'{d.name}: frontmatter name mismatch')
 if 'description:' not in txt: errors.append(f'{d.name}: missing description')
 if not c.exists(): errors.append(f'{d.name}: missing skill-card.md')
print(f'skills={len([p for p in skills.iterdir() if p.is_dir()])} errors={len(errors)}')
for e in errors: print('ERROR',e)
sys.exit(1 if errors else 0)
