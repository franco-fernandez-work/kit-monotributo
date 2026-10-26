# Integración: copiar a tools/ junto a anses_arts.py y agregar ARTS.update(__import__("ronda9_arts").ARTS_R9) al inicio de main() en tools/build_site.py
from anses_arts import _oferta
NOTA = '<p class="nota">Información general y orientativa, sin carácter de asesoramiento legal ni financiero. Confirmá índices, plazos y normas en la fuente oficial antes de actuar.</p>'
CALC = """<div class="lectura" id="calc" style="background:var(--hoja);border:1px solid var(--linea);padding:16px;border-radius:4px">
<h2 style="margin-top:0">¿Cuánto te va a costar de verdad?</h2>
<p><label>Precio acordado hoy (ARS)<br><input id="f-p" type="number" min="0" step="1000" value="3000000"></label></p>
<p><label>Ya pagaste (ARS)<br><input id="f-g" type="number" min="0" step="1000" value="500000"></label></p>
<p><label>Meses hasta el evento<br><input id="f-m" type="number" min="0" max="36" value="10"></label></p>
<p><label>Inflación mensual esperada (%)<br><input id="f-i" type="number" min="0" max="50" step="0.1" value="3"></label></p>
<p><button class="boton" id="f-b" type="button">Calcular</button></p><div id="f-r" aria-live="polite"></div></div>
<script>
(function(){var $=function(i){return document.getElementById(i)};
function m(n){return '$ '+Math.round(n).toLocaleString('es-AR')}
$('f-b').onclick=function(){var p=+$('f-p').value||0,g=+$('f-g').value||0,n=+$('f-m').value||0,i=(+$('f-i').value||0)/100;
var s=Math.max(0,p-g),f=Math.pow(1+i,n),pr=g+s*f;
$('f-r').innerHTML='<p>Si el saldo se ajusta por inflación, el total proyectado es <b>'+m(pr)+'</b>: <b>'+m(pr-p)+'</b> más que hoy.</p>'+(n>0?'<p>Para llegar con todo pagado tendrías que ahorrar unos <b>'+m((pr-g)/n)+' por mes</b>.</p>':'')+'<p class="nota">Estimación orientativa: si tu contrato tiene precio fijo, el saldo no se ajusta. Consultá el IPC en indec.gob.ar.</p>'}})();
</script>"""
FIE = ("Presupuesto de fiesta de 15 o casamiento con inflación: calculadora y guía",
 "Calculá cuánto te costará de verdad una fiesta de 15 o un casamiento si el saldo se ajusta por inflación, y qué pedir en el contrato del salón y los proveedores.",
 '<span class="etiqueta">Fiestas · Presupuesto</span><h1>Fiesta de 15 o casamiento: cuánto va a costar con inflación</h1>'
 '<p class="bajada">Pactás hoy un precio y pagás en cuotas durante meses. Si el contrato no dice cómo se ajusta, la diferencia la pagás vos. Probá la calculadora.</p>' + CALC +
 '<div class="lectura"><h2>Qué pedir en el contrato</h2><ul><li>Precio, fecha, horario y qué incluye, por escrito.</li><li>Cláusula de ajuste definida: con qué índice (por ejemplo, el IPC del INDEC) y cada cuánto, o precio fijo.</li><li>Un recibo por cada pago, con fecha, monto y concepto.</li><li>Qué pasa si cancela el proveedor y qué pasa si cancelás vos.</li></ul>'
 '<h2>Si algo sale mal</h2><p>Guardá contratos, recibos y chats. Podés presentar un reclamo en la oficina de Defensa del Consumidor de tu jurisdicción; para montos altos, consultá a un abogado.</p>'
 '<p class="nota">Fuentes: <a href="https://www.indec.gob.ar" rel="noopener">INDEC</a> (IPC) y <a href="https://www.argentina.gob.ar/produccion/defensadelconsumidor" rel="noopener">Defensa del Consumidor</a>.</p>' + NOTA + '</div>'
 + _oferta("fiesta", "Guía PDF + planilla", "Guía y organizador de fiesta con inflación", "Proveedores, pagos, invitados y proyección de costos en un solo archivo.",
   ["Guía PDF de 4 páginas: presupuesto, contratos y señas, inflación y cuotas, reclamos", "Planilla Excel con proyección de costos por proveedor (fijo, inflación o dólar)", "Calendario de pagos con vencimientos que se marcan solos", "Lista de invitados con confirmaciones y cronograma mes a mes"],
   "3.999", "Comprar la guía", "Pagás con Mercado Pago y la descargás al instante."))

VER = ("Presupuesto de vacaciones de verano: cuánto gastar y cómo controlarlo",
 "Cómo armar el presupuesto del veraneo por rubro, qué mirar antes de reservar y qué documentación revisar. Guía y planilla.",
 '<span class="etiqueta">Vacaciones · Presupuesto</span><h1>Vacaciones de verano: armá el presupuesto antes de reservar</h1>'
 '<p class="bajada">Los gastos chicos (peajes, comida, excursiones, estacionamiento) son los que rompen el presupuesto. Ordenarlos antes ayuda a decidir.</p>'
 '<div class="lectura"><h2>Los rubros que no pueden faltar</h2><ul><li>Alojamiento: precio por noche más limpieza y depósito.</li><li>Transporte: pasajes, combustible, peajes y estacionamiento.</li><li>Comidas por persona por día.</li><li>Excursiones, seguro o asistencia y compras.</li><li>Un 10% de imprevistos como mínimo.</li></ul>'
 '<h2>Antes de pagar una seña</h2><ul><li>Pedí el precio final y la política de cancelación por escrito.</li><li>Desconfiá de transferencias a terceros sin contrato.</li><li>Guardá capturas y comprobantes de la oferta.</li></ul>'
 '<h2>Documentación</h2><p>Verificá en <a href="https://www.cancilleria.gob.ar" rel="noopener">cancilleria.gob.ar</a> qué documento exige tu destino y si los menores necesitan autorización de viaje.</p>' + NOTA + '</div>'
 + _oferta("veraneo", "Guía PDF + planilla", "Guía y planilla de presupuesto de vacaciones", "Presupuesto por rubro, gastos reales y checklist de salida.",
   ["Guía PDF de 4 páginas: cuánto gastar, reservas, dinero en el exterior y documentación", "Planilla Excel con presupuesto por rubro y monedas con tu cotización", "Hoja de gastos reales con total por día", "Checklist antes de viajar"],
   "2.999", "Comprar la guía", "Pagás con Mercado Pago y la descargás al instante."))

FIN = ("Presupuesto de Navidad y Año Nuevo: regalos, cena y reparto de gastos",
 "Cómo organizar regalos con tope, cantidades de comida por persona y dividir los gastos de las fiestas sin discusiones.",
 '<span class="etiqueta">Fiestas · Fin de año</span><h1>Navidad y Año Nuevo: regalos, cena y cuentas claras</h1>'
 '<p class="bajada">Las fiestas se encarecen por compras de último momento y gastos que nadie anota. Un tope y una lista alcanzan.</p>'
 '<div class="lectura"><h2>Cantidades de referencia por persona (ajustables)</h2><ul><li>Carne, pollo o vitel toné: unos 300 g.</li><li>Guarnición y ensaladas: unos 200 g.</li><li>Postre: unos 150 g.</li><li>Bebidas sin alcohol: alrededor de 1 litro.</li><li>Brindis: alrededor de un tercio de botella.</li></ul>'
 '<h2>Orden de compras</h2><p>Pedí con anticipación pan dulce, carnes y bebidas; dejá frescos y hielo para el 22 o el 23. Guardá tickets de los regalos por si hay que cambiarlos.</p>'
 '<h2>Repartir gastos</h2><p>Anotá cada compra con quien pagó y dividí en partes iguales: la diferencia entre lo que puso cada uno y lo que le corresponde es el saldo.</p>' + NOTA + '</div>'
 + _oferta("fiestas", "Planilla + guía", "Planilla y guía de fiestas de fin de año", "Regalos con tope, cena por comensal y reparto de gastos.",
   ["Guía PDF de 4 páginas con checklist y cronograma", "Planilla Excel con regalos, presupuesto y diferencia por persona", "Hoja de cena con cantidades por comensal y costo total", "Reparto de gastos entre participantes y saldos"],
   "1.999", "Comprar la guía", "Pagás con Mercado Pago y la descargás al instante."))

ARTS_R9 = {"presupuesto-fiesta-15-casamiento-inflacion": FIE, "presupuesto-vacaciones-verano": VER, "presupuesto-navidad-fin-de-anio": FIN}
