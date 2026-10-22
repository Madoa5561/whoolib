import re, json, collections, os

VERBS = {'j94': 'GET', 'j78': 'POST', 'i78': 'PATCH', 'd82': 'DELETE', 'k78': 'PUT'}
BASE_OVERRIDES = {
    'gqa': 'https://open.spotify.com/',
    'bg4': 'https://routes.googleapis.com/',
}
NO_AUTH_IFACES = {'gqa', 'bg4'}


def norm_path(p):
    p = p.strip()
    p = re.sub(r'^/api/', '', p)
    p = p.lstrip('/')
    return p


def classify(params):
    path, query, headers, body, multipart, form = [], [], [], None, None, None
    resp = None
    for p in params:
        t = p['type']
        if t.startswith('w02<'):
            m = re.search(r'super (.+)>', t)
            if m:
                resp = m.group(1)
            continue
        anns = {a['name']: a['value'] for a in p['annotations']}
        if 'yb8' in anns:
            path.append((anns['yb8'], p['name'], t))
        elif 'uz8' in anns:
            query.append((anns['uz8'], p['name'], t))
        elif 'vo4' in anns:
            headers.append((anns['vo4'], p['name'], t))
        elif 'gp0' in anns:
            body = t
        elif 'ob8' in anns:
            multipart = t
        elif 'li3' in anns:
            form = (anns['li3'], p['name'], t)
    return path, query, headers, body, multipart, form, resp


def parse_ret(r):
    if not r:
        return None
    m = re.search(r'super (.+)>', r)
    t = (m.group(1) if m else r).strip()
    if t.startswith('zj9<') and t.endswith('>'):
        t = t[4:-1].strip()
    if t in ('Void', 'l3c', 'void', ''):
        return None
    return t


def main():
    rows = json.load(open('work/cache/api_catalog.json', encoding='utf-8'))
    out = []
    names = collections.Counter()
    for r in rows:
        verb = VERBS.get(r['annotation'])
        if not verb:
            continue
        path = norm_path(r['path'])
        p, q, h, body, mp, form, resp = classify(r['params'])
        base = (verb.lower() + '_' + re.sub(r'[^a-z0-9]+', '_', path.replace('{}', '')).strip('_')).lower()
        base = re.sub(r'_id_', '_', base)
        names[base] += 1
        name = base if names[base] == 1 else f"{base}_{r['interface'].lower()}"
        out.append({
            'name': name,
            'verb': verb,
            'path': path,
            'base_url': BASE_OVERRIDES.get(r['interface']),
            'path_params': [{'name': a, 'arg': b, 'type': c} for a, b, c in p],
            'query_params': [{'name': a, 'arg': b, 'type': c} for a, b, c in q],
            'header_params': [{'name': a, 'arg': b, 'type': c} for a, b, c in h],
            'body_type': body,
            'multipart': mp,
            'form': form,
            'response_type': parse_ret(resp or ''),
            'interface': r['interface'],
            'file': r['file'],
        })
    out.sort(key=lambda e: (e['path'], e['verb']))
    os.makedirs('work/cache', exist_ok=True)
    json.dump(out, open('work/cache/endpoints.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('endpoints:', len(out))
    print(collections.Counter(e['verb'] for e in out))
    # collisions
    dup = [k for k, v in names.items() if v > 1]
    print('name collisions:', len(dup), dup[:10])
    for e in out[:8]:
        print(e)


if __name__ == '__main__':
    main()
