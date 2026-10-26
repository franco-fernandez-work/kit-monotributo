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
import datetime, glob, html, json, os, re

NO_INDEX = {"terminos", "privacidad", "devoluciones", "arrepentimiento", "pedidos", "404"}
SIN_INDEXAR = {"pedidos", "404"}  # llevan noindex y no van al sitemap
MESES = "enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre".split()
# (clave, título del grupo, palabras del slug). Se toma el primer grupo que coincide.
TEMAS = [
    ("casas", "Empleadas domésticas", ["empleada-domestica"]),
    ("alquiler", "Alquileres", ["alquiler", "alquilar"]),
    ("familia", "Familia y trámites", ["menores", "alimentaria", "cole", "hereda", "sucesion", "auto", "progresar"]),
    ("sueldo", "Sueldo, aguinaldo y trabajo", ["aguinaldo", "vacaciones", "liquidacion", "ganancias", "siradig", "telegrama", "jubil", "aportes", "despido", "renuncia", "sueldo", "personal-de-temporada"]),
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
    """FAQPage con los subtítulos h2/h3 que son preguntas y el texto que sigue hasta el próximo subtítulo."""
    qs, vistas = [], set()
    cuerpo = re.split(r'<div class="mas-leer"', main_html)[0]
    cuerpo = re.sub(r"<section class=\"oferta\".*?</section>|<script.*?</script>|<form.*?</form>", "", cuerpo, flags=re.S)
    partes = re.split(r"(<h[23][^>]*>.*?</h[23]>)", cuerpo, flags=re.S)
    for i in range(1, len(partes) - 1, 2):
        q = _txt(partes[i])
        a = _txt(partes[i + 1])
        if q.endswith("?") and len(a) > 40 and q not in vistas:
            vistas.add(q)
            qs.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a[:900]}})
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": qs} if len(qs) >= 2 else None

def _bloque_faq(slug):
    try:
        preguntas = __import__("seo_faq").FAQ.get(slug, [])
    except ImportError:
        return ""
    if not preguntas:
        return ""
    return '<section class="faq"><h2>Preguntas frecuentes</h2>' + "".join(f"<h3>{q}</h3><p>{a}</p>" for q, a in preguntas) + "</section>"

def _relacionados(slug, pags, n=6):
    p = pags[slug]
    mismos = [s for s in pags if s != slug and s not in NO_INDEX and pags[s]["tema"] == p["tema"] and not pags[s].get("consolidada")]
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
       '.faq{margin-top:56px}.faq h3{margin:22px 0 6px;font-size:18px}'
       '.migas{font-size:14px;color:var(--tinta-2);margin:18px 0 10px}.migas a{color:var(--tinta-2)}.migas .act{white-space:nowrap}'
       '.fuentes{margin-top:40px;font-size:15px;color:var(--tinta-2)}.fuentes h2{font-size:18px;margin:0 0 6px}.fuentes ul{margin:0;padding-left:20px}'
       '.glosario dt{font-weight:700;margin-top:18px}.glosario dd{margin:4px 0 0}.fechas li{margin:12px 0}'
       '.submenu{display:flex;flex-wrap:wrap;gap:4px 16px;font-size:14px;margin-top:8px}.submenu a{color:var(--tinta-2)}'
       '.pie,.mas-leer{content-visibility:auto;contain-intrinsic-size:auto 320px}'
       '@media print{.top,.pie,.oferta,.mas-leer,.migas,.faq,.fuentes,.boton{display:none!important}body{background:#fff;color:#000}}'
       '@media (max-width:760px){.mas-leer ul{columns:1}}.indice-guias h2{margin-top:36px}.indice-guias ul{padding-left:20px}.indice-guias li{margin:8px 0}.indice-guias li span{display:block;color:var(--tinta-2);font-size:15px}')

def _fuentes(h):
    m = re.search(r'<link rel="stylesheet" href="(https://fonts\.googleapis\.com/[^"]+)">', h)
    if not m:
        return h
    href = m.group(1)
    return h.replace(m.group(0), f'<link rel="stylesheet" href="{href}" media="print" onload="this.media=\'all\'"><noscript><link rel="stylesheet" href="{href}"></noscript>')

ETIQUETAS = {}  # href -> texto corto del menú original de build_site.py

def _etiqueta(s, pags):
    if "/" + s in ETIQUETAS:
        return ETIQUETAS["/" + s]
    full = (pags[s]["h1"] or pags[s]["title"]).lstrip("¿")
    t = re.split(r"[:?(]", full)[0].strip()
    if len(t) < 15:
        t = full.replace(":", "").replace("?", "").replace("¿", "").strip()
    return t if len(t) <= 34 else t[:32].rsplit(" ", 1)[0] + "…"

def _menu(slug, pags, nombres):
    """Menú del encabezado: los temas y, debajo, solo las páginas del tema actual (antes eran 25 enlaces mezclados)."""
    tema = pags[slug]["tema"]
    temas = "".join(f'<a href="/guias#{k}"{' aria-current="true"' if k == tema else ""}>{t}</a>' for k, t in nombres.items())
    propias = sorted((s for s in pags if pags[s]["tema"] == tema and s not in NO_INDEX and s != slug and not pags[s].get("consolidada")),
                     key=lambda s: ("/" + s not in ETIQUETAS, pags[s]["og"] != "website", s))[:10]
    sub = "".join(f'<a href="/{s}">{html.escape(_etiqueta(s, pags))}</a>' for s in propias)
    return (f'<nav class="menu" aria-label="Temas">{temas}<a href="/guias">Todas</a><a class="arrep" href="/arrepentimiento">Botón de arrepentimiento</a></nav>'
            + (f'<nav class="submenu" aria-label="En este tema">{sub}</nav>' if sub else ""))

def _pagina(pags, base, plantilla_slug, slug, title, desc, cuerpo):
    """Arma una página nueva reusando el encabezado y el pie de una página ya escrita."""
    h = pags[plantilla_slug]["h"]
    url = f"{base}/{slug}"
    h = re.sub(r"<title>.*?</title>", lambda m: f"<title>{title}</title>", h, flags=re.S)
    for attr, val in (('name="description" content="', desc), ('property="og:description" content="', desc), ('property="og:title" content="', title)):
        h = re.sub(r'(<meta ' + re.escape(attr) + r')[^"]*', lambda m: m.group(1) + val, h)
    h = re.sub(r'(<link rel="canonical" href=")[^"]*', lambda m: m.group(1) + url, h)
    h = re.sub(r'(<meta property="og:url" content=")[^"]*', lambda m: m.group(1) + url, h)
    h = h.replace(' aria-current="page"', "")
    h = re.sub(r"(<main[^>]*>).*?(</main>)", lambda m: m.group(1) + "\n" + cuerpo + "\n" + m.group(2), h, flags=re.S)
    h = re.sub(r"(</main>\s*<footer.*?</footer>).*?(</body>)", r"\1\n\2", h, flags=re.S)  # sin el JS de la plantilla
    return h

def _indice(pags):
    grupos = [(k, t) for k, t, _ in TEMAS] + [("otros", "Más herramientas")]
    cuerpo = ['<span class="etiqueta">Índice</span><h1>Todas las calculadoras y guías</h1><p class="bajada">Herramientas gratis y guías para trámites y cuentas de Argentina, ordenadas por tema. También podés ver el <a href="/glosario">glosario</a> y las <a href="/fechas-clave">fechas clave</a>.</p><div class="lectura indice-guias">']
    for k, t in grupos:
        ss = sorted((s for s in pags if pags[s]["tema"] == k and s not in NO_INDEX and not pags[s].get("consolidada")), key=lambda s: (pags[s]["og"] != "website", s))
        if not ss:
            continue
        cuerpo.append(f'<h2 id="{k}">{t}</h2><ul>' + "".join(f'<li><a href="/{s}">{html.escape(pags[s]["h1"] or pags[s]["title"])}</a><span>{html.escape(pags[s]["desc"])}</span></li>' for s in ss) + "</ul>")
    cuerpo.append("</div>")
    return "".join(cuerpo)

def _ancla(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")

def _glosario(sp, pags):
    dl = "".join(f'<dt id="{_ancla(t)}">{t}</dt><dd>{d} <a href="{u}">Más</a></dd>' for t, d, u in sp.GLOSARIO if u.strip("/") in pags)
    return ('<span class="etiqueta">Glosario</span><h1>Glosario de monotributo, sueldos y trámites</h1>'
            '<p class="bajada">Qué significa cada término que usamos en las calculadoras, en dos líneas y con el enlace a la explicación completa.</p>'
            f'<div class="lectura"><dl class="glosario">{dl}</dl></div>')

def _fechas(sp, pags):
    li = "".join(f'<li><b>{f}:</b> {q} <a href="{u}">Ver más</a></li>' for f, _, q, u in sp.FECHAS if u.strip("/") in pags)
    return ('<span class="etiqueta">Calendario</span><h1>Fechas clave: aguinaldo, recategorización y SIRADIG</h1>'
            '<p class="bajada">Los vencimientos y fechas que usan nuestras calculadoras, en orden. Confirmá siempre en el organismo que corresponde.</p>'
            f'<div class="lectura"><ul class="fechas">{li}</ul></div>')

def _fecha_txt(d):
    return f"{d.day} de {MESES[d.month - 1]} de {d.year}"

def _fuentes_oficiales(sp, texto):
    li = [f'<li><a href="{u}" rel="noopener">{n}</a></li>' for pal, n, u in sp.FUENTES if any(x in texto for x in pal)]
    return f'<div class="fuentes"><h2>Fuentes oficiales</h2><ul>{"".join(li)}</ul><p>Cómo usamos estas fuentes: <a href="/metodologia">metodología</a>.</p></div>' if li else ""

def post(pub, base, hoy):
    sp = __import__("seo_pages")
    hoy_d = datetime.date.today()
    hoy = hoy_d.isoformat()
    pags = _leer(pub)
    org = {"@type": "Organization", "name": "CuentaClara", "url": f"{base}/", "logo": f"{base}/icon-512.png"}
    plantilla = "terminos" if "terminos" in pags else next(iter(pags))
    nombres = dict((k, t) for k, t, _ in TEMAS)
    nav = re.search(r'<nav class="menu" aria-label="Secciones">(.*?)</nav>', pags.get("", next(iter(pags.values())))["h"] if "" in pags else "", re.S)
    if nav:
        ETIQUETAS.update({h: _txt(t) for h, t in re.findall(r'<a href="([^"]+)"[^>]*>(.*?)</a>', nav.group(1))})
    # títulos más cercanos a la búsqueda
    for slug, (t, d) in sp.TITULOS.items():
        if slug in pags:
            h = pags[slug]["h"]
            h = re.sub(r"<title>.*?</title>", lambda m: f"<title>{t}</title>", h, flags=re.S)
            h = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m.group(1) + t, h)
            h = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + d, h)
            h = re.sub(r'(<meta property="og:description" content=")[^"]*', lambda m: m.group(1) + d, h)
            pags[slug].update(h=h, title=t, desc=d)
    for slug, destino in sp.CONSOLIDAR.items():
        if slug in pags and destino in pags:
            pags[slug]["consolidada"] = destino
    nuevas = [("guias", "Calculadoras y guías gratis para Argentina 2026", "Índice de todas las calculadoras gratis y guías: monotributo, sueldo y aguinaldo, alquileres, empleadas domésticas, compras online y trámites de familia.", _indice(pags), "Todas las calculadoras y guías"),
              ("glosario", "Glosario: monotributo, aguinaldo, IPC, SIRADIG y más", "Qué es la recategorización, el impuesto integrado, el SAC, el IPC, el ICL, el SIRADIG, la Factura E y otros términos, explicados en dos líneas.", _glosario(sp, pags), "Glosario"),
              ("fechas-clave", "Fechas clave 2026-2027: aguinaldo, recategorización y SIRADIG", "Cuándo vence el aguinaldo, la recategorización del Monotributo y el SIRADIG, y cuándo publica el IPC el INDEC. Calendario con enlaces a cada calculadora.", _fechas(sp, pags), "Fechas clave"),
              ("metodologia", "Cómo hacemos las calculadoras: fuentes y metodología", "De dónde salen los datos de nuestras calculadoras (ARCA, INDEC, BCRA, ANSES, Boletín Oficial), cómo se calculan, cuándo se actualizan y cómo avisar un error.", sp.METODOLOGIA, "Metodología"),
              ("404", "Página no encontrada", "La página que buscás no existe o cambió de dirección.", sp.NO_ENCONTRADA, "No encontrada")]
    for slug, t, d, cuerpo, h1 in nuevas:
        f = os.path.join(pub, slug + ".html")
        open(f, "w", encoding="utf-8").write(_pagina(pags, base, plantilla, slug, t, d, cuerpo))
        pags[slug] = dict(f=f, h=open(f, encoding="utf-8").read(), title=t, h1=h1, desc=d, og="website", tema="indice")
    for slug, p in pags.items():
        h = p["h"]
        h = re.sub(r'<nav class="menu" aria-label="Secciones">.*?</nav>', lambda mm: _menu(slug, pags, nombres), h, count=1, flags=re.S)
        h = re.sub(r"(<b>(?:Modelos?|Cálculo) orientativos?\.</b>)\s*Modelos? orientativos?\.\s*", lambda mm: mm.group(1) + " ", h)
        if p.get("consolidada"):
            h = re.sub(r'(<link rel="canonical" href=")[^"]*', lambda mm: mm.group(1) + f'{base}/{p["consolidada"]}', h)
        if "application/ld+json" in h and "mas-leer" in h:
            continue
        url = f"{base}/{slug}" if slug else f"{base}/"
        tema = p["tema"]
        if slug not in NO_INDEX and "<main" in h and 'class="faq"' not in h:
            h = h.replace("</main>", _bloque_faq(slug) + "\n</main>", 1)
        m = re.search(r"<main.*?</main>", h, re.S)
        main_html = m.group(0) if m else ""
        lds = []
        if slug == "":
            lds.append({"@context": "https://schema.org", "@type": "WebSite", "name": "CuentaClara", "url": f"{base}/", "inLanguage": "es-AR", "publisher": org})
            lds.append(dict({"@context": "https://schema.org"}, **org))
        else:
            migas = [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": f"{base}/"}]
            if tema in nombres:
                migas.append({"@type": "ListItem", "position": 2, "name": nombres[tema], "item": f"{base}/guias#{tema}"})
            migas.append({"@type": "ListItem", "position": len(migas) + 1, "name": p["h1"] or p["title"], "item": url})
            lds.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": migas})
        if slug not in NO_INDEX:
            lds += _productos(main_html, url, p["desc"], org, base)
            if p["og"] == "article":
                lds.append({"@context": "https://schema.org", "@type": "Article", "headline": (p["h1"] or p["title"])[:110], "description": p["desc"],
                            "inLanguage": "es-AR", "datePublished": "2026-10-24", "dateModified": hoy, "mainEntityOfPage": url, "author": org, "publisher": org,
                            "image": f"{base}/og-{tema}.png" if tema in nombres else f"{base}/og.png"})
            elif "<input" in main_html and tema != "indice":
                lds.append({"@context": "https://schema.org", "@type": "WebApplication", "name": p["h1"] or p["title"], "url": url, "applicationCategory": "FinanceApplication",
                            "operatingSystem": "Web", "inLanguage": "es-AR", "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "ARS"}, "provider": org})
            if slug == "glosario":
                lds.append({"@context": "https://schema.org", "@type": "DefinedTermSet", "name": "Glosario", "url": url,
                            "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t, "description": _txt(d), "url": f"{url}#{_ancla(t)}"} for t, d, u in sp.GLOSARIO if u.strip("/") in pags]})
            if slug == "fechas-clave":
                lds.append({"@context": "https://schema.org", "@type": "ItemList", "name": "Fechas clave", "itemListElement": [
                    {"@type": "ListItem", "position": i + 1, "name": f"{f}: {q}", "url": f"{base}{u}"} for i, (f, _, q, u) in enumerate(x for x in sp.FECHAS if x[3].strip("/") in pags)]})
            fq = _faq(main_html)
            if fq:
                lds.append(fq)
            if m and slug != "":
                ruta = '<a href="/">Inicio</a>' + (f' › <a href="/guias#{tema}">{nombres[tema]}</a>' if tema in nombres else "")
                h = re.sub(r"(<main[^>]*>)", lambda mm: mm.group(1) + f'\n<nav class="migas" aria-label="Ruta">{ruta} · <span class="act">Actualizado el {_fecha_txt(hoy_d)}</span></nav>', h, count=1)
            if m and tema != "indice":
                h = h.replace("</main>", _fuentes_oficiales(sp, _txt(re.sub(r'<section class="oferta".*?</section>|<div class="mas-leer".*?</div>', "", main_html, flags=re.S))) + _relacionados(slug, pags) + "\n</main>", 1)
        img = f"{base}/og-{tema}.png" if tema in nombres else f"{base}/og.png"
        cab = (f'<meta property="og:image" content="{img}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">'
               '<link rel="icon" href="/favicon.ico" sizes="48x48"><link rel="icon" href="/favicon-96.png" type="image/png" sizes="96x96"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><meta name="theme-color" content="#10263d">'
               f'<link rel="alternate" hreflang="es-AR" href="{url}">'
               + ('<meta name="robots" content="noindex, follow">' if slug in SIN_INDEXAR else '<meta name="robots" content="max-snippet:-1, max-image-preview:large">'))
        h = h.replace("</head>", cab + "".join(_ld(x) for x in lds) + "</head>", 1)
        h = _fuentes(h)
        if 'href="/guias">Todas' not in h:
            h = h.replace('<div class="legal">', '<div class="legal"><a href="/guias">Todas las calculadoras y guías</a><a href="/glosario">Glosario</a><a href="/fechas-clave">Fechas clave</a><a href="/metodologia">Cómo hacemos las calculadoras</a>', 1)
        open(p["f"], "w", encoding="utf-8").write(h)
    css = os.path.join(pub, "estilo.css")
    s = open(css, encoding="utf-8").read()
    if ".mas-leer" not in s:
        open(css, "a", encoding="utf-8").write("\n" + CSS + "\n")
    sm = os.path.join(pub, "sitemap.xml")
    s = open(sm, encoding="utf-8").read()
    for slug in SIN_INDEXAR | {k for k, v in pags.items() if v.get("consolidada")}:
        s = re.sub(r"<url><loc>" + re.escape(f"{base}/{slug}") + r"</loc>.*?</url>\n?", "", s)
    s = re.sub(r"<lastmod>[^<]*</lastmod>", f"<lastmod>{hoy}</lastmod>", s)
    for slug, *_ in nuevas:
        if slug not in SIN_INDEXAR and f"<loc>{base}/{slug}</loc>" not in s:
            s = s.replace("</urlset>", f"<url><loc>{base}/{slug}</loc><lastmod>{hoy}</lastmod></url>\n</urlset>")
    open(sm, "w", encoding="utf-8").write(s)
    rb = os.path.join(pub, "robots.txt")
    r = open(rb, encoding="utf-8").read()
    if "Disallow: /api/" not in r:
        open(rb, "w", encoding="utf-8").write(r.replace("Sitemap:", "Disallow: /api/\nDisallow: /recibos/api/\nSitemap:", 1))
    return len(pags)
