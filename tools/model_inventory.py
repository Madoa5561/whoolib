import re, glob, json, os

SRC = 'work/src/sources'
OUT = 'work/cache/model_catalog.json'

PAT = re.compile(r'new al8\("([^"]+)",\s*\w+,\s*(\d+)\)(.*?)descriptor\s*=', re.S)
KEY = re.compile(r'\.j\(\s*(?:"([^"]+)"|([A-Za-z_][\w.]*))\s*,\s*(true|false)\)')
CONST = re.compile(r'static final String ([A-Z0-9_]+)\s*=\s*"([^"]*)"')


def build_consts(files):
    consts = {}
    for p in files:
        s = open(p, encoding='utf-8', errors='ignore').read()
        if 'static final String' not in s:
            continue
        for name, val in CONST.findall(s):
            consts.setdefault(name, val)
            consts.setdefault(name.split('.')[-1], val)
    return consts


def main():
    files = glob.glob(os.path.join(SRC, '**', '*.java'), recursive=True)
    consts = build_consts(files)
    models = {}
    unresolved = 0
    for p in files:
        s = open(p, encoding='utf-8', errors='ignore').read()
        if 'new al8("' not in s:
            continue
        for m in PAT.finditer(s):
            fqcn, count, body = m.group(1), int(m.group(2)), m.group(3)
            keys = []
            for lit, ident, opt in KEY.findall(body):
                if lit:
                    k = lit
                else:
                    k = consts.get(ident.split('.')[-1], ident)
                    if k == ident:
                        unresolved += 1
                keys.append([k, opt == 'true'])
            if len(keys) != count:
                keys = keys[:count]
            models[fqcn] = {'count': count, 'keys': keys, 'file': p.replace('\\', '/')}
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(models, f, ensure_ascii=False, indent=1)
    bad = [(k, v['count'], len(v['keys'])) for k, v in models.items() if v['count'] != len(v['keys'])]
    print('models:', len(models), 'mismatch:', len(bad), 'unresolved:', unresolved)
    for b in bad[:20]:
        print(' ', b)
    print(models.get('app.whoo.data.api.request.UserAccount'))


if __name__ == '__main__':
    main()
