import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
import gan_data as G

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "private", "ganancias.xlsx")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
AZUL = "1F4E79"; CLARO = "DDEBF7"; INPUT = "FFF2CC"; VERDE = "E2EFDA"
H = Font(bold=True, color="FFFFFF"); B = Font(bold=True)
fill = lambda c: PatternFill("solid", fgColor=c)
thin = Side(style="thin", color="BFBFBF"); box = Border(top=thin, bottom=thin, left=thin, right=thin)
ARS = '"$" #,##0.00'; PCT = '0.0%'
MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
wb = Workbook()

def title(ws, text, sub):
    ws["A1"] = text; ws["A1"].font = Font(bold=True, size=16, color=AZUL)
    ws["A2"] = sub; ws["A2"].font = Font(italic=True, color="595959")

def cab(ws, row, heads, widths, h=58):
    for i, (t, w) in enumerate(zip(heads, widths), 1):
        c = ws.cell(row=row, column=i, value=t); c.font = H; c.fill = fill(AZUL); c.border = box
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        ws.column_dimensions[c.column_letter].width = w
    ws.row_dimensions[row].height = h

def put(ws, ref, v, fmt=None, bg=None, bold=False):
    c = ws[ref]; c.value = v; c.border = box
    if fmt: c.number_format = fmt
    if bg: c.fill = fill(bg)
    if bold: c.font = B
    return c

# ---------- Inicio ----------
ws = wb.active; ws.title = "Inicio"
title(ws, "Planilla de Ganancias en el Sueldo (4ª categoría) 2026", "Mes a mes: cuánto te retienen, qué ahorrás con cada deducción del SIRADIG y cuánto cobrás. Excel y Google Sheets.")
ws.column_dimensions["A"].width = 120
lines = [
 "CÓMO USARLA",
 "1. Pestaña 'Mis datos': cargá tu sueldo bruto de cada mes (celdas amarillas), tu situación familiar y los gastos que declarás en el SIRADIG, mes por mes.",
 "2. Pestaña 'Retención mensual': calcula con el método acumulado que usa tu empleador cuánto te retienen cada mes y cuánto cobrás neto.",
 "3. Pestaña 'Resumen': impuesto del año, retenciones, y cuánto te ahorran las deducciones del SIRADIG. Sirve para decidir qué cargar antes del cierre.",
 "4. Pestañas 'Escala' y 'Deducciones': valores oficiales de ARCA para 2026 (art. 94 y art. 30). Los de julio a diciembre ya incluyen la actualización por IPC.",
 "5. Pestaña 'Parámetros': porcentaje de aportes y topes de las deducciones. Cambialos si tu caso es distinto.",
 "",
 "Celdas amarillas = las cargás vos. Celdas celestes y verdes = se calculan solas. Los datos de ejemplo se pisan o se borran.",
 "",
 "QUÉ DEDUCCIONES CONTEMPLA (SIRADIG, Formulario 572 web)",
 "Cargas de familia: cónyuge o conviviente e hijos (también incapacitados), con tope de la ganancia no imponible. Si compartís un hijo con tu pareja, cargá 0,5 por hijo.",
 "Alquiler de vivienda: 40% de lo pagado, hasta la ganancia no imponible. Servicio doméstico: lo pagado, hasta la ganancia no imponible.",
 "Gastos médicos y paramédicos: 40% de lo facturado, hasta el 5% de tu ganancia neta. Donaciones a entidades reconocidas: hasta el 5% de tu ganancia neta.",
 "Intereses de crédito hipotecario, primas de seguro de vida y cuota sindical. Aportes jubilatorios, de obra social y PAMI: porcentaje configurable (17% por defecto).",
 "Deducciones personales de ARCA: ganancia no imponible y deducción especial (empleados en relación de dependencia, art. 30 inc. c apartado 1).",
 "",
 "AVISO",
 "Herramienta de cálculo orientativa que replica el método acumulado de la retención. Tu recibo puede diferir por conceptos no remunerativos, horas extra, topes de aportes,",
 "ajustes del empleador o criterios de liquidación. Los topes de intereses hipotecarios y seguro de vida cambian cada período: cargalos en 'Parámetros'.",
 "Verificá con tu empleador o un contador antes de decidir. Para uso propio, prohibida su reventa.",
]
for i, l in enumerate(lines, 4):
    ws.cell(row=i, column=1, value=l)
    if l.startswith(("CÓMO", "QUÉ", "AVISO")): ws.cell(row=i, column=1).font = Font(bold=True, color=AZUL, size=12)

# ---------- Parámetros ----------
wp = wb.create_sheet("Parámetros")
title(wp, "Parámetros", "Cambiá lo que no coincida con tu caso.")
par = [
 ("Aportes de ley sobre el bruto (jubilación 11% + obra social 3% + PAMI 3%)", 0.17, PCT, "Si tenés otro porcentaje, cambialo."),
 ("Alquiler: porcentaje deducible", 0.40, PCT, "Se aplica sobre lo pagado en el año."),
 ("Gastos médicos: porcentaje deducible de lo facturado", 0.40, PCT, ""),
 ("Gastos médicos y donaciones: límite sobre la ganancia neta", 0.05, PCT, "Cada concepto tiene su límite."),
 ("Tope anual de intereses hipotecarios (vacío = sin tope)", None, ARS, "Cargá el tope vigente que informa ARCA para el período."),
 ("Tope anual de primas de seguro de vida (vacío = sin tope)", None, ARS, "Cargá el tope vigente que informa ARCA para el período."),
]
cab(wp, 4, ["Parámetro", "Valor", "Nota"], [66, 18, 62], 24)
for i, (t, v, f, n) in enumerate(par, 5):
    put(wp, f"A{i}", t); put(wp, f"B{i}", v, f, INPUT); put(wp, f"C{i}", n)
P_APORTE, P_ALQ, P_MED, P_LIM, P_HIP, P_SEG = (f"'Parámetros'!$B${r}" for r in range(5, 11))

# ---------- Deducciones (acumuladas por mes) ----------
wd = wb.create_sheet("Deducciones")
title(wd, "Deducciones personales acumuladas (art. 30, ARCA 2026)", "Enero a junio: tabla ARCA de enero-junio. Julio a diciembre: actualizada +16,85% por IPC. Importes acumulados al cierre de cada mes.")
cab(wd, 4, ["Mes", "N°", "Ganancia no imponible", "Cónyuge", "Hijo", "Hijo incapacitado", "Deducción especial (apartado 1)"], [16, 6, 22, 22, 22, 22, 26], 42)
for m in range(1, 13):
    d = G.deducciones(m); r = 4 + m
    put(wd, f"A{r}", MESES[m - 1]); put(wd, f"B{r}", m)
    for col, k in zip("CDEFG", ["gni", "conyuge", "hijo", "incap", "especial"]):
        put(wd, f"{col}{r}", d[k], ARS)

# ---------- Escala (por mes) ----------
we = wb.create_sheet("Escala")
title(we, "Escala del art. 94 (ARCA 2026), acumulada por mes", "Cada mes tiene su tabla: la ganancia neta acumulada se ubica en un tramo y se aplica 'fijo + % sobre el excedente'.")
cab(we, 4, ["Mes", "N°", "Tramo", "Desde", "Pagan (fijo)", "Más el %"], [16, 6, 8, 22, 22, 12], 30)
BLOQ = {}
r = 5
for m in range(1, 13):
    BLOQ[m] = (r, r + 8)
    for i, (desde, fijo, p) in enumerate(G.escala(m), 1):
        put(we, f"A{r}", MESES[m - 1]); put(we, f"B{r}", m); put(we, f"C{r}", i)
        put(we, f"D{r}", desde, ARS); put(we, f"E{r}", fijo, ARS); put(we, f"F{r}", p / 100, '0%')
        r += 1

def impuesto(m, x):
    a, b = BLOQ[m]; D = f"Escala!$D${a}:$D${b}"; E = f"Escala!$E${a}:$E${b}"; F = f"Escala!$F${a}:$F${b}"
    k = f"MATCH({x},{D},1)"
    return f"IF({x}<=0,0,INDEX({E},{k})+({x}-INDEX({D},{k}))*INDEX({F},{k}))"

# ---------- Mis datos ----------
wm = wb.create_sheet("Mis datos")
title(wm, "Mis datos", "Celdas amarillas: las cargás vos. Los números de ejemplo se pisan o se borran.")
put(wm, "A4", "¿Tenés cónyuge o conviviente a cargo? (Sí / No)", bold=True); put(wm, "C4", "No", bg=INPUT)
put(wm, "A5", "Hijos a cargo (0,5 por hijo si lo compartís con tu pareja)", bold=True); put(wm, "C5", 1, '0.0', INPUT)
put(wm, "A6", "Hijos incapacitados para el trabajo", bold=True); put(wm, "C6", 0, '0.0', INPUT)
dv = DataValidation(type="list", formula1='"Sí,No"', allow_blank=False); wm.add_data_validation(dv); dv.add("C4")
heads = ["Mes", "Sueldo bruto mensual", "Aguinaldo (SAC) bruto", "Otros ingresos del mes (horas extra, bonos)", "Alquiler pagado", "Servicio doméstico pagado",
         "Gastos médicos facturados", "Donaciones", "Intereses hipotecarios", "Prima de seguro de vida", "Cuota sindical"]
cab(wm, 9, heads, [52, 20, 18, 22, 16, 18, 18, 16, 16, 16, 16], 62)
for i, m in enumerate(MESES):
    r = 10 + i
    put(wm, f"A{r}", m)
    put(wm, f"B{r}", 3000000, ARS, INPUT)
    put(wm, f"C{r}", "=MAX(B10:B15)/2" if i == 5 else "=MAX(B16:B21)/2" if i == 11 else 0, ARS, INPUT)
    put(wm, f"D{r}", 0, ARS, INPUT)
    put(wm, f"E{r}", 600000, ARS, INPUT)
    for col in "FGHIJK": put(wm, f"{col}{r}", 0, ARS, INPUT)
wm["A23"] = "El aguinaldo de junio y diciembre se propone como la mitad del mayor sueldo del semestre. Pisalo si cobrás otra cosa."
wm["A23"].font = Font(italic=True, color="595959")
wm.freeze_panes = "B10"

# ---------- Retención mensual ----------
wr = wb.create_sheet("Retención mensual")
title(wr, "Retención mensual (método acumulado)", "Cada mes: ganancia neta acumulada, impuesto acumulado y lo que te retienen en ese mes. Negativo = te lo devuelven.")
hd = ["Mes", "Bruto del mes", "Bruto acumulado", "Aportes acumulados", "Cuota sindical acumulada", "Alquiler deducible", "Servicio doméstico deducible",
      "Intereses hipotecarios deducibles", "Seguro de vida deducible", "Ganancia neta antes de médicos y donaciones", "Gastos médicos deducibles", "Donaciones deducibles",
      "Deducciones personales acumuladas", "Ganancia neta sujeta a impuesto", "Impuesto acumulado", "Retenido en meses anteriores", "Retención del mes", "Cobrás neto (aprox.)"]
cab(wr, 4, hd, [14] + [19] * 17, 74)
MD = "'Mis datos'!"
for i in range(12):
    m = i + 1; r = 5 + i; d = 10 + i
    sm = lambda col: f"SUM({MD}${col}$10:{col}{d})"
    put(wr, f"A{r}", MESES[i])
    put(wr, f"B{r}", f"={MD}B{d}+{MD}C{d}+{MD}D{d}", ARS, CLARO)
    put(wr, f"C{r}", f"=SUM(B$5:B{r})", ARS, CLARO)
    put(wr, f"D{r}", f"=C{r}*{P_APORTE}", ARS, CLARO)
    put(wr, f"E{r}", f"={sm('K')}", ARS, CLARO)
    gni = f"Deducciones!$C${4 + m}"
    put(wr, f"F{r}", f"=MIN({sm('E')}*{P_ALQ},{gni})", ARS, CLARO)
    put(wr, f"G{r}", f"=MIN({sm('F')},{gni})", ARS, CLARO)
    put(wr, f"H{r}", f'=IF({P_HIP}="",{sm("I")},MIN({sm("I")},{P_HIP}*{m}/12))', ARS, CLARO)
    put(wr, f"I{r}", f'=IF({P_SEG}="",{sm("J")},MIN({sm("J")},{P_SEG}*{m}/12))', ARS, CLARO)
    put(wr, f"J{r}", f"=MAX(0,C{r}-D{r}-E{r}-F{r}-G{r}-H{r}-I{r})", ARS, CLARO)
    put(wr, f"K{r}", f"=MIN({sm('G')}*{P_MED},{P_LIM}*J{r})", ARS, CLARO)
    put(wr, f"L{r}", f"=MIN({sm('H')},{P_LIM}*J{r})", ARS, CLARO)
    dr = 4 + m
    cargas = f"IF('Mis datos'!$C$4=\"Sí\",Deducciones!$D${dr},0)+'Mis datos'!$C$5*Deducciones!$E${dr}+'Mis datos'!$C$6*Deducciones!$F${dr}"
    put(wr, f"M{r}", f"=Deducciones!$C${dr}+MIN({cargas},Deducciones!$C${dr})+Deducciones!$G${dr}", ARS, CLARO)
    put(wr, f"N{r}", f"=MAX(0,J{r}-K{r}-L{r}-M{r})", ARS, CLARO)
    put(wr, f"O{r}", "=" + impuesto(m, f"N{r}"), ARS, CLARO)
    put(wr, f"P{r}", f"=SUM(Q$4:Q{r-1})" if i else 0, ARS, CLARO)
    put(wr, f"Q{r}", f"=O{r}-P{r}", ARS, VERDE, True)
    put(wr, f"R{r}", f"=B{r}-B{r}*{P_APORTE}-{MD}K{d}-Q{r}", ARS, VERDE, True)
wr.freeze_panes = "B5"

# ---------- Resumen ----------
wz = wb.create_sheet("Resumen")
title(wz, "Resumen del año", "Con los datos de 'Mis datos' y las escalas de ARCA de diciembre 2026.")
wz.column_dimensions["A"].width = 72; wz.column_dimensions["B"].width = 24
RR = "'Retención mensual'!"
filas = [
 ("Bruto anual (con aguinaldo)", f"={RR}C16"),
 ("Aportes de ley del año", f"={RR}D16"),
 ("Ganancia neta sujeta a impuesto", f"={RR}N16"),
 ("Impuesto a las Ganancias del año", f"={RR}O16"),
 ("Retenciones mes a mes (suma)", f"=SUM({RR}Q5:Q16)"),
 ("Alícuota efectiva sobre el bruto", "=IF(B4=0,0,B7/B4)"),
 ("Sueldo neto anual aproximado", f"=SUM({RR}R5:R16)"),
 ("", None),
 ("SI NO CARGARAS NADA EN EL SIRADIG (solo deducciones personales y cargas)", None),
 ("Ganancia neta sujeta a impuesto sin deducciones del SIRADIG", f"=MAX(0,{RR}C16-{RR}D16-{RR}M16)"),
 ("Impuesto sin deducciones del SIRADIG", "=" + impuesto(12, "B13")),
 ("LO QUE TE AHORRAN LAS DEDUCCIONES DEL SIRADIG", "=B14-B7"),
 ("Ahorro por mes (promedio)", "=B15/12"),
]
for i, (t, f) in enumerate(filas, 4):
    c = wz.cell(row=i, column=1, value=t)
    if f:
        c.border = box
        put(wz, f"B{i}", f, PCT if "Alícuota" in t else ARS, VERDE if "AHORRAN" in t else CLARO, "AHORRAN" in t)
    if t.startswith(("SI NO", "LO QUE")): c.font = Font(bold=True, color=AZUL)
wz["A18"] = "La alícuota efectiva y los netos son aproximados: no incluyen conceptos no remunerativos ni ajustes que haga tu empleador."
wz["A18"].font = Font(italic=True, color="595959")

orden = ["Inicio", "Mis datos", "Retención mensual", "Resumen", "Parámetros", "Deducciones", "Escala"]
wb._sheets = [wb[n] for n in orden]
for w in wb.worksheets: w.sheet_view.showGridLines = False
wb.save(OUT); print("ok", OUT)
