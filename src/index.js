// Venta automática con Mercado Pago Checkout Pro: /comprar?p=<producto> crea la preferencia,
// /gracias verifica el pago y /descargar entrega el archivo solo si el pago está aprobado.
import kit from "../private/kit.xlsx";
import vendedores from "../private/vendedores.xlsx";
import alquileres from "../private/alquileres.xlsx";
import casas from "../private/casas.xlsx";
import vacaciones from "../private/vacaciones.xlsx";
import liquidacion from "../private/liquidacion.xlsx";
import ganancias from "../private/ganancias.xlsx";
import packAlq from "../private/pack-alquiler.zip";
import packFre from "../private/pack-freelancers.zip";
import packCombo from "../private/pack-combo.zip";
import guia from "../private/guia.pdf";
import packKitGuia from "../private/pack-kitguia.zip";
import packReclamos from "../private/pack-reclamos.zip";
import packTelegramas from "../private/pack-telegramas.zip";
import packBoletoAuto from "../private/pack-boletoauto.zip";
import packAlqTemp from "../private/pack-alqtemp.zip";
import packViajeMenor from "../private/pack-viajemenor.zip";
import packAlimentos from "../private/pack-alimentos.zip";
import packLibretaAuh from "../private/Pack-Libreta-AUH-2026.zip";
import packJubila from "../private/Pack-Jubilacion-2026.zip";
import packCud from "../private/Pack-CUD-2026.zip";
import packReclamosRei from "../private/Pack-Reclamos-Reintegros-2026.zip";
import packSaludFam from "../private/Pack-Salud-Familiar-2026.zip";
import packEscolar from "../private/Pack-Ayuda-Escolar-2026.zip";
import packFiesta from "../private/Pack-Fiesta-Casamiento-2026.zip";
import packVeraneo from "../private/Pack-Vacaciones-Verano-2026.zip";
import packFiestas from "../private/Pack-Fiestas-Fin-de-Anio-2026.zip";
import packEmprend from "../private/Pack-Emprendedores-Stock-Costos-2026.zip";
import guiaExterior from "../private/guia-exterior.pdf";
import guiaCobrar from "../private/guia-cobrar.pdf";
import guiaAlquilar from "../private/guia-alquilar.pdf";
import guiaAguinaldo from "../private/guia-aguinaldo.pdf";
import guiaSucesion from "../private/guia-sucesion.pdf";
import guiaJubilacion from "../private/guia-jubilacion.pdf";
import guiaSalir from "../private/guia-salir.pdf";
import guiaMudanza from "../private/guia-mudanza.pdf";
import guiaRenovar from "../private/guia-renovar.pdf";
import guiaCosta from "../private/guia-costa.pdf";
import presupuesto from "../private/presupuesto.xlsx";
import stock from "../private/stock.xlsx";
import packDeposito from "../private/pack-deposito.zip";
import packTemporada from "../private/pack-temporada.zip";
import packCole from "../private/pack-cole.zip";
import siradig from "../private/siradig.xlsx";
import packAlqEstud from "../private/pack-alqestud.zip";
import packSiradigCombo from "../private/pack-siradigcombo.zip";
import { manejarQR, refrescarQR } from "./qr.js";
import { manejarRecibos } from "./recibos.js";
import { manejarPedidos } from "./pedidos.js";
import { manejarLegal, revocado } from "./legal.js";
import { limitar, pagoInexistente, marcarInexistente, registrarDescarga, MAX_DESCARGAS } from "./limite.js";

const PRODUCTOS = {
  kit: {
    ref: "kitmono2026", titulo: "Kit Monotributista 2026 (planilla Excel / Google Sheets)",
    nombre: "Kit Monotributista 2026", precio: 6999, archivo: kit, filename: "Kit-Monotributista-2026.xlsx", volver: "/",
  },
  vendedores: {
    ref: "vendedores2026", titulo: "Calculadora de Precios para Vendedores 2026 (planilla Excel / Google Sheets)",
    nombre: "Calculadora de Precios para Vendedores", precio: 4999, archivo: vendedores, filename: "Calculadora-Precios-Vendedores-2026.xlsx", volver: "/precios-mercado-libre",
  },
  alquileres: {
    ref: "alquileres2026", titulo: "Planilla de Alquileres 2026 (planilla Excel / Google Sheets)",
    nombre: "Planilla de Alquileres 2026", precio: 3999, archivo: alquileres, filename: "Planilla-Alquileres-2026.xlsx", volver: "/aumento-alquiler",
  },
  casas: {
    ref: "casas2026", titulo: "Planilla Casas Particulares 2026 (planilla Excel / Google Sheets)",
    nombre: "Planilla Casas Particulares 2026", precio: 4999, archivo: casas, filename: "Planilla-Casas-Particulares-2026.xlsx", volver: "/sueldo-empleada-domestica",
  },
  vacaciones: {
    ref: "vacaciones2026", titulo: "Planilla de Vacaciones del Equipo (planilla Excel / Google Sheets)",
    nombre: "Planilla de Vacaciones del Equipo", precio: 4999, archivo: vacaciones, filename: "Planilla-Vacaciones-Equipo.xlsx", volver: "/calculadora-vacaciones",
  },
  liquidacion: {
    ref: "liquidacion2026", titulo: "Planilla de Liquidación Final e Indemnización (planilla Excel / Google Sheets)",
    nombre: "Planilla de Liquidación Final", precio: 5999, archivo: liquidacion, filename: "Planilla-Liquidacion-Final.xlsx", volver: "/calculadora-liquidacion-final",
  },
  alqpack: { ref: "alqpack2026", titulo: "Pack Contratos de Alquiler 2026 (modelos Word)", nombre: "Pack Contratos de Alquiler 2026",
    precio: 4999, archivo: packAlq, filename: "Pack-Contratos-Alquiler-2026.zip", mime: "application/zip", volver: "/contratos-alquiler-modelo-word" },
  frepack: { ref: "frepack2026", titulo: "Pack Contratos para Freelancers 2026 (modelos Word)", nombre: "Pack Contratos para Freelancers 2026",
    precio: 5999, archivo: packFre, filename: "Pack-Contratos-Freelancers-2026.zip", mime: "application/zip", volver: "/contratos-freelancers-monotributo" },
  combo: { ref: "combo2026", titulo: "Combo Freelancers + Kit Monotributista 2026", nombre: "Combo Contratos Freelancers + Kit Monotributista",
    precio: 9999, archivo: packCombo, filename: "Combo-Freelancer-Monotributista-2026.zip", mime: "application/zip", volver: "/contratos-freelancers-monotributo" },
  ganancias: {
    ref: "ganancias2026", titulo: "Planilla de Ganancias en el Sueldo 2026 (planilla Excel / Google Sheets)",
    nombre: "Planilla de Ganancias en el Sueldo", precio: 5999, archivo: ganancias, filename: "Planilla-Ganancias-Sueldo-2026.xlsx", volver: "/calculadora-ganancias-sueldo",
  },
  guia: { ref: "guia2026", titulo: "Guía: Primer año de monotributo (PDF)", nombre: "Guía: Primer año de monotributo",
    precio: 2999, archivo: guia, filename: "Guia-Primer-Anio-Monotributo.pdf", mime: "application/pdf", volver: "/guia-primer-ano-monotributo" },
  kitguia: { ref: "kitguia2026", titulo: "Kit Monotributista 2026 + Guía Primer año (planilla y PDF)", nombre: "Kit Monotributista 2026 + Guía Primer año",
    precio: 8999, archivo: packKitGuia, filename: "Kit-Monotributista-y-Guia.zip", mime: "application/zip", volver: "/guia-primer-ano-monotributo" },
  reclamos: { ref: "reclamos2026", titulo: "Pack 8 Cartas de Reclamo de Consumo (modelos Word)", nombre: "Pack Reclamos de Consumo",
    precio: 2999, archivo: packReclamos, filename: "Pack-Reclamos-de-Consumo.zip", mime: "application/zip", volver: "/generador-reclamo-consumidor" },
  telegramas: { ref: "telegramas2026", titulo: "Pack 9 Telegramas y Cartas Documento Laborales (modelos Word)", nombre: "Pack Telegramas Laborales",
    precio: 4999, archivo: packTelegramas, filename: "Pack-Telegramas-Laborales.zip", mime: "application/zip", volver: "/telegrama-renuncia-modelo" },
  boletoauto: { ref: "boletoauto2026", titulo: "Pack Compraventa de Auto Usado: boleto, recibos y checklists (modelos Word)", nombre: "Pack Compraventa de Auto Usado",
    precio: 3999, archivo: packBoletoAuto, filename: "Pack-Compraventa-Auto-Usado.zip", mime: "application/zip", volver: "/boleto-compraventa-auto-usado" },
  alqtemp: { ref: "alqtemp2026", titulo: "Pack Alquiler Temporario de Verano (modelos Word)", nombre: "Pack Alquiler Temporario de Verano",
    precio: 2999, archivo: packAlqTemp, filename: "Pack-Alquiler-Temporario-Verano.zip", mime: "application/zip", volver: "/alquiler-temporario-verano" },
  viajemenor: { ref: "viajemenor2026", titulo: "Pack Autorización de Viaje de Menores (modelos Word)", nombre: "Pack Autorización de Viaje de Menores",
    precio: 2999, archivo: packViajeMenor, filename: "Pack-Autorizacion-Viaje-Menores.zip", mime: "application/zip", volver: "/autorizacion-viaje-menores" },
  alimentos: { ref: "alimentos2026", titulo: "Planilla de Gastos del Hijo y Guía de Cuota Alimentaria (modelo Word)", nombre: "Planilla de Gastos del Hijo (cuota alimentaria)",
    precio: 3999, archivo: packAlimentos, filename: "Planilla-Gastos-del-Hijo.zip", mime: "application/zip", volver: "/cuota-alimentaria-aguinaldo" },
  alqestud: { ref: "alqestud2026", titulo: "Pack Alquiler para Estudiantes (modelos Word)", nombre: "Pack Alquiler para Estudiantes",
    precio: 2999, archivo: packAlqEstud, filename: "Pack-Alquiler-Estudiantes.zip", mime: "application/zip", volver: "/contrato-alquiler-estudiante" },
  cole: { ref: "cole2026", titulo: "Pack Vuelta al Cole: planilla anual, guía de ahorro y lista de útiles (planillas Excel + PDF)", nombre: "Pack Vuelta al Cole: planilla, guía y lista de útiles",
    precio: 2999, archivo: packCole, filename: "Pack-Vuelta-al-Cole.zip", mime: "application/zip", volver: "/presupuesto-vuelta-al-cole" },
  siradig: { ref: "siradig2026", titulo: "Organizador SIRADIG: comprobantes y deducciones (planilla Excel / Google Sheets)", nombre: "Organizador SIRADIG",
    precio: 3999, archivo: siradig, filename: "Organizador-SIRADIG-2026.xlsx", volver: "/siradig-que-puedo-deducir" },
  siradigcombo: { ref: "siradigcombo2026", titulo: "Combo SIRADIG + Ganancias en el Sueldo (dos planillas)", nombre: "Combo Organizador SIRADIG + Ganancias en el Sueldo",
    precio: 7999, archivo: packSiradigCombo, filename: "Combo-SIRADIG-Ganancias.zip", mime: "application/zip", volver: "/siradig-que-puedo-deducir" },
  exterior: { ref: "exterior2026", titulo: "Guía: Comprar afuera sin sorpresas (PDF)", nombre: "Guía: Comprar afuera sin sorpresas",
    precio: 2999, archivo: guiaExterior, filename: "Guia-Comprar-Afuera-Sin-Sorpresas.pdf", mime: "application/pdf", volver: "/calculadora-compras-exterior" },
  cobrar: { ref: "cobrar2026", titulo: "Guía: Cobrar del exterior siendo freelancer (PDF)", nombre: "Guía: Cobrar del exterior siendo freelancer",
    precio: 4999, archivo: guiaCobrar, filename: "Guia-Cobrar-Del-Exterior-Freelancer.pdf", mime: "application/pdf", volver: "/cobrar-del-exterior-freelancer" },
  alquilar: { ref: "alquilar2026", titulo: "Guía: Alquilar sin inmobiliaria (PDF)", nombre: "Guía: Alquilar sin inmobiliaria",
    precio: 3999, archivo: guiaAlquilar, filename: "Guia-Alquilar-Sin-Inmobiliaria.pdf", mime: "application/pdf", volver: "/alquilar-sin-inmobiliaria" },
  aguinaldo: { ref: "aguinaldo2026", titulo: "Guía: Dónde poner el aguinaldo (PDF)", nombre: "Guía: Dónde poner el aguinaldo",
    precio: 2999, archivo: guiaAguinaldo, filename: "Guia-Donde-Poner-El-Aguinaldo.pdf", mime: "application/pdf", volver: "/donde-poner-el-aguinaldo" },
  sucesion: { ref: "sucesion2026", titulo: "Guía: Sucesión sin perder tiempo (PDF)", nombre: "Guía: Sucesión sin perder tiempo",
    precio: 4999, archivo: guiaSucesion, filename: "Guia-Sucesion-Sin-Perder-Tiempo.pdf", mime: "application/pdf", volver: "/quien-hereda-sucesion-sin-testamento" },
  libreta: { ref: "libreta2026", titulo: "Libreta AUH 2026: guía y carpeta (PDF + planilla Excel)", nombre: "Libreta AUH 2026: guía y carpeta",
    precio: 2999, archivo: packLibretaAuh, filename: "Pack-Libreta-AUH-2026.zip", mime: "application/zip", volver: "/libreta-auh-como-presentar" },
  jubila: { ref: "jubila2026", titulo: "Mi camino a la jubilación: guía y planilla (PDF + planilla Excel)", nombre: "Mi camino a la jubilación: guía y planilla",
    precio: 3999, archivo: packJubila, filename: "Pack-Jubilacion-2026.zip", mime: "application/zip", volver: "/me-puedo-jubilar-calculadora" },
  cud: { ref: "cud2026", titulo: "CUD: guía y carpeta de documentación (PDF + planilla Excel)", nombre: "CUD: guía y carpeta de documentación",
    precio: 2999, archivo: packCud, filename: "Pack-CUD-2026.zip", mime: "application/zip", volver: "/cud-documentacion-y-pasos" },
  reclamos: { ref: "reclamos2026", titulo: "Reclamos y reintegros a tu obra social o prepaga: guía y carpeta (PDF + planilla Excel)", nombre: "Reclamos y reintegros a tu obra social o prepaga",
    precio: 2999, archivo: packReclamosRei, filename: "Pack-Reclamos-Reintegros-2026.zip", mime: "application/zip", volver: "/reclamo-obra-social-prepaga-paso-a-paso" },
  saludfam: { ref: "saludfam2026", titulo: "Carpeta de salud familiar: vacunas, controles y turnos (PDF + planilla Excel)", nombre: "Carpeta de salud familiar",
    precio: 2999, archivo: packSaludFam, filename: "Pack-Salud-Familiar-2026.zip", mime: "application/zip", volver: "/calendario-vacunacion-turnos-hospital-publico" },
  escolar: { ref: "escolar2026", titulo: "Ayuda Escolar Anual: guía y carpeta (PDF + planilla Excel)", nombre: "Ayuda Escolar Anual: guía y carpeta",
    precio: 1999, archivo: packEscolar, filename: "Pack-Ayuda-Escolar-2026.zip", mime: "application/zip", volver: "/ayuda-escolar-anual-certificado-escolar" },
  fiesta: { ref: "fiesta2026", titulo: "Fiesta de 15 o casamiento con inflación: guía y organizador (PDF + planilla Excel)", nombre: "Fiesta de 15 o casamiento con inflación",
    precio: 3999, archivo: packFiesta, filename: "Pack-Fiesta-Casamiento-2026.zip", mime: "application/zip", volver: "/presupuesto-fiesta-15-casamiento-inflacion" },
  veraneo: { ref: "veraneo2026", titulo: "Vacaciones de verano: guía y presupuesto (PDF + planilla Excel)", nombre: "Vacaciones de verano: guía y presupuesto",
    precio: 2999, archivo: packVeraneo, filename: "Pack-Vacaciones-Verano-2026.zip", mime: "application/zip", volver: "/presupuesto-vacaciones-verano" },
  fiestas: { ref: "fiestas2026", titulo: "Fiestas de fin de año: guía y planilla de regalos y cena (PDF + planilla Excel)", nombre: "Fiestas de fin de año: regalos, cena y reparto",
    precio: 1999, archivo: packFiestas, filename: "Pack-Fiestas-Fin-de-Anio-2026.zip", mime: "application/zip", volver: "/presupuesto-navidad-fin-de-anio" },
  emprendedor: { ref: "emprendedor2026", titulo: "Stock, costos y ventas para emprendedores: guía y planilla (PDF + planilla Excel)", nombre: "Stock, costos y ventas para emprendedores",
    precio: 2999, archivo: packEmprend, filename: "Pack-Emprendedores-Stock-Costos-2026.zip", mime: "application/zip", volver: "/calculadora-precio-margen-emprendedores" },
  deposito10: { ref: "deposito10_2026", titulo: "Pack Recuperá tu depósito de alquiler: guía, cartas y planilla (PDF + planilla Excel)", nombre: "Pack Recuperá tu depósito de alquiler",
    precio: 2999, archivo: packDeposito, filename: "Pack-Recuperar-Deposito.zip", mime: "application/zip", volver: "/recuperar-deposito-alquiler" },
  cole27: { ref: "cole27_2026", titulo: "Pack Vuelta al Cole: planilla anual, guía de ahorro y lista de útiles (planillas Excel + PDF)", nombre: "Pack Vuelta al Cole: planilla, guía y lista de útiles",
    precio: 2999, archivo: packCole, filename: "Pack-Vuelta-al-Cole.zip", mime: "application/zip", volver: "/presupuesto-vuelta-al-cole" },
  jubilacion: { ref: "jubilacion2026", titulo: "Guía: Jubilación ANSES paso a paso (PDF)", nombre: "Guía: Jubilación ANSES paso a paso",
    precio: 3999, archivo: guiaJubilacion, filename: "Guia-Jubilacion-ANSES-Paso-A-Paso.pdf", mime: "application/pdf", volver: "/cuantos-aportes-necesito-para-jubilarme" },
  salir: { ref: "salir2026", titulo: "Guía: Salir del monotributo (PDF)", nombre: "Guía: Salir del monotributo",
    precio: 3999, archivo: guiaSalir, filename: "Guia-Salir-Del-Monotributo.pdf", mime: "application/pdf", volver: "/salir-del-monotributo-cuanto-cuesta" },
  mudanza: { ref: "mudanza2026", titulo: "Guía: Mudanza sin estafas (PDF)", nombre: "Guía: Mudanza sin estafas",
    precio: 2999, archivo: guiaMudanza, filename: "Guia-Mudanza-Sin-Estafas.pdf", mime: "application/pdf", volver: "/mudanza-calculadora-metros-cubicos" },
  renovar: { ref: "renovar2026", titulo: "Guía: Se vence tu alquiler (PDF)", nombre: "Guía: Se vence tu alquiler",
    precio: 2999, archivo: guiaRenovar, filename: "Guia-Se-Vence-Tu-Alquiler.pdf", mime: "application/pdf", volver: "/renovar-alquiler-o-mudarse" },
  costa: { ref: "costa2026", titulo: "Guía: Vender en la costa o en ferias (PDF)", nombre: "Guía: Vender en la costa o en ferias",
    precio: 2999, archivo: guiaCosta, filename: "Guia-Vender-En-La-Costa-Ferias.pdf", mime: "application/pdf", volver: "/vender-en-la-costa-feria-punto-de-equilibrio" },
  presupuesto: { ref: "presupuesto2026", titulo: "Presupuesto Familiar 2027 con IPC (planilla Excel / Google Sheets)", nombre: "Presupuesto Familiar 2027 con IPC",
    precio: 3999, archivo: presupuesto, filename: "Presupuesto-Familiar-2027-IPC.xlsx", volver: "/presupuesto-familiar-2027-inflacion" },
  temporada: { ref: "temporada2026", titulo: "Pack Personal de Temporada (modelos Word)", nombre: "Pack Personal de Temporada",
    precio: 3999, archivo: packTemporada, filename: "Pack-Personal-de-Temporada.zip", mime: "application/zip", volver: "/contratar-personal-de-temporada-verano" },
  stock: { ref: "stock2026", titulo: "Planilla de Stock, Costos y Ventas para Emprendedores (planilla Excel / Google Sheets)", nombre: "Planilla de Stock, Costos y Ventas",
    precio: 2999, archivo: stock, filename: "Planilla-Stock-Costos-Ventas.xlsx", volver: "/vender-en-navidad-margen-precio-stock" },
  deposito: { ref: "deposito2026", titulo: "Pack Recuperá tu depósito de alquiler: guía, cartas y planilla (PDF + planilla Excel)", nombre: "Pack Recuperá tu depósito de alquiler",
    precio: 2999, archivo: packDeposito, filename: "Pack-Recuperar-Deposito.zip", mime: "application/zip", volver: "/recuperar-deposito-alquiler" },
  recibos: { ref: "recibos2026", titulo: "Generador de recibos y presupuestos en PDF: 10 documentos", nombre: "10 documentos del generador de recibos y presupuestos",
    precio: 990, app: "/recibos-presupuestos-pdf", volver: "/recibos-presupuestos-pdf" },
};
const IPC_URL = "https://apis.datos.gob.ar/series/api/series/?ids=148.3_INIVELNAL_DICI_M_26&format=json&limit=120&sort=desc";
const porRef = (ref) => Object.values(PRODUCTOS).find((p) => p.ref === ref);
const DIAS_DESCARGA = 30;
const api = (env) => env.MP_API || "https://api.mercadopago.com";

const FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;700&family=Bricolage+Grotesque:opsz,wght@12..96,700&family=JetBrains+Mono:wght@600&display=swap">';
const html = (body, status = 200) =>
  new Response(
    `<!doctype html><html lang="es-AR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>CuentaClara</title><meta name="robots" content="noindex">${FONTS}<link rel="stylesheet" href="/estilo.css"></head><body><header class="top"><div class="wrap"><a class="marca" href="/" aria-label="CuentaClara, inicio"><img class="logo logo-claro" src="/img/cuentaclara.svg" alt="CuentaClara" width="170" height="32"><img class="logo logo-oscuro" src="/img/cuentaclara-oscuro.svg" alt="" width="170" height="32"><span class="lema">Tus cuentas, claras. Tus trámites, resueltos.</span></a></div></header><main class="wrap"><div class="mensaje">${body}</div></main><footer class="pie"><div class="wrap"><div class="legal"><a href="/terminos">Términos y condiciones</a><a href="/privacidad">Política de privacidad</a><a href="/devoluciones">Devoluciones</a><a class="arrep" href="/arrepentimiento">Botón de arrepentimiento</a></div></div></footer></body></html>`,
    { status, headers: { "content-type": "text/html; charset=utf-8" } }
  );

// Devuelve { prod, estado }: prod si el pago está aprobado, vigente y no revocado; estado = status de Mercado Pago.
async function consultarPago(env, id) {
  if (!/^\d{1,20}$/.test(id || "")) return { prod: null, estado: "inexistente" };
  if (await revocado(env, id)) return { prod: null, estado: "revocado" };
  if (await pagoInexistente(env, id)) return { prod: null, estado: "inexistente" };
  let p;
  try {
    const r = await fetch(`${api(env)}/v1/payments/${id}`, {
      headers: { Authorization: `Bearer ${env.MP_ACCESS_TOKEN}` },
    });
    if (!r.ok) {
      if (r.status === 404) await marcarInexistente(env, id);
      return { prod: null, estado: "inexistente" };
    }
    p = await r.json();
  } catch {
    return { prod: null, estado: "error" };
  }
  const prod = porRef(p.external_reference);
  if (!prod) return { prod: null, estado: "inexistente" };
  const vigente = Date.now() - Date.parse(p.date_approved) < DIAS_DESCARGA * 864e5;
  const ok = p.status === "approved" && p.transaction_amount >= prod.precio && vigente;
  return { prod: ok ? prod : null, estado: p.status === "approved" && !vigente ? "vencido" : p.status };
}
const pagoValido = async (env, id) => (await consultarPago(env, id)).prod;

const demasiados = () => html("<h1>Demasiados intentos</h1><p>Hiciste muchos pedidos seguidos desde esta conexión. Probá de nuevo en un rato.</p>", 429);

export default {
  async scheduled(event, env, ctx) {
    ctx.waitUntil(refrescarQR(env));
  },
  async fetch(req, env, ctx) {
    const url = new URL(req.url);

    const qr = await manejarQR(req, env, ctx);
    if (qr) return qr;
    const lg = await manejarLegal(req, env, Object.values(PRODUCTOS).map((p) => p.ref));
    if (lg) return lg;
    const rc = await manejarRecibos(req, env);
    if (rc) return rc;
    const pd = await manejarPedidos(req, env);
    if (pd) return pd;

    if (url.pathname === "/api/ipc") {
      // Proxy con caché de la serie oficial del INDEC para la calculadora de alquileres.
      const r = await fetch(env.IPC_URL || IPC_URL, { cf: { cacheTtl: 21600, cacheEverything: true } }).catch(() => null);
      if (!r?.ok) return Response.json({ error: "IPC no disponible" }, { status: 502 });
      const { data } = await r.json();
      return Response.json({ datos: data.filter(([, v]) => v != null).reverse() }, { headers: { "cache-control": "public, max-age=21600" } });
    }

    if (url.pathname === "/comprar") {
      const prod = PRODUCTOS[url.searchParams.get("p") || "kit"];
      if (!prod) return html('<h1>Ese producto no existe</h1><p><a class="boton" href="/">Volver al inicio</a></p>', 404);
      if (url.searchParams.get("ok") !== "1") {
        // Aviso previo al pago: entrega inmediata y fin del reembolso una vez descargado (art. 1116 inc. c CCyC, Disp. 954/2025 art. 3 inc. a).
        const pre = `/comprar?p=${encodeURIComponent(url.searchParams.get("p") || "kit")}&ok=1`;
        const aviso = prod.app
          ? "Cada documento que generes usa un crédito, y los créditos ya usados no se reembolsan."
          : "Apenas descargues el archivo, la compra se considera entregada y ya no podés arrepentirte con reembolso.";
        return html(`<span class="etiqueta">Antes de pagar</span><h1>${prod.nombre}</h1><p>Precio: <b>$ ${prod.precio.toLocaleString("es-AR")}</b>, pago único con Mercado Pago.</p><p><b>Entrega inmediata.</b> ${aviso} Es la excepción del art. 1116 inc. c del Código Civil y Comercial para archivos digitales de uso permanente. Hasta que descargues, podés usar el <a href="/arrepentimiento">botón de arrepentimiento</a> dentro de los 10 días y se te reembolsa el 100%. Detalle en la <a href="/devoluciones">política de devoluciones</a>.</p><p><a class="boton" href="${pre}">Entendido, ir a pagar</a> <a href="${prod.volver}">Volver</a></p>`);
      }
      const r = await fetch(`${api(env)}/checkout/preferences`, {
        method: "POST",
        headers: { Authorization: `Bearer ${env.MP_ACCESS_TOKEN}`, "content-type": "application/json" },
        body: JSON.stringify({
          items: [{ id: prod.ref, title: prod.titulo, quantity: 1, unit_price: prod.precio, currency_id: "ARS" }],
          external_reference: prod.ref,
          back_urls: {
            success: `${url.origin}/gracias`,
            pending: `${url.origin}/gracias`,
            failure: `${url.origin}${prod.volver}`,
          },
          auto_return: "approved",
          statement_descriptor: "KITMONOTRIBUTO",
        }),
      }).catch(() => null);
      if (!r?.ok) return html(`<h1>No pudimos abrir el pago</h1><p>Probá de nuevo en unos minutos.</p><p><a class="boton" href="${prod.volver}">Volver</a></p>`, 502);
      const pref = await r.json();
      return Response.redirect(pref.init_point, 303);
    }

    if (url.pathname === "/recuperar") {
      const id = (url.searchParams.get("id") || "").replace(/\s/g, "");
      if (!id) return html(`<span class="etiqueta">Recuperar compra</span><h1>¿Perdiste la descarga?</h1><p>Ingresá el <b>número de operación</b> que figura en el comprobante de Mercado Pago (también en el mail del pago o en Tu actividad). Te llevamos de nuevo a tu página de descarga. Si pagaste en efectivo, aparece cuando el pago se acredita.</p><form method="get" action="/recuperar" class="arr-form"><label for="id">Número de operación</label><input id="id" name="id" inputmode="numeric" pattern="[0-9]{5,20}" required autocomplete="off" placeholder="Solo números"><button class="boton" type="submit">Buscar mi compra</button></form>`);
      if (!/^\d{5,20}$/.test(id)) return html('<h1>Número no válido</h1><p>El número de operación tiene solo dígitos. Revisalo en tu comprobante de Mercado Pago.</p><p><a class="boton" href="/recuperar">Probar de nuevo</a></p>', 400);
      if (await limitar(env, req, "recuperar", 15, 3600)) return demasiados();
      return Response.redirect(`${url.origin}/gracias?payment_id=${id}`, 303);
    }

    if (url.pathname === "/gracias") {
      const id = url.searchParams.get("payment_id");
      const status = url.searchParams.get("status") || url.searchParams.get("collection_status");
      if (await limitar(env, req, "gracias", 60, 3600)) return demasiados();
      const { prod, estado: est } = await consultarPago(env, id);
      if (prod?.app)
        return html(`<span class="etiqueta">Pago aprobado</span><h1>Ya tenés 10 documentos</h1><p>Se cargaron en tu navegador. Si cambiás de dispositivo, usá siempre este enlace.</p><p><a class="boton" href="${prod.app}?pago=${id}">Crear mis documentos</a></p><p class="nota">Guardá esta página: el código ${id} es tu llave. Si la perdés, lo recuperás en <a href="/recuperar">/recuperar</a> con el número de operación de tu comprobante de Mercado Pago.</p>`);
      if (prod)
        return html(`<span class="etiqueta">Pago aprobado</span><h1>Gracias por tu compra</h1><p>Ya podés descargar <b>${prod.nombre}</b>.</p><p><a class="boton" href="/descargar?payment_id=${id}">${prod.mime === "application/pdf" ? "Descargar la guía (PDF)" : prod.mime ? "Descargar el pack (ZIP)" : "Descargar la planilla"}</a></p><p class="nota">Guardá esta página: el enlace funciona durante ${DIAS_DESCARGA} días y permite hasta ${MAX_DESCARGAS} descargas. Si la perdés, entrá a <a href="/recuperar">/recuperar</a> con el número de operación de tu comprobante de Mercado Pago.${prod.mime ? "" : " Para abrirla en Google Sheets: Archivo, Importar, Subir."}</p>`);
      if (est === "pending" || est === "in_process" || est === "authorized" || status === "pending" || status === "in_process")
        return html(`<span class="etiqueta">Pago en proceso</span><h1>Tu pago se está acreditando</h1><p>Si pagaste en efectivo (Rapipago, Pago Fácil), puede demorar hasta unas horas. Cuando Mercado Pago lo apruebe, volvé a abrir esta página o entrá a <a href="/recuperar">/recuperar</a> con el número de operación de tu comprobante, y vas a ver el botón de descarga. Guardala en favoritos.</p>`);
      if (est === "vencido")
        return html(`<h1>El enlace de descarga venció</h1><p>El enlace funciona durante ${DIAS_DESCARGA} días desde el pago aprobado.</p>`, 410);
      return html(`<h1>No encontramos un pago aprobado</h1><p>Si acabás de pagar, recargá esta página en un minuto. Si perdiste el enlace, usá <a href="/recuperar">/recuperar</a> con el número de operación de tu comprobante de Mercado Pago.</p><p><a class="boton" href="/">Volver al inicio</a></p>`, 404);
    }

    if (url.pathname === "/descargar") {
      if (await limitar(env, req, "descargar", 20, 3600)) return demasiados();
      const idd = url.searchParams.get("payment_id");
      const prod = await pagoValido(env, idd);
      if (prod?.archivo && !(await registrarDescarga(env, idd)))
        return html(`<h1>Llegaste al límite de descargas</h1><p>Cada pago permite ${MAX_DESCARGAS} descargas. Si ya bajaste el archivo, buscalo en la carpeta de descargas de tu dispositivo.</p>`, 429);
      if (!prod || !prod.archivo) return html("<h1>Enlace no válido o vencido</h1><p>El enlace de descarga funciona solo con un pago aprobado y durante 30 días.</p>", 403);
      return new Response(prod.archivo, {
        headers: {
          "content-type": prod.mime || "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
          "content-disposition": `attachment; filename="${prod.filename}"`,
          "cache-control": "private, no-store",
        },
      });
    }

    return env.ASSETS.fetch(req);
  },
};
