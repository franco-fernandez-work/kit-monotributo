"""Genera private/pack-reclamos.zip y private/pack-telegramas.zip (Word editables). Necesita python-docx: correr local y commitear los zips."""
import os, re, zipfile, io, unicodedata
from packs_lib import Doc
import legal_data as L

PRIV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "private")
LAB = {"preaviso_texto": "elegí: Cumpliré el preaviso hasta el DD/MM. / No cumpliré el preaviso.", "pedido_final": "Solicito que se retire la comunicación y se respeten mis condiciones de trabajo"}

def fill(t):
    """{campo} -> [[campo]] para que quede resaltado en Word."""
    return re.sub(r"\{(\w+)\}", lambda m: "[[" + LAB.get(m.group(1), m.group(1).replace("_", " ")) + "]]", t)

def build_doc(pack, num, item, kind):
    d = Doc(pack, item["titulo"], item["cuando"])
    d.box("Antes de enviar", [f"**Normas:** {item['normas']}", f"**Plazo:** {item['plazo']}", "Completá los campos resaltados en amarillo y borrá lo que no aplique."] +
          (["**Reuní estas pruebas:** " + "; ".join(item["pruebas"]) + "."] if "pruebas" in item else []))
    if kind == "cons":
        d.h("Carta de reclamo"); d.p("[[Ciudad]], [[fecha]]", False)
        d.p("\n".join(fill(l) for l in L.CAB_CONS.split("\n")), False)
        for par in item["cuerpo"]: d.p(fill(par))
        d.p(L.PIE_CONS); d.p(fill(L.FIRMA_CONS), False)
        d.h("Segunda intimación (si no contestan)"); d.p(fill(item["segunda"]))
        d.h("Cómo enviarla"); d.bullets(["Por mail o formulario del proveedor, guardando la captura y el acuse; o por carta documento si querés máxima prueba.", "Guardá siempre una copia con fecha."])
    else:
        d.h("Versión telegrama (TCL gratuito)"); d.p(fill(item["telegrama"]).upper(), False, 10)
        d.p("Texto en mayúsculas listo para el Correo. Completá los campos y revisá que no sea demasiado largo; si no entra, usá la carta documento.", False, 9, italic=True)
        d.h("Versión carta documento (más completa)"); d.p("[[Ciudad]], [[fecha]]", False)
        d.p("\n".join(fill(l) for l in L.CAB_LAB.split("\n")), False)
        for par in item["carta"]: d.p(fill(par))
        d.p(L.PIE_LAB); d.p(fill(L.FIRMA_LAB), False)
        d.h("Qué sigue"); d.bullets(["Guardá la constancia de imposición y el aviso de recepción.", "Esperá el plazo y registrá si hubo respuesta; la contestación del empleador debe responderse en 2 días hábiles (art. 57 LCT).", "Si no cumple, consultá el modelo siguiente del pack."])
    return d

def leeme(pack, titulo, sub, blocks, usos):
    d = Doc(pack, titulo, sub)
    d.box("Importante", [L.AVISO, "Los textos citan normas vigentes a octubre de 2026. Verificalos antes de enviar: la normativa y su interpretación cambian."])
    d.h("Qué incluye"); d.bullets(usos)
    for t, items in blocks:
        d.h(t); d.bullets(items)
    return d

def zip_pack(name, files):
    with zipfile.ZipFile(os.path.join(PRIV, name), "w", zipfile.ZIP_DEFLATED) as z:
        for fn, doc in files:
            buf = io.BytesIO(); doc.d.save(buf); z.writestr(fn, buf.getvalue())

def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-")

def main():
    # reclamos
    files = [("00-LEEME-Guia-de-reclamos.docx", leeme("Pack Reclamos de Consumo", "Guía de reclamos de consumo", "Cómo usar el pack y dónde reclamar", L.GUIA_CONS,
        [f"{i+1:02d}. {r['titulo']}" for i, r in enumerate(L.RECLAMOS)]))]
    for i, r in enumerate(L.RECLAMOS, 1):
        files.append((f"{i:02d}-{slug(r['titulo'])}.docx", build_doc("Pack Reclamos de Consumo", i, r, "cons")))
    zip_pack("pack-reclamos.zip", files)
    # telegramas
    files = [("00-LEEME-Guia-de-plazos-y-envio.docx", leeme("Pack Telegramas Laborales", "Guía de plazos y envío", "Cómo enviar telegramas gratis y en qué orden", L.GUIA_LAB,
        [f"{i+1:02d}. {r['titulo']}" for i, r in enumerate(L.TELEGRAMAS)]))]
    for i, r in enumerate(L.TELEGRAMAS, 1):
        files.append((f"{i:02d}-{slug(r['titulo'])}.docx", build_doc("Pack Telegramas Laborales", i, r, "lab")))
    zip_pack("pack-telegramas.zip", files)
    print("ok")

if __name__ == "__main__":
    main()
