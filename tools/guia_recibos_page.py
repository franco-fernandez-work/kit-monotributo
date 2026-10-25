"""Páginas de la guía PDF (/guia-primer-ano-monotributo) y del generador de recibos (/recibos-presupuestos-pdf). Se importan desde build_site.main()."""

CSS_EXTRA = r"""
/* guía y generador */
.portada-guia{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}
@media (max-width:860px){.portada-guia{grid-template-columns:1fr}}
.portada-guia>*{min-width:0}
.tapa{aspect-ratio:3/4;max-width:340px;width:100%;background:#10263d;color:#fff;border-radius:3px;padding:30px 26px;position:relative;box-shadow:0 18px 40px -22px rgba(16,38,61,.55);overflow:hidden}
.tapa::before{content:"";position:absolute;left:0;right:0;top:12px;height:3px;background:repeating-linear-gradient(90deg,#3f8fcf 0 14px,transparent 14px 22px)}
.tapa small{display:block;font:600 10px/1.3 var(--f-num);letter-spacing:.12em;color:#7ab6e6;margin-top:22px}
.tapa b{display:block;font:700 40px/1 var(--f-display);margin-top:18px;letter-spacing:-.02em}
.tapa p{color:#c9d6e3;font-size:14px;margin-top:16px}
.tapa .sello{position:absolute;right:22px;bottom:26px;width:86px;height:86px;border-color:#3f8fcf;color:#3f8fcf}
.tapa .sello b{font-size:28px;margin:0;color:#3f8fcf}
.indice{list-style:none;padding:0;margin:0;counter-reset:c}
.indice li{display:grid;grid-template-columns:2.2em 1fr;gap:6px;padding:12px 0;border-bottom:1px dashed var(--linea);counter-increment:c}
.indice li::before{content:counter(c);font:600 13px var(--f-num);color:var(--celeste);padding-top:3px}
.indice b{display:block}
.indice span{color:var(--tinta-2);font-size:15px}
.precio-grande{font:700 44px/1 var(--f-display);letter-spacing:-.02em}
.opciones{display:grid;gap:14px;justify-items:start;margin-top:22px}
.opcion2{display:grid;gap:6px;font-size:15px;color:var(--tinta-2);max-width:46ch}
.gen{display:grid;grid-template-columns:1fr 1fr;gap:28px;align-items:start}
@media (max-width:900px){.gen{grid-template-columns:1fr}}
.gen>*{min-width:0}
.tipos{display:flex;flex-wrap:wrap;gap:8px}
.tipos button{font:600 14px var(--f-texto);padding:9px 14px;border:1.5px solid var(--linea);border-radius:4px;background:var(--papel);color:var(--tinta);cursor:pointer}
.tipos button[aria-pressed="true"]{background:var(--tinta);color:var(--papel);border-color:var(--tinta)}
.gen .campo input,.gen .campo textarea{font:500 16px var(--f-texto);width:100%;min-width:0;border:1.5px solid var(--linea);border-radius:4px;background:var(--papel);color:var(--tinta);padding:10px 12px}
.gen .campo input:focus,.gen .campo textarea:focus{outline:none;border-color:var(--celeste)}
.gen .campo textarea{min-height:64px;resize:vertical}
.gen .campo label{font-size:14px}
.itemrow{display:grid;grid-template-columns:1fr 60px 104px 30px;gap:8px;align-items:center;margin-bottom:8px}
.itemrow button{border:0;background:transparent;color:var(--sello);font:700 20px var(--f-texto);cursor:pointer}
.link{background:none;border:0;padding:0;color:var(--celeste);font:600 15px var(--f-texto);cursor:pointer;text-decoration:underline}
.credito{display:flex;flex-wrap:wrap;gap:10px 16px;align-items:center;justify-content:space-between;padding:14px 16px;border:1.5px solid var(--celeste);border-radius:4px;background:var(--celeste-suave)}
.hoja-prev{background:#fff;color:#10263d;border:1px solid var(--linea);border-radius:3px;padding:22px 20px;font-size:13px;line-height:1.45;position:sticky;top:12px;min-height:420px;overflow-x:auto}
.hoja-prev h3{font:700 22px var(--f-display);margin:0 0 2px}
.hoja-prev .fila{display:flex;justify-content:space-between;gap:10px}
.hoja-prev table{min-width:0;font-size:12px}
.hoja-prev th,.hoja-prev td{padding:5px 6px;color:#10263d}
.hoja-prev td{font-family:var(--f-texto)}
.hoja-prev .tot{font:700 17px var(--f-num);text-align:right;margin-top:10px}
.hoja-prev .letras{font-size:12px;color:#4b5e72}
.hoja-prev .pie-doc{margin-top:18px;font-size:10px;color:#6c7d8f;border-top:1px dashed #d6dfe8;padding-top:8px}
.estado-gen{min-height:1.4em;margin-top:8px}
"""

TAPA = '<div class="tapa"><small>GUÍA PRÁCTICA · OCT. 2026</small><b>Primer año<br>de monotributo</b><p>Alta, facturas, pagos y recategorización sin errores caros.</p><div class="sello"><b>A–K</b></div></div>'

GUIA_BODY = f"""<div class="portada-guia"><div><span class="etiqueta">Guía en PDF · 11 páginas</span><h1>Primer año de monotributo</h1>
<p class="bajada">Lo que nadie te explica cuando te inscribís: cómo darte de alta, qué categoría elegir, cómo facturar, cuándo pagar y cómo no equivocarte en la recategorización.</p>
<div class="opciones"><a class="boton" href="/comprar?p=guia">Comprar la guía <span class="num">$ 2.999</span></a>
<div class="opcion2"><span>¿Todavía no llevás la cuenta de tus facturas? <a href="/comprar?p=kitguia"><b>Guía + Kit Monotributista por $ 8.999</b></a> en un solo pago (ahorrás $ 1.000).</span><span class="nota">Pagás con Mercado Pago y la descargás al instante.</span></div></div></div>{TAPA}</div>
<h2>Qué incluye</h2>
<ol class="indice"><li><div><b>El alta, paso a paso</b><span>Qué necesitás, cómo inscribirte en ARCA y qué hacer el mismo día.</span></div></li>
<li><div><b>Cómo elegir tu primera categoría</b><span>La tabla A–K vigente, un ejemplo y cómo dejar margen para no pasarte.</span></div></li>
<li><div><b>Factura C sin vueltas</b><span>Punto de venta, comprobantes en línea y las reglas que más se rompen.</span></div></li>
<li><div><b>Pagar la cuota</b><span>Vencimiento, medios de pago y qué pasa si dejás de pagar.</span></div></li>
<li><div><b>Recategorización</b><span>Qué mira ARCA, cómo se hace y la multa del 50% por omitirla.</span></div></li>
<li><div><b>Ingresos Brutos y tasas municipales</b><span>El impuesto que la cuota no incluye y cómo averiguar el tuyo.</span></div></li>
<li><div><b>Los 12 errores caros del primer año</b><span>Qué cuesta cada uno y el hábito que lo evita.</span></div></li>
<li><div><b>Calendario del primer año y glosario</b><span>Mes por mes, para imprimir o guardar en el celular.</span></div></li></ol>
<div class="lectura"><h2>Para quién es</h2><p>Para quien se inscribe o está por inscribirse: freelancers, vendedores, oficios, creadores. Está escrita en lenguaje claro y con las escalas vigentes de agosto 2026 a enero 2027. Es información general: no reemplaza a un contador ni a ARCA.</p>
<p>Si ya estás inscripto, empezá por el capítulo de recategorización y el de errores. La <a href="/escalas-monotributo-2026">escala de categorías</a> y la <a href="/recategorizacion-monotributo-febrero-2027">fecha de recategorización</a> están gratis en la web.</p></div>
<section class="oferta"><div><span class="etiqueta">PDF</span><h2>Guía: Primer año de monotributo</h2><p>11 páginas, descarga inmediata, sin suscripción.</p><ul><li>Se descarga durante 30 días con tu pago aprobado</li><li>Se abre en el celular, la compu o impresa</li></ul></div>
<div class="compra"><span class="precio-grande num">$ 2.999</span><a class="boton" href="/comprar?p=guia">Comprar la guía</a><a href="/comprar?p=kitguia" class="nota">O llevate la guía + el Kit Monotributista por $ 8.999</a></div></section>"""

GEN_BODY = r"""<span class="etiqueta">Generador online · pago por uso</span><h1>Recibos y presupuestos en PDF</h1>
<p class="bajada">Completás los datos, ves cómo queda y descargás un PDF prolijo. Recibo de alquiler, recibo de pago o presupuesto. Sin cuentas ni instalación.</p>
<div class="gen" style="margin-top:28px">
<div class="comp"><div class="comp-cab"><span>Documento</span><span id="n-cred">Creá el tuyo</span></div><div class="comp-cuerpo">
<div class="tipos" role="group" aria-label="Tipo de documento"><button type="button" data-t="alquiler" aria-pressed="true">Recibo de alquiler</button><button type="button" data-t="pago" aria-pressed="false">Recibo de pago</button><button type="button" data-t="presupuesto" aria-pressed="false">Presupuesto</button></div>
<div class="fila2"><div class="campo"><label for="f-num">Número</label><input id="f-num" placeholder="0001-00000001"></div><div class="campo"><label for="f-fecha">Fecha</label><input id="f-fecha" type="date"></div></div>
<div class="campo"><label for="f-em" id="l-em">Propietario</label><input id="f-em" placeholder="Nombre y apellido o razón social"></div>
<div class="fila2"><div class="campo"><label for="f-emdoc">CUIT / DNI</label><input id="f-emdoc" inputmode="numeric"></div><div class="campo"><label for="f-emdom">Domicilio</label><input id="f-emdom"></div></div>
<div class="campo"><label for="f-re" id="l-re">Inquilino</label><input id="f-re" placeholder="Nombre y apellido o razón social"></div>
<div class="fila2"><div class="campo"><label for="f-redoc">CUIT / DNI</label><input id="f-redoc" inputmode="numeric"></div><div class="campo" id="c-inm"><label for="f-inm">Inmueble</label><input id="f-inm" placeholder="Dirección alquilada"></div></div>
<div class="campo" id="c-per"><label for="f-per" id="l-per">Período</label><input id="f-per" placeholder="Noviembre 2026"></div>
<div class="campo"><label>Detalle</label><div id="items"></div><button type="button" class="link" id="add">+ Agregar renglón</button></div>
<div class="campo"><label for="f-obs">Observaciones</label><textarea id="f-obs" placeholder="Forma de pago, aclaraciones"></textarea></div>
<div class="credito" id="cred-box"><span id="cred-t">Cargando saldo…</span><span id="cred-a"></span></div>
<div><button type="button" class="boton" id="pdf">Descargar PDF <span class="num">1 crédito</span></button><p class="estado-gen estado" id="est" role="status"></p></div>
<details class="nota"><summary>Ya compré y tengo un código de pago</summary><div class="campo" style="margin-top:10px"><label for="f-cod">Código de pago de Mercado Pago</label><input id="f-cod" inputmode="numeric" placeholder="Ej. 1234567890"><button type="button" class="link" id="cod-ok" style="margin-top:8px">Cargar mis créditos</button></div></details>
</div></div>
<div><div class="hoja-prev" id="prev" aria-label="Vista previa"></div><p class="nota" style="margin-top:10px">Vista previa aproximada. El PDF final sale sin marcas ni publicidad.</p></div></div>
<div class="lectura"><h2>Cómo funciona</h2><ol><li>Completás los datos. La vista previa es gratis, sin límite.</li><li>Pagás <b>$ 990</b> con Mercado Pago y recibís <b>10 documentos</b> que no vencen.</li><li>Cada PDF que descargás usa 1 crédito. Los créditos quedan en tu navegador y en el enlace que te damos al pagar.</li></ol>
<h2>Qué es y qué no es</h2><p>Son comprobantes de gestión: recibos de pago y presupuestos. <b>No son facturas</b> y no reemplazan a la Factura C de ARCA si estás inscripto en el Monotributo. Para un recibo de alquiler no existe una forma oficial única: el documento deja constancia de lo que se pagó, por quién y de qué período.</p>
<p>Por ejemplo: un propietario entrega un recibo de alquiler por mes, o un electricista envía un presupuesto con validez de 15 días. Si necesitás los modelos de contrato, mirá el <a href="/contratos-alquiler-modelo-word">Pack Contratos de Alquiler</a>.</p></div>
<section class="oferta"><div><span class="etiqueta">Pago por uso</span><h2>10 documentos por $ 990</h2><ul><li>Recibos de alquiler, recibos de pago y presupuestos</li><li>Con importe en letras y total calculado</li><li>Los créditos no vencen</li></ul></div>
<div class="compra"><a class="boton" href="/comprar?p=recibos">Comprar 10 documentos <span class="num">$ 990</span></a><span class="nota">Pagás con Mercado Pago y los créditos se activan solos.</span></div></section>"""

GEN_JS = r"""<script src="/vendor/jspdf.umd.min.js" defer></script><script defer>
addEventListener("DOMContentLoaded",()=>{const $=i=>document.getElementById(i);let tipo="alquiler";const K="km_pagos";
const TIT={alquiler:"Recibo de alquiler",pago:"Recibo de pago",presupuesto:"Presupuesto"};
const pesos=n=>"$ "+n.toLocaleString("es-AR",{minimumFractionDigits:2,maximumFractionDigits:2});
const U=["","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez","once","doce","trece","catorce","quince","dieciséis","diecisiete","dieciocho","diecinueve","veinte","veintiuno","veintidós","veintitrés","veinticuatro","veinticinco","veintiséis","veintisiete","veintiocho","veintinueve"];
const D=["","","","treinta","cuarenta","cincuenta","sesenta","setenta","ochenta","noventa"];
const C=["","ciento","doscientos","trescientos","cuatrocientos","quinientos","seiscientos","setecientos","ochocientos","novecientos"];
function m999(n){if(n===100)return"cien";const s=[];if(n>=100){s.push(C[Math.floor(n/100)]);n%=100}if(n<30){if(n)s.push(U[n])}else{const d=Math.floor(n/10),u=n%10;s.push(D[d]+(u?" y "+U[u]:""))}return s.join(" ")}
const apoc=t=>t.replace(/uno$/,"un");
function letras(n){let e=Math.floor(n),c=Math.round((n-e)*100);if(c===100){e++;c=0}const p=[];
if(e===0)p.push("cero");else{const mm=Math.floor(e/1e6),mi=Math.floor(e/1e3)%1e3,r=e%1e3;
if(mm)p.push(mm===1?"un millón":apoc(m999(mm))+" millones");
if(mi)p.push(mi===1?"mil":apoc(m999(mi))+" mil");
if(r)p.push(m999(r));if(e%1e6===0&&e>=1e6)p.push("de")}
return (p.join(" ")+" pesos"+(c?" con "+String(c).padStart(2,"0")+"/100":""))}
const num=v=>{v=String(v).trim().replace(/\./g,"").replace(",",".");const n=parseFloat(v);return isFinite(n)?n:0};
const val=i=>$(i).value.trim();
const items=()=>[...$("items").children].map(r=>{const[a,b,c]=r.querySelectorAll("input");const q=num(b.value),p=num(c.value);return{d:a.value.trim(),q,p,t:q*p}}).filter(i=>i.d||i.t);
const data=()=>{const it=items();return{tipo,tit:TIT[tipo],num:val("f-num"),fecha:val("f-fecha"),em:val("f-em"),emdoc:val("f-emdoc"),emdom:val("f-emdom"),re:val("f-re"),redoc:val("f-redoc"),inm:val("f-inm"),per:val("f-per"),obs:val("f-obs"),it,tot:it.reduce((s,i)=>s+i.t,0)}};
const fdate=s=>s?s.split("-").reverse().join("/"):"";
const esc=s=>String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"})[c]);
const mkRow=(d="",q="1",p="")=>{const r=document.createElement("div");r.className="itemrow";r.innerHTML='<input aria-label="Descripción" placeholder="Descripción"><input aria-label="Cantidad" inputmode="decimal" value="'+q+'"><input aria-label="Precio unitario" inputmode="decimal" placeholder="0,00"><button type="button" aria-label="Quitar renglón">×</button>';
const[a,,c,x]=r.children;a.value=d;c.value=p;x.onclick=()=>{if($("items").children.length>1){r.remove();draw()}};r.addEventListener("input",draw);return r};
function draw(){const d=data();const alq=tipo==="alquiler",pre=tipo==="presupuesto";
$("c-inm").style.display=alq?"":"none";$("c-per").style.display=tipo==="pago"?"none":"";
$("l-em").textContent=alq?"Propietario":pre?"Quién presupuesta":"Quién recibe el pago";$("l-re").textContent=alq?"Inquilino":pre?"Cliente":"Quién paga";
$("l-per").textContent=alq?"Período":"Validez del presupuesto";$("f-per").placeholder=alq?"Noviembre 2026":"15 días";
$("prev").innerHTML='<div class="fila"><h3>'+d.tit+'</h3><span>N° '+esc(d.num||"—")+'</span></div><div>'+fdate(d.fecha)+'</div><p style="margin:10px 0 4px"><b>'+(alq?"Propietario":pre?"Emisor":"Recibe")+':</b> '+esc(d.em||"—")+' '+esc(d.emdoc)+'<br>'+esc(d.emdom)+'</p><p style="margin:0 0 8px"><b>'+(alq?"Inquilino":"Cliente")+':</b> '+esc(d.re||"—")+' '+esc(d.redoc)+(alq&&d.inm?'<br>Inmueble: '+esc(d.inm):"")+(d.per&&tipo!=="pago"?'<br>'+(alq?"Período":"Validez")+': '+esc(d.per):"")+'</p><table><thead><tr><th style="text-align:left">Detalle</th><th>Cant.</th><th>Precio</th><th>Total</th></tr></thead><tbody>'+d.it.map(i=>'<tr><td style="text-align:left">'+esc(i.d)+'</td><td>'+i.q+'</td><td>'+pesos(i.p)+'</td><td>'+pesos(i.t)+'</td></tr>').join("")+'</tbody></table><div class="tot">Total '+pesos(d.tot)+'</div><div class="letras">'+(d.tot?"Son "+letras(d.tot):"")+'</div>'+(d.obs?'<p style="margin-top:10px">'+esc(d.obs)+'</p>':"")+'<div class="pie-doc">Documento no válido como factura.</div>';
try{localStorage.setItem("km_form",JSON.stringify({em:d.em,emdoc:d.emdoc,emdom:d.emdom}))}catch{}}
document.querySelectorAll(".tipos button").forEach(b=>b.onclick=()=>{tipo=b.dataset.t;document.querySelectorAll(".tipos button").forEach(x=>x.setAttribute("aria-pressed",x===b));draw()});
$("add").onclick=()=>{$("items").append(mkRow())};
document.querySelectorAll(".gen input,.gen textarea").forEach(e=>e.addEventListener("input",draw));
const pagos=()=>{try{return JSON.parse(localStorage.getItem(K)||"[]")}catch{return[]}};
const guardar=a=>{try{localStorage.setItem(K,JSON.stringify([...new Set(a)]))}catch{}};
let saldo=0;
function estado(n){saldo=n;$("n-cred").textContent=n?n+" créditos":"Sin créditos";$("cred-t").innerHTML=n?"Te quedan <b>"+n+"</b> documentos.":"Para descargar el PDF necesitás créditos.";$("cred-a").innerHTML=n?"":'<a class="boton" href="/comprar?p=recibos" style="padding:11px 16px;font-size:15px">Comprar 10 por $ 990</a>'}
async function refrescar(){const ids=pagos();if(!ids.length){estado(0);return}
try{const r=await fetch("/recibos/api/saldo?ids="+ids.join(","));const j=await r.json();guardar(j.packs.map(p=>p.id));estado(j.saldo||0)}catch{$("cred-t").textContent="No pudimos consultar tus créditos. Recargá la página."}}
$("cod-ok").onclick=()=>{const v=val("f-cod").replace(/\D/g,"");if(v){guardar([...pagos(),v]);$("f-cod").value="";refrescar()}};
const q=new URLSearchParams(location.search).get("pago");if(q&&/^\d{1,20}$/.test(q)){guardar([...pagos(),q]);history.replaceState(null,"",location.pathname)}
function pdf(d){const{jsPDF}=window.jspdf;const doc=new jsPDF({unit:"mm",format:"a4"});const W=210,M=18;let y;
doc.setFillColor(16,38,61);doc.rect(0,0,W,30,"F");doc.setTextColor(255,255,255);doc.setFont("helvetica","bold");doc.setFontSize(20);doc.text(d.tit,M,18);
doc.setFont("helvetica","normal");doc.setFontSize(10);doc.text("N° "+(d.num||"—"),W-M,13,{align:"right"});doc.text(fdate(d.fecha),W-M,19,{align:"right"});
y=44;const blk=(t,n,dn,dom,ex)=>{doc.setFont("helvetica","bold");doc.setFontSize(8);doc.setTextColor(75,94,114);doc.text(t.toUpperCase(),M,y);y+=5;doc.setFontSize(12);doc.setTextColor(16,38,61);doc.text(n||"—",M,y);y+=5.5;doc.setFont("helvetica","normal");doc.setFontSize(10);
[dn?"CUIT / DNI: "+dn:"",dom,...ex].filter(Boolean).forEach(l=>{const ls=doc.splitTextToSize(l,W-2*M);doc.text(ls,M,y);y+=5*ls.length});y+=4};
const alq=d.tipo==="alquiler",pre=d.tipo==="presupuesto";
blk(alq?"Propietario":pre?"Emisor":"Recibe",d.em,d.emdoc,d.emdom,[]);
blk(alq?"Inquilino":"Cliente",d.re,d.redoc,"",[...(alq&&d.inm?["Inmueble: "+d.inm]:[]),...(d.per&&d.tipo!=="pago"?[(alq?"Período: ":"Validez: ")+d.per]:[])]);
y+=2;const cx=[M,W-M-82,W-M-50,W-M];doc.setFillColor(230,241,250);doc.rect(M,y-5,W-2*M,8,"F");doc.setFont("helvetica","bold");doc.setFontSize(9);doc.setTextColor(75,94,114);
doc.text("DETALLE",M+2,y);doc.text("CANT.",cx[1],y,{align:"right"});doc.text("PRECIO",cx[2],y,{align:"right"});doc.text("TOTAL",cx[3]-2,y,{align:"right"});y+=8;doc.setFont("helvetica","normal");doc.setFontSize(10);doc.setTextColor(16,38,61);
d.it.forEach(i=>{const l=doc.splitTextToSize(i.d||"—",cx[1]-M-30);if(y+l.length*5>255){doc.addPage();y=24}doc.text(l,M+2,y);doc.text(String(i.q),cx[1],y,{align:"right"});doc.text(pesos(i.p),cx[2],y,{align:"right"});doc.text(pesos(i.t),cx[3]-2,y,{align:"right"});y+=l.length*5+1.5;doc.setDrawColor(214,223,232);doc.line(M,y-3,W-M,y-3)});
y+=6;if(y>235){doc.addPage();y=24}doc.setFont("helvetica","bold");doc.setFontSize(14);doc.text("TOTAL  "+pesos(d.tot),W-M-2,y,{align:"right"});y+=7;doc.setFont("helvetica","normal");doc.setFontSize(9);doc.setTextColor(75,94,114);const ls=doc.splitTextToSize("Son "+letras(d.tot),W-2*M);doc.text(ls,W-M-2,y,{align:"right"});y+=5*ls.length+6;
if(d.obs){doc.setTextColor(16,38,61);doc.setFontSize(10);doc.text(doc.splitTextToSize(d.obs,W-2*M),M,y)}
doc.setDrawColor(214,223,232);doc.line(M,278,W-M,278);doc.setFontSize(8);doc.setTextColor(108,125,143);doc.text("Documento no válido como factura.",M,283);
if(!pre){doc.setDrawColor(16,38,61);doc.line(W-M-60,266,W-M,266);doc.text("Firma y aclaración",W-M-30,270,{align:"center"})}
doc.save((d.tit+(d.num?" "+d.num:"")).replace(/[^\w\- ]+/g,"")+".pdf")}
$("pdf").onclick=async()=>{const d=data(),e=$("est");e.className="estado-gen estado";
const mal=t=>{e.textContent=t;e.classList.add("mal")};
if(!d.it.length||!d.tot)return mal("Agregá al menos un renglón con importe.");
if(!window.jspdf)return mal("Todavía se está cargando el generador. Probá de nuevo.");
if(saldo<1)return mal("No tenés créditos. Comprá 10 documentos por $ 990.");
$("pdf").disabled=true;try{const r=await fetch("/recibos/api/usar",{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify({ids:pagos()})});const j=await r.json();
if(!j.ok){estado(0);return mal("No hay créditos disponibles.")}
pdf(d);estado(j.saldo);e.textContent="Listo. Te quedan "+j.saldo+" documentos.";e.classList.add("bien")}catch{mal("No pudimos descontar el crédito. Probá de nuevo.")}finally{$("pdf").disabled=false}};
$("f-fecha").value=new Date().toISOString().slice(0,10);try{const f=JSON.parse(localStorage.getItem("km_form")||"{}");$("f-em").value=f.em||"";$("f-emdoc").value=f.emdoc||"";$("f-emdom").value=f.emdom||""}catch{}
$("items").append(mkRow("Alquiler mensual","1",""));draw();refrescar();
});
</script>"""

def pages():
    return {
     "guia-primer-ano-monotributo": ("Guía: Primer año de monotributo (PDF 2026)", "Guía en PDF para tu primer año de monotributo: alta, categoría, factura C, pago de la cuota, recategorización, Ingresos Brutos y los 12 errores caros. Escalas de agosto 2026.", GUIA_BODY, ""),
     "recibos-presupuestos-pdf": ("Generador de recibos y presupuestos en PDF", "Creá recibos de alquiler, recibos de pago y presupuestos en PDF online, con importe en letras. Pagás $ 990 por 10 documentos con Mercado Pago, sin cuentas.", GEN_BODY, GEN_JS),
    }
