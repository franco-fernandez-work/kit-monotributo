import os, datetime
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.workbook.defined_name import DefinedName

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "private", "casas.xlsx")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
AZUL = "1F4E79"; CLARO = "DDEBF7"; INPUT = "FFF2CC"
H = Font(bold=True, color="FFFFFF"); B = Font(bold=True)
fill = lambda c: PatternFill("solid", fgColor=c)
thin = Side(style="thin", color="BFBFBF"); box = Border(top=thin, bottom=thin, left=thin, right=thin)
ARS = '"$" #,##0.00'; FECHA = "dd/mm/yyyy"; MES = "mmm yyyy"

from escalas_cp import CATS, ESCALAS

wb = Workbook()

def title(ws, text, sub):
    ws["A1"] = text; ws["A1"].font = Font(bold=True, size=16, color=AZUL)
    ws["A2"] = sub; ws["A2"].font = Font(italic=True, color="595959")

def cabecera(ws, row, heads, widths, col0=1):
    for i, (t, w) in enumerate(zip(heads, widths), col0):
        c = ws.cell(row=row, column=i, value=t); c.font = H; c.fill = fill(AZUL); c.border = box
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        ws.column_dimensions[chr(64 + i)].width = w
    ws.row_dimensions[row].height = 32

def form(ws, filas, start=4, wl=40, wv=22):
    # filas: (etiqueta, nombre, valor_o_formula, formato, es_input)
    ws.column_dimensions["A"].width = wl; ws.column_dimensions["B"].width = wv; ws.column_dimensions["C"].width = 60
    for r, (lab, name, val, fmt, inp, nota) in enumerate(filas, start):
        if lab is None: continue
        ws.cell(row=r, column=1, value=lab).font = B
        c = ws.cell(row=r, column=2, value=val); c.border = box
        if fmt: c.number_format = fmt
        c.fill = fill(INPUT if inp else CLARO)
        if nota: ws.cell(row=r, column=3, value=nota).font = Font(color="595959")
        if name: wb.defined_names[name] = DefinedName(name, attr_text=f"'{ws.title}'!$B${r}")

# Inicio
ws = wb.active; ws.title = "Inicio"
title(ws, "Planilla Casas Particulares 2026", "Sueldo, recibo, aguinaldo, vacaciones y liquidación final de tu empleada. Excel y Google Sheets.")
ws.column_dimensions["A"].width = 115
lines = [
 "CÓMO USARLO",
 "1. Pestaña 'Sueldo': elegí mes, categoría y modalidad, y cargá las horas si paga por hora. Abajo tenés el recibo listo para imprimir.",
 "2. Pestaña 'Aguinaldo': cargá lo que cobró cada mes del semestre y te da el medio aguinaldo, también si entró a mitad de semestre.",
 "3. Pestaña 'Vacaciones': cuántos días le corresponden por antigüedad y cuánto se le paga.",
 "4. Pestaña 'Liquidación final': para despido o renuncia, con preaviso, indemnización, aguinaldo y vacaciones proporcionales.",
 "5. Pestaña 'Escalas': salarios mínimos oficiales de agosto a diciembre 2026 (Resolución 6/2026 de la CNTCP).",
 "   Cuando salga una escala nueva, agregá las filas del mes al final con el primer día del mes en la columna 'Mes'.",
 "",
 "Celdas amarillas = las cargás vos. Celdas celestes = se calculan solas.",
 "",
 "REGLAS QUE APLICA (Ley 26.844)",
 "Antigüedad: 1% del básico por cada año trabajado con el mismo empleador.",
 "Zona desfavorable: 31% adicional en La Pampa, Río Negro, Chubut, Neuquén, Santa Cruz, Tierra del Fuego y Patagones.",
 "Aguinaldo: 50% de la mejor remuneración mensual del semestre, proporcional a los días trabajados. Vence el 30/6 y el 18/12.",
 "Vacaciones: 14 días hasta 5 años, 21 hasta 10, 28 hasta 20 y 35 con más de 20. Cada día se paga sueldo mensual / 25.",
 "Preaviso: 10 días con menos de 1 año de antigüedad, 1 mes con más. Indemnización: 1 sueldo por año o fracción mayor a 3 meses.",
 "",
 "AVISO",
 "Herramienta de cálculo orientativa. Los aportes y contribuciones se pagan a ARCA según las horas semanales (ver arca.gob.ar).",
 "Ante un despido o un conflicto, consultá a un contador o abogado laboral. Para uso personal, prohibida su reventa.",
]
for i, l in enumerate(lines, 4):
    ws.cell(row=i, column=1, value=l)
    if l in ("CÓMO USARLO", "REGLAS QUE APLICA (Ley 26.844)", "AVISO"): ws.cell(row=i, column=1).font = Font(bold=True, color=AZUL, size=12)

# Escalas
e = wb.create_sheet("Escalas")
title(e, "Salarios mínimos de casas particulares", "Resolución 6/2026 CNTCP. Agregá meses nuevos al final.")
cabecera(e, 4, ["Mes", "Categoría", "Hora con retiro", "Hora sin retiro", "Mensual con retiro", "Mensual sin retiro"], [12, 34, 15, 15, 17, 17])
r = 5
for (y, m), vals in ESCALAS.items():
    for cat, v in zip(CATS, vals):
        e.cell(row=r, column=1, value=datetime.date(y, m, 1)).number_format = MES
        e.cell(row=r, column=2, value=cat)
        for j, x in enumerate(v, 3):
            c = e.cell(row=r, column=j, value=x if x else None); c.number_format = ARS
        for j in range(1, 7): e.cell(row=r, column=j).border = box
        r += 1
FIN = 300
for rr in range(r, FIN + 1):
    for j in range(1, 7): e.cell(row=rr, column=j).fill = fill(INPUT)
    e.cell(row=rr, column=1).number_format = MES
e.freeze_panes = "A5"
for n, col in (("EMes", "A"), ("ECat", "B"), ("EHC", "C"), ("EHS", "D"), ("EMC", "E"), ("EMS", "F")):
    wb.defined_names[n] = DefinedName(n, attr_text=f"'Escalas'!${col}$5:${col}${FIN}")
cl = wb.create_sheet("Listas"); cl.sheet_state = "hidden"
for i, c in enumerate(CATS, 1): cl.cell(row=i, column=1, value=c)
wb.defined_names["Cats"] = DefinedName("Cats", attr_text=f"'Listas'!$A$1:$A${len(CATS)}")

def dv(ws, formula, cell):
    d = DataValidation(type="list", formula1=formula, allow_blank=True); ws.add_data_validation(d); d.add(cell)

# Sueldo
s = wb.create_sheet("Sueldo", 1)
title(s, "Sueldo del mes", "Cargá las celdas amarillas. El recibo de abajo se completa solo.")
col = '"Con retiro","Sin retiro"'
filas = [
 ("Empleador/a", "Empleador", "Nombre y apellido", None, True, None),
 ("CUIL del empleador/a", "CuilEmp", "", None, True, None),
 ("Trabajador/a", "Trabajador", "Nombre y apellido", None, True, None),
 ("CUIL del trabajador/a", "CuilTrab", "", None, True, None),
 ("Mes que se paga", "Mes", datetime.date(2026, 10, 1), MES, True, "Primer día del mes. Tiene que existir en la pestaña Escalas."),
 ("Categoría", "Cat", "Tareas generales", None, True, None),
 ("Modalidad", "Modal", "Con retiro", None, True, "Con retiro: no vive en la casa. Sin retiro: vive en la casa."),
 ("Forma de pago", "Forma", "Por hora", None, True, None),
 ("Horas trabajadas en el mes", "Horas", 48, "0.0", True, "Solo si paga por hora."),
 ("Fecha de ingreso", "Ingreso", datetime.date(2022, 3, 1), FECHA, True, None),
 ("Zona desfavorable", "Zona", "No", None, True, "31% adicional en Patagonia y Patagones."),
 ("Otros adicionales (horas extra, etc.)", "Extra", 0, ARS, True, None),
 ("Descuentos (adelantos, etc.)", "Desc", 0, ARS, True, None),
 (None, None, None, None, None, None),
 ("Valor hora / mensual de la escala", "ValEsc", '=IF(Forma="Por hora",SUMIFS(IF(Modal="Con retiro",EHC,EHS),EMes,Mes,ECat,Cat),SUMIFS(IF(Modal="Con retiro",EMC,EMS),EMes,Mes,ECat,Cat))', ARS, False, "Si da 0, falta la escala de ese mes o la combinación no existe (caseros es sin retiro)."),
 ("Salario básico", "Basico", '=IF(Forma="Por hora",ValEsc*Horas,ValEsc)', ARS, False, None),
 ("Años de antigüedad", "Anios", '=DATEDIF(Ingreso,EOMONTH(Mes,0),"y")', "0", False, None),
 ("Adicional por antigüedad", "Antig", "=Basico*1%*Anios", ARS, False, None),
 ("Adicional zona desfavorable", "ZonaAd", '=IF(Zona="Sí",Basico*31%,0)', ARS, False, None),
 ("Total bruto", "Bruto", "=Basico+Antig+ZonaAd+Extra", ARS, False, None),
 ("Neto a cobrar", "Neto", "=Bruto-Desc", ARS, False, None),
]
form(s, filas)
dv(s, "=Cats", "B9"); dv(s, f'"Con retiro,Sin retiro"', "B10"); dv(s, '"Por hora,Mensual"', "B11"); dv(s, '"Sí,No"', "B14")
s["B23"].font = B; s["B24"].font = Font(bold=True, size=13)
# Recibo
R = 27
s.cell(row=R, column=1, value="RECIBO DE SUELDO").font = Font(bold=True, size=14, color=AZUL)
rec = [
 ("Empleador/a", "=Empleador&IF(CuilEmp<>\"\",\" · CUIL \"&CuilEmp,\"\")"),
 ("Trabajador/a", "=Trabajador&IF(CuilTrab<>\"\",\" · CUIL \"&CuilTrab,\"\")"),
 ("Período", "=Mes"),
 ("Categoría", '=Cat&" · "&Modal&IF(Forma="Por hora"," · "&Horas&" horas","")'),
 ("Fecha de ingreso", "=Ingreso"),
 ("Salario básico", "=Basico"), ("Antigüedad", '=Antig'), ("Zona desfavorable", "=ZonaAd"), ("Otros adicionales", "=Extra"),
 ("Descuentos", "=-Desc"), ("NETO A COBRAR", "=Neto"),
]
for i, (lab, f) in enumerate(rec, R + 1):
    s.cell(row=i, column=1, value=lab).font = B; c = s.cell(row=i, column=2, value=f)
    c.border = box; s.cell(row=i, column=1).border = box
    if i - R > 5: c.number_format = ARS
    elif lab == "Período": c.number_format = "mmmm yyyy"
    elif lab == "Fecha de ingreso": c.number_format = FECHA
s.cell(row=R + len(rec), column=2).font = Font(bold=True, size=13)
s.cell(row=R + len(rec) + 3, column=1, value="Firma del empleador/a: ____________________")
s.cell(row=R + len(rec) + 3, column=2, value="Firma del trabajador/a: ____________________")

# Aguinaldo
a = wb.create_sheet("Aguinaldo", 2)
title(a, "Aguinaldo (SAC)", "Cargá lo que cobró en cada mes del semestre. Si entró a mitad de semestre, poné su fecha de ingreso.")
a.column_dimensions["A"].width = 40; a.column_dimensions["B"].width = 22; a.column_dimensions["C"].width = 60
a["A4"] = "Semestre"; a["A4"].font = B; a["B4"] = "Segundo (jul-dic)"; dv(a, '"Primero (ene-jun),Segundo (jul-dic)"', "B4")
a["A5"] = "Año"; a["A5"].font = B; a["B5"] = 2026
a["A6"] = "Fecha de ingreso (si fue en este semestre)"; a["A6"].font = B; a["B6"].number_format = FECHA
a["A7"] = "Fecha de egreso (si se fue en este semestre)"; a["A7"].font = B; a["B7"].number_format = FECHA
for c in ("B4", "B5", "B6", "B7"): a[c].fill = fill(INPUT); a[c].border = box
a["A9"] = "Mes"; a["B9"] = "Remuneración bruta"; a["A9"].font = H; a["B9"].font = H; a["A9"].fill = fill(AZUL); a["B9"].fill = fill(AZUL)
for i in range(6):
    r = 10 + i
    a[f"A{r}"] = f'=DATE($B$5,IF(LEFT($B$4,7)="Primero",1,7)+{i},1)'; a[f"A{r}"].number_format = MES
    a[f"B{r}"].fill = fill(INPUT); a[f"B{r}"].number_format = ARS; a[f"B{r}"].border = box; a[f"A{r}"].border = box
a["B10"] = 498582.06; a["B11"] = 512142.96; a["B12"] = 520337.24
ini = 'DATE($B$5,IF(LEFT($B$4,7)="Primero",1,7),1)'; fin = f"EOMONTH({ini},5)"
calc = [
 ("Mejor remuneración del semestre", "=MAX(B10:B15)", ARS),
 ("Días del semestre", f"={fin}-{ini}+1", "0"),
 ("Días trabajados", f"=MIN({fin},IF(B7=\"\",{fin},B7))-MAX({ini},IF(B6=\"\",{ini},B6))+1", "0"),
 ("Aguinaldo a pagar", "=B17/2*B19/B18", ARS),
 ("Vence", f'=IF(LEFT($B$4,7)="Primero",DATE($B$5,6,30),DATE($B$5,12,18))', FECHA),
]
for i, (lab, f, fmt) in enumerate(calc, 17):
    a[f"A{i}"] = lab; a[f"A{i}"].font = B; a[f"B{i}"] = f; a[f"B{i}"].number_format = fmt; a[f"B{i}"].fill = fill(CLARO); a[f"B{i}"].border = box
a["B20"].font = Font(bold=True, size=13)
a["C17"] = "Incluí básico, antigüedad, zona y adicionales remunerativos."; a["C17"].font = Font(color="595959")

# Vacaciones
v = wb.create_sheet("Vacaciones", 3)
title(v, "Vacaciones", "Se cuentan con la antigüedad al 31 de diciembre del año.")
form(v, [
 ("Fecha de ingreso", "VIng", datetime.date(2022, 3, 1), FECHA, True, None),
 ("Año de las vacaciones", "VAnio", 2026, "0", True, None),
 ("Sueldo mensual", "VSueldo", 520337.24, ARS, True, "Si cobra por hora, el promedio mensual."),
 ("Antigüedad al 31/12 (años)", "VAnt", "=DATEDIF(VIng,DATE(VAnio,12,31),\"y\")", "0", False, None),
 ("Días que le corresponden", "VDias", "=IF(DATEDIF(VIng,DATE(VAnio,12,31),\"m\")<6,INT(NETWORKDAYS(VIng,DATE(VAnio,12,31))/20),IF(VAnt<5,14,IF(VAnt<10,21,IF(VAnt<20,28,35))))", "0", False, "Con menos de 6 meses: 1 día cada 20 trabajados."),
 ("Valor de cada día", "VDia", "=VSueldo/25", ARS, False, None),
 ("Total a pagar por vacaciones", "VTot", "=VDias*VDia", ARS, False, "Se paga antes de que empiecen."),
])

# Liquidación final
l = wb.create_sheet("Liquidación final", 4)
title(l, "Liquidación final", "Despido sin causa o renuncia. Orientativa: ante un conflicto consultá a un profesional.")
form(l, [
 ("Fecha de ingreso", "LIng", datetime.date(2022, 3, 1), FECHA, True, None),
 ("Fecha de egreso", "LEg", datetime.date(2026, 10, 20), FECHA, True, None),
 ("Motivo", "LMot", "Despido sin causa", None, True, None),
 ("¿Se dio preaviso?", "LPre", "No", None, True, None),
 ("Mejor remuneración mensual del último año", "LMejor", 520337.24, ARS, True, None),
 ("Sueldo del mes de egreso", "LSueldo", 520337.24, ARS, True, None),
 ("Días de vacaciones ya tomados este año", "LVTom", 0, "0", True, None),
 (None, None, None, None, None, None),
 ("Antigüedad (meses)", "LMeses", "=DATEDIF(LIng,LEg,\"m\")", "0", False, None),
 ("Sueldo por los días trabajados del mes", "LHab", "=LSueldo/DAY(EOMONTH(LEg,0))*DAY(LEg)", ARS, False, None),
 ("Indemnización por antigüedad", "LInd", '=IF(LMot="Despido sin causa",LMejor*MAX(1,INT(LMeses/12)+IF(MOD(LMeses,12)>3,1,0)),0)', ARS, False, "1 sueldo por año o fracción mayor a 3 meses."),
 ("Preaviso", "LPrev", '=IF(AND(LMot="Despido sin causa",LPre="No"),IF(LMeses<12,LSueldo/30*10,LSueldo),0)', ARS, False, "10 días con menos de 1 año, 1 mes con más."),
 ("Integración del mes de despido", "LInt", '=IF(AND(LMot="Despido sin causa",LPre="No"),LSueldo/DAY(EOMONTH(LEg,0))*(DAY(EOMONTH(LEg,0))-DAY(LEg)),0)', ARS, False, None),
 ("Aguinaldo proporcional", "LSAC", "=LMejor/2*(LEg-IF(MONTH(LEg)<=6,DATE(YEAR(LEg),1,1),DATE(YEAR(LEg),7,1))+1)/IF(MONTH(LEg)<=6,181,184)", ARS, False, None),
 ("Vacaciones no gozadas", "LVac", "=MAX(0,IF(DATEDIF(LIng,DATE(YEAR(LEg),12,31),\"y\")<5,14,IF(DATEDIF(LIng,DATE(YEAR(LEg),12,31),\"y\")<10,21,IF(DATEDIF(LIng,DATE(YEAR(LEg),12,31),\"y\")<20,28,35)))*(LEg-DATE(YEAR(LEg),1,1)+1)/365-LVTom)*LSueldo/25", ARS, False, "Proporcionales al tiempo trabajado en el año."),
 ("SAC sobre preaviso e integración", "LSAC2", "=(LPrev+LInt)/12", ARS, False, None),
 ("TOTAL", "LTot", "=LHab+LInd+LPrev+LInt+LSAC+LVac+LSAC2", ARS, False, None),
])
dv(l, '"Despido sin causa,Renuncia"', "B6"); dv(l, '"Sí,No"', "B7")
l["B20"].font = Font(bold=True, size=13)

for w in wb.worksheets: w.sheet_view.showGridLines = False
wb.active = 0
wb.save(OUT); print("ok", OUT)
