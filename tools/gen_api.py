import sys, re, keyword
sys.path.insert(0, '.')
from whoolib._endpoints import ENDPOINTS

HEADER = '''"""Generated API method wrappers (do not edit by hand).

Each method maps 1:1 to a Retrofit endpoint found in the whoo APK.
Arguments use the wire-level parameter names; see ``docs/ENDPOINTS.md``.
"""

from __future__ import annotations

from typing import Any, Mapping, Optional


class API:
    """Facade over :class:`whoolib.client.WhooClient` with one method per endpoint."""

    def __init__(self, client: "WhooClient"):
        self._client = client

'''


def pyident(s):
    s = s.replace('[]', '')
    s = re.sub(r'[^0-9a-zA-Z_]+', '_', s)
    s = re.sub(r'_+', '_', s).strip('_') or 'value'
    if s[0].isdigit():
        s = 'p_' + s
    if keyword.iskeyword(s) or s in ('None', 'True', 'False'):
        s += '_'
    return s


def build():
    out = [HEADER]
    for name, e in sorted(ENDPOINTS.items()):
        used = set()

        def arg(wire):
            a = pyident(wire)
            while a in used:
                a += '_'
            used.add(a)
            return a

        path_args = [(w, arg(w)) for w, _, _ in e.path_params]
        query_args = [(w, arg(w)) for w, _, _ in e.query_params]
        form_args = [(w, arg(w)) for w, _, _ in e.form if w]

        params = ['self'] + [a for _, a in path_args]
        kw = [f'{a}: Any = None' for _, a in query_args]
        kw += [f'{a}: Any = None' for _, a in form_args]
        if e.body_type:
            kw.append('body: Any = None')
        if e.multipart:
            kw.append('parts: Any = None')
        kw.append('headers: Optional[Mapping[str, str]] = None')
        params.append('*')
        params += kw

        call = [f'        return self._client.call({name!r},']
        if path_args:
            call.append('            path={' + ', '.join(f'{w!r}: {a}' for w, a in path_args) + '},')
        if query_args:
            call.append('            query={' + ', '.join(f'{w!r}: {a}' for w, a in query_args) + '},')
        if form_args:
            call.append('            form={' + ', '.join(f'{w!r}: {a}' for w, a in form_args) + '},')
        if e.body_type:
            call.append('            body=body,')
        if e.multipart:
            call.append('            parts=parts,')
        call.append('            headers=headers,')
        call.append('        )')

        doc = [f'{e.verb} {e.path}']
        if e.path_params or e.query_params:
            doc.append('')
            doc.append('Params: ' + ', '.join(w for w, _, _ in e.path_params + e.query_params))
        if e.body_type:
            doc.append(f'Body: {e.body_type}')
        if e.multipart:
            doc.append('Multipart: mapping field -> str | bytes | (filename, bytes[, content_type])')
        doc.append(f'Response: {e.response_type or "empty"}')
        doc.append(f'Auth: {"required" if e.auth else "not required"}')

        out.append(f'    def {name}({", ".join(params)}) -> Any:')
        out.append(f'        """{doc[0]}')
        for line in doc[1:]:
            out.append('        ' + line if line else '')
        out.append('        """')
        out.extend(call)
        out.append('')

    open('whoolib/api.py', 'w', encoding='utf-8').write('\n'.join(out))

    md = ['# whoo API endpoint catalog', '',
          f'Total: **{len(ENDPOINTS)}** endpoints '
          f'(GET {sum(1 for e in ENDPOINTS.values() if e.verb == "GET")}, '
          f'POST {sum(1 for e in ENDPOINTS.values() if e.verb == "POST")}, '
          f'PUT {sum(1 for e in ENDPOINTS.values() if e.verb == "PUT")}, '
          f'DELETE {sum(1 for e in ENDPOINTS.values() if e.verb == "DELETE")}, '
          f'PATCH {sum(1 for e in ENDPOINTS.values() if e.verb == "PATCH")})', '',
          '| method | path | path params | query params | body | response | auth |',
          '|---|---|---|---|---|---|---|']
    for name, e in sorted(ENDPOINTS.items(), key=lambda kv: kv[1].path):
        pp = ', '.join(w for w, _, _ in e.path_params) or '-'
        qp = ', '.join(w for w, _, _ in e.query_params) or '-'
        b = e.body_type or ('multipart' if e.multipart else '-')
        r = e.response_type or '-'
        md.append(f'| `{e.verb}` | `{e.path}` | {pp} | {qp} | {b} | {r} | {"yes" if e.auth else "no"} |')
    open('docs/ENDPOINTS.md', 'w', encoding='utf-8').write('\n'.join(md) + '\n\n'
        '## Base URL overrides\n\n'
        'Most endpoints use `https://www.wh00.ooo/api/`. Two interfaces in the APK use a\n'
        'different Retrofit base URL and are marked accordingly:\n\n'
        '| interface | base URL | endpoints |\n|---|---|---|\n'
        '| `gqa` | `https://open.spotify.com/` | `GET api/token` |\n'
        '| `bg4` | `https://routes.googleapis.com/` | `GET directions/v2:computeRoutes` |\n')
    print('api methods:', len(ENDPOINTS))


if __name__ == '__main__':
    build()
