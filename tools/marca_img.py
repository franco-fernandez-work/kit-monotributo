"""Genera las imágenes de marca CuentaClara en public/ (correr local y commitear; no corre en Cloudflare)."""
import glob, os, re
from PIL import Image, ImageDraw, ImageFont
A = os.path.join(os.path.dirname(__file__), "assets"); P = os.path.join(os.path.dirname(__file__), "..", "public")
LEMA = "Tus cuentas, claras. Tus trámites, resueltos."
sq = Image.open(f"{A}/cuadrado-1024.png").convert("RGB")
sq.resize((512, 512), Image.LANCZOS).save(f"{P}/icon-512.png")
sq.resize((180, 180), Image.LANCZOS).save(f"{P}/apple-touch-icon.png")
sq.resize((96, 96), Image.LANCZOS).save(f"{P}/favicon-96.png")
sq.save(f"{P}/favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
logo = Image.open(f"{A}/logo-horizontal.png").convert("RGBA")
def fuente(n): return ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf" if n else r"C:\Windows\Fonts\segoeui.ttf", n or 10)
# og.png genérica: marca + lema
im = Image.new("RGB", (1200, 630), "#f5f7f9"); d = ImageDraw.Draw(im)
d.rectangle([40, 40, 1160, 590], fill="white", outline="#10263d", width=4); d.rectangle([40, 40, 1160, 70], fill="#3f8fcf")
w = 760; l = logo.resize((w, round(w * logo.height / logo.width)), Image.LANCZOS)
im.paste(l, (100, 190), l)
d.text((100, 190 + l.height + 40), LEMA, font=ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 40), fill="#4b5e72")
d.text((100, 520), "Calculadoras y planillas para Argentina", font=ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 28), fill="#b3343c")
im.save(f"{P}/og.png", optimize=True)
# og-<tema>.png: reemplaza el pie "Kit Monotributista · gratis" por el logo
chico = logo.resize((round(46 * logo.width / logo.height), 46), Image.LANCZOS)
for f in glob.glob(f"{P}/og-*.png"):
    i = Image.open(f).convert("RGB"); dd = ImageDraw.Draw(i)
    dd.rectangle([90, 515, 700, 575], fill="white"); i.paste(chico, (100, 522), chico)
    dd.text((100 + chico.width + 20, 530), "· gratis", font=ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 28), fill="#b3343c")
    i.save(f, optimize=True)
