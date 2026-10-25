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
import { manejarQR } from "./qr.js";
import { manejarRecibos } from "./recibos.js";
import { manejarLegal, revocado } from "./legal.js";

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
  telegramas: { ref: "telegramas2026", titulo: "Pack 10 Telegramas y Cartas Documento Laborales (modelos Word)", nombre: "Pack Telegramas Laborales",
    precio: 4999, archivo: packTelegramas, filename: "Pack-Telegramas-Laborales.zip", mime: "application/zip", volver: "/telegrama-renuncia-modelo" },
  boletoauto: { ref: "boletoauto2026", titulo: "Pack Compraventa de Auto Usado: boleto, recibos y checklists (modelos Word)", nombre: "Pack Compraventa de Auto Usado",
    precio: 3999, archivo: packBoletoAuto, filename: "Pack-Compraventa-Auto-Usado.zip", mime: "application/zip", volver: "/boleto-compraventa-auto-usado" },
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
    `<!doctype html><html lang="es-AR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kit Monotributista</title><meta name="robots" content="noindex">${FONTS}<link rel="stylesheet" href="/estilo.css"></head><body><header class="top"><div class="wrap"><a class="marca" href="/"><i>A–K</i>Kit Monotributista</a></div></header><main class="wrap"><div class="mensaje">${body}</div></main><footer class="pie"><div class="wrap"><div class="legal"><a href="/terminos">Términos y condiciones</a><a href="/privacidad">Política de privacidad</a><a href="/devoluciones">Devoluciones</a><a class="arrep" href="/arrepentimiento">Botón de arrepentimiento</a></div></div></footer></body></html>`,
    { status, headers: { "content-type": "text/html; charset=utf-8" } }
  );

async function pagoValido(env, id) {
  if (!/^\d{1,20}$/.test(id || "")) return null;
  if (await revocado(env, id)) return null;
  let p;
  try {
    const r = await fetch(`${api(env)}/v1/payments/${id}`, {
      headers: { Authorization: `Bearer ${env.MP_ACCESS_TOKEN}` },
    });
    if (!r.ok) return null;
    p = await r.json();
  } catch {
    return null;
  }
  const prod = porRef(p.external_reference);
  const vigente = Date.now() - Date.parse(p.date_approved) < DIAS_DESCARGA * 864e5;
  const ok = prod && p.status === "approved" && p.transaction_amount >= prod.precio && vigente;
  return ok ? prod : null;
}

export default {
  async fetch(req, env, ctx) {
    const url = new URL(req.url);

    const qr = await manejarQR(req, env, ctx);
    if (qr) return qr;
    const lg = await manejarLegal(req, env, Object.values(PRODUCTOS).map((p) => p.ref));
    if (lg) return lg;
    const rc = await manejarRecibos(req, env);
    if (rc) return rc;

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

    if (url.pathname === "/gracias") {
      const id = url.searchParams.get("payment_id");
      const status = url.searchParams.get("status") || url.searchParams.get("collection_status");
      const prod = await pagoValido(env, id);
      if (prod?.app)
        return html(`<span class="etiqueta">Pago aprobado</span><h1>Ya tenés 10 documentos</h1><p>Se cargaron en tu navegador. Si cambiás de dispositivo, usá siempre este enlace.</p><p><a class="boton" href="${prod.app}?pago=${id}">Crear mis documentos</a></p><p class="nota">Guardá esta página: el código ${id} es tu llave y no se recupera.</p>`);
      if (prod)
        return html(`<span class="etiqueta">Pago aprobado</span><h1>Gracias por tu compra</h1><p>Ya podés descargar <b>${prod.nombre}</b>.</p><p><a class="boton" href="/descargar?payment_id=${id}">${prod.mime === "application/pdf" ? "Descargar la guía (PDF)" : prod.mime ? "Descargar el pack (ZIP)" : "Descargar la planilla"}</a></p><p class="nota">Guardá esta página: el enlace funciona durante ${DIAS_DESCARGA} días.${prod.mime ? "" : " Para abrirla en Google Sheets: Archivo, Importar, Subir."}</p>`);
      if (status === "pending" || status === "in_process")
        return html(`<span class="etiqueta">Pago en proceso</span><h1>Tu pago se está acreditando</h1><p>Cuando Mercado Pago lo apruebe, volvé a abrir esta misma página y vas a ver el botón de descarga. Guardala en favoritos.</p>`);
      return html(`<h1>No encontramos un pago aprobado</h1><p>Si acabás de pagar, recargá esta página en un minuto.</p><p><a class="boton" href="/">Volver al inicio</a></p>`, 404);
    }

    if (url.pathname === "/descargar") {
      const prod = await pagoValido(env, url.searchParams.get("payment_id"));
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
