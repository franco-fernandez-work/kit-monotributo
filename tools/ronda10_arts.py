# Integración: copiar a tools/ junto a anses_arts.py y agregar ARTS.update(__import__("ronda10_arts").ARTS_R10) al inicio de main() en tools/build_site.py
from anses_arts import _oferta
NOTA = '<p class="nota">Información general y orientativa, sin carácter de asesoramiento legal, contable ni financiero. Confirmá índices, plazos y normas en la fuente oficial antes de actuar.</p>'
def _calc(pref, titulo, campos, js, boton="Calcular"):
    inp = "".join(f'<p><label>{l}<br><input id="{pref}-{k}" type="number" min="0" step="{st}" value="{v}"></label></p>' for k,l,st,v in campos)
    return (f'<div class="lectura" id="calc" style="background:var(--hoja);border:1px solid var(--linea);padding:16px;border-radius:4px"><h2 style="margin-top:0">{titulo}</h2>{inp}'
            f'<p><button class="boton" id="{pref}-b" type="button">{boton}</button></p><div id="{pref}-r" aria-live="polite"></div></div>'
            f'<script>(function(){{var $=function(i){{return document.getElementById(i)}};function m(n){{return \'$ \'+Math.round(n).toLocaleString(\'es-AR\')}}'
            f'$(\'{pref}-b\').onclick=function(){{{js}}}}})();</script>')

EMP_CALC = _calc("e","¿A qué precio tenés que vender?",
 [("c","Costo unitario del producto (ARS)","100","1000"),("e","Envío y packaging por unidad (ARS)","50","200"),("k","Comisión del canal (%)","0.1","10"),("g","Margen que querés ganar sobre el precio (%)","1","30")],
 "var c=+$('e-c').value||0,e=+$('e-e').value||0,k=(+$('e-k').value||0)/100,g=(+$('e-g').value||0)/100,d=1-k-g;"
 "if(d<=0){$('e-r').innerHTML='<p>Comisión y margen suman 100% o más: no hay precio posible. Bajá alguno.</p>';return}"
 "var p=Math.ceil((c+e)/d);$('e-r').innerHTML='<p>Precio sugerido: <b>'+m(p)+'</b>.</p><p>De cada venta: comisión <b>'+m(p*k)+'</b> y ganancia <b>'+m(p*g)+'</b> (el costo es '+m(c+e)+').</p>"
 "<p class=\"nota\">Cálculo orientativo. Impuestos y cuota de monotributo no están incluidos.</p>'")
EMP = ("Calculadora de precio y margen para emprendedores: stock, costos y ventas",
 "Calculá el precio de venta que cubre costo, envío y comisión del canal, y llevá el stock y la ganancia del mes con una planilla.",
 '<span class="etiqueta">Emprendedores · Navidad</span><h1>Precio con margen real: cuánto tenés que cobrar</h1>'
 '<p class="bajada">Si fijás el precio sumando un porcentaje al costo, la comisión del canal te come la ganancia. Probá la cuenta correcta.</p>' + EMP_CALC +
 '<div class="lectura"><h2>La fórmula</h2><p><b>Precio = (costo + envío) ÷ (1 − comisión − margen)</b>. El margen se calcula sobre el precio de venta, no sobre el costo.</p>'
 '<h2>Tres errores que se repiten</h2><ul><li>Olvidar la comisión de Mercado Libre o de la pasarela de pago.</li><li>No actualizar el costo cuando sube la mercadería.</li><li>Quedarse sin stock del producto más vendido en el pico de diciembre.</li></ul>' + NOTA + '</div>'
 + _oferta("emprendedor", "Guía PDF + planilla", "Guía y planilla de stock, costos y ventas", "Precio sugerido, stock automático con alerta de reposición y ganancia del mes.",
   ["Guía PDF de 4 páginas: costo real, precio y margen, stock, cierre del mes", "Planilla Excel con precio sugerido por producto y margen real", "Registro de ventas y compras con stock que se calcula solo", "Presupuesto mensual (plan vs. real) y Panel conectados al stock y a las ventas, más checklist de Navidad"],
   "2.999", "Comprar la guía", "Pagás con Mercado Pago y la descargás al instante."))

DEP_CALC = _calc("d","¿Cuánto te corresponde recuperar?",
 [("m","Depósito entregado (ARS)","10000","500000"),("a","Actualización acumulada pactada en el contrato (%)","1","0"),("x","Descuentos que aceptás con comprobante (ARS)","1000","0")],
 "var d=+$('d-m').value||0,a=(+$('d-a').value||0)/100,x=+$('d-x').value||0,t=d*(1+a);"
 "$('d-r').innerHTML='<p>Depósito actualizado: <b>'+m(t)+'</b>. Menos descuentos aceptados: <b>'+m(x)+'</b>.</p><p>A recuperar: <b>'+m(Math.max(0,t-x))+'</b>.</p>"
 "<p class=\"nota\">La actualización depende de lo que diga tu contrato. Si no dice nada, dejá 0.</p>'")
DEP = ("Cómo recuperar el depósito de alquiler: pasos, pruebas y cartas modelo",
 "Qué reunir antes de entregar el departamento, cómo discutir los descuentos y qué escribir si no te devuelven el depósito.",
 '<span class="etiqueta">Alquileres · Inquilinos</span><h1>Recuperar el depósito del alquiler: qué hacer antes de irte</h1>'
 '<p class="bajada">La mayoría de los depósitos se retienen por falta de pruebas, no por falta de derecho. Esto es lo que conviene tener.</p>' + DEP_CALC +
 '<div class="lectura"><h2>Antes de entregar las llaves</h2><ul><li>Releé el contrato: monto, actualización y plazo de devolución.</li><li>Buscá el inventario y las fotos del día que entraste.</li><li>Sacá fotos y video de cada ambiente, con fecha.</li><li>Pagá y guardá los comprobantes de servicios y expensas.</li><li>Firmá un acta de restitución de llaves, con fecha y estado.</li></ul>'
 '<h2>Qué dice la ley hoy</h2><p>Desde el DNU 70/2023, el artículo 1196 del Código Civil y Comercial permite que las partes pacten libremente monto, moneda y forma de devolución del depósito. Por eso manda tu contrato. Verificá el texto vigente en <a href="https://www.argentina.gob.ar/normativa" rel="noopener">argentina.gob.ar/normativa</a>.</p>'
 '<p class="nota">No reemplaza a un abogado: si el monto es importante o el conflicto escala, consultá antes de avanzar.</p>' + NOTA + '</div>'
 + _oferta("deposito10", "Guía PDF + planilla + cartas", "Guía, planilla y cartas modelo para recuperar el depósito", "Pruebas, descuentos y reclamo por escrito, en un solo pack.",
   ["Guía PDF de 4 páginas con tres cartas modelo (pedido, respuesta a descuentos, intimación)", "Planilla Excel: depósito actualizado, plazo de devolución y monto a recuperar", "Estado de ingreso vs. salida y descuentos con o sin comprobante", "Cierre de servicios y cronograma de salida"],
   "2.999", "Comprar la guía", "Pagás con Mercado Pago y la descargás al instante."))

COLE_CALC = _calc("v","¿Cuánto ahorrar por mes para la vuelta al cole?",
 [("t","Total estimado hoy: útiles, uniformes, cuotas (ARS)","10000","300000"),("n","Meses hasta la compra","1","3"),("i","Inflación mensual esperada (%)","0.1","3")],
 "var t=+$('v-t').value||0,n=+$('v-n').value||0,i=(+$('v-i').value||0)/100,f=t*Math.pow(1+i,n);"
 "$('v-r').innerHTML='<p>Total proyectado: <b>'+m(f)+'</b>.</p>'+(n>0?'<p>Ahorro mensual sugerido: <b>'+m(f/n)+'</b>.</p>':'')+'<p class=\"nota\">Estimación orientativa con la inflación que cargues.</p>'")
COLE = ("Vuelta al cole 2027: presupuesto, lista de útiles y ahorro mensual",
 "Calculá cuánto ahorrar por mes para la vuelta al cole, armá la lista de útiles reutilizando lo que ya tenés y compará precios.",
 '<span class="etiqueta">Familia · Vuelta al cole</span><h1>Vuelta al cole 2027: cuánto ahorrar por mes</h1>'
 '<p class="bajada">Matrícula, cuota, uniformes y útiles llegan juntos en febrero. Un plan de ahorro desde diciembre evita el apuro.</p>' + COLE_CALC +
 '<div class="lectura"><h2>Cómo ahorrar en la lista de útiles</h2><ul><li>Revisá primero lo que sobró del año pasado.</li><li>Comprá lo que sirve para varios hermanos en una sola vez.</li><li>Compará el mismo artículo en tres comercios antes de decidir.</li><li>Evitá el último fin de semana antes de clases.</li></ul>'
 '<h2>Beneficios con fecha límite</h2><p>La Ayuda Escolar Anual de ANSES requiere certificado de escolaridad y un trámite en Mi ANSES. Confirmá requisitos y plazos en <a href="https://www.argentina.gob.ar/anses" rel="noopener">argentina.gob.ar/anses</a>.</p>' + NOTA + '</div>'
 + _oferta("cole27", "Guía PDF + planilla", "Guía y planilla de vuelta al cole", "Presupuesto, útiles por hijo, comparador de precios y beneficios.",
   ["Guía PDF de 4 páginas: presupuesto, útiles, precios y beneficios", "Planilla Excel con presupuesto por rubro y ahorro mensual", "Lista de útiles por hijo con lo que ya tenés", "Comparador de precios entre tres comercios y cronograma"],
   "2.499", "Comprar la guía", "Pagás con Mercado Pago y la descargás al instante."))

ARTS_R10 = {"calculadora-precio-margen-emprendedores": EMP}  # DEP y COLE se unificaron con /recuperar-deposito-alquiler y /presupuesto-vuelta-al-cole (301 en public/_redirects)
