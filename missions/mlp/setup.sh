#!/usr/bin/env bash
# Arma el entorno para el notebook de la clase 3 y para la misión.
#
#   cd missions/mlp && ./setup.sh
#
# Qué hace:
#   1. Crea el entorno virtual .venv si no existe.
#   2. Instala las dependencias de requirements.txt.
#   3. Registra el kernel de Jupyter con un nombre propio, mlp-venv.
#   4. Verifica que los imports del notebook funcionen.
#
# Es idempotente: correrlo dos veces no rompe nada.

set -euo pipefail

cd "$(dirname "$0")"
VENV=".venv"
KERNEL_NAME="mlp-venv"
KERNEL_LABEL="Python (mlp .venv)"

# --- 1. el intérprete base --------------------------------------------------
# Se necesita Python 3.10 o superior. El de macOS (/usr/bin/python3, 3.9) no sirve
# para estas versiones de TensorFlow.
find_python() {
  for c in python3.13 python3.12 python3.11 python3.10 python3; do
    if command -v "$c" >/dev/null 2>&1; then
      if "$c" -c 'import sys; sys.exit(0 if sys.version_info >= (3,10) else 1)' 2>/dev/null; then
        echo "$c"; return 0
      fi
    fi
  done
  return 1
}

if [ ! -d "$VENV" ]; then
  PY="$(find_python)" || {
    echo "ERROR: no encontré Python 3.10 o superior." >&2
    echo "       En macOS: brew install python@3.12" >&2
    exit 1
  }
  echo "==> Creando el entorno virtual con $($PY --version)"
  "$PY" -m venv "$VENV"
else
  echo "==> El entorno virtual ya existe ($("$VENV/bin/python" --version))"
fi

PYBIN="$VENV/bin/python"

# --- 2. dependencias --------------------------------------------------------
echo "==> Instalando dependencias (puede tardar varios minutos la primera vez)"
"$PYBIN" -m pip install --quiet --upgrade pip
"$PYBIN" -m pip install --quiet -r requirements.txt

# --- 3. kernel de Jupyter con nombre propio ---------------------------------
# Sin esto el kernel queda registrado como "python3" y choca con el Python del
# sistema: el notebook se reengancha al intérprete equivocado y falla con
# ModuleNotFoundError aunque todo esté instalado acá.
echo "==> Registrando el kernel de Jupyter como '$KERNEL_NAME'"
"$PYBIN" -m ipykernel install --user --name "$KERNEL_NAME" --display-name "$KERNEL_LABEL" >/dev/null

# --- 4. verificación --------------------------------------------------------
echo "==> Verificando los imports del notebook"
"$PYBIN" - <<'PYCHECK'
import sys
mods = ["pandas", "numpy", "matplotlib", "sklearn", "keras", "tensorflow"]
falla = False
for m in mods:
    try:
        mod = __import__(m)
        print("    ok     %-12s %s" % (m, getattr(mod, "__version__", "?")))
    except Exception as e:
        print("    FALLA  %-12s %s" % (m, e)); falla = True
sys.exit(1 if falla else 0)
PYCHECK

cat <<MSG

Listo. Hay dos formas de abrir el notebook.

1) VS Code
   Abrí house-prices.ipynb y elegí el kernel "$KERNEL_LABEL",
   arriba a la derecha. El archivo ya viene apuntado a ese kernel, así que lo
   normal es que lo tome solo.

2) Jupyter en el navegador
   Desde esta carpeta:

       .venv/bin/jupyter lab

   Ojo: tiene que ser el jupyter del entorno, con esa ruta o después de
   activarlo con "source .venv/bin/activate". Un jupyter de afuera no ve
   estas dependencias.

Si aparece "ModuleNotFoundError: No module named 'pandas'", no falta nada
instalado: el notebook se enganchó al Python del sistema, que no tiene los
paquetes. Volvé a elegir el kernel "$KERNEL_LABEL" y listo.
MSG
