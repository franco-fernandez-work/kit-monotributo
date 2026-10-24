// Venta automática con Mercado Pago Checkout Pro: /comprar crea la preferencia,
// /gracias verifica el pago y /descargar entrega el archivo solo si el pago está aprobado.
import kit from "../private/kit.xlsx";

const PRODUCTO = "Kit Monotributista 2026 (planilla Excel / Google Sheets)";
const PRECIO = 6999; // ARS
const REF = "kitmono2026";
const DIAS_DESCARGA = 30;
const api = (env) => env.MP_API || "https://api.mercadopago.com";

const html = (body, status = 200) =>
  new Response(
    `<!doctype html><html lang="es-AR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kit Monotributista 2026</title><meta name="robots" content="noindex"><style>body{font:17px/1.6 system-ui,sans-serif;max-width:640px;margin:40px auto;padding:0 16px;background:#fff;color:#1a1a1a}h1{color:#1f4e79}a.b{display:inline-block;background:#1f4e79;color:#fff;padding:12px 20px;border-radius:8px;text-decoration:none;font-weight:600}@media(prefers-color-scheme:dark){body{background:#121417;color:#e8e8e8}h1{color:#7fb3e6}}</style></head><body>${body}</body></html>`,
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
  const vigente = Date.now() - Date.parse(p.date_approved) < DIAS_DESCARGA * 864e5;
  const ok = p.status === "approved" && p.external_reference === REF && p.transaction_amount >= PRECIO && vigente;
  return ok ? p : null;
}

export default {
  async fetch(req, env) {
    const url = new URL(req.url);

    if (url.pathname === "/comprar") {
      const r = await fetch(`${api(env)}/checkout/preferences`, {
        method: "POST",
        headers: { Authorization: `Bearer ${env.MP_ACCESS_TOKEN}`, "content-type": "application/json" },
        body: JSON.stringify({
          items: [{ id: REF, title: PRODUCTO, quantity: 1, unit_price: PRECIO, currency_id: "ARS" }],
          external_reference: REF,
          back_urls: {
            success: `${url.origin}/gracias`,
            pending: `${url.origin}/gracias`,
            failure: `${url.origin}/`,
          },
          auto_return: "approved",
          statement_descriptor: "KITMONOTRIBUTO",
        }),
      }).catch(() => null);
      if (!r?.ok) return html("<h1>No pudimos iniciar el pago</h1><p>Probá de nuevo en unos minutos.</p>", 502);
      const pref = await r.json();
      return Response.redirect(pref.init_point, 303);
    }

    if (url.pathname === "/gracias") {
      const id = url.searchParams.get("payment_id");
      const status = url.searchParams.get("status") || url.searchParams.get("collection_status");
      if (await pagoValido(env, id))
        return html(`<h1>¡Gracias por tu compra!</h1><p>Tu pago fue aprobado. Descargá tu planilla:</p><p><a class="b" href="/descargar?payment_id=${id}">Descargar Kit Monotributista 2026</a></p><p>Guardá esta página: el enlace funciona durante ${DIAS_DESCARGA} días. Para usarla en Google Sheets: Archivo → Importar.</p>`);
      if (status === "pending" || status === "in_process")
        return html(`<h1>Tu pago está en proceso</h1><p>Cuando Mercado Pago lo apruebe, volvé a abrir esta misma página (guardala en favoritos) y vas a ver el botón de descarga.</p>`);
      return html(`<h1>No encontramos un pago aprobado</h1><p>Si acabás de pagar, recargá esta página en un minuto.</p><p><a class="b" href="/">Volver</a></p>`, 404);
    }

    if (url.pathname === "/descargar") {
      if (!(await pagoValido(env, url.searchParams.get("payment_id"))))
        return html("<h1>Enlace no válido o vencido</h1>", 403);
      return new Response(kit, {
        headers: {
          "content-type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
          "content-disposition": 'attachment; filename="Kit-Monotributista-2026.xlsx"',
          "cache-control": "private, no-store",
        },
      });
    }

    return env.ASSETS.fetch(req);
  },
};
