"""Páginas legales: términos, privacidad, devoluciones, botón de arrepentimiento y datos del vendedor. Se importa desde build_site.
Los datos del vendedor se completan UNA vez en VENDEDOR (los marcadores [COMPLETAR ...] salen tal cual en el sitio hasta entonces)."""

VENDEDOR = {
    "nombre": "[COMPLETAR: nombre y apellido del titular]",
    "cuit": "[COMPLETAR: CUIT]",
    "domicilio": "[COMPLETAR: domicilio legal, ciudad y provincia]",
    "email": "[COMPLETAR: email de contacto]",
}
DC_URL = "https://www.argentina.gob.ar/produccion/defensadelconsumidor/formulario"
V = VENDEDOR

CSS = r"""
/* legales */
.pie .wrap{display:block}
.pie .legal{display:flex;flex-wrap:wrap;gap:6px 18px;margin-top:10px;padding-top:10px;border-top:1px dashed var(--linea)}
.pie .legal a{color:var(--tinta-2)}
.pie .arrep,.menu .arrep{font-weight:700;color:var(--sello);border:1px solid var(--sello);border-radius:3px;padding:1px 8px}
.pie .vend{margin-top:8px;font-size:13px}
.legalbody h2{margin-top:30px}
.legalbody ol,.legalbody ul{padding-left:22px}
.legalbody li{margin:6px 0}
.arr-form{display:grid;gap:14px;max-width:560px;margin:18px 0}
.arr-form input,.arr-form select,.arr-form textarea{width:100%;font:400 16px var(--f-texto);padding:11px 12px;border:1.5px solid var(--linea);border-radius:4px;background:var(--papel);color:var(--tinta)}
.arr-form label{display:block;font-weight:700;font-size:15px;margin-bottom:6px}
.arr-form button{cursor:pointer;border:0;justify-self:start}
.arr-res{max-width:560px;border:1.5px solid var(--linea);border-radius:4px;padding:16px 18px;background:var(--hoja);display:none}
.arr-res.ok{border-color:#2f7d4f}.arr-res.mal{border-color:var(--sello)}
.arr-res b.cod{font:600 18px var(--f-num)}
"""

def footer():
    return (f'<footer class="pie"><div class="wrap"><span class="nombre"><b>CuentaClara</b> · Tus cuentas, claras. Tus trámites, resueltos.</span><span>Información general actualizada a octubre de 2026. No reemplaza a un contador ni la información oficial de ARCA.</span> <span>Pagos procesados por Mercado Pago</span>'
            f'<div class="legal"><a href="/terminos">Términos y condiciones</a><a href="/privacidad">Política de privacidad</a><a href="/devoluciones">Devoluciones</a><a href="/recuperar">¿Perdiste la descarga?</a>'
            f'<a href="/pedidos">¿No encontrás lo que buscás? Pedilo</a><a class="arrep" href="/arrepentimiento">Botón de arrepentimiento</a><a href="{DC_URL}" rel="noopener" target="_blank">Defensa del Consumidor: reclamos</a></div>'
            '</div></footer>')  # sin datos del vendedor a la vista por decisión de Franco (25/10); VENDEDOR queda por si hace falta

def _pag(titulo, cuerpo):
    return f'<article class="legalbody"><span class="etiqueta">Legales</span><h1>{titulo}</h1><p class="nota">Última actualización: 25 de octubre de 2026.</p>{cuerpo}</article>'

TERMINOS = _pag("Términos y condiciones", f"""
<h2>1. Quién vende</h2>
<p>CuentaClara es el nombre de este sitio, operado por su titular (el "Vendedor"). Al comprar o usar los servicios aceptás estos términos.</p>
<h2>2. Qué se vende</h2>
<p>Productos digitales de entrega inmediata (planillas .xlsx, packs de modelos en Word, guía en PDF, créditos del generador de recibos y presupuestos) y el servicio de QR dinámicos por suscripción mensual. Las calculadoras y generadores gratuitos se ofrecen sin garantía de resultado.</p>
<h2>3. Precios y pago</h2>
<p>Los precios están en pesos argentinos, con impuestos incluidos, y se muestran antes de pagar. El pago se procesa por Mercado Pago; el Vendedor no recibe ni guarda datos de tu tarjeta. La suscripción de QR se renueva cada mes hasta que la cancelés desde tu cuenta de Mercado Pago.</p>
<h2>4. Entrega</h2>
<p>Con el pago aprobado, el sitio habilita la descarga en la página de agradecimiento, durante 30 días con el mismo enlace, hasta 5 descargas por pago. No hay cuentas ni envío por mail: si perdés el enlace, lo recuperás en <a href="/recuperar">/recuperar</a> con el número de operación de tu comprobante de Mercado Pago (los pagos en efectivo quedan disponibles cuando se acreditan). Los créditos de recibos no vencen y se asocian al código de pago.</p>
<p><b>Entrega inmediata.</b> La entrega es inmediata y el archivo es de uso permanente: una vez descargado el archivo (o usado un crédito de recibos) se aplica la excepción del art. 1116 inc. c del Código Civil y Comercial, prevista en el art. 3 inc. a de la Disposición 954/2025, y no corresponde el reembolso por arrepentimiento. Te lo avisamos antes de pagar.</p>
<h2>5. Naturaleza del contenido</h2>
<p>Todo el material es información general y modelos orientativos, actualizados a octubre de 2026. No es asesoramiento contable, legal ni impositivo y no reemplaza a un profesional ni a la información oficial (ARCA, Boletín Oficial). Las normas cambian: verificá los valores vigentes antes de decidir. El Vendedor no responde por decisiones tomadas solo con base en el material, sin perjuicio de los derechos que la Ley 24.240 te reconoce como consumidor.</p>
<h2>6. Uso permitido y propiedad</h2>
<p>La compra te da una licencia personal, no exclusiva e intransferible para usar el material. Podés adaptar los modelos a tus propios casos. No podés revenderlo ni redistribuirlo. El servicio de QR no puede usarse para destinos ilícitos, engañosos, de phishing o malware; el sistema bloquea destinos peligrosos y el Vendedor puede desactivar un QR que los incumpla.</p>
<h2>7. Arrepentimiento y devoluciones</h2>
<p>Tenés derecho a arrepentirte de la compra dentro de los 10 días corridos de pagada, desde el <a href="/arrepentimiento">botón de arrepentimiento</a>, con reembolso total mientras no hayas descargado el archivo ni usado créditos (excepción del art. 1116 inc. c del Código Civil y Comercial). El botón siempre registra tu solicitud. Detalle en la <a href="/devoluciones">política de devoluciones</a>.</p>
<h2>8. Disponibilidad</h2>
<p>El servicio es automático y se ofrece "tal cual está". Puede haber interrupciones por mantenimiento o de proveedores (Mercado Pago, Cloudflare). El Vendedor no atiende consultas personalizadas: toda gestión se hace desde el sitio.</p>
<h2>9. Defensa del consumidor</h2>
<p>Como consumidor podés presentar reclamos ante la autoridad de aplicación de tu jurisdicción o en la <a href="{DC_URL}" rel="noopener" target="_blank">Ventanilla Federal de Defensa del Consumidor</a>.</p>
<h2>10. Ley y jurisdicción</h2>
<p>Rige la ley argentina. Para conflictos de consumo, es competente la justicia del domicilio real del consumidor (art. 36 de la Ley 24.240).</p>
""")

PRIVACIDAD = _pag("Política de privacidad", f"""
<p>Responsable de la base de datos: el titular del sitio. Cumplimos la Ley 25.326 de Protección de los Datos Personales.</p>
<h2>Qué datos tratamos</h2>
<ul>
<li><b>Compras:</b> el pago lo procesa Mercado Pago. Recibimos solo el código de pago, el producto y el estado. No vemos ni guardamos datos de tarjeta.</li>
<li><b>QR dinámicos:</b> tu email, la dirección de destino, el estado de la suscripción y escaneos agregados por día y país (sin IP ni identificación de quien escanea).</li>
<li><b>Generador de recibos:</b> los datos de tus documentos se arman en tu navegador y no se envían a nuestros servidores. En el servidor solo se guarda el código de pago y los créditos usados.</li>
<li><b>Botón de arrepentimiento:</b> los datos del formulario (código de pago, nombre, email, motivo opcional) y el resultado.</li>
<li><b>Navegación:</b> el sitio no usa cookies de seguimiento ni publicidad. Guarda en tu navegador (localStorage) tus códigos de pago y datos de formulario para tu comodidad. Cloudflare registra datos técnicos de acceso (IP, navegador) para operar y proteger el sitio, y las tipografías se cargan desde Google Fonts.</li>
</ul>
<h2>Para qué</h2>
<p>Para entregarte lo que compraste, operar tu QR, procesar arrepentimientos y reembolsos, cumplir obligaciones legales y fiscales, y prevenir fraude y abuso. No vendemos ni cedemos tus datos. Los comparten solo los proveedores necesarios para el servicio: Mercado Pago (pagos) y Cloudflare (alojamiento y base de datos), que pueden almacenar datos fuera de Argentina.</p>
<h2>Cuánto tiempo</h2>
<p>Los datos de compras y arrepentimientos se conservan el tiempo que exigen las obligaciones fiscales y de defensa del consumidor. Los de un QR se conservan mientras la suscripción esté activa.</p>
<h2>Tus derechos</h2>
<p>Podés pedir acceso, rectificación, actualización o supresión de tus datos desde el formulario de <a href="/pedidos">pedidos</a>. El acceso es gratuito a intervalos no inferiores a seis meses, salvo interés legítimo (art. 14 Ley 25.326). Podés cancelar el QR desde Mercado Pago y pedir su baja.</p>
<p>La <b>Agencia de Acceso a la Información Pública</b>, órgano de control de la Ley 25.326, tiene la atribución de atender las denuncias y reclamos de quienes vean afectados sus derechos por incumplimiento de las normas de protección de datos personales.</p>
""")

DEVOLUCIONES = _pag("Política de devoluciones", f"""
<h2>Derecho de arrepentimiento</h2>
<p>Podés revocar la compra, sin dar motivos y sin costo, dentro de los <b>10 días corridos</b> desde que el pago fue aprobado (art. 34 de la Ley 24.240, art. 1110 del Código Civil y Comercial y Disposición 954/2025 de la Subsecretaría de Defensa del Consumidor y Lealtad Comercial). El botón de arrepentimiento aplica a todos los productos de este sitio y siempre registra tu solicitud.</p>
<h2>Productos digitales ya descargados</h2>
<p>Los archivos son de entrega inmediata y uso permanente. El art. 1116 inc. c del Código Civil y Comercial excluye del arrepentimiento los archivos informáticos descargados de inmediato para uso permanente, y el art. 3 inc. a de la Disposición 954/2025 mantiene esa excepción. Por eso te lo avisamos <b>antes de pagar</b>: <b>si todavía no descargaste el archivo (ni usaste créditos del generador de recibos), el reembolso es total y automático; si ya lo descargaste, registramos la solicitud, desactivamos el enlace y no hay reembolso automático</b>. Si el archivo no se puede abrir o llega dañado, tenés derecho a que se te entregue uno en condiciones: volvé a abrir el enlace de descarga.</p>
<h2>Cómo se hace</h2>
<ol>
<li>Entrá al <a href="/arrepentimiento">botón de arrepentimiento</a> (también está en el pie de todas las páginas).</li>
<li>Cargá el código de pago que figura en tu comprobante de Mercado Pago y en el enlace de la página de agradecimiento.</li>
<li>El sistema verifica el pago y el plazo, registra la solicitud y te da una constancia con un código.</li>
</ol>
<h2>Qué pasa después</h2>
<ul>
<li>El reembolso es por el <b>100% del precio</b> y se ordena a Mercado Pago de forma automática, al mismo medio de pago. La acreditación depende de Mercado Pago y de tu banco o tarjeta.</li>
<li>El enlace de descarga y los créditos del pedido se desactivan. Dejá de usar el material.</li>
<li><b>Suscripción de QR:</b> el reembolso aplica al cobro del período dentro de los 10 días y el QR se da de baja. También podés cancelar en cualquier momento desde Mercado Pago para que no se cobre el mes siguiente.</li>
</ul>
<h2>Fuera de plazo o si algo falla</h2>
<p>Si el archivo no se descarga o llega dañado, volvé a abrir el enlace de la página de agradecimiento (funciona 30 días). Si seguís con problemas, usá el botón de arrepentimiento mientras estés en plazo. Los reclamos se pueden presentar ante <a href="{DC_URL}" rel="noopener" target="_blank">Defensa del Consumidor</a>.</p>
""")

ARREP_BODY = f"""
<span class="etiqueta">Disp. SSDCyLC 954/2025</span><h1>Botón de arrepentimiento</h1>
<p>Si te arrepentiste de tu compra, completá el formulario. Tenés <b>10 días corridos</b> desde el pago. El sistema es automático: verifica el pago, desactiva la descarga y ordena el reembolso total a tu medio de pago. No hace falta explicar motivos.</p>
<form class="arr-form" id="arr" novalidate>
<div><label for="a-pago">Código de pago de Mercado Pago</label><input id="a-pago" name="pago" inputmode="numeric" autocomplete="off" placeholder="Ej.: 123456789012" required></div>
<div><label for="a-nom">Nombre y apellido</label><input id="a-nom" name="nombre" autocomplete="name" required></div>
<div><label for="a-em">Email (opcional, para tu constancia)</label><input id="a-em" name="email" type="email" autocomplete="email"></div>
<div><label for="a-mot">Motivo (opcional)</label><textarea id="a-mot" name="motivo" rows="2" maxlength="300"></textarea></div>
<div style="display:none"><label>No completar<input name="web" tabindex="-1" autocomplete="off"></label></div>
<button class="boton" type="submit">Arrepentirme de la compra</button>
</form>
<div class="arr-res" id="arr-res" role="status" aria-live="polite"></div>
<p class="nota">El código de pago está en el comprobante de Mercado Pago y en la página de agradecimiento de tu compra. Más información en la <a href="/devoluciones">política de devoluciones</a> y los <a href="/terminos">términos</a>. Si necesitás presentar un reclamo, <a href="{DC_URL}" rel="noopener" target="_blank">Defensa del Consumidor</a>.</p>
"""

ARREP_JS = """<script>
const f=document.getElementById("arr"),r=document.getElementById("arr-res");
f.addEventListener("submit",async e=>{e.preventDefault();const b=f.querySelector("button");b.disabled=true;
const d=Object.fromEntries(new FormData(f));r.style.display="block";r.className="arr-res";r.textContent="Procesando…";
try{const x=await fetch("/arrepentimiento/enviar",{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify(d)});
const j=await x.json();r.className="arr-res "+(j.ok?"ok":"mal");r.innerHTML="";
const p=document.createElement("p");p.textContent=j.mensaje||"No se pudo procesar. Probá de nuevo.";r.appendChild(p);
if(j.codigo){const c=document.createElement("p");c.innerHTML="Código de constancia: <b class=cod></b><br>Fecha: ";c.querySelector("b").textContent=j.codigo;c.append(j.fecha||"");r.appendChild(c)}
}catch{r.className="arr-res mal";r.textContent="No se pudo procesar. Probá de nuevo."}b.disabled=false});
</script>"""

PAGES = {
    "terminos": ("Términos y condiciones", "Términos y condiciones de uso y compra de CuentaClara: productos digitales, entrega, precios, arrepentimiento y datos del vendedor.", TERMINOS, ""),
    "privacidad": ("Política de privacidad", "Cómo tratamos tus datos personales según la Ley 25.326: qué datos guardamos, para qué, con quién se comparten y cómo ejercer tus derechos.", PRIVACIDAD, ""),
    "devoluciones": ("Política de devoluciones", "Política de devoluciones de productos digitales: arrepentimiento de 10 días corridos (reembolso total si todavía no descargaste), cómo se solicita y qué pasa después.", DEVOLUCIONES, ""),
    "arrepentimiento": ("Botón de arrepentimiento", "Formulario automático para arrepentirte de tu compra dentro de los 10 días corridos: verifica el pago, desactiva la descarga y ordena el reembolso si todavía no descargaste.", ARREP_BODY, ARREP_JS),
}
