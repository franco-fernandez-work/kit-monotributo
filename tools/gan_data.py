"""Escala del art. 94 y deducciones del art. 30 de Ganancias 2026 (ARCA, RG 4003).
Base: tablas anuales de enero a junio. Julio a diciembre: +16,85% por IPC. Los acumulados mensuales
son lineales: meses 1-6 a razón de 1/12 del valor de enero-junio y meses 7-12 a razón de 1/12 del valor ajustado."""
F2 = 1.168453  # 16,85% redondeado; calibrado contra los acumulados oficiales a diciembre
# (desde, fijo, porcentaje) de la escala anual enero-junio 2026
ESC_H1 = [(0.00, 0.00, 5), (2000030.09, 100001.50, 9), (4000060.17, 280004.21, 12), (6000090.26, 520007.82, 15),
          (9000135.40, 970014.59, 19), (18000270.80, 2680040.32, 23), (27000406.20, 4750071.46, 27),
          (40500609.30, 8395126.30, 31), (60750913.96, 14672720.74, 35)]
# Deducciones anuales enero-junio 2026
DED_H1 = {"gni": 5151802.50, "conyuge": 4851964.66, "hijo": 2446863.48, "incap": 4893726.96, "especial": 18031308.76}
# Valores oficiales acumulados a diciembre 2026 (PDF de ARCA, julio a diciembre): para controlar la interpolación
DED_DIC = {"gni": 5585736.93, "conyuge": 5260643.86, "hijo": 2652961.90, "incap": 5305923.78, "especial": 19550079.27}
ESC_DIC_LIM = [2168491.89, 4336983.77, 6505475.65, 9758213.49, 19516426.99, 29274640.48, 43911960.73, 65867941.10]

def factor(m):
    return (m if m <= 6 else 6 + (m - 6) * F2) / 12

def escala(m):
    """Tramos acumulados al mes m: lista de (desde, fijo, pct)."""
    k = factor(m); out = []; fijo = 0.0; prev = None
    desde = [round(d * k, 2) for d, _, _ in ESC_H1]
    for i, (_, _, p) in enumerate(ESC_H1):
        if i: fijo += (desde[i] - desde[i - 1]) * ESC_H1[i - 1][2] / 100
        out.append((desde[i], round(fijo, 2), p))
    return out

def deducciones(m):
    k = factor(m); return {a: round(v * k, 2) for a, v in DED_H1.items()}

def impuesto(neta, m=12):
    if neta <= 0: return 0.0
    t = [x for x in escala(m) if x[0] <= neta][-1]
    return t[1] + (neta - t[0]) * t[2] / 100

if __name__ == "__main__":
    e = escala(12)
    print([round(abs(e[i][0] - ESC_DIC_LIM[i - 1]), 2) for i in range(1, 9)])
    d = deducciones(12); print({a: round(d[a] - DED_DIC[a], 2) for a in d})
    print(escala(9)[1], deducciones(9)["gni"])
