#!/usr/bin/env python3
"""Genera `output-layer-types.csv`, el dataset del notebook de la capa de salida.

El universo es el mismo de `input-data-types.csv` — casas — pero acá lo que varía
no es cómo entra el dato sino **qué se predice**: una columna objetivo por cada
familia de salida que la clase recorre.

Todo es sintético y con semilla fija: cada objetivo se arma con una regla explícita
más ruido, así cada sección del notebook sabe cuál es su piso de error y se puede
decir con honestidad cuándo un modelo recuperó todo lo que había para recuperar.

    python3 output-layer-types-gen.py
"""
import numpy as np
import pandas as pd

RNG = np.random.default_rng(42)
N = 2000

# --- Las variables de entrada, compartidas por todas las secciones ------------
# Se eligieron ya listas para entrar a una red: numéricas con magnitud y dos
# categóricas de cardinalidad baja. La codificación de la entrada es el tema del
# OTRO notebook; acá tiene que estar resuelta para no distraer.
m2 = RNG.integers(35, 260, N).astype(float)
banos = RNG.integers(1, 5, N).astype(float)
antiguedad = RNG.integers(0, 60, N).astype(float)
ingreso_zona = RNG.lognormal(11.4, 0.45, N).round()

ESTADOS = ["regular", "bueno", "muy bueno", "excelente"]
estado_i = RNG.integers(0, 4, N)
estado = np.array(ESTADOS)[estado_i]

BARRIOS = ["centro", "norte", "sur", "costa", "parque", "industrial"]
barrio_i = RNG.integers(0, 6, N)
barrio = np.array(BARRIOS)[barrio_i]
# Cuánto suma cada barrio al precio, en miles. No es lineal en el índice: el
# índice del barrio no significa nada, y eso tiene que verse en los números.
BARRIO_K = np.array([95.0, 120.0, 40.0, 150.0, 70.0, 10.0])

# Señal de precio "limpia", en miles de dólares.
precio_k = (
    1.85 * m2
    + 22.0 * banos
    - 1.1 * antiguedad
    + 0.00042 * ingreso_zona
    + np.array([0.0, 28.0, 52.0, 88.0])[estado_i]
    + BARRIO_K[barrio_i]
    + 40.0
)

# --- 1 · Regresión de un valor -----------------------------------------------
# Ruido homocedástico de $12.000, MÁS un 1,5% de precios con un cero de más:
# el error de carga que hace la diferencia entre MSE y Huber. Es el argumento
# de la clase, así que el dataset tiene que contenerlo de verdad.
precio = precio_k * 1000 + RNG.normal(0, 12_000, N)
typo = RNG.random(N) < 0.015
precio[typo] *= 10
precio = precio.round()

# --- 2 · Conteo ---------------------------------------------------------------
# Visitas en la primera semana. Poisson de verdad: la varianza crece con la
# media, que es exactamente lo que MSE con salida lineal no puede representar.
lam_visitas = np.exp(0.55 + 0.0075 * m2 - 0.010 * antiguedad + 0.45 * (estado_i / 3))
visitas_semana = RNG.poisson(lam_visitas)

# --- 3 · Binaria --------------------------------------------------------------
# ¿Se vendió en los primeros 60 días? Probabilidad logística sobre la señal.
z_vendio = (
    -1.35
    + 0.020 * (100 - antiguedad)
    + 0.55 * (estado_i - 1.5)
    - 0.0000021 * precio_k * 1000
    + 0.30 * (barrio_i == 3)          # la costa se vende sola
)
p_vendio = 1 / (1 + np.exp(-z_vendio))
se_vendio = (RNG.random(N) < p_vendio).astype(int)

# --- 4 · Multiclase excluyente ------------------------------------------------
# Segmento comercial. Tres clases que NO se solapan: una casa cae en una sola.
# Los cortes son por cuantil, así las tres quedan pobladas.
q1, q2 = np.quantile(precio_k, [0.40, 0.80])
segmento = np.where(precio_k < q1, "economica",
           np.where(precio_k < q2, "media", "premium"))

# --- 5 · Multi-etiqueta -------------------------------------------------------
# Tres atributos que pueden darse juntos, o ninguno. Es el caso del ticket que
# es urgente Y de facturación: forzarlos a competir sería un error de modelado.
p_pileta = 1 / (1 + np.exp(-(-2.6 + 0.016 * m2 + 0.9 * (barrio_i == 3))))
p_credito = 1 / (1 + np.exp(-(1.9 - 0.045 * antiguedad + 0.5 * (estado_i - 1.5))))
p_reciclar = 1 / (1 + np.exp(-(-1.7 + 0.055 * antiguedad - 0.8 * (estado_i - 1.5))))
tiene_pileta = (RNG.random(N) < p_pileta).astype(int)
apto_credito = (RNG.random(N) < p_credito).astype(int)
a_reciclar = (RNG.random(N) < p_reciclar).astype(int)

# --- 6 y 7 · Cuantiles y distribución ----------------------------------------
# Días hasta vender. Asimétrico a la derecha y **heterocedástico**: cuanto más
# cara la casa, más incierta la espera. Un solo número no responde la pregunta
# del negocio ("¿cuánto tardo en el peor caso?"), y una σ constante miente.
mu_dias = 34 - 14 * p_vendio + 0.045 * precio_k * 0.1
sigma_dias = 6 + 0.055 * precio_k          # la incertidumbre crece con el precio
dias_para_vender = np.clip(
    RNG.normal(mu_dias, sigma_dias) + RNG.exponential(6, N), 1, None).round()

df = pd.DataFrame({
    "listing_id": RNG.permutation(np.arange(100_000, 100_000 + N)),
    "m2": m2.astype(int),
    "banos": banos.astype(int),
    "antiguedad": antiguedad.astype(int),
    "ingreso_zona": ingreso_zona.astype(int),
    "estado": estado,
    "barrio": barrio,
    "precio": precio.astype(np.int64),
    "visitas_semana": visitas_semana,
    "se_vendio": se_vendio,
    "segmento": segmento,
    "tiene_pileta": tiene_pileta,
    "apto_credito": apto_credito,
    "a_reciclar": a_reciclar,
    "dias_para_vender": dias_para_vender.astype(int),
})

df.to_csv("output-layer-types.csv", index=False)

print(f"{len(df)} filas -> output-layer-types.csv\n")
print(df.head(5).to_string(index=False))
print("\n--- reparto de cada objetivo ---")
print(f"precio                mediana ${np.median(precio):,.0f}   "
      f"con un cero de mas: {typo.sum()} filas ({typo.mean():.1%})")
print(f"visitas_semana        media {visitas_semana.mean():.2f}   "
      f"varianza {visitas_semana.var():.2f}   maximo {visitas_semana.max()}")
print(f"se_vendio             positivos {se_vendio.mean():.1%}")
print("segmento             ", df.segmento.value_counts().to_dict())
print(f"multi-etiqueta        pileta {tiene_pileta.mean():.1%}   "
      f"credito {apto_credito.mean():.1%}   reciclar {a_reciclar.mean():.1%}")
print(f"  filas con 0 / 1 / 2 / 3 etiquetas: "
      f"{np.bincount(tiene_pileta + apto_credito + a_reciclar, minlength=4).tolist()}")
print(f"dias_para_vender      mediana {np.median(dias_para_vender):.0f}   "
      f"P90 {np.quantile(dias_para_vender, .9):.0f}   maximo {dias_para_vender.max():.0f}")
