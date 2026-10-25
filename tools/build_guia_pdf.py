"""Genera private/guia.pdf (Primer año de monotributo) y private/pack-kitguia.zip. Requiere reportlab (solo local): python tools/build_guia_pdf.py"""
import os, sys, zipfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_site import CATS, ars
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, NextPageTemplate, Flowable

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "private")
TINTA, TINTA2, CEL, SUAVE, LINEA, SELLO = HexColor("#10263d"), HexColor("#4b5e72"), HexColor("#3f8fcf"), HexColor("#e6f1fa"), HexColor("#d6dfe8"), HexColor("#b3343c")
W, H = A4
M = 22 * mm

def st(name, **k):
    base = dict(fontName="Helvetica", fontSize=10.5, leading=15.5, textColor=TINTA, spaceAfter=7, alignment=TA_LEFT)
    base.update(k)
    return ParagraphStyle(name, **base)

S = {
    "p": st("p"),
    "h1": st("h1", fontName="Helvetica-Bold", fontSize=25, leading=28, spaceAfter=6, spaceBefore=0),
    "h2": st("h2", fontName="Helvetica-Bold", fontSize=14, leading=18, spaceBefore=12, spaceAfter=5),
    "et": st("et", fontName="Courier-Bold", fontSize=8.5, leading=11, textColor=CEL, spaceAfter=8),
    "baj": st("baj", fontSize=12.5, leading=18, textColor=TINTA2, spaceAfter=12),
    "li": st("li", leftIndent=14, bulletIndent=2, spaceAfter=4),
    "nota": st("nota", fontSize=9, leading=13, textColor=TINTA2),
    "cell": st("cell", fontSize=9.5, leading=13, spaceAfter=0),
    "cellb": st("cellb", fontName="Helvetica-Bold", fontSize=9.5, leading=13, spaceAfter=0),
    "num": st("num", fontName="Courier", fontSize=9, leading=12, spaceAfter=0),
}

class Caja(Flowable):
    """Recuadro con borde celeste a la izquierda (consejo o alerta)."""
    def __init__(self, titulo, texto, color=CEL, fondo=SUAVE):
        super().__init__()
        self.titulo, self.texto, self.color, self.fondo = titulo, texto, color, fondo
    def wrap(self, aw, ah):
        self.aw = aw
        self.p1 = Paragraph(self.titulo, st("ct", fontName="Courier-Bold", fontSize=8.5, leading=11, textColor=self.color, spaceAfter=3))
        self.p2 = Paragraph(self.texto, st("cx", fontSize=10, leading=14.5, spaceAfter=0))
        w = aw - 26
        h1 = self.p1.wrap(w, ah)[1]; h2 = self.p2.wrap(w, ah)[1]
        self.h = h1 + h2 + 22
        return aw, self.h + 8
    def draw(self):
        c = self.canv
        c.setFillColor(self.fondo); c.rect(0, 4, self.aw, self.h, stroke=0, fill=1)
        c.setFillColor(self.color); c.rect(0, 4, 3.5, self.h, stroke=0, fill=1)
        self.p1.drawOn(c, 16, 4 + self.h - 11 - self.p1.height)
        self.p2.drawOn(c, 16, 4 + 11 - 0 + 0)

def P(t, s="p"): return Paragraph(t, S[s])
def L(items): return [Paragraph(i, S["li"], bulletText="•") for i in items]
def H2(t): return Paragraph(t, S["h2"])

def cap(num, et, titulo, baj=None):
    out = [Paragraph(f"CAPÍTULO {num} · {et}", S["et"]), Paragraph(titulo, S["h1"])]
    if baj: out.append(Paragraph(baj, S["baj"]))
    return out

def tabla(cols, filas, widths, mono_from=None):
    data = [[Paragraph(f"<b>{c}</b>", st("th", fontName="Helvetica-Bold", fontSize=8.5, leading=11, textColor=TINTA2, spaceAfter=0)) for c in cols]]
    for f in filas:
        data.append([Paragraph(str(c), S["cellb"] if i == 0 else S["cell"]) for i, c in enumerate(f)])
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), SUAVE), ("LINEBELOW", (0, 0), (-1, 0), 0.8, CEL),
        ("LINEBELOW", (0, 1), (-1, -1), 0.4, LINEA), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5), ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6)]))
    return t

def portada(c, doc):
    c.saveState()
    c.setFillColor(TINTA); c.rect(0, 0, W, H, stroke=0, fill=1)
    c.setStrokeColor(CEL); c.setLineWidth(3); c.setDash(14, 8); c.line(0, H - 10 * mm, W, H - 10 * mm); c.setDash()
    c.setFillColor(HexColor("#7ab6e6")); c.setFont("Courier-Bold", 10); c.drawString(M, H - 38 * mm, "GUÍA PRÁCTICA · ACTUALIZADA A OCTUBRE DE 2026")
    c.setFillColor(white); c.setFont("Helvetica-Bold", 52)
    for i, linea in enumerate(["Primer año", "de monotributo"]): c.drawString(M, H - 70 * mm - i * 58, linea)
    c.setFont("Helvetica", 15); c.setFillColor(HexColor("#c9d6e3"))
    for i, linea in enumerate(["Cómo darte de alta, facturar, pagar y recategorizarte", "sin errores caros. En lenguaje claro, paso a paso."]): c.drawString(M, H - 120 * mm - i * 22, linea)
    c.saveState(); c.translate(W - 62 * mm, 70 * mm); c.rotate(-8)
    c.setStrokeColor(CEL); c.setLineWidth(2.4); c.circle(0, 0, 30 * mm); c.setLineWidth(0.8); c.circle(0, 0, 27.5 * mm)
    c.setFillColor(CEL); c.setFont("Helvetica-Bold", 34); c.drawCentredString(0, -4, "A–K"); c.setFont("Courier-Bold", 8); c.drawCentredString(0, -20, "MONOTRIBUTO")
    c.restoreState()
    c.setFillColor(HexColor("#7ab6e6")); c.setFont("Courier", 9); c.drawString(M, 18 * mm, "CuentaClara · kit-monotributo.fernandezfrancowork.workers.dev")
    c.restoreState()

def interior(c, doc):
    c.saveState()
    c.setStrokeColor(LINEA); c.setLineWidth(0.5); c.line(M, H - 15 * mm, W - M, H - 15 * mm)
    c.setFillColor(TINTA2); c.setFont("Courier", 8); c.drawString(M, H - 12 * mm, "PRIMER AÑO DE MONOTRIBUTO")
    c.drawRightString(W - M, H - 12 * mm, "KIT MONOTRIBUTISTA")
    c.line(M, 15 * mm, W - M, 15 * mm)
    c.drawString(M, 10 * mm, "Información general. No reemplaza a un contador ni a la información oficial de ARCA.")
    c.drawRightString(W - M, 10 * mm, str(doc.page - 1))
    c.restoreState()

def contenido():
    f = []
    f.append(NextPageTemplate("interior")); f.append(PageBreak())
    # Indice + intro
    f += cap("0", "ANTES DE EMPEZAR", "Cómo usar esta guía", "Pensada para quien se inscribe por primera vez. Se lee en media hora y se consulta durante todo el año.")
    f.append(P("El Monotributo es un régimen simplificado: pagás una cuota mensual fija que junta el impuesto integrado (reemplaza al IVA y a Ganancias), tu aporte jubilatorio y la obra social. A cambio, no presentás declaraciones juradas complicadas. Lo que sí tenés que hacer es <b>facturar cada venta, pagar cada mes y recategorizarte dos veces por año</b>. Casi todos los problemas del primer año salen de olvidarse de una de esas tres cosas."))
    f.append(tabla(["Capítulo", "Qué resuelve"], [
        ("1. El alta", "Qué necesitás y cómo inscribirte en ARCA, paso a paso."),
        ("2. Tu categoría", "Cómo elegir la primera categoría y cuánto vas a pagar."),
        ("3. Facturar", "Factura C, punto de venta y qué completar."),
        ("4. Pagar la cuota", "Cuándo vence, cómo se paga y qué pasa si no."),
        ("5. Recategorización", "Calendario, qué se mira y la multa del 50%."),
        ("6. Ingresos Brutos", "El impuesto provincial que no incluye la cuota."),
        ("7. Errores caros", "Los 12 que más se repiten y cómo evitarlos."),
        ("8. Calendario", "Tu primer año, mes por mes.")], [38 * mm, W - 2 * M - 38 * mm]))
    f.append(Spacer(1, 12))
    f.append(Caja("CÓMO LEER LOS CUADROS", "Los recuadros celestes son consejos. Los rojos son <b>alertas</b>: errores que cuestan plata o te sacan del régimen."))
    f.append(P("Los importes y fechas de esta guía corresponden a las escalas vigentes de agosto de 2026 a enero de 2027. Cambian dos veces por año: antes de decidir algo con plata, confirmalos en ARCA.", "nota"))
    f.append(PageBreak())

    # 1 Alta
    f += cap("1", "EL ALTA", "Inscribirte en el Monotributo", "Se hace online, es gratis y lleva unos 20 minutos si tenés todo a mano.")
    f.append(H2("Qué necesitás antes"))
    f += L(["<b>CUIL o CUIT</b> (si trabajaste alguna vez en blanco ya tenés CUIL; el alta lo convierte en CUIT).",
            "<b>Clave Fiscal nivel 3 o superior.</b> Se obtiene desde la web de ARCA validando tu identidad (con la app o en una oficina). Si todavía no la tenés, empezá por acá, porque es lo que más demora.",
            "<b>Un email y un teléfono</b> de contacto que uses de verdad: ahí llegan los avisos.",
            "<b>Tu domicilio</b> real y, si tenés local u oficina, el domicilio de la actividad.",
            "<b>Qué vas a hacer</b>: la actividad que vas a facturar, explicada en una frase, y una estimación de cuánto vas a facturar en el año."])
    f.append(H2("Paso a paso"))
    for i, t in enumerate([
        "Entrá a arca.gob.ar con tu CUIT y Clave Fiscal.",
        "Abrí el servicio <b>Monotributo</b>. Si no aparece en tu panel, agregalo desde \"Administrador de Relaciones de Clave Fiscal\".",
        "Elegí <b>Inscripción</b> y completá tus datos personales y de contacto.",
        "Cargá la <b>actividad</b> que vas a realizar. Elegí la que mejor describa lo que facturás; después podés sumar otras.",
        "Indicá si es <b>servicios</b> o <b>venta de bienes</b> y completá los parámetros (superficie, energía y alquiler si tenés local).",
        "Elegí tu <b>categoría</b> (capítulo 2) y tu <b>obra social</b>.",
        "Revisá todo, confirmá y <b>guardá el comprobante</b> de inscripción."], 1):
        f.append(Paragraph(f"<b>{i}.</b>&nbsp; {t}", st("pa", leftIndent=16, firstLineIndent=-16, spaceAfter=5)))
    f.append(Spacer(1, 4))
    f.append(Caja("DESPUÉS DEL ALTA, EL MISMO DÍA", "Habilitá tu punto de venta para facturar (capítulo 3) y activá el <b>Domicilio Fiscal Electrónico</b>: es donde ARCA te notifica. Una notificación que no abrís igual corre los plazos."))
    f.append(P("Con el alta tenés además la <b>Constancia de Inscripción</b>, el documento que te piden clientes, bancos y plataformas para verificar que sos monotributista. Descargala desde el servicio \"Constancia de Inscripción\" cada vez que la necesites: siempre se emite actualizada.", "p"))
    f.append(PageBreak())

    # 2 Categoría
    f += cap("2", "TU CATEGORÍA", "Elegir tu primera categoría", "Es la decisión más importante del año: define cuánto pagás y hasta cuánto podés facturar.")
    f.append(P("La categoría depende, sobre todo, de tus <b>ingresos brutos de los últimos 12 meses</b>. También cuentan la superficie del local, la energía eléctrica consumida y el alquiler que pagás por el lugar de trabajo. Si algún parámetro excede el límite de una categoría, te corresponde la siguiente."))
    f.append(tabla(["Cat.", "Ingresos brutos anuales hasta", "Cuota mensual servicios", "Cuota mensual bienes"],
                   [(c, ars(t), ars(s), ars(b)) for c, t, s, b in CATS],
                   [14 * mm, 52 * mm, 52 * mm, W - 2 * M - 118 * mm]))
    f.append(P("Escalas vigentes de agosto 2026 a enero 2027. Fuente: ARCA.", "nota"))
    f.append(H2("Cómo elegir sin pasarte"))
    f += L(["Estimá cuánto vas a facturar en tus <b>primeros 12 meses</b>, con prudencia: contá los meses flojos.",
            "Buscá esa cifra en la tabla. Si estás justo en el borde, elegí la categoría siguiente: pagás un poco más pero evitás tener que subir enseguida.",
            "Elegir una categoría <b>más baja</b> de la que te corresponde para pagar menos sale caro: en la recategorización te cobran la diferencia y puede haber multa.",
            "Servicios y bienes pagan lo mismo hasta la categoría B; desde la C la cuota de servicios es más alta."])
    f.append(Caja("EJEMPLO", "Mariana diseña logos y piensa facturar unos $ 800.000 por mes. Son $ 9.600.000 al año: entra en la <b>categoría A</b> (tope $ 12.009.410,45). Como puede crecer, deja margen: si sube a $ 1.000.000 por mes (12 millones) está al límite y va a cambiar de categoría en la primera recategorización."))
    f.append(P("Para ver tu categoría con tus números, usá la <b>calculadora gratis</b> en la web del Kit Monotributista.", "nota"))
    f.append(PageBreak())

    # 3 Facturar
    f += cap("3", "FACTURAR", "Factura C, paso a paso", "Como monotributista emitís <b>Factura C</b>. No discrimina IVA: el importe que ponés es el que cobra el cliente.")
    f.append(H2("Habilitar el punto de venta"))
    f.append(P("Antes de la primera factura necesitás un punto de venta. En el servicio <b>\"Administración de Puntos de Venta y Domicilios\"</b> agregá uno y elegí el sistema <b>\"Factura en Línea - Monotributo\"</b> (o \"Monotributo - Web Services\" si vas a usar un programa). El mismo domicilio de la actividad sirve para todos."))
    f.append(H2("Emitir una factura"))
    for i, t in enumerate([
        "Entrá al servicio <b>Comprobantes en línea</b> (o a la app Mi ARCA, desde el celular).",
        "Elegí tu punto de venta y el tipo de comprobante: <b>Factura C</b>.",
        "Indicá concepto: <i>Productos</i>, <i>Servicios</i> o <i>Productos y Servicios</i>. Si es servicio, completá el período facturado.",
        "Cargá los datos del cliente. A un consumidor final se le puede emitir sin identificar, salvo que el monto supere el límite que fija ARCA. A una empresa le pedís el CUIT.",
        "Describí lo vendido con claridad (qué, cuánto, cuándo) e ingresá el importe.",
        "Confirmá. Se genera con su <b>CAE</b> y código QR. Descargá el PDF y enviáselo al cliente."], 1):
        f.append(Paragraph(f"<b>{i}.</b>&nbsp; {t}", st("pa", leftIndent=16, firstLineIndent=-16, spaceAfter=5)))
    f.append(H2("Reglas que conviene tener claras"))
    f += L(["<b>Se factura cuando se vende o se presta el servicio</b>, no cuando cobrás, y siempre con el nombre del que paga. La factura de un cobro no la puede hacer otra persona.",
            "<b>Todas las ventas llevan factura</b>, incluso las chicas, en efectivo o por transferencia. Es lo que respalda tu categoría.",
            "Una factura emitida <b>no se borra</b>: si te equivocaste, se corrige con una nota de crédito.",
            "Guardá copia de todo (PDF) durante varios años. Los pedidos de bancos y plataformas llegan tarde.",
            "Una factura \"a nombre de la cuenta del cliente\" o a un tercero solo si de verdad es el que compra."])
    f.append(Caja("ALERTA: FACTURA DE MÁS DE LA CATEGORÍA", "El total facturado en 12 meses es lo que mide ARCA. Revisalo cada mes (en el Kit Monotributista se hace solo): si te pasás del tope sin darte cuenta, en la próxima recategorización subís de categoría.", SELLO, HexColor("#f6e3e4")))
    f.append(PageBreak())

    # 4 Pagar
    f += cap("4", "PAGAR LA CUOTA", "Cuándo y cómo se paga", "La cuota mensual vence el <b>día 20 de cada mes</b>. Si cae en un día no hábil, pasa al siguiente hábil.")
    f.append(P("Lo que pagás cada mes tiene tres partes: el <b>impuesto integrado</b>, el <b>aporte jubilatorio</b> (SIPA) y la <b>obra social</b>. Los dos últimos son lo que te da acceso a la jubilación y a la cobertura de salud, por eso conviene pagar siempre, aunque ese mes no hayas vendido."))
    f.append(H2("Medios de pago"))
    f += L(["<b>Débito automático</b> desde cuenta bancaria o tarjeta de crédito: el más cómodo, se activa desde el servicio de Monotributo. Evita olvidos.",
            "<b>VEP</b> (volante electrónico de pago) desde home banking o desde Mercado Pago.",
            "<b>Pago desde billeteras virtuales</b> y puntos de pago presenciales con el código del VEP."])
    f.append(P("Después de pagar, el sistema acredita la cuota (puede demorar un día). Guardá el comprobante: es la prueba si más adelante figura una deuda por error."))
    f.append(H2("Qué pasa si no pagás"))
    f += L(["La deuda <b>suma intereses</b> mes a mes y ARCA puede reclamarla.",
            "Sin cuotas pagas <b>no estás cubierto</b> por la obra social y no sumás aportes jubilatorios.",
            "Dejarlo sin pagar durante muchos meses puede terminar en la <b>baja de oficio</b>, que te obliga a volver a empezar y a regularizar lo adeudado.",
            "Si no vas a trabajar por un tiempo, no dejes de pagar: da de baja la actividad. Es más barato que acumular deuda."])
    f.append(Caja("CONSEJO", "Poné un recordatorio el día 15 de cada mes. Si activás el débito automático, igual verificá que el débito haya salido: un rechazo por falta de saldo cuenta como cuota impaga."))
    f.append(H2("Si querés dejar el régimen"))
    f.append(P("Podés darte de baja desde el mismo servicio de Monotributo, siempre que no tengas deuda. La baja <b>no cancela</b> lo ya adeudado: se cancela cuando regularizás los pagos. Para pasar a otro régimen (por ejemplo responsable inscripto) consultalo antes con un contador."))
    f.append(PageBreak())

    # 5 Recategorización
    f += cap("5", "RECATEGORIZACIÓN", "Dos veces por año, sin falta", "Es obligatoria aunque no cambie tu categoría. Se hace en febrero y en agosto.")
    f.append(P("Cada semestre tenés que revisar si tu categoría sigue siendo la correcta. La de <b>febrero</b> mira lo facturado de enero a diciembre del año anterior; la de <b>agosto</b>, de julio a junio. Vence el 5 del mes: confirmá el día exacto en ARCA, porque a veces se corre."))
    f.append(H2("Qué se mira"))
    f += L(["<b>Ingresos brutos</b> de los últimos 12 meses (todo lo facturado, sin descontar gastos).",
            "<b>Alquileres devengados</b> en ese período.",
            "<b>Superficie</b> afectada a la actividad.",
            "<b>Energía eléctrica</b> consumida en el año."])
    f.append(P("Si ninguno superó los límites de tu categoría, no cambia nada, pero tenés que confirmarla. Si alguno los superó, <b>subís</b>. Si quedaste por debajo de los de la categoría anterior, podés <b>bajar</b> y pagar menos."))
    f.append(H2("Cómo se hace"))
    for i, t in enumerate(["Entrá a arca.gob.ar con tu CUIT y Clave Fiscal.", "Abrí el servicio de <b>Monotributo</b> y elegí <b>Recategorización</b>.", "Revisá los datos de los últimos 12 meses.", "Confirmá tu categoría actual o elegí la nueva.", "<b>Guardá el comprobante</b>."], 1):
        f.append(Paragraph(f"<b>{i}.</b>&nbsp; {t}", st("pa", leftIndent=16, firstLineIndent=-16, spaceAfter=4)))
    f.append(Spacer(1, 4))
    f.append(Caja("ALERTA: LA MULTA DEL 50%", "Si te correspondía subir y no te recategorizaste, la multa es del <b>50%</b> sobre el impuesto integrado y los aportes que debías pagar. Además, ARCA puede recategorizarte de oficio si cruza tus acreditaciones bancarias, compras o gastos con lo que declaraste. Te avisa por el Domicilio Fiscal Electrónico y tenés 15 días para presentar un descargo.", SELLO, HexColor("#f6e3e4")))
    f.append(H2("Tu primera recategorización"))
    f.append(P("Si te inscribiste hace menos de 12 meses, no tenés un año completo de ingresos. En ese caso ARCA considera lo facturado desde el alta y lo proyecta a 12 meses para comparar con los topes. Confirmá en ARCA el criterio vigente: es la recategorización en la que más gente se equivoca."))
    f.append(PageBreak())

    # 6 IIBB
    f += cap("6", "INGRESOS BRUTOS", "El impuesto que la cuota no incluye", "Ingresos Brutos (IIBB) es un impuesto <b>provincial</b>. Se paga aparte de la cuota del Monotributo.")
    f.append(P("Cada provincia (y la Ciudad de Buenos Aires) tiene su propio régimen. Algunas ofrecen un <b>régimen simplificado</b> para monotributistas con una cuota fija por categoría; otras tienen alícuotas sobre lo facturado. Por eso no podemos darte un número único: depende de dónde vivís y de cuál es tu actividad."))
    f.append(H2("Qué hacer en el primer mes"))
    f += L(["Entrá a la web de tu agencia provincial de rentas (ARBA, AGIP, API, DGR, según tu provincia) y buscá <b>\"inscripción de monotributista en Ingresos Brutos\"</b>.",
            "Averiguá si corresponde el <b>régimen simplificado</b> y qué cuota pagarías según tu categoría y actividad.",
            "Si vendés a clientes de <b>otras provincias</b>, consultá si te corresponde el Convenio Multilateral.",
            "Algunas actividades y provincias tienen exenciones o alícuotas reducidas: preguntalo, no lo supongas."])
    f.append(Caja("OJO CON LAS RETENCIONES", "Los bancos y las billeteras virtuales pueden <b>retener o percibir</b> IIBB cuando te acreditan cobros. Si estás inscripto, esas retenciones suelen descontarse del impuesto; si no te inscribiste, las perdés. Revisá tus extractos."))
    f.append(H2("Tasas municipales"))
    f.append(P("Si tenés local u oficina habilitada, el municipio cobra una tasa de comercio e industria (o similar). Se tramita en la municipalidad y es independiente de ARCA y de la provincia. Trabajando desde tu casa, consultá si tu municipio te exige alguna habilitación."))
    f.append(PageBreak())

    # 7 Errores
    f += cap("7", "ERRORES CAROS", "Los 12 errores del primer año", "Todos se evitan con un hábito sencillo.")
    errores = [
        ("No facturar ventas chicas", "Cada venta sin factura es ingreso no declarado. Si ARCA cruza tus acreditaciones, la diferencia te pone en otra categoría con multa.", "Facturá todo, siempre, el mismo día."),
        ("Elegir categoría de menos", "Pagar menos al inicio se paga después, con diferencias e intereses.", "Elegí con margen y revisá cada mes."),
        ("No recategorizarse", "Es una obligación, aunque no cambie nada. La multa por omisión es del 50%.", "Calendario: febrero y agosto, con alarma."),
        ("Mirar solo el mes, no los 12", "El tope se mide sobre los últimos 12 meses móviles, no por mes.", "Llevá la suma acumulada actualizada."),
        ("Mezclar plata personal y del negocio", "Hace imposible explicar de dónde sale cada ingreso y dificulta el cruce con ARCA.", "Abrí una cuenta o billetera sólo para cobrar."),
        ("Olvidarte de Ingresos Brutos", "Es el impuesto que más sorprende: se acumula sin que lo veas.", "Inscribite el primer mes (capítulo 6)."),
        ("No pagar por «no facturé»", "La cuota es fija, se facture o no. No pagar acumula deuda.", "Débito automático o baja de la actividad."),
        ("No abrir el Domicilio Fiscal Electrónico", "Las intimaciones corren desde que llegan, las leas o no.", "Revisalo al menos una vez por semana."),
        ("Facturar a terceros", "La factura debe ir al nombre de quien paga.", "Pedí los datos del cliente real."),
        ("Actividad mal cargada", "Si facturás algo que no declaraste, queda fuera de tu inscripción.", "Sumá las actividades que realmente hacés."),
        ("Perder los comprobantes", "Sin respaldo no podés defender tu categoría ante un reclamo.", "Una carpeta por año, con PDF de todo."),
        ("Ignorar el tope de exclusión", "Pasarte de la categoría K te saca del régimen: pasás a responsable inscripto.", "Proyectá con anticipación y consultá un contador."),
    ]
    f.append(tabla(["Error", "Por qué cuesta", "Cómo evitarlo"], errores, [48 * mm, 70 * mm, W - 2 * M - 118 * mm]))
    f.append(PageBreak())

    # 8 Calendario
    f += cap("8", "CALENDARIO", "Tu primer año, mes por mes", "Imprimilo o guardalo en el celular.")
    f.append(tabla(["Cuándo", "Qué hacer"], [
        ("Semana del alta", "Alta en ARCA · punto de venta · Domicilio Fiscal Electrónico · inscripción en Ingresos Brutos · activar débito automático."),
        ("Todos los meses, antes del 20", "Pagar la cuota. Verificar que el pago figure acreditado."),
        ("Todos los meses", "Facturar cada venta. Sumar la facturación acumulada de los últimos 12 meses y compararla con el tope de tu categoría."),
        ("Cada semana", "Mirar el Domicilio Fiscal Electrónico."),
        ("Febrero", "Recategorización (vence el 5). Se mira enero a diciembre del año anterior."),
        ("Agosto", "Recategorización (vence el 5). Se mira julio a junio."),
        ("Diciembre / enero", "Revisar cuánto facturaste en el año. Si vas a pasarte del tope, hablalo con un contador antes."),
        ("Si cambiás de actividad o de domicilio", "Actualizarlo en ARCA en el momento. No esperar a la recategorización.")], [48 * mm, W - 2 * M - 48 * mm]))
    f.append(Spacer(1, 10))
    f.append(H2("Glosario mínimo"))
    f.append(tabla(["Término", "Significa"], [
        ("ARCA", "Agencia de Recaudación y Control Aduanero. Antes AFIP."),
        ("Clave Fiscal", "Tu acceso a los servicios de ARCA. Nivel 3 o superior para el Monotributo."),
        ("CAE", "Código de autorización de la factura electrónica."),
        ("Impuesto integrado", "La parte de la cuota que reemplaza a IVA y Ganancias."),
        ("SIPA", "Sistema Integrado Previsional: tu aporte para la jubilación."),
        ("VEP", "Volante electrónico de pago."),
        ("CLAE", "Código de actividad económica.")], [38 * mm, W - 2 * M - 38 * mm]))
    f.append(PageBreak())

    # Cierre
    f += cap("+", "PARA SEGUIR", "Una cosa menos para acordarte")
    f.append(P("Si llegaste hasta acá, ya sabés lo que hace falta. Lo que más se olvida es <b>llevar la cuenta de los últimos 12 meses</b>: el Kit Monotributista lo hace por vos."))
    f += L(["Cargás cada factura con fecha e importe.", "La planilla calcula tu facturación de los últimos 12 meses y la categoría que te corresponde.", "Te avisa cuánto margen te queda antes de subir de categoría o de la exclusión.", "Proyecta tu ritmo de los últimos 3 meses y alerta antes de que te pases."])
    f.append(Caja("KIT MONOTRIBUTISTA 2026", "Planilla para Excel y Google Sheets, con las escalas editables para cuando cambien. kit-monotributo.fernandezfrancowork.workers.dev"))
    f.append(Spacer(1, 10))
    f.append(P("Aviso importante", "h2"))
    f.append(P("Esta guía es información general y educativa, actualizada a octubre de 2026. No constituye asesoramiento profesional, contable ni legal, y no reemplaza a un contador ni a la información oficial de ARCA. Los importes, fechas y reglas pueden cambiar. Confirmá los datos vigentes en arca.gob.ar antes de tomar decisiones. Está prohibida su reventa o redistribución.", "nota"))
    return f

def main():
    os.makedirs(ROOT, exist_ok=True)
    out = os.path.join(ROOT, "guia.pdf")
    doc = BaseDocTemplate(out, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=24 * mm, bottomMargin=22 * mm,
                          title="Primer año de monotributo", author="CuentaClara", subject="Guía práctica de Monotributo 2026")
    fr = Frame(M, 22 * mm, W - 2 * M, H - 46 * mm, id="n", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="portada", frames=[fr], onPage=portada), PageTemplate(id="interior", frames=[fr], onPage=interior)])
    doc.build([Spacer(1, 1)] + contenido())
    z = os.path.join(ROOT, "pack-kitguia.zip")
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(os.path.join(ROOT, "kit.xlsx"), "Kit-Monotributista-2026.xlsx")
        zf.write(out, "Guia-Primer-Anio-Monotributo.pdf")
    print("ok", os.path.getsize(out), os.path.getsize(z))

if __name__ == "__main__":
    main()
