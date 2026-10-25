"""Marca CuentaClara: corre al final de build.sh sobre public/ ya armado (logo, lema, títulos, favicon con versión, CSS)."""
import glob, os, re
AQUI = os.path.dirname(os.path.abspath(__file__)); PUB = os.path.join(AQUI, "..", "public")
LEMA = "Tus cuentas, claras. Tus trámites, resueltos."
NOMBRE = "CuentaClara"
VER = "2"

def svg_limpio(src, dst):
    s = open(os.path.join(AQUI, "assets", src), encoding="utf-8").read()
    s = re.sub(r"<metadata>.*?</metadata>", "", s, flags=re.S)
    os.makedirs(os.path.join(PUB, "img"), exist_ok=True)
    open(os.path.join(PUB, "img", dst), "w", encoding="utf-8").write(s)

MARCA = (f'<a class="marca" href="/" aria-label="{NOMBRE}, inicio"><img class="logo logo-claro" src="/img/cuentaclara.svg" alt="{NOMBRE}" width="170" height="32">'
         f'<img class="logo logo-oscuro" src="/img/cuentaclara-oscuro.svg" alt="" width="170" height="32"><span class="lema">{LEMA}</span></a>')
CSS = """
/* marca CuentaClara */
.marca{flex-direction:column;align-items:flex-start;gap:5px;font-weight:400}
.marca .logo{display:block;width:170px;height:32px}
.marca .logo-oscuro{display:none}
.marca .lema{font:500 12.5px/1.2 var(--f-texto);color:var(--tinta-2);letter-spacing:0}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .marca .logo-claro{display:none}:root:not([data-theme="light"]) .marca .logo-oscuro{display:block}}
:root[data-theme="dark"] .marca .logo-claro{display:none}:root[data-theme="dark"] .marca .logo-oscuro{display:block}
@media (max-width:520px){.marca .logo{width:150px;height:28px}.marca .lema{font-size:12px}}
.pie .nombre{display:block;margin-bottom:6px;color:var(--tinta)}
"""

def pagina(h):
    h = re.sub(r'<a class="marca" href="/"><i>A–K</i>Kit Monotributista</a>', lambda m: MARCA, h)
    h = h.replace('og:site_name" content="Kit Monotributista"', f'og:site_name" content="{NOMBRE}"')
    h = re.sub(r"<title>([^<]*)</title>", lambda m: m.group(0) if NOMBRE in m.group(1) else f"<title>{m.group(1)} | {NOMBRE}</title>", h, count=1)
    h = re.sub(r'(<link rel="(?:icon|apple-touch-icon)" href="/(?:favicon\.ico|favicon-96\.png|apple-touch-icon\.png))(")', lambda m: f"{m.group(1)}?v={VER}{m.group(2)}", h)
    if 'name="application-name"' not in h:
        h = h.replace("</head>", f'<meta name="application-name" content="{NOMBRE}"><meta name="apple-mobile-web-app-title" content="{NOMBRE}"></head>', 1)
    return h

if __name__ == "__main__":
    svg_limpio("logo-horizontal.svg", "cuentaclara.svg"); svg_limpio("logo-horizontal-oscuro.svg", "cuentaclara-oscuro.svg")
    n = 0
    for f in glob.glob(os.path.join(PUB, "**", "*.html"), recursive=True):
        h = open(f, encoding="utf-8").read(); g = pagina(h)
        if g != h: open(f, "w", encoding="utf-8").write(g); n += 1
    css = os.path.join(PUB, "estilo.css"); s = open(css, encoding="utf-8").read()
    if "marca CuentaClara" not in s: open(css, "a", encoding="utf-8").write(CSS)
    print(f"marca: {n} páginas")
