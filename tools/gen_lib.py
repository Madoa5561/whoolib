import json, re, os, keyword
from collections import Counter, defaultdict

EP = json.load(open('work/cache/endpoints.json', encoding='utf-8'))
MODELS = json.load(open('work/cache/model_catalog.json', encoding='utf-8'))

PUBLIC = ('email/login', 'email/users', 'validate/', 'password/forget', 'api/token')


def ident(s):
    s = s.replace('[]', '')
    s = re.sub(r'[^0-9a-zA-Z_]+', '_', s)
    s = re.sub(r'_+', '_', s).strip('_')
    if not s:
        s = 'value'
    if s[0].isdigit():
        s = 'p_' + s
    if keyword.iskeyword(s) or s in ('None', 'True', 'False'):
        s += '_'
    return s


# ---------- model names ----------
used = Counter()
MODEL_NAME = {}
for fqcn in MODELS:
    tail = fqcn.split('.')[-1].replace('$', '_')
    tail = ident(tail)
    base = tail
    if used[base]:
        parts = fqcn.split('.')
        parent = ident(parts[-2]) if len(parts) > 1 else 'X'
        base = f'{tail}_{parent}'
    n = 2
    while used[base]:
        base = f'{tail}_{n}'
        n += 1
    used[base] += 1
    MODEL_NAME[fqcn] = base

def path_name(p):
    parts = [x for x in re.split(r'[^0-9A-Za-z]+', p) if x]
    words = []
    for x in parts:
        x = re.sub(r'(?<=[a-z0-9])(?=[A-Z])', '_', x)
        words.append(x.lower())
    return '_'.join(words)


# ---------- endpoint names ----------
names = Counter()
for e in EP:
    base = f"{e['verb'].lower()}_{path_name(e['path'])}"
    n = names[base]
    names[base] += 1
    e['name'] = base if n == 0 else f'{base}_{n + 1}'

for e in EP:
    e['auth'] = (not any(e['path'].startswith(p) for p in PUBLIC)) and e['interface'] not in ('gqa', 'bg4')
    if e['body_type']:
        e['body_model'] = MODEL_NAME.get('app.whoo.data.api.' + e['body_type']) or MODEL_NAME.get(e['body_type'])
    else:
        e['body_model'] = None
    e['response_model'] = None
    if e['response_type']:
        e['response_model'] = (MODEL_NAME.get('app.whoo.data.api.response.' + e['response_type'])
                               or MODEL_NAME.get('app.whoo.data.api.' + e['response_type'])
                               or MODEL_NAME.get(e['response_type']))

os.makedirs('whoolib', exist_ok=True)
os.makedirs('docs', exist_ok=True)

# ---------- _endpoints.py ----------
lines = ['"""Generated endpoint catalog (do not edit by hand)."""', '',
         'from dataclasses import dataclass', 'from typing import Optional', '', '',
         '@dataclass(frozen=True)', 'class Endpoint:',
         '    name: str', '    verb: str', '    path: str', '    base_url: Optional[str]',
         '    path_params: tuple', '    query_params: tuple', '    header_params: tuple',
         '    body_type: Optional[str]', '    body_model: Optional[str]',
         '    multipart: bool', '    form: tuple', '    response_type: Optional[str]',
         '    response_model: Optional[str]', '    auth: bool', '    interface: str', '', '',
         'ENDPOINTS = {']
for e in EP:
    pp = tuple((p['name'], p['arg'], p['type']) for p in e['path_params'])
    qp = tuple((p['name'], p['arg'], p['type']) for p in e['query_params'])
    hp = tuple((p['name'], p['arg'], p['type']) for p in e['header_params'])
    form = (e['form'],) if e['form'] else ()
    line = (f'    {e["name"]!r}: Endpoint({e["name"]!r}, {e["verb"]!r}, {e["path"]!r}, {e["base_url"]!r}, '
            f'{pp!r}, {qp!r}, {hp!r}, {e["body_type"]!r}, {e["body_model"]!r}, '
            f'{bool(e["multipart"])!r}, {form!r}, {e["response_type"]!r}, {e["response_model"]!r}, '
            f'{e["auth"]!r}, {e["interface"]!r}),')
    lines.append(line)
lines.append('}')
lines.append('')
lines.append('BY_NAME = ENDPOINTS')
lines.append('')
open('whoolib/_endpoints.py', 'w', encoding='utf-8').write('\n'.join(lines))

# ---------- models.py ----------
M = ['"""Generated model classes (do not edit by hand)."""', '',
     'from __future__ import annotations', '',
     'from dataclasses import dataclass, field', 'from typing import Any, ClassVar, Dict, Optional', '',
     '', 'class Model:',
     '    __json_keys__: ClassVar[tuple] = ()', '',
     '    def to_dict(self) -> dict:',
     '        out = {}',
     '        for key, attr in self.__json_keys__:',
     '            val = getattr(self, attr, None)',
     '            if val is None:',
     '                continue',
     '            if isinstance(val, Model):',
     '                val = val.to_dict()',
     '            elif isinstance(val, list):',
     '                val = [v.to_dict() if isinstance(v, Model) else v for v in val]',
     '            out[key] = val',
     '        return out', '',
     '    @classmethod',
     '    def from_dict(cls, data):',
     '        if not isinstance(data, dict):',
     '            return data',
     '        kwargs = {}',
     '        for key, attr in cls.__json_keys__:',
     '            if key in data:',
     '                kwargs[attr] = data[key]',
     '        return cls(**kwargs)', '',
     '']

for fqcn, info in MODELS.items():
    name = MODEL_NAME[fqcn]
    keys = info['keys']
    attrs = []
    pairs = []
    used_attr = set()
    for k, opt in keys:
        a = ident(k)
        while a in used_attr:
            a += '_'
        used_attr.add(a)
        attrs.append(a)
        pairs.append((k, a))
    M.append('@dataclass')
    M.append(f'class {name}(Model):')
    if not attrs:
        M.append('    pass')
    for a in attrs:
        M.append(f'    {a}: Any = None')
    kv = ', '.join(f'({k!r}, {a!r})' for k, a in pairs)
    M.append(f'    __json_keys__: ClassVar[tuple] = ({kv},)' if len(pairs) == 1 else f'    __json_keys__: ClassVar[tuple] = ({kv})')
    M.append('')
    M.append('')

M.append('MODEL_REGISTRY = {')
for fqcn, name in MODEL_NAME.items():
    M.append(f'    {fqcn!r}: {name},')
M.append('}')
M.append('')
M.append('MODEL_BY_NAME = {')
for fqcn, name in MODEL_NAME.items():
    M.append(f'    {name!r}: {name},')
M.append('}')
open('whoolib/models.py', 'w', encoding='utf-8').write('\n'.join(M))

print('generated _endpoints.py, models.py', len(EP), len(MODELS))

# ---------- docs/MODELS.md ----------
md = ['# whoo API model catalog', '',
      f'Total: **{len(MODELS)}** serializable models extracted from '
      '`kotlinx.serialization` descriptors.', '',
      '| class | JSON keys | FQCN |', '|---|---|---|']
for fqcn, info in sorted(MODELS.items(), key=lambda kv: MODEL_NAME[kv[0]]):
    keys = ', '.join(f'`{k}`' for k, _opt in info['keys'])
    md.append(f'| `{MODEL_NAME[fqcn]}` | {keys} | `{fqcn}` |')
open('docs/MODELS.md', 'w', encoding='utf-8').write('\n'.join(md) + '\n')
