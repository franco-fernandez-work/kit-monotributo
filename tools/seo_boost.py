"""SEO de todo el sitio, como último paso del build (se llama al final de main() en build_site.py).
Relee cada .html ya escrito en public/ y le suma, sin tocar el contenido de cada página:
- datos estructurados JSON-LD: BreadcrumbList en todas, WebSite + Organization en la home,
  Product + Offer por cada botón /comprar?p=..., Article en las páginas de artículo y FAQPage
  cuando hay 2 o más subtítulos h2 que son preguntas;
- un bloque "Seguí leyendo" con enlaces a páginas del mismo tema (antes había ~26 páginas
  a las que solo se llegaba por el sitemap);
- la carga de Google Fonts sin bloquear el render;
- la página /guias con el índice de todo el sitio (enlazada desde el pie) y la suma al sitemap.
Las páginas nuevas entran solas: el tema se deduce del slug con TEMAS."""
import glob, html, json, os, re

NO_INDEX = {"terminos", "privacidad", "devoluciones", "arrepentimiento", "pedidos"}
# (clave, título del grupo, palabras del slug). Se toma el primer grupo que coincide.
TEMAS = [
    ("casas", "Empleadas domésticas", ["empleada-domestica"]),
    ("alquiler", "Alquileres", ["alquiler", "alquilar"]),
    ("familia", "Familia y trámites", ["menores", "alimentaria", "cole", "hereda", "sucesion", "auto", "progresar"]),
    ("sueldo", "Sueldo, aguinaldo y trabajo", ["aguinaldo", "vacaciones", "liquidacion", "ganancias", "siradig", "telegrama", "jubil", "aportes", "despido", "renuncia", "sueldo"]),
    ("mono", "Monotributo y freelancers", ["monotributo", "escalas", "recategoriz", "freelancer", "recibos", "facturar"]),
    ("ventas", "Vender y comprar online", ["mercado-libre", "compras", "reclamo", "arrepentimiento", "exterior", "vender-en"]),
]
TEMA_HOME = "mono"

def _tema(slug):
    if slug == "":
        return TEMA_HOME
    for k, _, pal in TEMAS:
        if any(p in slug for p in pal):
            return k
    return "otros"

def _txt(s):
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", s)).split())

def _ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + "</script>"

def _leer(pub):
    pags = {}
    for f in sorted(glob.glob(os.path.join(pub, "*.html"))):
        slug = os.path.basename(f)[:-5]
        if slug.startswith("google"):
            continue
        slug = "" if slug == "index" else slug
        h = open(f, encoding="utf-8").read()
        if "<main" not in h:
            continue
        t = re.search(r"<title>(.*?)</title>", h, re.S)
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S)
        d = re.search(r'<meta name="description" content="([^"]*)"', h)
        og = re.search(r'og:type" content="(\w+)"', h)
        pags[slug] = dict(f=f, h=h, title=_txt(t.group(1)) if t else slug, h1=_txt(h1.group(1)) if h1 else "",
                          desc=html.unescape(d.group(1)) if d else "", og=og.group(1) if og else "website", tema=_tema(slug))
    return pags

def _productos(main_html, url, desc, org, base):
    out, vistos = [], set()
    for sec in re.findall(r'<section class="oferta".*?</section>', main_html, re.S):
        h2 = re.search(r"<h2[^>]*>(.*?)</h2>", sec, re.S)
        par = re.search(r"<p[^>]*>(.*?)</p>", sec, re.S)
        texto = _txt(par.group(1)) if par and len(_txt(par.group(1))) > 30 else desc
        for ref, precio in re.findall(r'href="/comprar\?p=(\w+)"[^>]*>[^<]*<span class="num">\$\s*([\d.]+)', sec):
            if ref in vistos:
                continue
            vistos.add(ref)
            out.append({"@context": "https://schema.org", "@type": "Product", "name": _txt(h2.group(1)) if h2 else ref,
                        "description": texto, "sku": ref, "image": f"{base}/og.png", "brand": {"@type": "Brand", "name": org["name"]},
                        "offers": {"@type": "Offer", "price": precio.replace(".", ""), "priceCurrency": "ARS",
                                   "availability": "https://schema.org/InStock", "url": url, "seller": org}})
    return out

def _faq(main_html):
    qs = []
    partes = re.split(r"(<h2[^>]*>.*?</h2>)", main_html, flags=re.S)
    for i in range(1, len(partes) - 1, 2):
        q = _txt(partes[i])
        a = re.split(r'<section class="oferta"|<aside|<div class="mas-leer"', partes[i + 1])[0]
        a = _txt(a)
        if q.endswith("?") and len(a) > 40:
            qs.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a[:900]}})
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": qs} if len(qs) >= 2 else None

def _relacionados(slug, pags, n=6):
    p = pags[slug]
    mismos = [s for s in pags if s != slug and s not in NO_INDEX and pags[s]["tema"] == p["tema"]]
    # primero las calculadoras (website) y después los artículos; orden estable por slug
    grupo = sorted(mismos + [slug], key=lambda s: (pags[s]["og"] != "website", s))
    i = grupo.index(slug)
    mismos = (grupo[i + 1:] + grupo[:i])
    if len(mismos) < 3:
        mismos += [s for s in ("", "aguinaldo", "aumento-alquiler", "calculadora-liquidacion-final") if s in pags and s != slug and s not in mismos]
    li = "".join(f'<li><a href="/{s}">{html.escape(pags[s]["h1"] or pags[s]["title"])}</a></li>' for s in mismos[:n])
    return f'<div class="mas-leer"><h2>Seguí leyendo</h2><ul>{li}</ul><p><a href="/guias">Ver todas las calculadoras y guías</a></p></div>'

CSS = ('.mas-leer{margin-top:56px;padding-top:20px;border-top:1px solid var(--linea)}.mas-leer h2{margin:0 0 10px;font-size:20px}'
       '.mas-leer ul{margin:0;padding-left:20px;columns:2;column-gap:32px}.mas-leer li{margin:6px 0;break-inside:avoid}'
       '@media (max-width:760px){.mas-leer ul{columns:1}}.indice h2{margin-top:36px}.indice ul{padding-left:20px}.indice li{margin:8px 0}.indice li span{display:block;color:var(--tinta-2);font-size:15px}')

def _fuentes(h):
    m = re.search(r'<link rel="stylesheet" href="(https://fonts\.googleapis\.com/[^"]+)">', h)
    if not m:
        return h
    href = m.group(1)
    return h.replace(m.group(0), f'<link rel="stylesheet" href="{href}" media="print" onload="this.media=\'all\'"><noscript><link rel="stylesheet" href="{href}"></noscript>')

def _indice(pags, base, plantilla_slug, hoy):
    """Arma public/guias.html reusando el encabezado y el pie de una página ya escrita."""
    grupos = [(k, t) for k, t, _ in TEMAS] + [("otros", "Más herramientas")]
    cuerpo = ['<span class="etiqueta">Índice</span><h1>Todas las calculadoras y guías</h1><p class="bajada">Herramientas gratis y guías para trámites y cuentas de Argentina, ordenadas por tema.</p><div class="lectura indice">']
    for k, t in grupos:
        ss = sorted((s for s in pags if pags[s]["tema"] == k and s not in NO_INDEX), key=lambda s: (pags[s]["og"] != "website", s))
        if not ss:
            continue
        cuerpo.append(f"<h2>{t}</h2><ul>" + "".join(f'<li><a href="/{s}">{html.escape(pags[s]["h1"] or pags[s]["title"])}</a><span>{html.escape(pags[s]["desc"])}</span></li>' for s in ss) + "</ul>")
    cuerpo.append("</div>")
    h = pags[plantilla_slug]["h"]
    title, desc = "Calculadoras y guías gratis para Argentina 2026", "Índice de todas las calculadoras gratis y guías: monotributo, sueldo y aguinaldo, alquileres, empleadas domésticas, compras online y trámites de familia."
    h = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", h, flags=re.S)
    h = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + desc, h)
    h = re.sub(r'(<meta property="og:description" content=")[^"]*', lambda m: m.group(1) + desc, h)
    h = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m.group(1) + title, h)
    h = re.sub(r'(<link rel="canonical" href=")[^"]*', lambda m: m.group(1) + f"{base}/guias", h)
    h = re.sub(r'(<meta property="og:url" content=")[^"]*', lambda m: m.group(1) + f"{base}/guias", h)
    h = h.replace(' aria-current="page"', "")
    h = re.sub(r"(<main[^>]*>).*?(</main>)", lambda m: m.group(1) + "\n" + "".join(cuerpo) + "\n" + m.group(2), h, flags=re.S)
    h = re.sub(r"(</main>\s*<footer.*?</footer>).*?(</body>)", r"\1\n\2", h, flags=re.S)  # sin el JS de la plantilla
    return h

def post(pub, base, hoy):
    pags = _leer(pub)
    org = {"@type": "Organization", "name": "Kit Monotributista", "url": f"{base}/"}
    plantilla = "terminos" if "terminos" in pags else next(iter(pags))
    open(os.path.join(pub, "guias.html"), "w", encoding="utf-8").write(_indice(pags, base, plantilla, hoy))
    pags["guias"] = dict(f=os.path.join(pub, "guias.html"), h=open(os.path.join(pub, "guias.html"), encoding="utf-8").read(),
                         title="Calculadoras y guías", h1="Todas las calculadoras y guías", desc="", og="website", tema="indice")
    for slug, p in pags.items():
        h = p["h"]
        if "application/ld+json" in h and "mas-leer" in h:
            continue
        url = f"{base}/{slug}" if slug else f"{base}/"
        m = re.search(r"<main.*?</main>", h, re.S)
        main_html = m.group(0) if m else ""
        lds = []
        if slug == "":
            lds.append({"@context": "https://schema.org", "@type": "WebSite", "name": "Kit Monotributista", "url": f"{base}/", "inLanguage": "es-AR", "publisher": org})
            lds.append(dict({"@context": "https://schema.org"}, **org))
        else:
            lds.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Inicio", "item": f"{base}/"},
                {"@type": "ListItem", "position": 2, "name": p["h1"] or p["title"], "item": url}]})
        if slug not in NO_INDEX:
            lds += _productos(main_html, url, p["desc"], org, base)
            if p["og"] == "article":
                lds.append({"@context": "https://schema.org", "@type": "Article", "headline": (p["h1"] or p["title"])[:110], "description": p["desc"],
                            "inLanguage": "es-AR", "datePublished": hoy, "dateModified": hoy, "mainEntityOfPage": url, "author": org, "publisher": org})
            fq = _faq(main_html)
            if fq:
                lds.append(fq)
            if slug != "guias" and m:
                h = h.replace("</main>", _relacionados(slug, pags) + "\n</main>", 1)
        og_img = f'<meta property="og:image" content="{base}/og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">'
        h = h.replace("</head>", og_img + "".join(_ld(x) for x in lds) + "</head>", 1)
        h = _fuentes(h)
        if 'href="/guias">Todas' not in h:
            h = h.replace('<div class="legal">', '<div class="legal"><a href="/guias">Todas las calculadoras y guías</a>', 1)
        open(p["f"], "w", encoding="utf-8").write(h)
    css = os.path.join(pub, "estilo.css")
    s = open(css, encoding="utf-8").read()
    if ".mas-leer" not in s:
        open(css, "a", encoding="utf-8").write("\n" + CSS + "\n")
    sm = os.path.join(pub, "sitemap.xml")
    s = open(sm, encoding="utf-8").read()
    if f"<loc>{base}/guias</loc>" not in s:
        s = s.replace("</urlset>", f"<url><loc>{base}/guias</loc><lastmod>{hoy}</lastmod></url>\n</urlset>")
        open(sm, "w", encoding="utf-8").write(s)
    return len(pags)
