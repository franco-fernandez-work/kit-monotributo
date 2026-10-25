"""Ronda 2 (HUECOS.md #4-#6): alquiler temporario de verano, autorización de viaje de menores y documentos de cuota alimentaria.
build_site.main() importa PAGES y CSS; `python tools/ronda2.py` arma los 3 zips en private/ (necesita python-docx; correr local y commitear; NO corre en Cloudflare)."""
import io, os, zipfile
import legal_pages as LP

AV = "Modelo orientativo. No reemplaza el asesoramiento de un escribano/a o abogado/a. Verificá los requisitos vigentes antes de firmar o viajar."
AVH = f'<p class="avisolegal"><b>Modelos orientativos.</b> {AV}</p>'
PAGO = "Pagás con Mercado Pago y lo descargás al instante. Modelos orientativos: no reemplazan asesoramiento legal."

CSS = r"""
/* ronda 2 */
.r2chk{display:grid;gap:8px;margin:14px 0;padding:0;list-style:none}
.r2chk label{display:flex;gap:12px;align-items:flex-start;padding:12px 14px;border:1px solid var(--linea);border-radius:4px;background:var(--hoja);cursor:pointer;font-size:15px;line-height:1.4}
.r2chk input{margin-top:3px;width:18px;height:18px;accent-color:var(--celeste);flex:none}
.r2chk label:has(input:checked){border-color:var(--ok);background:color-mix(in srgb,var(--ok) 9%,var(--hoja))}
.r2bar{height:8px;border-radius:4px;background:var(--linea);overflow:hidden;margin:6px 0 4px}
.r2bar i{display:block;height:100%;width:0;background:var(--ok);transition:width .25s}
.r2res{background:var(--hoja);border:1px solid var(--linea);border-left:5px solid var(--celeste);border-radius:4px;padding:18px 20px;display:grid;gap:10px}
.r2res b.g{font:600 26px var(--f-num);font-variant-numeric:tabular-nums}
.r2res .fil{display:flex;justify-content:space-between;gap:12px;border-bottom:1px dashed var(--linea);padding-bottom:6px;font-size:15px}
.r2res .fil span:last-child{font:600 16px var(--f-num);font-variant-numeric:tabular-nums;text-align:right}
.r2quien{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px;margin:18px 0}
.r2quien div{background:var(--hoja);border:1px solid var(--linea);border-radius:4px;padding:14px 16px;font-size:14.5px}
.r2quien h3{font:600 12px var(--f-num);letter-spacing:.08em;text-transform:uppercase;margin:0 0 6px;color:var(--celeste)}
.r2quien div.no h3{color:var(--sello)}.r2quien p{margin:0}
.r2dos{display:grid;grid-template-columns:1fr 1fr;gap:28px;align-items:start;margin-top:28px}
@media (max-width:900px){.r2dos{grid-template-columns:1fr}}
"""

def quien(items):
    return '<div class="r2quien">' + "".join(f'<div{" class=no" if no else ""}><h3>{t}</h3><p>{x}</p></div>' for t, x, no in items) + "</div>"

def head(et, h1, baj):
    return f'<span class="etiqueta">{et}</span><h1>{h1}</h1><p class="bajada">{baj}</p>'

def lec(s): return f'<div class="lectura">{s}</div>'

def field(id_, label, val, pre="", suf="", step="any"):
    return (f'<div class="campo"><label for="{id_}">{label}</label><div class="entrada">{f"<span>{pre}</span>" if pre else ""}'
            f'<input id="{id_}" type="number" inputmode="decimal" min="0" step="{step}" value="{val}">{f"<span>{suf}</span>" if suf else ""}</div></div>')

def js(body):
    return "<script>(function(){const $=i=>document.getElementById(i);const n=i=>Math.max(0,parseFloat($(i).value)||0);const ars=v=>'$ '+Math.round(v).toLocaleString('es-AR');" + body + "})();</script>"

# ===================================================================== 4. ALQUILER TEMPORARIO
def of_temp():
    return LP.oferta("alqtemp", "Pack en Word (.docx)", "Pack Alquiler Temporario de Verano",
        "Los papeles para alquilar una casa o departamento por días, semanas o la temporada, de los dos lados del mostrador.",
        ["Contrato de locación temporaria y anexo de inventario y estado", "Recibo de seña y reserva, y recibo de pago", "Acta de entrega y devolución de llaves", "Reglamento de la casa y guía anti-estafa para inquilinos y propietarios"],
        "2.999", "Comprar el pack", PAGO, '<a class="nota" href="/contratos-alquiler-modelo-word">¿Alquiler de vivienda permanente? Pack de contratos de alquiler</a>')

CHK = ["El alquiler lo ofrece una cuenta con historial, reseñas y datos reales: no un perfil nuevo con fotos de catálogo.",
       "Las fotos no aparecen en otras publicaciones (búsqueda inversa de imágenes) y la dirección existe en el mapa.",
       "Hay una forma de verificar al titular: DNI, factura de servicio o el nombre en la plataforma coincide con el de la cuenta bancaria.",
       "El precio es parecido al de otras casas de la zona y las fechas de más demanda no están regaladas.",
       "No te apuran con frases como «hay otro interesado, señá hoy»: una oferta seria da tiempo para verificar.",
       "La seña va por transferencia o por la plataforma, nunca en efectivo a un desconocido, y a una cuenta a nombre del propietario o inmobiliaria.",
       "Podés ver la casa en videollamada o con alguien de confianza, y te mandan un contrato o reserva escrita antes de pagar.",
       "Quedó por escrito qué incluye el precio (ropa blanca, limpieza, servicios), las fechas y la política de cancelación y devolución.",
       "Te dan recibo de cada pago con fecha, monto y concepto.",
       "El día de la entrega firmás un inventario con el estado de la casa, y sacás fotos."]

BODY_T = (head("Gratis · Alquiler temporario", "Alquiler de verano: checklist anti-estafa y calculadora de seña", "Antes de transferir una seña, tildá lo que pudiste verificar. Después calculá cuánto señar, cuánto es el saldo y cuánto dejar de depósito.")
 + '<div class="r2dos"><div><h2 style="margin-top:0">Checklist anti-estafa</h2><ul class="r2chk" id="tm-chk">' + "".join(f'<li><label><input type="checkbox"> <span>{c}</span></label></li>' for c in CHK)
 + '</ul><div class="r2bar"><i id="tm-bar"></i></div><p class="nota" id="tm-sc"></p></div>'
 + '<div class="comp"><div class="comp-cab"><span>Seña, saldo y depósito</span><span>Gratis</span></div><div class="comp-cuerpo">'
 + '<div class="fila2">' + field("tm-noche", "Precio por noche", 80000, "$") + field("tm-noches", "Noches", 14, "", "", "1") + "</div>"
 + '<div class="fila2">' + field("tm-sena", "Seña (% del total)", 30, "", "%") + field("tm-dep", "Depósito (% del total)", 10, "", "%") + "</div>"
 + '<div class="r2res" aria-live="polite"><div class="fil"><span>Total del alquiler</span><span id="tm-t"></span></div><div class="fil"><span>Seña al reservar</span><span id="tm-s"></span></div><div class="fil"><span>Saldo al ingresar</span><span id="tm-sa"></span></div><div class="fil"><span>Depósito en garantía (reintegrable)</span><span id="tm-d"></span></div></div>'
 + '<p class="nota">Los porcentajes son los usos más habituales del mercado, no una regla legal: lo que vale es lo que quede escrito en la reserva.</p></div></div></div>'
 + AVH
 + lec("<h2>Qué papel hace falta y quién interviene</h2>") + quien([
    ("Sin escribano ni juzgado", "En un alquiler de temporada corto alcanza con un contrato o reserva firmado por las partes, con recibo de cada pago y un inventario. No hace falta escribano.", False),
    ("Sellado e impuestos", "Algunas provincias cobran impuesto de sellos o exigen registrar contratos de locación. Consultalo en el organismo recaudador de la provincia donde está la casa.", False),
    ("Cuándo sí ver a un profesional", "Si el plazo es largo, el monto es alto o el titular no es quien alquila (administra, subalquila), pedí a un escribano o abogado que revise la documentación.", True)])
 + lec("<h2>Qué suma el pack</h2><p>Reutiliza el contrato temporario y el inventario del pack de alquileres y agrega lo propio de la temporada:</p>")
 + LP.modelos_html([dict(titulo="Contrato de locación temporaria", cuando="Plazo corto, destino turístico o de descanso."), dict(titulo="Recibo de seña y reserva", cuando="Fechas, monto y política de cancelación."),
                    dict(titulo="Inventario y estado", cuando="Para el día de la entrega, con fotos."), dict(titulo="Acta de entrega de llaves", cuando="Entrada y salida, con lecturas de servicios."),
                    dict(titulo="Reglamento de la casa", cuando="Horarios, mascotas, ruido, limpieza y daños."), dict(titulo="Recibo de pago", cuando="Saldo y depósito.")])
 + of_temp())

JS_T = js("""const c=document.querySelectorAll('#tm-chk input');
function a(){const t=n('tm-noche')*n('tm-noches'),s=t*Math.min(100,n('tm-sena'))/100,d=t*Math.min(100,n('tm-dep'))/100;$('tm-t').textContent=ars(t);$('tm-s').textContent=ars(s);$('tm-sa').textContent=ars(t-s);$('tm-d').textContent=ars(d)}
function k(){const x=[...c].filter(e=>e.checked).length;$('tm-bar').style.width=(x*100/c.length)+'%';$('tm-sc').textContent=x+' de '+c.length+' verificados. '+(x<6?'Todavía no señes: faltan controles.':x<c.length?'Vas bien: completá lo que falta antes de pagar.':'Verificaste todo lo que se puede verificar.')}
document.querySelectorAll('.comp input').forEach(e=>e.addEventListener('input',a));c.forEach(e=>e.addEventListener('change',k));a();k();""")

# ===================================================================== 5. VIAJE DE MENORES
def of_viaje():
    return LP.oferta("viajemenor", "Pack en Word (.docx)", "Pack Autorización de Viaje de Menores",
        "Modelos y guía por caso para que el chico viaje con los papeles que corresponden, en el país o en la nota que te piden para el exterior.",
        ["Autorización dentro del país: con un solo padre y con terceros (abuelos, tíos)", "Nota a la empresa de micros y declaración de domicilio", "Borrador de autorización para el exterior (para llevar al escribano o a Migraciones)", "Guía: qué papel necesitás en cada caso y quién lo emite"],
        "2.999", "Comprar el pack", PAGO)

BODY_V = (head("Gratis · Viajes con menores", "¿Qué papel necesita un menor para viajar?", "Elegí adónde viaja y con quién. Te decimos qué papel corresponde y quién lo tiene que emitir.")
 + '<div class="r2dos"><div class="comp"><div class="comp-cab"><span>Tu caso</span><span>Gratis</span></div><div class="comp-cuerpo">'
 + '<div class="campo"><label for="vm-d">Destino</label><select id="vm-d"><option value="n">Dentro de Argentina</option><option value="m">Exterior: países del Mercosur y asociados</option><option value="e">Exterior: otro destino</option></select></div>'
 + '<div class="campo"><label for="vm-q">¿Con quién viaja?</label><select id="vm-q"><option value="a">Con ambos padres</option><option value="u">Con uno solo de los padres</option><option value="t">Con otra persona (abuelos, tíos, amigos)</option><option value="s">Solo</option></select></div>'
 + '<div class="campo"><label for="vm-t">Transporte</label><select id="vm-t"><option value="b">Micro de larga distancia</option><option value="v">Avión</option><option value="c">Auto particular</option></select></div>'
 + '</div></div><div><div class="r2res" id="vm-out" aria-live="polite"></div></div></div>'
 + AVH
 + lec("<h2>Qué exige cada organismo</h2>") + quien([
    ("Escribano", "Certifica la firma de los padres en la autorización para salir del país con un solo padre o con terceros. También puede hacerlo un juez de paz o una autoridad consular.", False),
    ("Migraciones y Registro Civil", "Migraciones recibe la autorización de salida del país en sus delegaciones y el Registro Civil lo hace en algunas jurisdicciones. Los requisitos cambian: confirmalos en argentina.gob.ar/migraciones.", False),
    ("Juzgado", "Hace falta una autorización judicial si uno de los padres no la da o no se lo encuentra. Un modelo no la reemplaza.", True)])
 + lec("<h2>Lo que no se puede resolver con un modelo</h2><ul><li><b>Salir del país</b> con un solo padre o con terceros exige una autorización con firma certificada. El modelo del pack es el texto que llevás al escribano o a Migraciones: sin esa certificación no tiene valor para salir.</li><li><b>Dentro del país</b> la ley no exige una autorización especial, pero muchas empresas de transporte y alojamientos piden una nota firmada por los padres. Confirmalo con la empresa.</li></ul>")
 + lec("<h2>Qué suma el pack</h2>")
 + LP.modelos_html([dict(titulo="Autorización con un solo padre", cuando="Viaje nacional con el chico y un progenitor."), dict(titulo="Autorización a terceros", cuando="Abuelos, tíos o un adulto de confianza."),
                    dict(titulo="Nota a la empresa de micros", cuando="Para presentar en la boletería o al subir."), dict(titulo="Declaración de domicilio", cuando="Datos de contacto y lugar de estadía."),
                    dict(titulo="Borrador para el exterior", cuando="Para llevar al escribano o a Migraciones."), dict(titulo="Guía por caso", cuando="Qué papel y quién lo emite.")])
 + of_viaje())

JS_V = js("""function a(){const d=$('vm-d').value,q=$('vm-q').value,t=$('vm-t').value;let h,w,x='';
if(q==='a'){h=d==='n'?'No necesitás autorización especial':'Documento de cada uno y partida de nacimiento';w=d==='n'?'Viajan con ambos padres: alcanza el DNI del chico y los de los padres. Llevá una copia de la partida o libreta por las dudas.':'Viaja con ambos padres: llevan sus pasaportes o DNI según el destino, y la partida de nacimiento o libreta que acredite el vínculo.';x='Quién emite: nadie.'}
else if(d==='n'){h='Autorización simple, recomendada';w=(q==='u'?'Viaja con uno solo de los padres: no hace falta escribano, pero conviene llevar una autorización firmada por el otro padre.':q==='t'?'Viaja con terceros: llevá una autorización firmada por ambos padres, con copia de sus DNI.':'Viaja solo: las empresas suelen exigir una autorización firmada por ambos padres, y algunas no permiten viajar solos a menores de cierta edad.')+(t==='b'?' Consultá a la empresa de micros qué piden: algunas exigen firma certificada.':t==='v'?' Consultá a la aerolínea: para menores sin acompañante tienen servicio propio.':'');x='Quién emite: los padres, y la certificación es opcional (la pide la empresa).'}
else{h='Autorización de salida con firma certificada';w=(q==='u'?'Con un solo padre, el otro debe autorizar la salida del país.':q==='t'?'Con terceros, ambos padres deben autorizar la salida del país.':'Un menor solo necesita la autorización de ambos padres para salir del país.')+(d==='m'?' En países del Mercosur y asociados rige el mismo requisito.':' Además, confirmá qué exige el país de destino.');x='Quién emite: escribano, juez de paz, autoridad consular o Migraciones (en algunas jurisdicciones, también el Registro Civil).'}
$('vm-out').innerHTML='<b class="g">'+h+'</b><p style="margin:0">'+w+'</p><p class="nota" style="margin:0">'+x+'</p>'}
['vm-d','vm-q','vm-t'].forEach(i=>$(i).addEventListener('change',a));a();""")

# ===================================================================== 6. CUOTA ALIMENTARIA
def of_alim():
    return LP.oferta("alimentos", "Modelo en Word (.docx)", "Planilla de gastos del hijo",
        "Una planilla para ordenar y documentar los gastos mensuales del hijo, con una guía breve.",
        ["Planilla de gastos del hijo por rubro (vivienda, salud, educación, cuidado y más)", "Guía: qué se resuelve entre las partes, qué requiere juez y por qué conviene llevar los comprobantes"],
        "3.999", "Comprar el pack", PAGO, '<a class="nota" href="/aguinaldo">Calculá el aguinaldo (SAC) de diciembre</a>')

BODY_A = (head("Gratis · Cuota alimentaria", "¿La cuota alimentaria incluye el aguinaldo?", "Depende de cómo se fijó. Calculá cuánto corresponde en diciembre y en qué casos el aguinaldo integra la cuota.")
 + '<div class="r2dos"><div class="comp"><div class="comp-cab"><span>Tu cuota</span><span>Gratis</span></div><div class="comp-cuerpo">'
 + '<div class="campo"><label for="al-f">¿Cómo se fijó la cuota?</label><select id="al-f"><option value="p">Porcentaje de los ingresos del alimentante</option><option value="m">Monto fijo en pesos</option></select></div>'
 + '<div class="fila2">' + field("al-s", "Sueldo mensual de referencia", 1200000, "$") + field("al-p", "Porcentaje", 25, "", "%") + "</div>"
 + '<div class="campo" id="al-mw">' + field("al-m", "Monto fijo mensual", 300000, "$") + "</div>"
 + '<div class="campo"><label for="al-a">¿El aguinaldo está incluido en la cuota?</label><select id="al-a"><option value="s">Sí: se paga también sobre el SAC</option><option value="n">No: solo sobre el sueldo mensual</option></select></div>'
 + '</div></div><div><div class="r2res" id="al-out" aria-live="polite"></div>'
 + '<p class="nota">Estimación con valores que cargás vos. Para el SAC exacto, usá la <a href="/aguinaldo">calculadora de aguinaldo</a>.</p></div></div>'
 + AVH
 + lec("<h2>Qué se resuelve entre las partes y qué necesita juez</h2>") + quien([
    ("Entre las partes", "Pueden acordar la cuota, la forma de pago y los gastos extra, y llevar un registro de los pagos con recibos. Sirve de prueba.", False),
    ("Homologación judicial", "El convenio cobra fuerza ejecutiva recién cuando el juzgado de familia lo homologa. Hasta entonces, un reclamo requiere ir al juez.", False),
    ("Juzgado, sin atajos", "Aumentar o reducir la cuota, o ejecutar una deuda cuando el otro no cumple, se tramita ante el juzgado. Una intimación escrita ayuda, pero no reemplaza el proceso.", True)])
 + lec("<h2>El aguinaldo y la cuota</h2><ul><li>Si la cuota es un <b>porcentaje de los ingresos</b>, suele incluir lo que cobra el alimentante, también el SAC. Conviene que el convenio lo diga expresamente.</li><li>Si es un <b>monto fijo</b>, el aguinaldo no lo modifica salvo que se haya pactado un monto extra en junio y diciembre.</li><li>El convenio homologado manda: si dice otra cosa, aplicá lo que dice.</li></ul>")
 + lec("<h2>Qué suma el pack</h2>")
 + LP.modelos_html([dict(titulo="Planilla de gastos del hijo", cuando="Salud, educación, vivienda, útiles y recreación."), dict(titulo="Guía breve", cuando="Qué se resuelve entre las partes y cuándo hace falta el juzgado.")])
 + of_alim())

JS_A = js("""function a(){const f=$('al-f').value,inc=$('al-a').value==='s',s=n('al-s'),p=n('al-p')/100,m=n('al-m');$('al-mw').style.display=f==='m'?'':'none';
const cuota=f==='p'?s*p:m,sac=f==='p'&&inc?s*p/2:0;
$('al-out').innerHTML='<div class="fil"><span>Cuota mensual</span><span>'+ars(cuota)+'</span></div><div class="fil"><span>Cuota adicional por SAC (junio y diciembre)</span><span>'+ars(sac)+'</span></div><div class="fil"><span>Total a pagar en diciembre</span><span>'+ars(cuota+sac)+'</span></div><p class="nota" style="margin:0">'+(f==='m'?'Monto fijo: el aguinaldo no suma salvo pacto expreso.':inc?'Con porcentaje y SAC incluido, el 50% del sueldo mensual por el porcentaje se suma en cada semestre.':'El convenio no incluye el SAC: no corresponde cuota adicional.')+'</p>'}
document.querySelectorAll('.gen input,.comp input,.comp select').forEach(e=>e.addEventListener('input',a));a();""")

PAGES = {
 "alquiler-temporario-verano": ("Alquiler temporario de verano: checklist anti-estafa y modelo de contrato", "Checklist gratis para no caer en estafas al alquilar una casa de verano y calculadora de seña y depósito. Pack con contrato de temporada, recibo de seña y reglamento por $2.999.", BODY_T, JS_T),
 "autorizacion-viaje-menores": ("Autorización de viaje de menores: qué papel necesitás y quién lo emite", "Asistente gratis: dentro del país o al exterior, con uno de los padres o con terceros. Qué exige el escribano, Migraciones o la empresa de micros. Pack de modelos por $2.999.", BODY_V, JS_V),
 "cuota-alimentaria-aguinaldo": ("¿La cuota alimentaria incluye el aguinaldo? Calculá diciembre", "Cuánto corresponde de cuota alimentaria con aguinaldo en diciembre y cuándo el SAC integra la cuota. Planilla de gastos del hijo por $3.999.", BODY_A, JS_A),
}
# ===================================================================== packs Word
def build():
    from packs_lib import Doc
    here = os.path.dirname(os.path.abspath(__file__)); priv = os.path.join(here, "..", "private")

    def mk(pack, titulo, sub, box=None):
        d = Doc(pack, titulo, sub)
        d.box("Antes de usarlo", box or [AV, "Completá los campos resaltados en amarillo y borrá lo que no aplique."])
        return d

    def save(name, docs, extra=()):
        with zipfile.ZipFile(os.path.join(priv, name), "w", zipfile.ZIP_DEFLATED) as z:
            for fn, d in docs:
                buf = io.BytesIO(); d.d.save(buf); z.writestr(fn, buf.getvalue())
            for fn, data in extra:
                z.writestr(fn, data)
        print("ok", name, len(docs) + len(extra))

    # ------------------------------------------------ alquiler temporario
    P = "Pack Alquiler Temporario de Verano"
    L = lambda t, s, b=None: mk(P, t, s, b)
    d = Doc(P, "Guía y contenido del pack", "Cómo usar los modelos")
    d.box("Importante", [AV, "Sirve para propietarios e inquilinos: leé el modelo completo antes de firmar."])
    d.h("Qué incluye"); d.bullets(["01. Contrato de locación temporaria (del pack de alquileres)", "02. Anexo de inventario y estado (del pack de alquileres)", "03. Recibo de seña y reserva", "04. Acta de entrega y devolución de llaves", "05. Reglamento de la casa", "06. Recibo de pago (del pack de alquileres)", "07. Checklist anti-estafa"])
    d.h("Qué exige escribano, registro o juzgado")
    d.bullets(["Un alquiler de temporada corto no exige escribano: alcanza con el contrato o la reserva firmados, recibos de cada pago y un inventario.", "Algunas provincias cobran impuesto de sellos o exigen registrar contratos: consultá al organismo recaudador de la provincia donde está la casa.", "Si el titular no es quien alquila (administra o subalquila), pedí a un escribano o abogado que revise la documentación antes de pagar."])
    d.h("Seña y depósito"); d.bullets(["Los porcentajes habituales (seña de 30% a 50% y depósito del 10% al 20%) son usos del mercado, no una regla legal. Lo que vale es lo que quede escrito.", "Pagá siempre por transferencia a una cuenta a nombre del propietario o de la inmobiliaria y pedí recibo."])
    docs = [("00-LEEME-Guia-del-pack.docx", d)]
    d = L("Recibo de seña y reserva", "Reserva del alquiler temporario")
    d.p("[[Ciudad]], [[fecha]]", False)
    d.p("Recibí de [[inquilino]], DNI [[dni]], la suma de $ [[monto]] ([[monto en letras]]) en concepto de seña y reserva del inmueble ubicado en [[dirección]], por el período del [[fecha de ingreso]] al [[fecha de egreso]], con un precio total de $ [[precio total]]. El saldo de $ [[saldo]] se abonará el [[fecha de ingreso]], al momento de la entrega de llaves.")
    d.h("Política de cancelación"); d.bullets(["Si el inquilino cancela con más de [[días]] días de anticipación: [[devolución de la seña, total o parcial]].", "Si el inquilino cancela con menos anticipación o no se presenta: la seña [[se pierde / se devuelve en parte]].", "Si el propietario cancela o no entrega la casa: devuelve la seña en [[doble / simple]] dentro de [[días]] días."])
    d.p("El depósito en garantía de $ [[monto]] se devolverá dentro de [[días]] días del egreso, una vez controlado el estado de la casa y descontados daños comprobados.")
    d.firmas(["Propietario/a o administrador/a", "Inquilino/a"]); docs.append(("03-Recibo-de-sena-y-reserva.docx", d))
    d = L("Acta de entrega y devolución de llaves", "Ingreso y egreso")
    d.p("[[Ciudad]], [[fecha]]", False)
    d.p("Se deja constancia de que en la fecha se entregan las llaves del inmueble de [[dirección]] a [[inquilino]], DNI [[dni]].")
    d.table(["Concepto", "Ingreso", "Egreso"], [["Juegos de llaves entregados", "[[cantidad]]", "[[cantidad]]"], ["Lectura de luz", "[[kWh]]", "[[kWh]]"], ["Lectura de gas", "[[m3]]", "[[m3]]"], ["Estado general", "[[detalle]]", "[[detalle]]"], ["Daños o faltantes", "[[detalle]]", "[[detalle]]"], ["Limpieza", "[[detalle]]", "[[detalle]]"]], [6, 4.5, 4.5])
    d.p("Ambas partes declaran haber revisado el estado de la casa en el momento del ingreso y adjuntan fotos fechadas.")
    d.firmas(["Propietario/a", "Inquilino/a"]); docs.append(("04-Acta-de-entrega-de-llaves.docx", d))
    d = L("Reglamento de la casa", "Normas de convivencia durante la estadía")
    d.h("Normas"); d.bullets(["Capacidad máxima: [[cantidad]] personas. No se admiten huéspedes adicionales sin autorización.", "Horario de silencio: de [[hora]] a [[hora]]. Respetá a los vecinos.", "Mascotas: [[permitidas / no permitidas]].", "Fumar: [[permitido en exteriores / prohibido]].", "Basura: se deposita en [[lugar]] los días [[días]].", "Uso de parrilla, pileta y espacios comunes: [[condiciones]].", "Los daños comprobados se descuentan del depósito en garantía.", "Salida (check-out): hasta las [[hora]] del día de egreso; ingreso desde las [[hora]]."])
    d.p("Para consultas durante la estadía: [[nombre y teléfono del contacto]].", False)
    docs.append(("05-Reglamento-de-la-casa.docx", d))
    d = L("Checklist anti-estafa", "Antes de enviar la seña")
    d.table(["Verificación", "Resultado"], [[c, "[[ ]]"] for c in CHK], [11, 4])
    docs.append(("07-Checklist-anti-estafa.docx", d))
    z = zipfile.ZipFile(os.path.join(priv, "pack-alquiler.zip"))
    reuse = [("01-Contrato-Locacion-Temporaria.docx", z.read("02-Contrato-Locacion-Temporaria.docx")), ("02-Anexo-Inventario-Estado-Inmueble.docx", z.read("04-Anexo-Inventario-Estado-Inmueble.docx")), ("06-Recibo-de-Pago.docx", z.read("07-Recibo-de-Alquiler.docx"))]
    save("pack-alqtemp.zip", docs, reuse)

    # ------------------------------------------------ viaje de menores
    P = "Pack Autorización de Viaje de Menores"
    L = lambda t, s, b=None: mk(P, t, s, b)
    d = Doc(P, "Guía por caso", "Qué papel necesitás y quién lo emite")
    d.box("Importante", [AV, "Para salir del país, estos modelos son el texto que se lleva al escribano o a Migraciones: sin la certificación de la firma no tienen valor."])
    d.table(["Caso", "Papel", "Quién lo emite"], [
        ["Dentro del país, con ambos padres", "DNI de todos. No requiere autorización.", "Nadie"],
        ["Dentro del país, con un solo padre", "Autorización simple del otro padre (recomendada).", "Los padres; certificar es opcional"],
        ["Dentro del país, con terceros", "Autorización de ambos padres + copia de sus DNI.", "Los padres; algunas empresas piden firma certificada"],
        ["Al exterior, con ambos padres", "Documentos de viaje y partida de nacimiento.", "Nadie"],
        ["Al exterior, con un solo padre o con terceros", "Autorización de salida con firma certificada.", "Escribano, juez de paz, autoridad consular o Migraciones"],
        ["Falta de acuerdo o padre ausente", "Autorización judicial.", "Juzgado de familia"]], [5, 6, 5])
    d.p("Los requisitos de Migraciones, del Registro Civil y de cada empresa cambian: confirmalos antes de viajar en argentina.gob.ar/migraciones y con la empresa de transporte.")
    docs = [("00-LEEME-Guia-por-caso.docx", d)]
    d = L("Autorización de viaje dentro del país (un padre)", "Viaje nacional con un solo progenitor")
    d.p("[[Ciudad]], [[fecha]]", False)
    d.p("Yo, [[nombre del padre/madre que NO viaja]], DNI [[dni]], con domicilio en [[domicilio]], en mi carácter de [[padre / madre]] de [[nombre del menor]], DNI [[dni del menor]], nacido/a el [[fecha de nacimiento]], AUTORIZO a que viaje junto con [[nombre del padre/madre que viaja]], DNI [[dni]], con destino a [[destino]], desde el [[fecha de salida]] hasta el [[fecha de regreso]], por [[medio de transporte]].")
    d.p("Declaro conocer y aceptar los datos del viaje. Para consultas me pueden contactar al [[teléfono]].")
    d.firmas(["Padre/madre que autoriza"]); docs.append(("01-Autorizacion-nacional-un-padre.docx", d))
    d = L("Autorización de viaje dentro del país (terceros)", "Viaje con abuelos, tíos u otro adulto")
    d.p("[[Ciudad]], [[fecha]]", False)
    d.p("Nosotros, [[nombre del padre]], DNI [[dni]], y [[nombre de la madre]], DNI [[dni]], padres de [[nombre del menor]], DNI [[dni del menor]], nacido/a el [[fecha de nacimiento]], AUTORIZAMOS a que viaje junto con [[nombre del adulto responsable]], DNI [[dni]], vínculo: [[abuelo/a, tío/a, otro]], con destino a [[destino]], desde el [[fecha de salida]] hasta el [[fecha de regreso]], por [[medio de transporte]], quedando el menor a su cuidado durante el viaje.")
    d.p("El adulto responsable está facultado para [[autorizar atención médica de urgencia / realizar trámites vinculados al viaje]]. Teléfonos de contacto de los padres: [[teléfonos]].")
    d.firmas(["Padre", "Madre"]); docs.append(("02-Autorizacion-nacional-terceros.docx", d))
    d = L("Nota a la empresa de transporte", "Para presentar en la boletería")
    d.p("[[Ciudad]], [[fecha]]", False)
    d.p("Señores [[empresa de transporte]]\nPresente", False)
    d.p("Ref.: viaje del menor [[nombre]], DNI [[dni del menor]], [[origen]] - [[destino]], fecha [[fecha]], pasaje N.º [[número]].")
    d.p("Nos dirigimos a ustedes para informar que prestamos conformidad al viaje del menor mencionado, quien viaja [[solo / acompañado por nombre y DNI]]. Quedamos a disposición para cualquier requisito adicional que la empresa exija en estos casos, y adjuntamos copia de nuestros DNI.")
    d.firmas(["Padre/madre"]); docs.append(("03-Nota-a-la-empresa-de-micros.docx", d))
    d = L("Declaración de domicilio y contacto", "Datos para el viaje")
    d.table(["Dato", "Detalle"], [["Menor", "[[nombre y DNI]]"], ["Domicilio de los padres", "[[domicilio]]"], ["Teléfonos de los padres", "[[teléfonos]]"], ["Lugar de estadía", "[[dirección y teléfono]]"], ["Adulto responsable en el viaje", "[[nombre, DNI y teléfono]]"], ["Obra social y alergias", "[[datos]]"]], [6, 9])
    d.p("Declaro que los datos son ciertos y que me comprometo a informar cualquier cambio.")
    d.firmas(["Declarante"]); docs.append(("04-Declaracion-de-domicilio.docx", d))
    d = L("Borrador de autorización de salida del país", "Para llevar al escribano o a Migraciones", [AV, "Este texto NO vale por sí solo: la firma debe certificarla un escribano, un juez de paz, la autoridad consular o Migraciones, según corresponda."])
    d.p("[[Ciudad]], [[fecha]]", False)
    d.p("Yo, [[nombre]], DNI [[dni]], padre/madre de [[nombre del menor]], DNI [[dni del menor]], AUTORIZO su salida de la República Argentina junto con [[acompañante: padre/madre/tercero, con nombre y DNI]], con destino a [[país]], desde el [[fecha de salida]] hasta el [[fecha de regreso]], por [[medio de transporte]]. Esta autorización [[es por única vez / vale para múltiples viajes hasta fecha]].")
    d.firmas(["Padre/madre que autoriza"]); docs.append(("05-Borrador-autorizacion-exterior.docx", d))
    save("pack-viajemenor.zip", docs)

    # ------------------------------------------------ cuota alimentaria
    P = "Planilla de Gastos del Hijo"
    L = lambda t, s: mk(P, t, s, [AV, "Planilla orientativa para ordenar gastos: no reemplaza al juez ni a un abogado/a.", "Completá los campos resaltados en amarillo y borrá lo que no aplique."])
    d = Doc(P, "Guía y contenido del pack", "Qué se resuelve entre las partes y qué requiere juez")
    d.box("Importante", [AV, "Riesgo: un mal planteo puede perjudicar al niño o a quien reclama. Ante una situación de violencia o de urgencia, consultá a un abogado/a o a la defensoría de tu jurisdicción."])
    d.h("Qué incluye"); d.bullets(["01. Planilla de gastos del hijo"])
    d.h("Qué requiere juez")
    d.bullets(["El convenio tiene fuerza ejecutiva cuando lo homologa el juzgado de familia competente.", "Aumentar, reducir o dejar sin efecto la cuota se tramita ante el juzgado.", "Reclamar por vía judicial una deuda de cuotas se hace ante el juzgado. La intimación documentada ayuda a probar la mora.", "El aguinaldo integra la cuota si se fijó como porcentaje de los ingresos y así lo dice el convenio. Si no se aclara, pedirlo por escrito evita discusiones."])
    d.h("Qué se hace entre las partes"); d.bullets(["Acordar la cuota, la fecha y la forma de pago, y los gastos extra (salud, útiles, colegio).", "Documentar cada pago con recibo o transferencia.", "Llevar la planilla de gastos para fundar cualquier pedido de actualización."])
    docs = [("00-LEEME-Guia-del-pack.docx", d)]
    d = L("Planilla de gastos del hijo", "Base para fundar la cuota")
    d.table(["Rubro", "Monto mensual ($)", "Observaciones"], [[r, "[[ ]]", "[[ ]]"] for r in ["Vivienda (proporción)", "Alimentación", "Salud y obra social", "Educación (cuota, útiles, transporte)", "Vestimenta", "Recreación y deporte", "Cuidado (niñera, guardería)", "Otros"]] + [["TOTAL", "[[ ]]", ""]], [7, 4, 4])
    d.p("Guardá los comprobantes de cada gasto: los va a pedir el juzgado si se discute el monto.")
    docs.append(("01-Planilla-de-gastos-del-hijo.docx", d))
    save("pack-alimentos.zip", docs)

if __name__ == "__main__":
    build()
