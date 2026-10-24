import os, datetime
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import Rule
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.workbook.defined_name import DefinedName

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "private", "liquidacion.xlsx")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
AZUL = "1F4E79"; CLARO = "DDEBF7"; INPUT = "FFF2CC"; ROJO = "F8CBAD"
H = Font(bold=True, color="FFFFFF"); B = Font(bold=True)
fill = lambda c: PatternFill("solid", fgColor=c)
thin = Side(style="thin", color="BFBFBF"); box = Border(top=thin, bottom=thin, left=thin, right=thin)
ARS = '"$" #,##0.00'; FECHA = "dd/mm/yyyy"
N0, N1 = 8, 37          # 30 personas
D = datetime.date
wb = Workbook()

def title(ws, text, sub):
    ws["A1"] = text; ws["A1"].font = Font(bold=True, size=16, color=AZUL)
    ws["A2"] = sub; ws["A2"].font = Font(italic=True, color="595959")

def cab(ws, row, heads, widths):
    for i, (t, w) in enumerate(zip(heads, widths), 1):
        c = ws.cell(row=row, column=i, value=t); c.font = H; c.fill = fill(AZUL); c.border = box
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        ws.column_dimensions[c.column_letter].width = w
    ws.row_dimensions[row].height = 58

# ---------- Inicio ----------
ws = wb.active; ws.title = "Inicio"
title(ws, "Planilla de Liquidación Final e Indemnización", "Despido sin causa o renuncia: todos los rubros, el recibo para imprimir y hasta 30 personas. Excel y Google Sheets.")
ws.column_dimensions["A"].width = 120
lines = [
 "CÓMO USARLO",
 "1. Pestaña 'Liquidaciones': una fila por persona. Cargá nombre, tipo de egreso, fechas de ingreso y egreso, y la mejor remuneración mensual normal y habitual.",
 "2. Opcional: el promedio salarial de tu convenio (columna F) para aplicar el tope del art. 245, y los días de vacaciones que ya gozó en el año.",
 "3. Cada fila calcula sola indemnización, preaviso, integración del mes, SAC y vacaciones proporcionales, total bruto, descuentos estimados y neto.",
 "4. Pestaña 'Recibo': elegí la persona e imprimí el recibo de liquidación final para firmar.",
 "5. Pestaña 'Parámetros': período de prueba y porcentaje de aportes. Cambialos si tu convenio o tu caso son distintos.",
 "",
 "Celdas amarillas = las cargás vos. Celdas celestes = se calculan solas. Las 3 filas de ejemplo se pisan o se borran.",
 "",
 "REGLAS QUE APLICA (LCT 20.744, texto según Ley 27.802)",
 "Indemnización por antigüedad (art. 245): un mes de la mejor remuneración mensual normal y habitual por año de servicio o fracción mayor de tres meses (mínimo un mes).",
 "Base (art. 245 reformado): no incluye aguinaldo, vacaciones ni premios no mensuales. Con tope de 3 veces el promedio del convenio y piso del 67% de la mejor remuneración (Vizzoti).",
 "Preaviso (art. 231): 1 mes hasta 5 años de antigüedad y 2 meses con más de 5. Si no se otorga, se paga como indemnización sustitutiva (art. 232).",
 "Integración del mes de despido (art. 233): los días que faltan hasta fin de mes si el despido no cae el último día. Aguinaldo sobre preaviso e integración: un doceavo.",
 "Período de prueba (art. 92 bis, Ley 27.802): 6 meses por defecto. Sin indemnización ni preaviso por despido durante la prueba. Renuncia: no hay indemnización.",
 "SAC proporcional (art. 123) y vacaciones no gozadas proporcionales (art. 156, sueldo / 25 por día) corresponden en toda extinción, también en la renuncia.",
 "Fondo de Asistencia Laboral (FAL): financia al empleador pero no cambia lo que se le debe a la persona; no está en esta planilla.",
 "",
 "AVISO",
 "Herramienta de cálculo orientativa para sueldos mensuales, no reemplaza el asesoramiento profesional. Convenios colectivos, remuneración variable, jornal,",
 "acuerdos y criterios judiciales pueden modificar los resultados. Verificá con un contador o abogado laboral. Para uso propio, prohibida su reventa.",
]
for i, l in enumerate(lines, 4):
    ws.cell(row=i, column=1, value=l)
    if l.startswith(("CÓMO", "REGLAS", "AVISO")): ws.cell(row=i, column=1).font = Font(bold=True, color=AZUL, size=12)

# ---------- Parámetros ----------
p = wb.create_sheet("Parámetros")
title(p, "Parámetros", "Cambialos solo si tu caso lo pide.")
p.column_dimensions["A"].width = 44; p.column_dimensions["B"].width = 14; p.column_dimensions["C"].width = 80
p["A4"] = "Período de prueba (meses)"; p["B4"] = 6; p["C4"] = "Ley 27.802: 6 meses. Algunos convenios o empresas chicas tienen más."
p["A5"] = "Descuentos sobre rubros remunerativos"; p["B5"] = 0.17; p["B5"].number_format = "0%"; p["C5"] = "Jubilación 11% + obra social 3% + PAMI 3%. No incluye Ganancias ni cuota sindical."
for r in (4, 5):
    p.cell(row=r, column=1).font = B; p.cell(row=r, column=2).fill = fill(INPUT); p.cell(row=r, column=2).border = box
    p.cell(row=r, column=3).font = Font(color="595959")
wb.defined_names["PruebaMeses"] = DefinedName("PruebaMeses", attr_text="'Parámetros'!$B$4")
wb.defined_names["Aportes"] = DefinedName("Aportes", attr_text="'Parámetros'!$B$5")

# ---------- Liquidaciones ----------
e = wb.create_sheet("Liquidaciones")
title(e, "Liquidaciones", "Una fila por persona. Amarillo = lo cargás vos.")
e["A4"] = "Tope: 3 veces el promedio salarial de tu convenio (columna F). Si la dejás vacía, se usa la remuneración completa."; e["A4"].font = Font(color="595959")
e["A5"] = "Período de prueba y aportes se cambian en 'Parámetros'."; e["A5"].font = Font(color="595959")
heads = ["Nombre", "Tipo de egreso", "Fecha de ingreso", "Fecha de egreso", "Mejor remuneración mensual normal y habitual", "Promedio salarial del convenio (opcional)",
         "Días de vacaciones ya gozados en el año", "¿Ya cobró el mes del egreso?",
         "Años completos de antigüedad", "Años para la indemnización", "Base de cálculo (art. 245)", "Indemnización por antigüedad (art. 245)",
         "Preaviso (art. 232)", "Integración mes de despido (art. 233)", "SAC sobre preaviso e integración", "Sueldo de los días del mes trabajados",
         "SAC proporcional", "Vacaciones proporcionales", "SAC sobre vacaciones", "TOTAL BRUTO", "Descuentos estimados", "NETO A COBRAR", "Observación",
         "Aux: en período de prueba", "Aux: días de vacaciones por año", "Aux: días trabajados en el año", "Aux: días de vacaciones proporcionales"]
cab(e, 7, heads, [26, 18, 13, 13, 19, 18, 14, 13, 12, 12, 17, 19, 17, 17, 16, 17, 17, 17, 15, 19, 16, 19, 38, 11, 11, 11, 13])
ejemplo = [
    ("Ejemplo: Laura Pérez", "Despido sin causa", D(2018, 3, 5), D(2026, 11, 12), 1600000, None, 0, "No"),
    ("Ejemplo: Diego Sosa", "Renuncia", D(2022, 8, 1), D(2026, 11, 30), 1350000, None, 7, "No"),
    ("Ejemplo: Ana Ríos", "Despido sin causa", D(2026, 8, 3), D(2026, 11, 20), 1100000, None, 0, "No"),
]
for r in range(N0, N1 + 1):
    act = f'AND($A{r}<>"",$C{r}<>"",$D{r}<>"",N($E{r})>0,$D{r}>=$C{r})'
    desp = f'$B{r}="Despido sin causa"'
    f = {
     9:  f'=IF({act},DATEDIF($C{r},$D{r},"y"),"")',
     10: f'=IF({act},IF(AND({desp},$X{r}=0),MAX(1,$I{r}+IF(EDATE($C{r},12*$I{r}+3)<$D{r},1,0)),0),"")',
     11: f'=IF({act},IF(N($F{r})>0,MAX(MIN($E{r},3*$F{r}),0.67*$E{r}),$E{r}),"")',
     12: f'=IF({act},$J{r}*$K{r},"")',
     13: f'=IF({act},IF(AND({desp},$X{r}=0),IF($D{r}>EDATE($C{r},60),2,1)*$E{r},0),"")',
     14: f'=IF({act},IF(AND({desp},$X{r}=0),$E{r}/30*(EOMONTH($D{r},0)-$D{r}),0),"")',
     15: f'=IF({act},($M{r}+$N{r})/12,"")',
     16: f'=IF({act},IF($H{r}="Sí",0,MIN($E{r},$E{r}/30*DAY($D{r}))),"")',
     17: (f'=IF({act},$E{r}/2*($D{r}-MAX($C{r},IF(MONTH($D{r})<=6,DATE(YEAR($D{r}),1,1),DATE(YEAR($D{r}),7,1)))+1)'
          f'/(IF(MONTH($D{r})<=6,DATE(YEAR($D{r}),6,30),DATE(YEAR($D{r}),12,31))-IF(MONTH($D{r})<=6,DATE(YEAR($D{r}),1,1),DATE(YEAR($D{r}),7,1))+1),"")'),
     18: f'=IF({act},$AA{r}*$E{r}/25,"")',
     19: f'=IF({act},$R{r}/12,"")',
     20: f'=IF({act},$L{r}+$M{r}+$N{r}+$O{r}+$P{r}+$Q{r}+$R{r}+$S{r},"")',
     21: f'=IF({act},Aportes*($P{r}+$Q{r}+$R{r}+$S{r}),"")',
     22: f'=IF({act},$T{r}-$U{r},"")',
     23: (f'=IF($A{r}="","",IF(NOT({act}),"Revisá fechas y remuneración",IF(AND({desp},$X{r}=1),"Período de prueba: sin indemnización ni preaviso",'
          f'IF(AND({desp},$I{r}=0),"Mínimo de un mes de indemnización",IF(N($F{r})>0,IF($E{r}>3*$F{r},"Aplica tope del convenio","Sin tope"),"Sin tope cargado")))))'),
     24: f'=IF({act},IF(EDATE($C{r},PruebaMeses)>$D{r},1,0),"")',
     25: f'=IF({act},IF(DATE(YEAR($D{r}),12,31)<=EDATE($C{r},60),14,IF(DATE(YEAR($D{r}),12,31)<=EDATE($C{r},120),21,IF(DATE(YEAR($D{r}),12,31)<=EDATE($C{r},240),28,35))),"")',
     26: f'=IF({act},$D{r}-MAX($C{r},DATE(YEAR($D{r}),1,1))+1,"")',
     27: f'=IF({act},MAX(0,$Y{r}*$Z{r}/365-N($G{r})),"")',
    }
    for col in range(1, 28):
        c = e.cell(row=r, column=col); c.border = box
        if col in f: c.value = f[col]; c.fill = fill(CLARO)
        else: c.fill = fill(INPUT)
    for col in (3, 4): e.cell(row=r, column=col).number_format = FECHA
    for col in (5, 6, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22): e.cell(row=r, column=col).number_format = ARS
    e.cell(row=r, column=27).number_format = "0.0"
    e.cell(row=r, column=20).font = B; e.cell(row=r, column=22).font = B
for i, (n, t, ing, egr, s, cv, g, cob) in enumerate(ejemplo, N0):
    for col, v in zip((1, 2, 3, 4, 5, 6, 7, 8), (n, t, ing, egr, s, cv, g, cob)): e.cell(row=i, column=col, value=v)
for r in range(N0, N1 + 1):
    if e.cell(row=r, column=8).value is None: e.cell(row=r, column=8, value="No")
e.freeze_panes = "B8"
dv1 = DataValidation(type="list", formula1='"Despido sin causa,Renuncia"', allow_blank=True); e.add_data_validation(dv1); dv1.add(f"B{N0}:B{N1}")
dv2 = DataValidation(type="list", formula1='"Sí,No"', allow_blank=True); e.add_data_validation(dv2); dv2.add(f"H{N0}:H{N1}")
dv3 = DataValidation(type="date", operator="greaterThan", formula1="36526", allow_blank=True, showErrorMessage=True, errorTitle="Fecha", error="Escribí una fecha, por ejemplo 12/11/2026.")
e.add_data_validation(dv3); dv3.add(f"C{N0}:D{N1}")
rojo = DifferentialStyle(fill=PatternFill(bgColor=ROJO, fill_type="solid"), font=Font(color="9C0006"))
e.conditional_formatting.add(f"W{N0}:W{N1}", Rule(type="expression", dxf=rojo, formula=[f'OR(LEFT($W{N0},6)="Revisá",LEFT($W{N0},7)="Período")']))

# ---------- Recibo ----------
a = wb.create_sheet("Recibo")
title(a, "Recibo de liquidación final", "Elegí la persona. Imprimí la hoja y firmala.")
a.column_dimensions["A"].width = 52; a.column_dimensions["B"].width = 26; a.column_dimensions["C"].width = 40
a["A4"] = "Persona"; a["A4"].font = B
a["B4"] = f"=Liquidaciones!A{N0}"; a["B4"].fill = fill(INPUT); a["B4"].border = box
dvl = DataValidation(type="list", formula1=f"=Liquidaciones!$A${N0}:$A${N1}", allow_blank=False); a.add_data_validation(dvl); dvl.add("B4")
a["A5"] = "Empleador (razón social)"; a["A5"].font = B; a["B5"].fill = fill(INPUT); a["B5"].border = box
a["A6"] = "CUIT del empleador"; a["A6"].font = B; a["B6"].fill = fill(INPUT); a["B6"].border = box
a["A7"] = "Lugar y fecha de pago"; a["A7"].font = B; a["B7"].fill = fill(INPUT); a["B7"].border = box
a["A8"] = "Fila en 'Liquidaciones'"; a["B8"] = f'=IFERROR(MATCH(B4,Liquidaciones!$A${N0}:$A${N1},0),"")'
a["A8"].font = Font(color="808080"); a["B8"].font = Font(color="808080")
def idx(col): return f'IFERROR(INDEX(Liquidaciones!${col}${N0}:${col}${N1},$B$8),"")'
a["A10"] = "Rubro"; a["B10"] = "Importe"
for c in ("A10", "B10"): a[c].font = H; a[c].fill = fill(AZUL); a[c].alignment = Alignment(horizontal="center")
rows = [
 ("Tipo de egreso", idx("B"), None), ("Fecha de ingreso", idx("C"), FECHA), ("Fecha de egreso", idx("D"), FECHA),
 ("Mejor remuneración mensual normal y habitual", idx("E"), ARS),
 ("Indemnización por antigüedad (art. 245 LCT)", idx("L"), ARS), ("Preaviso (art. 232 LCT)", idx("M"), ARS),
 ("Integración del mes de despido (art. 233 LCT)", idx("N"), ARS), ("SAC sobre preaviso e integración", idx("O"), ARS),
 ("Sueldo de los días trabajados del mes", idx("P"), ARS), ("SAC proporcional (art. 123 LCT)", idx("Q"), ARS),
 ("Vacaciones proporcionales no gozadas (art. 156 LCT)", idx("R"), ARS), ("SAC sobre vacaciones", idx("S"), ARS),
 ("TOTAL BRUTO", idx("T"), ARS), ("Descuentos de ley (aportes)", idx("U"), ARS), ("NETO A COBRAR", idx("V"), ARS),
]
for i, (lab, f, fmt) in enumerate(rows, 11):
    a.cell(row=i, column=1, value=lab).font = B
    cc = a.cell(row=i, column=2, value="=" + f); cc.border = box; cc.fill = fill(CLARO); cc.alignment = Alignment(horizontal="right")
    if fmt: cc.number_format = fmt
for r in (23, 25):
    a.cell(row=r, column=1).font = Font(bold=True, color=AZUL, size=12); a.cell(row=r, column=2).font = Font(bold=True, size=12)
a["A28"] = "Firma del empleador: ______________________________"
a["A30"] = "Recibí la suma indicada en concepto de liquidación final. Firma, aclaración y fecha: ______________________________"
a["A32"] = "Importes orientativos. Verificá con tu contador o abogado laboral antes de pagar. Guardá una copia firmada."
a["A32"].font = Font(italic=True, color="595959")
for ws_ in (e, a, p): ws_.sheet_view.showGridLines = False
a.page_setup.orientation = "portrait"; a.page_setup.fitToWidth = 1
wb.save(OUT)
print("ok", OUT)
