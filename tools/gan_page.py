"""Calculadora gratis de Ganancias en el sueldo (4ª categoría) y su oferta. Se importa desde build_site.py."""
import json
import gan_data as G
from build_site import ars

DED = G.deducciones(12)
ESC = G.escala(12)
CFG = json.dumps({"ded": DED, "esc": [[d, f, p] for d, f, p in ESC]})

def tabla_escala():
    filas = []
    for i, (d, f, p) in enumerate(ESC):
        hasta = ars(ESC[i + 1][0]) if i < len(ESC) - 1 else "en adelante"
        filas.append(f'<tr><td class="cat">{i + 1}</td><td>{ars(d)}</td><td>{hasta}</td><td>{ars(f)}</td><td>{p}%</td></tr>')
    return ('<div class="tabla-wrap"><table><thead><tr><th>Tramo</th><th>Más de</th><th>Hasta</th><th>Pagan</th><th>Más el</th></tr></thead><tbody>'
            + "".join(filas) + "</tbody></table></div>")

def tabla_ded():
    n = [("Ganancia no imponible", "gni"), ("Cónyuge o conviviente", "conyuge"), ("Cada hijo", "hijo"), ("Hijo incapacitado para el trabajo", "incap"), ("Deducción especial (empleados, apartado 1)", "especial")]
    return ('<div class="tabla-wrap"><table style="min-width:0"><thead><tr><th>Concepto</th><th>Anual acumulado a diciembre 2026</th></tr></thead><tbody>'
            + "".join(f"<tr><td>{t}</td><td>{ars(DED[k])}</td></tr>" for t, k in n) + "</tbody></table></div>")

def oferta_gan():
    return """<section class="oferta" aria-labelledby="of-gan"><div><span class="etiqueta">Planilla para Excel y Google Sheets</span><h2 id="of-gan">Planilla de Ganancias en el Sueldo</h2>
<p>Cargás tus sueldos y tus gastos del SIRADIG y ves, mes por mes, cuánto te retienen y cuánto te ahorra cada deducción.</p>
<ul><li>Retención mensual con el método acumulado y las escalas oficiales de ARCA 2026</li><li>Aguinaldo, cargas de familia, alquiler, gastos médicos, servicio doméstico, donaciones, hipotecario y seguro de vida</li><li>Resumen con lo que te ahorrás por cargar el SIRADIG</li><li>Topes y aportes editables para actualizar cuando ARCA cambie los valores</li></ul></div>
<div class="compra"><a class="boton" href="/comprar?p=ganancias">Comprar la planilla <span class="num">$ 5.999</span></a><span class="nota">Pagás con Mercado Pago y la descargás al instante.</span></div></section>"""

GAN_BODY = """<section class="heroe">
<div><span class="etiqueta">Escalas de ARCA vigentes · Ganancias 4ª categoría</span>
<h1>Ganancias en el sueldo: cuánto te retienen y cuánto ahorrás con el SIRADIG</h1>
<p class="bajada">Poné tu sueldo bruto y los gastos que podés declarar. Calculamos el impuesto del año con las escalas oficiales de ARCA y cuánto te ahorran las deducciones.</p>
<ul class="puntos"><li><span class="num">5–35%</span><span><b>Escala progresiva</b> sobre la ganancia neta, después de restar deducciones.</span></li>
<li><span class="num">40%</span><span><b>Del alquiler</b> se puede deducir, hasta la ganancia no imponible.</span></li>
<li><span class="num">5%</span><span><b>De tu ganancia neta</b> es el límite para gastos médicos y donaciones.</span></li></ul></div>
<form class="comp" id="gan" aria-labelledby="gan-t" onsubmit="return false">
<div class="comp-cab"><span id="gan-t">Ganancias 2026</span><span>Estimación anual</span></div>
<div class="comp-cuerpo">
<div class="fila2"><div class="campo"><label for="sueldo">Sueldo bruto mensual</label><div class="entrada"><span>$</span><input id="sueldo" class="mon" inputmode="numeric" autocomplete="off" value="3.000.000"></div></div>
<div class="campo"><label for="aguin">Aguinaldo</label><div class="entrada"><select id="aguin"><option value="1">Incluido (13 sueldos)</option><option value="0">No incluir</option></select></div></div></div>
<div class="fila2"><div class="campo"><label for="conyuge">Cónyuge a cargo</label><div class="entrada"><select id="conyuge"><option value="0">No</option><option value="1">Sí</option></select></div></div>
<div class="campo"><label for="hijos">Hijos a cargo (0,5 si compartís)</label><div class="entrada"><input id="hijos" inputmode="decimal" value="1"></div></div></div>
<div class="fila2"><div class="campo"><label for="alq">Alquiler que pagás por mes</label><div class="entrada"><span>$</span><input id="alq" class="mon" inputmode="numeric" autocomplete="off" value="600.000"></div></div>
<div class="campo"><label for="dom">Servicio doméstico por mes</label><div class="entrada"><span>$</span><input id="dom" class="mon" inputmode="numeric" autocomplete="off" value="0"></div></div></div>
<div class="fila2"><div class="campo"><label for="med">Gastos médicos al año</label><div class="entrada"><span>$</span><input id="med" class="mon" inputmode="numeric" autocomplete="off" value="0"></div></div>
<div class="campo"><label for="otr">Donaciones, hipotecario y seguro de vida al año</label><div class="entrada"><span>$</span><input id="otr" class="mon" inputmode="numeric" autocomplete="off" value="0"></div></div></div>
<div class="resultado" aria-live="polite"><div class="sello" id="sello"><div><b id="r-mes">–</b><small>POR MES</small></div></div>
<dl class="datos"><div><dt>Impuesto del año</dt><dd id="r-imp">–</dd></div><div><dt>Ganancia neta imponible</dt><dd id="r-neta">–</dd></div><div><dt>Te ahorra el SIRADIG</dt><dd id="r-aho">–</dd></div><div><dt>% sobre el bruto</dt><dd id="r-pct">–</dd></div></dl></div>
<p class="estado" id="r-estado"></p>
</div></form></section>
<h2>Cómo se calcula</h2>
<div class="lectura"><p>El impuesto sale de tres pasos: se arma la ganancia neta, se restan las deducciones personales y se aplica la escala del artículo 94.</p>
<p class="num" style="background:var(--hoja);border:1px solid var(--linea);padding:14px 16px;border-radius:4px;overflow-x:auto">ganancia neta imponible = bruto anual − aportes − deducciones del SIRADIG − deducciones personales</p>
<h3>Deducciones personales 2026</h3>
<p>Son los valores oficiales de ARCA acumulados a diciembre de 2026. Enero a junio rigen con la tabla de ese semestre y julio a diciembre se actualizaron 16,85% por IPC.</p>""" + tabla_ded() + """
<h3>Escala del artículo 94</h3>""" + tabla_escala() + """
<h3>¿Qué se puede cargar en el SIRADIG?</h3>
<ul><li><b>Cargas de familia:</b> cónyuge e hijos, con tope de la ganancia no imponible.</li><li><b>Alquiler:</b> 40% de lo pagado, hasta la ganancia no imponible.</li><li><b>Servicio doméstico:</b> lo pagado, hasta la ganancia no imponible.</li><li><b>Gastos médicos:</b> 40% de lo facturado, hasta el 5% de la ganancia neta.</li><li><b>Donaciones:</b> a entidades reconocidas, hasta el 5% de la ganancia neta.</li><li><b>Intereses hipotecarios y seguro de vida:</b> con los topes que fija ARCA.</li></ul>
<h3>¿Por qué cargar el SIRADIG?</h3><p>Si no lo cargás, tu empleador no puede descontar esos gastos y te retiene de más. Lo que se paga de más se devuelve en la liquidación anual, pero cargarlo a tiempo te deja la plata en el bolsillo mes a mes.</p>
<p class="nota">Estimación orientativa. Usa 17% de aportes y no incluye conceptos no remunerativos, horas extra ni topes de aportes. Topes de ARCA: intereses hipotecarios hasta $20.000 al año y seguro de vida hasta $753.472,14 en 2026; en esta calculadora cargalos ya limitados. Tu recibo puede diferir: verificá con tu empleador o un contador.</p></div>
""" + oferta_gan()

GAN_JS = """<script>
const C=""" + CFG + """;
const $=id=>document.getElementById(id);
const f=n=>"$ "+Math.round(n).toLocaleString("es-AR");
const num=v=>Number((v||"0").replace(/[^0-9]/g,""));
const imp=x=>{if(x<=0)return 0;let t=C.esc[0];for(const e of C.esc)if(e[0]<=x)t=e;return t[1]+(x-t[0])*t[2]/100};
function calc(){const s=num($("sueldo").value),n=$("aguin").value==="1"?13:12;
 if(!s){$("r-estado").className="estado";$("r-estado").textContent="Poné tu sueldo bruto.";return}
 const brut=s*n,apor=brut*0.17,gni=C.ded.gni,
  alq=Math.min(num($("alq").value)*12*0.4,gni),dom=Math.min(num($("dom").value)*12,gni),otr=num($("otr").value);
 const base=Math.max(0,brut-apor-alq-dom-otr),med=Math.min(num($("med").value)*0.4,0.05*base);
 const hij=Math.max(0,parseFloat(($("hijos").value||"0").replace(",","."))||0);
 const carg=Math.min(($("conyuge").value==="1"?C.ded.conyuge:0)+hij*C.ded.hijo,gni),pers=gni+carg+C.ded.especial;
 const neta=Math.max(0,base-med-pers),neta0=Math.max(0,brut-apor-pers),t=imp(neta),t0=imp(neta0);
 $("r-mes").textContent=f(t/12);$("r-imp").textContent=f(t);$("r-neta").textContent=f(neta);$("r-aho").textContent=f(t0-t);$("r-pct").textContent=(t/brut*100).toFixed(1).replace(".",",")+"%";
 $("r-estado").className="estado bien";
 $("r-estado").textContent=t===0?"Con estos datos no pagarías Ganancias: tus deducciones superan tu ganancia neta.":"Tu retención promedio sería "+f(t/12)+" por mes. Sin cargar deducciones en el SIRADIG pagarías "+f(t0)+" en el año."}
document.querySelectorAll(".mon").forEach(i=>i.addEventListener("input",e=>{const x=e.target.value.replace(/[^0-9]/g,"");e.target.value=x?Number(x).toLocaleString("es-AR"):"";calc()}));
["aguin","conyuge"].forEach(i=>$(i).addEventListener("change",calc));$("hijos").addEventListener("input",calc);calc();
</script>"""

ARTS_GAN = {
"deducciones-siradig-ganancias-2026": ("Deducciones de Ganancias en el SIRADIG 2026: qué podés cargar",
"Qué gastos podés deducir de Ganancias en el SIRADIG 2026: alquiler 40%, gastos médicos, servicio doméstico, donaciones, hijos y más, con sus topes y las deducciones personales de ARCA.",
'<span class="etiqueta">Ganancias 4ª categoría · 2026</span><h1>Deducciones de Ganancias en el SIRADIG 2026</h1>\n<p class="bajada">Si cobrás sueldo y te retienen Ganancias, cargar estos gastos en el SIRADIG baja tu retención. Estos son los que aceptan y sus límites.</p>'
 '<div class="lectura"><h2>Deducciones personales de ARCA</h2>' + tabla_ded() +
 '<h2>Gastos que podés cargar</h2><ul><li><b>Alquiler de tu vivienda:</b> 40% de lo pagado, hasta la ganancia no imponible.</li><li><b>Servicio doméstico:</b> lo pagado a tu empleada, registrada, hasta la ganancia no imponible.</li>'
 '<li><b>Gastos médicos y paramédicos:</b> 40% de lo facturado, hasta el 5% de tu ganancia neta.</li><li><b>Donaciones:</b> a entidades reconocidas, hasta el 5% de la ganancia neta.</li><li><b>Cónyuge e hijos:</b> si no superan la ganancia no imponible en ingresos propios.</li><li><b>Intereses de crédito hipotecario y seguro de vida:</b> con topes que ARCA actualiza.</li><li><b>Aportes y cuota sindical:</b> se descuentan sin límite.</li></ul>'
 '<h2>Cómo se carga</h2><ol><li>Entrá a arca.gob.ar con Clave Fiscal.</li><li>Abrí el servicio SIRADIG - Trabajador.</li><li>Creá o editá el formulario 572 web del período.</li><li>Cargá cada deducción con el CUIT y el comprobante.</li><li>Enviá el formulario: tu empleador lo ve y ajusta la retención.</li></ol>'
 '<p>Para ver cuánto te ahorra cada gasto, probá la <a href="/calculadora-ganancias-sueldo">calculadora de Ganancias</a>.</p></div>' + oferta_gan()),
}
