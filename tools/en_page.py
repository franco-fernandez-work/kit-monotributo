"""Página /en (CuentaClara en inglés, productos de Gumroad). Corre en build.sh después de marca.py, sobre public/ ya armado.
Para sumar un producto: poner su slug de Gumroad (la parte final de /l/<slug>) en PRODUCTOS; los que tienen slug None no se muestran."""
import glob, os, re, sys
AQUI = os.path.dirname(os.path.abspath(__file__)); PUB = os.path.join(AQUI, "..", "public")
sys.path.insert(0, AQUI)
from build_site import BASE, HOY, FONTS
from marca import MARCA
TIENDA = "https://cuentaclaraarg.gumroad.com/l/"
LEMA = "Clear numbers. Ready-made templates."

# (slug Gumroad o None, nombre, descripción corta, precio USD)
PRODUCTOS = [
    ("iucsal", "Personal Finance Planner", "Log income and expenses, set a monthly budget per category and track your savings goals in one spreadsheet.", 12),
    ("kfyoy", "Pricing & Margin Calculator", "Enter cost, shipping and the margin you want, and see the exact price to charge on up to three sales channels.", 15),
    ("juoiwx", "Freelancer Contract Pack", "Agreement, NDA, proposal, quote and more, in plain language and ready to edit, from first proposal to final payment.", 19),
    ("agqqi", "Debt Payoff Planner", "List your debts, add what extra you can pay, pick Snowball or Avalanche and see the month you become debt-free.", 12),
    ("qjrkro", "Group Expense Splitter", "Log shared expenses and get one table showing who pays whom to settle up. For roommates, trips and couples.", 9),
    ("rsshp", "Freelancer Invoice Tracker", "Flags open and overdue invoices, ages late payments and shows how much to set aside for taxes.", 14),
    ("pxfhxf", "Subscription Tracker", "List everything that renews and see your monthly and yearly cost, with alerts before each renewal.", 9),
    # En cola (Gumroad deja crear 10 por día): al completar el slug aparecen solos.
    (None, "Stock & Inventory Planner", "Track stock, reorder points and margins for a small online shop.", 19),
    (None, "Overtime & Time-Off Tracker", "Log extra hours and turn them into days off, with running balances.", 12),
    (None, "Household Chores Organizer", "Split recurring chores by frequency and person, with a printable weekly view.", 12),
    (None, "Trip Checklist", "What to do and pack, by deadline, before you travel.", 6),
    (None, "Trip Bundle: Checklist + Budget", "The trip checklist plus the travel budget planner in one pack.", 12),
    (None, "Travel Budget Planner", "Plan the cost of a trip by category and compare it with what you actually spend.", 10),
    (None, "Wedding & Party Planner", "Guest list, budget and task timeline for weddings and parties.", 12),
    (None, "Holiday Gift & Dinner Planner", "Gift list, budget and dinner shopping list for the holidays.", 8),
    (None, "Back-to-School Budget", "Supplies, uniforms and fees per child against a school-year budget.", 8),
    (None, "Rental Property Rent Tracker", "Rent due, paid and late per tenant, with yearly income totals.", 12),
    (None, "Family Health & Medical Claims Organizer", "Appointments, receipts and insurance claims for the whole family.", 12),
    (None, "Moving Planner & Cost Calculator", "Moving timeline, packing list and cost estimate in one workbook.", 9),
    (None, "Market Stall & Pop-Up Break-Even Planner", "Find how many sales cover your stall costs, and what to price each item.", 8),
]

CSS = """
/* /en */
.en-intro{max-width:680px;margin:48px 0 8px}
.en-intro h1{font-size:clamp(32px,4.4vw,48px);margin:0 0 14px}
.en-intro p{color:var(--tinta-2);margin:0}
.en-lista{list-style:none;margin:36px 0 0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:20px}
.en-lista>li{display:flex;flex-direction:column;gap:10px;border:1px solid var(--linea);border-radius:4px;background:var(--hoja);padding:22px}
.en-lista h2{font-size:21px;margin:0}
.en-lista p{margin:0;color:var(--tinta-2);font-size:16px;flex:1}
.en-lista .pie-prod{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-top:6px}
.en-lista .precio{font:700 20px var(--f-num)}
.en-nota{margin-top:40px;color:var(--tinta-2);font-size:15px}
.lang{white-space:nowrap}
"""

def items():
    return "".join(
        f'<li><h2>{n}</h2><p>{d}</p><div class="pie-prod"><span class="precio">US$ {p}</span>'
        f'<a class="boton" href="{TIENDA}{s}" rel="noopener">Get it on Gumroad</a></div></li>'
        for s, n, d, p in PRODUCTOS if s)

def pagina():
    marca = MARCA.replace("Tus cuentas, claras. Tus trámites, resueltos.", LEMA).replace('inicio"', 'home"').replace('href="/"', 'href="/en"')
    t = "Spreadsheet Templates for Freelancers and Households | CuentaClara"
    d = "Ready-to-use Excel and Google Sheets templates: budgets, debt payoff, invoices, pricing and contracts. One-time price in USD, instant download from Gumroad."
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{BASE}/en">
<meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{BASE}/en"><meta property="og:type" content="website"><meta property="og:locale" content="en_US"><meta property="og:site_name" content="CuentaClara">
<meta property="og:image" content="{BASE}/og.png"><meta name="twitter:card" content="summary_large_image">
<link rel="alternate" hreflang="en" href="{BASE}/en"><link rel="alternate" hreflang="es-AR" href="{BASE}/"><link rel="alternate" hreflang="x-default" href="{BASE}/">
<link rel="icon" href="/favicon.ico?v=2" sizes="48x48"><link rel="icon" href="/favicon-96.png?v=2" type="image/png" sizes="96x96"><link rel="apple-touch-icon" href="/apple-touch-icon.png?v=2"><meta name="theme-color" content="#10263d">
<meta name="robots" content="max-snippet:-1, max-image-preview:large">
{FONTS}<link rel="stylesheet" href="/estilo.css"></head>
<body><header class="top"><div class="wrap">{marca}<nav class="menu" aria-label="Sections"><a href="/en" aria-current="page">Templates</a><a class="lang" href="/" hreflang="es-AR" lang="es-AR">Español (Argentina)</a></nav></div></header>
<main class="wrap">
<section class="en-intro"><span class="etiqueta">Templates for Excel and Google Sheets</span><h1>Spreadsheets that do the math for you</h1>
<p>Simple, tested templates for freelancers and households. Pay once in US dollars on Gumroad and download instantly. No subscription.</p></section>
<ul class="en-lista">{items()}</ul>
<p class="en-nota">Looking for Argentine tax and payroll tools (Monotributo, aguinaldo, rent updates)? Those are in Spanish on the <a href="/" hreflang="es-AR" lang="es-AR">main site</a>.</p>
</main>
<footer class="pie"><div class="wrap"><span class="nombre"><b>CuentaClara</b> · {LEMA}</span><span>Payments processed by Gumroad. Templates are general-purpose and are not financial, tax or legal advice.</span></div></footer>
</body></html>
"""

def main():
    w = lambda p, s: open(os.path.join(PUB, p), "w", encoding="utf-8").write(s)
    w("en.html", pagina())
    css = os.path.join(PUB, "estilo.css"); s = open(css, encoding="utf-8").read()
    if "/* /en */" not in s: open(css, "a", encoding="utf-8").write(CSS)
    link = '<a class="lang" href="/en" hreflang="en" lang="en">English</a>'
    n = 0
    for f in glob.glob(os.path.join(PUB, "**", "*.html"), recursive=True):
        if os.path.basename(f) == "en.html": continue
        h = open(f, encoding="utf-8").read(); g = h
        if 'class="lang"' not in g:
            g = g.replace('<a class="arrep" href="/arrepentimiento">Botón de arrepentimiento</a></nav>', f'{link}<a class="arrep" href="/arrepentimiento">Botón de arrepentimiento</a></nav>', 1)
            g = g.replace('<div class="legal">', f'<div class="legal">{link}', 1)
        if os.path.basename(f) == "index.html" and 'hreflang="x-default"' not in g:
            g = g.replace("</head>", f'<link rel="alternate" hreflang="en" href="{BASE}/en"><link rel="alternate" hreflang="x-default" href="{BASE}/"></head>', 1)
        if g != h: open(f, "w", encoding="utf-8").write(g); n += 1
    sm = os.path.join(PUB, "sitemap.xml"); s = open(sm, encoding="utf-8").read()
    hoy = (re.findall(r"<lastmod>([^<]*)</lastmod>", s) or [HOY])[-1]
    if f"<loc>{BASE}/en</loc>" not in s:
        open(sm, "w", encoding="utf-8").write(s.replace("</urlset>", f"<url><loc>{BASE}/en</loc><lastmod>{hoy}</lastmod></url>\n</urlset>"))
    print(f"en: {items().count('<li>')} productos, {n} páginas con enlace English")

if __name__ == "__main__":
    main()
