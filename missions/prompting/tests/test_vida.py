#!/usr/bin/env python3
"""Tests de la mision de prompting: el juego de la vida de Conway.

Uso:

    python3 test_vida.py [ruta/a/vida.py]

Sin argumento, busca `vida.py` en el mismo directorio que este test. El
script del alumno tiene que respetar la interfaz estandar del contrato,
que es lo que estos tests invocan.

Contrato que verifica (el mismo que esta en mission.md):
- Uso: python3 vida.py <archivo_estado_inicial> <generaciones>
- El archivo de estado es una grilla rectangular de lineas con '#' (celula
  viva) y '.' (celula muerta).
- El mundo es finito, del tamano de la grilla: fuera de los bordes todo
  esta muerto. Sin wrap-around.
- El script imprime por stdout la grilla resultante tras N generaciones,
  en el mismo formato, una linea por fila.
- Con generaciones = 0 imprime el estado inicial tal cual.
"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
    SCRIPT = Path(sys.argv.pop(1)).resolve()
else:
    SCRIPT = Path(__file__).resolve().parent / "vida.py"


def correr(estado: str, generaciones: int) -> str:
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
        f.write(estado)
        ruta = f.name
    r = subprocess.run(
        [sys.executable, str(SCRIPT), ruta, str(generaciones)],
        capture_output=True, text=True, timeout=30,
    )
    if r.returncode != 0:
        raise AssertionError(f"vida.py termino con error:\n{r.stderr}")
    return r.stdout.rstrip("\n")


class TestVida(unittest.TestCase):

    def test_generacion_cero_devuelve_el_estado_inicial(self):
        estado = ".....\n..#..\n..#..\n..#..\n....."
        self.assertEqual(correr(estado, 0), estado)

    def test_blinker_oscila_de_vertical_a_horizontal(self):
        vertical = ".....\n..#..\n..#..\n..#..\n....."
        horizontal = ".....\n.....\n.###.\n.....\n....."
        self.assertEqual(correr(vertical, 1), horizontal)

    def test_blinker_vuelve_al_original_en_dos_generaciones(self):
        vertical = ".....\n..#..\n..#..\n..#..\n....."
        self.assertEqual(correr(vertical, 2), vertical)

    def test_bloque_es_naturaleza_muerta(self):
        bloque = "....\n.##.\n.##.\n...."
        self.assertEqual(correr(bloque, 5), bloque)

    def test_celula_sola_muere_por_soledad(self):
        estado = "...\n.#.\n..."
        self.assertEqual(correr(estado, 1), "...\n...\n...")

    def test_grilla_vacia_sigue_vacia(self):
        estado = "....\n....\n....\n...."
        self.assertEqual(correr(estado, 3), estado)

    def test_glider_se_desplaza_una_diagonal_en_cuatro_generaciones(self):
        inicial = (
            ".#........\n"
            "..#.......\n"
            "###.......\n"
            "..........\n"
            "..........\n"
            "..........\n"
            "..........\n"
            "..........\n"
            "..........\n"
            ".........."
        )
        esperado = (
            "..........\n"
            "..#.......\n"
            "...#......\n"
            ".###......\n"
            "..........\n"
            "..........\n"
            "..........\n"
            "..........\n"
            "..........\n"
            ".........."
        )
        self.assertEqual(correr(inicial, 4), esperado)

    def test_nacimiento_por_tres_vecinas(self):
        estado = "....\n.##.\n.#..\n...."
        esperado = "....\n.##.\n.##.\n...."
        self.assertEqual(correr(estado, 1), esperado)

    def test_borde_sin_wrap(self):
        # Un blinker pegado al borde superior: las celulas de "afuera" estan
        # muertas, asi que el comportamiento cambia respecto de un mundo con wrap.
        estado = "###\n...\n..."
        esperado = ".#.\n.#.\n..."
        self.assertEqual(correr(estado, 1), esperado)


if __name__ == "__main__":
    if not SCRIPT.exists():
        print(f"No encuentro {SCRIPT}. Pasen la ruta: python3 test_vida.py ruta/a/vida.py")
        sys.exit(2)
    unittest.main(verbosity=2)
