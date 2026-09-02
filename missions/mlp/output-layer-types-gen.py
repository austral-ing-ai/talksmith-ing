#!/usr/bin/env python3
"""Genera `output-layer-types.csv` a partir de `input-data-types.csv`.

**Son las mismas 2000 casas.** Mismos `listing_id`, mismas columnas de entrada.
Lo único que se agrega son columnas objetivo: una por cada familia de salida que
recorre la clase.

Y hay una vuelta deliberada: **el precio deja de ser la respuesta y pasa a ser una
entrada más.** En el notebook de la entrada, `precio` era lo que se predecía; acá
es un dato que la casa ya tiene, y lo que se predice es otra cosa. Ese giro es el
punto: con el mismo dato de entrada, lo que cambia la última capa es *la tarea*.

Todo objetivo es sintético, con semilla fija y regla explícita, así cada sección
sabe cuál es su piso y se puede decir cuándo un modelo recuperó todo lo que había.

    python3 output-layer-types-gen.py
"""
import numpy as np
import pandas as pd

RNG = np.random.default_rng(42)

ORDEN_ESTADO = ["regular", "bueno", "muy bueno", "excelente"]
df = pd.read_csv("input-data-types.csv")
N = len(df)

# Las mismas features, en la forma en que ya salieron del otro notebook.
precio_k = df.precio.to_numpy() / 1000.0          # ahora es ENTRADA
m2 = df.m2.to_numpy().astype(float)
antiguedad = 2024.0 - df.anio_alta.to_numpy()
estado_i = pd.Categorical(df.estado, categories=ORDEN_ESTADO, ordered=True).codes
barrio_i = pd.Categorical(df.barrio).codes
n_barrios = barrio_i.max() + 1
# Cuánto ayuda cada barrio a vender rápido. No es lineal en el índice: el índice
# no significa nada, y eso tiene que verse en los números.
BARRIO_VENTA = RNG.normal(0, 0.45, n_barrios)

# --- La señal compartida ------------------------------------------------------
# Todo lo que sigue sale de acá, así los siete objetivos hablan de la misma casa:
# lo deseable que es. Positivo = se vende rápido y la miran mucho.
atractivo = (
    0.019 * (100.0 - antiguedad)
    + 0.55 * (estado_i - 1.5)
    - 0.0021 * precio_k
    + 0.0035 * m2
    + BARRIO_VENTA[barrio_i]
    - 1.05
)

# --- 1 y 6 y 7 · Regresión, percentiles y distribución --------------------------
# Días hasta vender. Continuo, asimétrico a la derecha y **heterocedástico**: a
# el tipo de vivienda manda sobre cuánta: sigma va de 5 días en un departamento
# a 30 en una casa. Un solo número no responde "¿cuánto tardo
# en el peor caso?", y una sigma constante miente sobre las caras.
mu_dias = 60.0 - 30.0 * atractivo
# La incertidumbre NO es la misma para todas: depende del tipo de vivienda. Un
# departamento se vende con una previsibilidad que una casa no tiene. Se eligió
# `tipo_vivienda` a propósito porque NO entra en `atractivo`: así la sigma es una
# señal propia y separable, y no un reflejo del error de la media.
SIGMA_TIPO = {"departamento": 5.0, "PH": 11.0, "duplex": 18.0, "casa": 30.0}
sigma_dias = df.tipo_vivienda.map(SIGMA_TIPO).to_numpy()
dias = RNG.normal(mu_dias, sigma_dias) + RNG.exponential(1.5, N)
dias = np.clip(dias, 1, None)
# Un 1,5% de fichas con la fecha de baja mal cargada: días que son diez veces lo
# real. Es el error de carga que separa MSE de Huber, y el dataset lo trae de
# verdad en vez de pedir que se lo imaginen.
typo = RNG.random(N) < 0.015
dias_cargado = dias.copy()
dias_cargado[typo] *= 10

# --- 2 · Conteo ---------------------------------------------------------------
# Visitas en la primera semana. Poisson de verdad: la varianza crece con la
# media, que es justo lo que una salida lineal con MSE no puede representar.
lam_visitas = np.exp(1.20 + 1.60 * atractivo)
visitas_semana = RNG.poisson(lam_visitas)

# --- 3 · Binaria --------------------------------------------------------------
p_vendio = 1.0 / (1.0 + np.exp(-(2.4 * atractivo + 0.35)))
se_vendio = (RNG.random(N) < p_vendio).astype(int)

# --- 4 · Multiclase excluyente ------------------------------------------------
# Segmento comercial: una casa cae en uno solo. Cortes por percentil del precio,
# así las tres clases quedan pobladas.
q1, q2 = np.quantile(precio_k, [0.40, 0.80])
segmento = np.where(precio_k < q1, "economica",
           np.where(precio_k < q2, "media", "premium"))

# --- 5 · Multi-etiqueta -------------------------------------------------------
# Tres atributos que pueden darse juntos, o ninguno. Es el caso del ticket que es
# urgente Y de facturación: forzarlos a competir sería un error de modelado.
def bernoulli(z):
    return (RNG.random(N) < 1.0 / (1.0 + np.exp(-z))).astype(int)

tiene_pileta = bernoulli(-2.5 + 0.014 * m2 + 0.0016 * precio_k)
apto_credito = bernoulli(1.8 - 0.042 * antiguedad + 0.5 * (estado_i - 1.5))
a_reciclar = bernoulli(-1.6 + 0.052 * antiguedad - 0.85 * (estado_i - 1.5))

out = pd.DataFrame({
    # --- entradas: las mismas del otro notebook, precio incluido -------------
    "listing_id": df.listing_id,
    "tiene_cochera": df.tiene_cochera,
    "m2": df.m2,
    "banos": df.banos,
    "ingreso_zona": df.ingreso_zona,
    "estado": df.estado,
    "tipo_vivienda": df.tipo_vivienda,
    "barrio": df.barrio,
    "codigo_postal": df.codigo_postal,
    "mes_venta": df.mes_venta,
    "anio_alta": df.anio_alta,
    "precio": df.precio,
    # --- objetivos: uno por familia de salida --------------------------------
    "dias_para_vender": dias_cargado.round().astype(np.int64),
    "dias_reales": dias.round().astype(np.int64),   # sin los errores de carga
    "visitas_semana": visitas_semana,
    "se_vendio": se_vendio,
    "segmento": segmento,
    "tiene_pileta": tiene_pileta,
    "apto_credito": apto_credito,
    "a_reciclar": a_reciclar,
})
out.to_csv("output-layer-types.csv", index=False)

print(f"{len(out)} filas -> output-layer-types.csv")
print(f"mismas casas que input-data-types.csv: "
      f"{bool((out.listing_id.to_numpy() == df.listing_id.to_numpy()).all())}\n")
print(out.head(5).to_string(index=False))
print("\n--- reparto de cada objetivo ---")
print(f"dias_para_vender   mediana {np.median(dias_cargado):.0f}   "
      f"P90 {np.quantile(dias_cargado, .9):.0f}   maximo {dias_cargado.max():.0f}   "
      f"mal cargados {typo.sum()} ({typo.mean():.1%})")
print(f"visitas_semana     media {visitas_semana.mean():.2f}   "
      f"varianza {visitas_semana.var():.2f}   maximo {visitas_semana.max()}")
print(f"se_vendio          positivos {se_vendio.mean():.1%}")
print("segmento          ", out.segmento.value_counts().to_dict())
print(f"multi-etiqueta     pileta {tiene_pileta.mean():.1%}   "
      f"credito {apto_credito.mean():.1%}   reciclar {a_reciclar.mean():.1%}")
print(f"  filas con 0/1/2/3 etiquetas: "
      f"{np.bincount(tiene_pileta + apto_credito + a_reciclar, minlength=4).tolist()}")
