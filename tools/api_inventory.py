import re, glob, json, os, collections

SRC = 'work/src/sources'
OUT = 'work/cache/api_catalog.json'

CONST = re.compile(r'static final String ([A-Z0-9_]+)\s*=\s*"([^"]*)"')


def strip_comments(s):
    s = re.sub(r'/\*.*?\*/', '', s, flags=re.S)
    return re.sub(r'//[^\n]*', '', s)


def split_params(text):
    parts, depth, cur = [], 0, []
    for ch in text:
        if ch in '<([':
            depth += 1
        elif ch in '>)]':
            depth -= 1
        if ch == ',' and depth == 0:
            parts.append(''.join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    if ''.join(cur).strip():
        parts.append(''.join(cur).strip())
    return parts


METHOD_RE = re.compile(
    r'(?m)^[ \t]*@(?P<ann>[a-z0-9_]+)\("(?P<path>[^"]*)"\)[ \t]*\n'
    r'(?:[ \t]*@[a-zA-Z0-9_.]+(?:\([^)]*\))?[ \t]*\n)*'
    r'[ \t]*(?:public |private |protected )?(?:static )?(?:final )?'
    r'(?P<ret>[\w.$<>?,\[\] ]+?)\s+(?P<name>\w+)\((?P<params>[^;]*?)\)\s*;'
)
PARAM_ANN = re.compile(r'@(\w+)(?:\(("(?:[^"\\]|\\.)*"|[A-Za-z_][\w.]*)\))?')


def build_consts(files):
    consts = {}
    for p in files:
        s = open(p, encoding='utf-8', errors='ignore').read()
        if 'static final String' not in s:
            continue
        for name, val in CONST.findall(s):
            consts[name] = val
    return consts


def parse_file(path, consts):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    if 'interface ' not in raw or '@' not in raw:
        return []
    s = strip_comments(raw)
    m = re.search(r'public interface (\w+)', s)
    if not m:
        return []
    iface = m.group(1)
    body = s[m.end():]
    out = []
    for mm in METHOD_RE.finditer(body):
        plist = []
        for p in split_params(mm.group('params')):
            p = p.strip()
            if not p:
                continue
            anns = []
            for a, v in PARAM_ANN.findall(p):
                if not v:
                    val = None
                elif v.startswith('"'):
                    val = v[1:-1]
                else:
                    val = consts.get(v.split('.')[-1], v)
                anns.append({'name': a, 'value': val})
            t = re.sub(r'@\w+(?:\([^)]*\))?\s*', '', p)
            t = re.sub(r'\bfinal\b', '', t).strip()
            toks = t.split()
            pname = toks[-1] if toks else ''
            ptype = ' '.join(toks[:-1])
            plist.append({'name': pname, 'type': ptype, 'annotations': anns})
        out.append({
            'interface': iface,
            'file': path.replace('\\', '/'),
            'annotation': mm.group('ann'),
            'path': mm.group('path'),
            'method': mm.group('name'),
            'returns': mm.group('ret').strip(),
            'params': plist,
        })
    return out


if __name__ == '__main__':
    files = glob.glob(os.path.join(SRC, '**', '*.java'), recursive=True)
    consts = build_consts(files)
    rows = []
    for p in files:
        rows.extend(parse_file(p, consts))
    rows.sort(key=lambda r: (r['path'], r['interface'], r['method']))
    os.makedirs('work/cache', exist_ok=True)
    json.dump(rows, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('methods:', len(rows), 'interfaces:', len({r['interface'] for r in rows}))
    print(collections.Counter(r['annotation'] for r in rows).most_common())
    pc = collections.Counter()
    for r in rows:
        for p in r['params']:
            for a in p['annotations']:
                pc[a['name']] += 1
    print('params:', pc.most_common(12))
