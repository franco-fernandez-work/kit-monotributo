"""Armado genérico de guías PDF (ronda 4). Reusa estilos y componentes de build_guia_pdf.
Cada guía es un módulo g_*.py con META (dict) y contenido(). `python tools/ronda4.py` genera private/guia-*.pdf (solo local, necesita reportlab)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_guia_pdf import (A4, mm, HexColor, white, TINTA, TINTA2, CEL, SUAVE, LINEA, SELLO, W, H, M, st, S, Caja, P, L, H2, cap, tabla,
                            BaseDocTemplate, PageTemplate, Frame, Spacer, PageBreak, NextPageTemplate, Paragraph)

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "private")
BASE_URL = "kit-monotributo.fernandezfrancowork.workers.dev"

def E(items):
    """Pasos numerados."""
    return [Paragraph(f"<b>{i}.</b>&nbsp; {t}", st("pa", leftIndent=16, firstLineIndent=-16, spaceAfter=5)) for i, t in enumerate(items, 1)]

def alerta(titulo, texto): return Caja(titulo, texto, color=SELLO, fondo=HexColor("#fbeeee"))
def consejo(titulo, texto): return Caja(titulo, texto)

def build(archivo, meta, contenido):
    def portada(c, doc):
        c.saveState()
        c.setFillColor(TINTA); c.rect(0, 0, W, H, stroke=0, fill=1)
        c.setStrokeColor(CEL); c.setLineWidth(3); c.setDash(14, 8); c.line(0, H - 10 * mm, W, H - 10 * mm); c.setDash()
        c.setFillColor(HexColor("#7ab6e6")); c.setFont("Courier-Bold", 10); c.drawString(M, H - 38 * mm, meta["etiqueta"])
        c.setFillColor(white); c.setFont("Helvetica-Bold", meta.get("tam", 46))
        for i, linea in enumerate(meta["titulo"]): c.drawString(M, H - 70 * mm - i * (meta.get("tam", 46) + 6), linea)
        c.setFont("Helvetica", 15); c.setFillColor(HexColor("#c9d6e3"))
        for i, linea in enumerate(meta["sub"]): c.drawString(M, H - 125 * mm - i * 22, linea)
        c.saveState(); c.translate(W - 62 * mm, 70 * mm); c.rotate(-8)
        c.setStrokeColor(CEL); c.setLineWidth(2.4); c.circle(0, 0, 30 * mm); c.setLineWidth(0.8); c.circle(0, 0, 27.5 * mm)
        c.setFillColor(CEL); c.setFont("Helvetica-Bold", 30); c.drawCentredString(0, -4, meta["sello"]); c.setFont("Courier-Bold", 8); c.drawCentredString(0, -20, meta["sello2"])
        c.restoreState()
        c.setFillColor(HexColor("#7ab6e6")); c.setFont("Courier", 9); c.drawString(M, 18 * mm, f"CuentaClara · {BASE_URL}")
        c.restoreState()
    def interior(c, doc):
        c.saveState()
        c.setStrokeColor(LINEA); c.setLineWidth(0.5); c.line(M, H - 15 * mm, W - M, H - 15 * mm)
        c.setFillColor(TINTA2); c.setFont("Courier", 8); c.drawString(M, H - 12 * mm, meta["cabecera"])
        c.drawRightString(W - M, H - 12 * mm, "KIT MONOTRIBUTISTA")
        c.line(M, 15 * mm, W - M, 15 * mm)
        c.drawString(M, 10 * mm, meta["pie"]); c.drawRightString(W - M, 10 * mm, str(doc.page - 1))
        c.restoreState()
    os.makedirs(ROOT, exist_ok=True)
    out = os.path.join(ROOT, archivo)
    doc = BaseDocTemplate(out, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=24 * mm, bottomMargin=22 * mm,
                          title=meta["nombre"], author="CuentaClara", subject=meta["nombre"])
    fr = Frame(M, 22 * mm, W - 2 * M, H - 46 * mm, id="n", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="portada", frames=[fr], onPage=portada), PageTemplate(id="interior", frames=[fr], onPage=interior)])
    f = [Spacer(1, 1), NextPageTemplate("interior"), PageBreak()] + list(contenido)
    doc.build(f)
    return out, doc.page


# ---------------------------------------------------------------- elementos visuales
from reportlab.platypus import Flowable as _Fl
OK_C = HexColor("#2f8f5b")

class Tiles(_Fl):
    """Fila de datos grandes: [(numero, rotulo), ...]."""
    def __init__(self, datos, color=CEL):
        super().__init__(); self.datos, self.color = datos, color
    def wrap(self, aw, ah):
        self.aw = aw; return aw, 62
    def draw(self):
        c = self.canv; n = len(self.datos); gap = 8; w = (self.aw - gap * (n - 1)) / n
        for i, (num, rot) in enumerate(self.datos):
            x = i * (w + gap)
            c.setFillColor(SUAVE); c.rect(x, 0, w, 56, stroke=0, fill=1)
            c.setFillColor(self.color); c.rect(x, 0, w, 3, stroke=0, fill=1)
            c.setFillColor(TINTA); c.setFont("Helvetica-Bold", 17); c.drawCentredString(x + w / 2, 30, num)
            c.setFillColor(TINTA2); c.setFont("Helvetica", 8.5)
            for j, ln in enumerate(rot.split("|")): c.drawCentredString(x + w / 2, 18 - j * 10, ln)

class Barra(_Fl):
    """Barra apilada de costos: titulo y [(rotulo, valor, color), ...]. Muestra el total al final."""
    def __init__(self, titulo, partes, unidad="USD"):
        super().__init__(); self.titulo, self.partes, self.u = titulo, partes, unidad
    def wrap(self, aw, ah):
        self.aw = aw; return aw, 62
    def draw(self):
        c = self.canv; tot = sum(v for _, v, _ in self.partes); w = self.aw - 70
        c.setFillColor(TINTA); c.setFont("Helvetica-Bold", 9.5); c.drawString(0, 48, self.titulo)
        x = 0; y = 24
        for r, v, col in self.partes:
            if v <= 0: continue
            sw = w * v / tot
            c.setFillColor(col); c.rect(x, y, sw, 16, stroke=0, fill=1)
            if sw > 60:
                c.setFillColor(white); c.setFont("Helvetica-Bold", 8); c.drawCentredString(x + sw / 2, y + 5, f"{v:,.0f}".replace(",", "."))
            x += sw
        c.setFillColor(TINTA); c.setFont("Helvetica-Bold", 10); c.drawString(w + 8, y + 4, f"{self.u} {tot:,.0f}".replace(",", "."))
        lx = 0; c.setFont("Helvetica", 8)
        for r, v, col in self.partes:
            if v <= 0: continue
            c.setFillColor(col); c.rect(lx, 6, 8, 8, stroke=0, fill=1)
            c.setFillColor(TINTA2); c.drawString(lx + 12, 7, r); lx += 22 + c.stringWidth(r, "Helvetica", 8) + 8

class Flujo(_Fl):
    """Pasos encadenados con flechas: [(titulo, detalle), ...]."""
    def __init__(self, pasos, color=CEL):
        super().__init__(); self.pasos, self.color = pasos, color
    def wrap(self, aw, ah):
        self.aw = aw; return aw, 70
    def draw(self):
        c = self.canv; n = len(self.pasos); gap = 14; w = (self.aw - gap * (n - 1)) / n
        for i, (t, d) in enumerate(self.pasos):
            x = i * (w + gap)
            c.setFillColor(white); c.setStrokeColor(self.color); c.setLineWidth(1.2); c.roundRect(x, 4, w, 60, 4, stroke=1, fill=1)
            c.setFillColor(self.color); c.circle(x + 11, 53, 7, stroke=0, fill=1)
            c.setFillColor(white); c.setFont("Helvetica-Bold", 8.5); c.drawCentredString(x + 11, 50, str(i + 1))
            c.setFillColor(TINTA); c.setFont("Helvetica-Bold", 8.8); c.drawString(x + 22, 51, t.replace("|", " "))
            c.setFillColor(TINTA2); c.setFont("Helvetica", 8)
            for j, ln in enumerate(d.split("|")): c.drawString(x + 7, 36 - j * 10, ln)
            if i < n - 1:
                c.setFillColor(self.color); ax = x + w + 2
                p = c.beginPath(); p.moveTo(ax, 28); p.lineTo(ax + gap - 4, 34); p.lineTo(ax, 40); p.close(); c.drawPath(p, stroke=0, fill=1)

class Checklist(_Fl):
    """Lista con casillas para tildar."""
    def __init__(self, items, titulo=None):
        super().__init__(); self.items, self.titulo = items, titulo
    def wrap(self, aw, ah):
        self.aw = aw; self.ps = [Paragraph(t, st("ck", fontSize=10, leading=13.5, spaceAfter=0)) for t in self.items]
        self.hs = [p.wrap(aw - 34, ah)[1] + 9 for p in self.ps]
        self.h = sum(self.hs) + (22 if self.titulo else 0); return aw, self.h
    def draw(self):
        c = self.canv; y = self.h
        if self.titulo:
            c.setFillColor(CEL); c.setFont("Courier-Bold", 8.5); c.drawString(0, y - 12, self.titulo); y -= 22
        for p, h in zip(self.ps, self.hs):
            c.setStrokeColor(TINTA2); c.setLineWidth(1); c.rect(2, y - 15, 11, 11, stroke=1, fill=0)
            p.drawOn(c, 24, y - h + 4); y -= h
            c.setStrokeColor(LINEA); c.setLineWidth(0.4); c.line(0, y + 1, self.aw, y + 1)
