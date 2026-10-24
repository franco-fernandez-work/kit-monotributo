// Venta automática con Mercado Pago Checkout Pro: /comprar?p=<producto> crea la preferencia,
// /gracias verifica el pago y /descargar entrega el archivo solo si el pago está aprobado.
import kit from "../private/kit.xlsx";
import vendedores from "../private/vendedores.xlsx";

const PRODUCTOS = {
  kit: {
    ref: "kitmono2026", titulo: "Kit Monotributista 2026 (planilla Excel / Google Sheets)",
    nombre: "Kit Monotributista 2026", precio: 6999, archivo: kit, filename: "Kit-Monotributista-2026.xlsx", volver: "/",
  },
  vendedores: {
    ref: "vendedores2026", titulo: "Calculadora de Precios para Vendedores 2026 (planilla Excel / Google Sheets)",
    nombre: "Calculadora de Precios para Vendedores", precio: 4999, archivo: vendedores, filename: "Calculadora-Precios-Vendedores-2026.xlsx", volver: "/precios-mercado-libre",
  },
};
const porRef = (ref) => Object.values(PRODUCTOS).find((p) => p.ref === ref);
const DIAS_DESCARGA = 30;
const api = (env) => env.MP_API || "https://api.mercadopago.com";

const FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;700&family=Bricolage+Grotesque:opsz,wght@12..96,700&family=JetBrains+Mono:wght@600&display=swap">';
const html = (body, status = 200) =>
  new Response(
    `<!doctype html><html lang="es-AR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kit Monotributista</title><meta name="robots" content="noindex">${FONTS}<link rel="stylesheet" href="/estilo.css"></head><body><header class="top"><div class="wrap"><a class="marca" href="/"><i>A–K</i>Kit Monotributista</a></div></header><main class="wrap"><div class="mensaje">${body}</div></main></body></html>`,
    { status, headers: { "content-type": "text/html; charset=utf-8" } }
  );

async function pagoValido(env, id) {
  if (!/^\d{1,20}$/.test(id || "")) return null;
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
  async fetch(req, env) {
    const url = new URL(req.url);

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
      if (prod)
        return html(`<span class="etiqueta">Pago aprobado</span><h1>Gracias por tu compra</h1><p>Ya podés descargar <b>${prod.nombre}</b>.</p><p><a class="boton" href="/descargar?payment_id=${id}">Descargar la planilla</a></p><p class="nota">Guardá esta página: el enlace funciona durante ${DIAS_DESCARGA} días. Para abrirla en Google Sheets: Archivo, Importar, Subir.</p>`);
      if (status === "pending" || status === "in_process")
        return html(`<span class="etiqueta">Pago en proceso</span><h1>Tu pago se está acreditando</h1><p>Cuando Mercado Pago lo apruebe, volvé a abrir esta misma página y vas a ver el botón de descarga. Guardala en favoritos.</p>`);
      return html(`<h1>No encontramos un pago aprobado</h1><p>Si acabás de pagar, recargá esta página en un minuto.</p><p><a class="boton" href="/">Volver al inicio</a></p>`, 404);
    }

    if (url.pathname === "/descargar") {
      const prod = await pagoValido(env, url.searchParams.get("payment_id"));
      if (!prod) return html("<h1>Enlace no válido o vencido</h1><p>El enlace de descarga funciona solo con un pago aprobado y durante 30 días.</p>", 403);
      return new Response(prod.archivo, {
        headers: {
          "content-type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
          "content-disposition": `attachment; filename="${prod.filename}"`,
          "cache-control": "private, no-store",
        },
      });
    }

    return env.ASSETS.fetch(req);
  },
};
