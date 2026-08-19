# Cómo trabajar la misión en Google Colab

Colab ya trae instalado todo lo que hace falta (pandas, numpy, scikit-learn, TensorFlow y Keras). No hay que instalar nada ni correr `setup.sh`: ese script es solo para trabajar en tu propia máquina.

La consigna completa está en [`mission.md`](mission.md).

---

## Lo más rápido: no subir nada

Los archivos de la materia se sirven por web, así que el notebook puede leer el CSV directo desde una URL. **No hace falta subir el dataset a Colab.**

### 1. Abrir el notebook de la clase

Este link abre el notebook de la clase en Colab, sin descargarlo:

**https://colab.research.google.com/github/austral-ing-ai/talksmith-ing/blob/main/missions/clase3/house-prices.ipynb**

Apenas se abre, andá a **Archivo → Guardar una copia en Drive**. Si no lo hacés, los cambios se pierden al cerrar la pestaña.

### 2. Leer los datos desde la URL

En vez de `pd.read_csv('house-prices-extended.csv')`, poné la URL:

```python
import pandas as pd

URL = "https://austral-ing-ai.github.io/talksmith-ing/missions/clase3/house-prices-extended.csv"
df = pd.read_csv(URL)

print(df.shape)   # (1460, 20)
df.head()
```

Eso es todo. Funciona en Colab, en tu máquina y en la de quien corrija, sin que nadie tenga que tener el archivo al lado.

> El notebook de la clase usa `housepricedata.csv`, que es el dataset viejo de 10 columnas. **La misión usa `house-prices-extended.csv`**, que es el de arriba. Si copiás celdas del notebook de la clase, acordate de cambiar el archivo.

---

## Si preferís subir los archivos a mano

Sirve igual, pero tiene una trampa que conviene conocer.

### Subir el notebook

**Archivo → Subir notebook** y elegí el `.ipynb` de tu computadora.

### Subir el CSV

En el panel izquierdo, el ícono de carpeta 📁 → **Subir al almacenamiento de sesión** y elegí `house-prices-extended.csv`. Después ya podés leerlo con el nombre a secas:

```python
df = pd.read_csv("house-prices-extended.csv")
```

O desde código, que te abre el diálogo de selección:

```python
from google.colab import files
files.upload()
```

**La trampa:** ese almacenamiento es **de la sesión**, no permanente. Cuando Colab desconecta el entorno (por inactividad, o pasadas unas horas), **el archivo desaparece** y el notebook deja de correr con `FileNotFoundError`. Hay que volver a subirlo cada vez.

Por eso conviene la URL: no se borra nunca.

### Con Google Drive, si el archivo es tuyo

Si vas a trabajar con un dataset propio y no querés resubirlo, montá tu Drive:

```python
from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/MyDrive/datos/mi-archivo.csv')
```

Te va a pedir autorizar la cuenta. El archivo queda entre sesiones.

---

## Antes de entregar

La misión pide **un solo `.ipynb`, ejecutado y con las salidas a la vista**, que vuelva a correr entero con *Restart & Run All*.

1. **Verificá que corre de cero.** En Colab: **Entorno de ejecución → Reiniciar y ejecutar todo**. Si algo falla, falla ahora y no en la corrección.
2. **Cuidado con el orden de las celdas.** Colab te deja ejecutar en cualquier orden, y un notebook que anduvo salteado puede romperse al correr de arriba a abajo. El reinicio del punto 1 es lo que lo detecta.
3. **Si subiste el CSV a mano, el corrector no lo tiene.** Un notebook que lee `house-prices-extended.csv` de la sesión le va a tirar `FileNotFoundError`. Usá la URL, o dejá bien claro en una celda de markdown qué archivo hay que tener al lado.
4. **Descargalo ejecutado:** **Archivo → Descargar → Descargar .ipynb**. Las salidas viajan adentro del archivo.
5. **Nombre del archivo:** `apellido1-apellido2-...ipynb`.

## Dos cosas útiles de Colab para esta misión

- **GPU gratis:** *Entorno de ejecución → Cambiar tipo de entorno de ejecución → GPU*. Para las redes de esta misión no hace falta, son chicas y andan bien en CPU, pero acelera si hacés muchas pruebas.
- **Colab desconecta por inactividad.** Si dejás entrenando algo largo y te vas, puede cortarse. Guardá seguido en Drive.

## Trabajar en tu máquina en vez de Colab

Si preferís local, en esta carpeta hay un [`setup.sh`](setup.sh) que arma el entorno completo:

```bash
cd missions/clase3
./setup.sh
```

Crea el entorno virtual, instala las versiones fijadas en [`requirements.txt`](requirements.txt) y registra el kernel de Jupyter. Al terminar te dice cómo abrir el notebook.
