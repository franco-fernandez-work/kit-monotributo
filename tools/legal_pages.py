"""Generadores gratis (reclamo de consumo y telegrama de renuncia) y ofertas de los packs. Se importa desde build_site.main()."""
import json
import legal_data as L

CSS = r"""
/* generadores legales */
.hoja-carta{background:#fff;color:#10263d;border:1px solid var(--linea);border-radius:3px;padding:24px 22px;font:400 14px/1.55 var(--f-texto);white-space:pre-wrap;word-break:break-word;min-height:380px;position:sticky;top:12px;overflow-wrap:anywhere}
.hoja-carta.tg{font:600 13px/1.6 var(--f-num);letter-spacing:.01em;background:#fffdf4;border-color:#e5dcae}
.copiar{display:flex;flex-wrap:wrap;gap:10px 14px;align-items:center;margin-top:12px}
.copiar .cuenta{font:600 13px var(--f-num);color:var(--tinta-2)}
.avisolegal{border-left:4px solid var(--sello);background:#fbf1f1;padding:12px 16px;font-size:14px;color:var(--tinta);border-radius:0 4px 4px 0;margin:22px 0}
.modelos{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:12px;list-style:none;padding:0;margin:18px 0}
.modelos li{background:var(--hoja);border:1px solid var(--linea);border-radius:4px;padding:14px 16px 14px 52px;position:relative;margin:0}
.modelos li::before{content:attr(data-n);position:absolute;left:14px;top:14px;font:600 13px var(--f-num);color:var(--celeste)}
.modelos b{display:block;font-size:15px}
.modelos span{display:block;color:var(--tinta-2);font-size:13.5px;margin-top:2px}
.pasos{counter-reset:p;list-style:none;padding:0;margin:14px 0}
.pasos li{counter-increment:p;padding:10px 0 10px 40px;position:relative;border-bottom:1px dashed var(--linea);margin:0}
.pasos li::before{content:counter(p);position:absolute;left:0;top:10px;width:26px;height:26px;border-radius:50%;background:var(--tinta);color:var(--papel);font:600 13px/26px var(--f-num);text-align:center}
@media (max-width:900px){.hoja-carta{position:static;min-height:0}}
.gen select{width:100%;font:500 16px var(--f-texto);padding:10px 12px;border:1.5px solid var(--linea);border-radius:4px;background:var(--papel);color:var(--tinta)}
"""

def campos_html(campos, pref):
    cs = [f'<div class="campo"><label for="{pref}-{k}">{t}</label><input id="{pref}-{k}" data-k="{k}" autocomplete="off"></div>' for k, t in campos]
    return "".join(f'<div class="fila2">{"".join(cs[i:i+2])}</div>' for i in range(0, len(cs), 2))

def modelos_html(items):
    return '<ol class="modelos">' + "".join(
        f'<li data-n="{i:02d}"><b>{m["titulo"]}</b><span>{m["cuando"]}</span></li>' for i, m in enumerate(items, 1)) + "</ol>"

def oferta(idp, etiqueta, titulo, bajada, items, precio, boton, nota, extra=""):
    li = "".join(f"<li>{i}</li>" for i in items)
    return (f'<section class="oferta" aria-labelledby="of-{idp}"><div><span class="etiqueta">{etiqueta}</span><h2 id="of-{idp}">{titulo}</h2><p>{bajada}</p><ul>{li}</ul></div>'
            f'<div class="compra"><a class="boton" href="/comprar?p={idp}">{boton} <span class="num">$ {precio}</span></a><span class="nota">{nota}</span>{extra}</div></section>')

def oferta_rec():
    return oferta("reclamos", "Pack en Word (.docx)", "Pack de 8 cartas de reclamo de consumo",
        "Las 8 situaciones más comunes, con la ley citada, segunda intimación y la guía para llegar al COPREC.",
        ["No llegó, llegó roto, arrepentimiento, baja de servicio", "Débito no autorizado, garantía, cobro indebido, publicidad engañosa", "Lista de pruebas a reunir en cada caso", "Guía: dónde reclamar y qué plazos corren (Ventanilla Federal, COPREC, OMIC)"],
        "2.999", "Comprar el pack", "Pagás con Mercado Pago y lo descargás al instante. Modelos orientativos: no reemplazan asesoramiento legal.")

def oferta_tel():
    return oferta("telegramas", "Pack en Word (.docx)", "Pack de 10 telegramas y cartas documento laborales",
        "Cada modelo viene en versión telegrama gratuito del Correo y en carta documento completa, con la norma citada.",
        ["Renuncia, intimación de pago, registración, aportes y vacaciones", "Despido indirecto, rechazo de sanción, respuesta a carta documento", "Pedido de certificados (art. 80) y rechazo de cambio de condiciones", "Guía de plazos y de cómo enviarlo gratis"],
        "4.999", "Comprar el pack", "Pagás con Mercado Pago y lo descargás al instante. Modelos orientativos: no reemplazan asesoramiento legal.",
        '<a class="nota" href="/calculadora-liquidacion-final">¿Cuánto te corresponde cobrar? Calculá tu liquidación final gratis</a>')

AVISO_HTML = f'<p class="avisolegal"><b>Modelos orientativos.</b> {L.AVISO}</p>'

def tpl_cons(r):
    return "\n\n".join([L.CAB_CONS] + r["cuerpo"] + [L.PIE_CONS, L.FIRMA_CONS])

FREE_R = [r for r in L.RECLAMOS if r["free"]]
TEL = L.TELEGRAMAS[0]

# --------------------------------------------------------------------------------- reclamo
REC_BODY = f"""<span class="etiqueta">Generador gratis · Ley 24.240</span>
<h1>Reclamo de consumo: armá tu carta en un minuto</h1>
<p class="bajada">Elegí tu caso, completá los datos y copiá la carta lista para enviar por mail, formulario o carta documento. Sin registro y sin salir de tu navegador.</p>
<div class="gen" style="margin-top:28px">
<div class="comp"><div class="comp-cab"><span>Tu caso</span><span>Gratis</span></div><div class="comp-cuerpo">
<div class="tipos" role="group" aria-label="Tipo de reclamo">{"".join(f'<button type="button" data-t="{r["id"]}" aria-pressed="{"true" if i == 0 else "false"}">{r["titulo"]}</button>' for i, r in enumerate(FREE_R))}</div>
<p class="nota" id="rc-cuando"></p>
{campos_html(L.CAMPOS_CONS, "rc")}
<div class="campo"><label for="rc-ciudad">Ciudad</label><input id="rc-ciudad" data-k="ciudad" autocomplete="off"></div>
</div></div>
<div><div class="hoja-carta" id="rc-out" aria-live="polite"></div>
<div class="copiar"><button type="button" class="boton" id="rc-copiar">Copiar carta</button><span class="cuenta" id="rc-est"></span></div></div></div>
{AVISO_HTML}
<div class="lectura"><h2>Qué hacer después de enviarla</h2>
<ol class="pasos"><li><b>Guardá la prueba de envío.</b> Captura del mail o formulario, o la constancia de la carta documento.</li><li><b>Esperá el plazo de la carta</b> (5 días hábiles en este modelo) sin pagar ni aceptar nada más.</li><li><b>Si no contestan o no resuelven</b>, reclamá en la Ventanilla Única Federal de Reclamos de Consumo (consumidor.gob.ar), en el COPREC o en la oficina de defensa del consumidor de tu provincia o municipio.</li></ol>
<h2>Dos derechos que casi nadie usa</h2>
<ul><li><b>Arrepentimiento:</b> en compras a distancia podés devolver el producto sin dar motivos dentro de los 10 días corridos de recibirlo (art. 34, Ley 24.240), con gastos de devolución a cargo del vendedor. <a href="/boton-de-arrepentimiento-compra-online">Cómo ejercerlo</a>.</li>
<li><b>Producto que no llega:</b> podés exigir el cumplimiento, aceptar otro producto o pedir que te devuelvan lo pagado (art. 10 bis).</li></ul></div>
<h2>Las otras 6 situaciones, en el pack</h2>
<p>La carta de la web cubre los dos casos más frecuentes. El pack suma el resto, en Word editable y con segunda intimación:</p>
{modelos_html([r for r in L.RECLAMOS if not r["free"]])}
{oferta_rec()}"""

def js_gen(pref, tpls, extra=""):
    return ("<script>(function(){const T=" + json.dumps(tpls, ensure_ascii=False) + ";const P='" + pref + "';let cur=Object.keys(T)[0];"
     "const $=i=>document.getElementById(i);const val=k=>{const e=$(P+'-'+k);return e?e.value.trim():''};"
     "const hoy=()=>new Date().toLocaleDateString('es-AR');" + extra + "})();</script>")

REC_JS = js_gen("rc", {r["id"]: tpl_cons(r) for r in FREE_R}, extra=r"""
const C=""" + json.dumps({r["id"]: r["cuando"] for r in FREE_R}, ensure_ascii=False) + r""";
function draw(){let t=T[cur].replace(/\{(\w+)\}/g,(m,k)=>val(k)||'['+k.replace(/_/g,' ')+']');
 const c=val('ciudad')||'[ciudad]';$('rc-out').textContent=c+', '+hoy()+'\n\n'+t;$('rc-cuando').textContent=C[cur]}
document.querySelectorAll('.gen input').forEach(e=>e.addEventListener('input',draw));
document.querySelectorAll('.tipos button').forEach(b=>b.addEventListener('click',()=>{cur=b.dataset.t;document.querySelectorAll('.tipos button').forEach(x=>x.setAttribute('aria-pressed',x===b));draw()}));
$('rc-copiar').addEventListener('click',async()=>{try{await navigator.clipboard.writeText($('rc-out').textContent);$('rc-est').textContent='Copiada. Pegala en tu mail o en la carta documento.'}catch(e){const r=document.createRange();r.selectNodeContents($('rc-out'));getSelection().removeAllRanges();getSelection().addRange(r);$('rc-est').textContent='Seleccionada: copiala con Ctrl+C.'}});
draw();""")

# --------------------------------------------------------------------------------- telegrama
TEL_CAMPOS = [("nombre", "Tu nombre y apellido"), ("dni", "Tu DNI"), ("puesto", "Tu puesto o tareas"), ("fecha_ingreso", "Fecha de ingreso"),
              ("fecha_efecto", "Fecha en que renunciás"), ("empleador", "Empleador (razón social)"), ("domicilio_empleador", "Domicilio del empleador")]

TEL_BODY = f"""<span class="etiqueta">Generador gratis · Ley de Contrato de Trabajo</span>
<h1>Telegrama de renuncia: modelo listo para el Correo</h1>
<p class="bajada">Completá tus datos y copiá el texto en mayúsculas. El telegrama laboral del Correo Argentino es gratuito para el trabajador.</p>
<div class="gen" style="margin-top:28px">
<div class="comp"><div class="comp-cab"><span>Renuncia</span><span>Gratis</span></div><div class="comp-cuerpo">
{campos_html(TEL_CAMPOS, "tg")}
<div class="campo"><label for="tg-pre">Preaviso</label><select id="tg-pre"><option value="no">No cumplo el preaviso</option><option value="si">Cumplo el preaviso</option></select></div>
<div class="campo" id="tg-cf" style="display:none"><label for="tg-fecha_preaviso">Cumplo hasta el</label><input id="tg-fecha_preaviso" data-k="fecha_preaviso" autocomplete="off"></div>
</div></div>
<div><div class="hoja-carta tg" id="tg-out" aria-live="polite"></div>
<div class="copiar"><button type="button" class="boton" id="tg-copiar">Copiar telegrama</button><span class="cuenta" id="tg-cuenta"></span></div><p class="nota" id="tg-est"></p></div></div>
{AVISO_HTML}
<div class="lectura"><h2>Cómo enviarlo gratis</h2>
<ol class="pasos"><li><b>Imprimí o llevá el texto</b> en una sucursal del Correo Argentino con tu DNI y la dirección completa del empleador, con código postal.</li><li><b>Pedí el telegrama colacionado laboral (TCL)</b>: es gratuito para el trabajador (Ley 23.789) y te dan una copia sellada.</li><li><b>Guardá la constancia</b> y el aviso de recepción: son la prueba de que renunciaste y cuándo.</li></ol>
<h2>Antes de renunciar</h2>
<ul><li>Renunciar <b>no da derecho a indemnización por despido</b>: se cobran el sueldo proporcional, el SAC y las vacaciones no gozadas. Calculá cuánto con la <a href="/calculadora-liquidacion-final">calculadora de liquidación final</a>.</li><li>La renuncia debe ser escrita y fehaciente (art. 240 LCT). No firmes nada que no entiendas.</li><li>Si el motivo es un incumplimiento del empleador (no te pagan, trabajás en negro), primero intimá: renunciar sin intimar te hace perder la indemnización.</li></ul></div>
<h2>Los otros 9 modelos, en el pack</h2>
<p>Además de la renuncia, el pack incluye las intimaciones y respuestas más frecuentes, cada una en telegrama y en carta documento:</p>
{modelos_html(L.TELEGRAMAS[1:])}
{oferta_tel()}"""

TEL_JS = js_gen("tg", {"r": TEL["telegrama"]}, extra=r"""
const pre=$('tg-pre');
function draw(){$('tg-cf').style.display=pre.value==='si'?'':'none';
 const pt=pre.value==='si'?'Cumpliré el preaviso hasta el '+(val('fecha_preaviso')||'[fecha]')+'.':'No cumpliré el preaviso.';
 let t=T.r.replace('{preaviso_texto}',pt).replace(/\{(\w+)\}/g,(m,k)=>val(k)||'['+k.replace(/_/g,' ')+']');
 t=('Dirigido a: '+(val('empleador')||'[empleador]')+', '+(val('domicilio_empleador')||'[domicilio del empleador]')+'.\n\n'+t+'\n\nFirma: '+(val('nombre')||'[nombre]')+', DNI '+(val('dni')||'[dni]')).toUpperCase();
 $('tg-out').textContent=t;const w=t.trim().split(/\s+/).length;$('tg-cuenta').textContent=w+' palabras · '+t.length+' caracteres'}
document.querySelectorAll('.gen input').forEach(e=>e.addEventListener('input',draw));pre.addEventListener('change',draw);
$('tg-copiar').addEventListener('click',async()=>{try{await navigator.clipboard.writeText($('tg-out').textContent);$('tg-est').textContent='Copiado. Pegalo en el formulario del Correo o llevalo impreso.'}catch(e){const r=document.createRange();r.selectNodeContents($('tg-out'));getSelection().removeAllRanges();getSelection().addRange(r);$('tg-est').textContent='Seleccionado: copialo con Ctrl+C.'}});
draw();""")

PAGES = {
 "generador-reclamo-consumidor": ("Generador de reclamo de consumo gratis: carta para compras online", "Armá gratis tu carta de reclamo de consumo: compra online que no llegó o arrepentimiento, con la Ley 24.240 citada. Copiala y enviala; pack con 8 cartas por $2.999.", REC_BODY, REC_JS),
 "telegrama-renuncia-modelo": ("Telegrama de renuncia: modelo gratis para enviar por el Correo", "Generador gratis de telegrama de renuncia (art. 240 LCT) en mayúsculas, listo para el Correo Argentino. Pack de 10 telegramas laborales por $4.999.", TEL_BODY, TEL_JS),
}

# --------------------------------------------------------------------------------- artículos
A1 = ('<span class="etiqueta">Compras online · Ley 24.240</span><h1>Botón de arrepentimiento: cómo devolver una compra online</h1>'
 '<p class="bajada">Si compraste por internet, teléfono o fuera del local, tenés 10 días corridos para arrepentirte y que te devuelvan el dinero, sin dar explicaciones.</p>'
 '<div class="lectura"><h2>Las reglas</h2><ul><li>El plazo es de <b>10 días corridos</b> desde que recibís el producto o firmás el contrato, lo que ocurra último (art. 34 de la Ley 24.240 y art. 1110 del Código Civil y Comercial).</li>'
 '<li>Los <b>gastos de devolución</b> corren por cuenta del vendedor.</li><li>El vendedor debe tener un <b>botón de arrepentimiento</b> visible en su sitio (Res. SCI 424/2020). Si no lo tiene, escribile igual: lo que cuenta es avisar a tiempo.</li>'
 '<li>No aplica a servicios ya prestados con tu consentimiento ni a productos hechos a medida, entre otros casos que fija la ley (art. 1111 CCyC).</li></ul>'
 '<h2>Qué hacer</h2><ol class="pasos"><li>Avisá dentro de los 10 días, por el mismo medio de la compra o por mail, y guardá la prueba.</li><li>Pedí instrucciones para la devolución y que se haga a cargo del vendedor.</li><li>Exigí el reintegro por el mismo medio de pago.</li></ol>'
 '<p>Armá la carta en un minuto con el <a href="/generador-reclamo-consumidor">generador gratis de reclamo</a>.</p></div>' + AVISO_HTML + oferta_rec())

A2 = ('<span class="etiqueta">Despido indirecto · LCT</span><h1>Telegrama de despido indirecto: cuándo y cómo se manda</h1>'
 '<p class="bajada">Darte por despedido por culpa del empleador es una decisión seria: solo corresponde si hubo un incumplimiento grave y después de intimarlo a que lo corrija.</p>'
 '<div class="lectura"><h2>Cuándo corresponde</h2><ul><li>Falta de pago de sueldo o SAC, trabajo no registrado o mal registrado, aportes retenidos y no depositados, cambios perjudiciales de condiciones.</li>'
 '<li>Antes hay que <b>intimar</b> por escrito, con plazo (2 días hábiles para el pago, 30 días corridos para la registración) y el apercibimiento (arts. 242 y 246 LCT).</li><li>La comunicación debe expresar con claridad la causa (art. 243).</li></ul>'
 '<h2>Orden</h2><ol class="pasos"><li>Intimá con telegrama colacionado laboral, que es gratuito.</li><li>Esperá el plazo y guardá todo.</li><li>Si no cumple, comunicá el despido indirecto y reclamá la liquidación y las indemnizaciones.</li><li>Calculá lo que te corresponde con la <a href="/calculadora-liquidacion-final">calculadora de liquidación final</a>.</li></ol>'
 '<p>Si lo que querés es dejar el trabajo sin culpa del empleador, usá el <a href="/telegrama-renuncia-modelo">modelo de renuncia</a>: no da indemnización.</p></div>' + AVISO_HTML + oferta_tel())

ARTS_LEGAL = {
 "boton-de-arrepentimiento-compra-online": ("Botón de arrepentimiento: cómo devolver una compra online (10 días)", "Cómo ejercer el arrepentimiento de compra en 10 días corridos (art. 34 Ley 24.240): plazos, quién paga la devolución y qué hacer si no hay botón.", A1),
 "telegrama-despido-indirecto-modelo": ("Telegrama de despido indirecto: cuándo se manda y cómo", "Cuándo corresponde darte por despedido por culpa del empleador, cómo intimar antes y qué reclamar: arts. 242, 243 y 246 de la LCT.", A2),
}
