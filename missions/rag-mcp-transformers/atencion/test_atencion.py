"""Tests de la catedra para la parte 4. Uso:

    python3 test_atencion.py ruta/a/atencion.py      (sin argumento busca atencion.py al lado)

El archivo tiene que definir, con numpy y nada mas:
    softmax(M)                              softmax por fila (ultimo eje)
    atencion(Q, K, V, mascara=False)        -> (salida, A)   con A = softmax(Q K^T / sqrt(d_k))
    autoatencion(X, Wq, Wk, Wv, mascara=False) -> (salida, A)
    multicabeza(X, cabezas, Wo, mascara=False) -> salida     cabezas = lista de (Wq, Wk, Wv)
    layer_norm(x, eps=1e-5)                 normaliza cada fila a media 0 y varianza 1

Los valores esperados son los del ejemplo de la clase 8 ("the cat sat", d = 4).
"""
import importlib.util, sys, unittest
from pathlib import Path
import numpy as np

RUTA = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("atencion.py")
sys.argv = sys.argv[:1]
spec = importlib.util.spec_from_file_location("atencion", RUTA)
at = importlib.util.module_from_spec(spec); spec.loader.exec_module(at)

X = np.array([[1, 0, 1, 0], [0, 2, 0, 1], [1, 1, 1, 1]], float)
WQ = np.eye(4)
WK = np.array([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], float)
WV = np.array([[1, 0], [0, 1], [1, 0], [0, 1]], float)


class TestSoftmax(unittest.TestCase):
    def test_filas_suman_uno(self):
        M = np.array([[1.5, 0, 1.5], [3, -2, 0.5]])
        np.testing.assert_allclose(at.softmax(M).sum(-1), 1)

    def test_valor_de_la_clase(self):
        np.testing.assert_allclose(at.softmax(np.array([[1.5, 0, 1.5]])), [[0.4498, 0.1004, 0.4498]], atol=1e-3)

    def test_estable_con_numeros_grandes(self):
        s = at.softmax(np.array([[1000.0, 1000.0]]))
        self.assertTrue(np.all(np.isfinite(s)))
        np.testing.assert_allclose(s, [[0.5, 0.5]])


class TestAtencion(unittest.TestCase):
    def test_matriz_de_atencion(self):
        _, A = at.autoatencion(X, WQ, WK, WV)
        np.testing.assert_allclose(A, [[0.1220, 0.5465, 0.3315], [0.4498, 0.1004, 0.4498], [0.1863, 0.3072, 0.5065]], atol=1e-3)

    def test_salida(self):
        out, _ = at.autoatencion(X, WQ, WK, WV)
        np.testing.assert_allclose(out, [[0.9069, 2.3026], [1.7993, 1.2007], [1.3856, 1.9345]], atol=1e-3)

    def test_formas_con_n_distinto_de_d(self):
        out, A = at.autoatencion(X, WQ, WK, WV)
        self.assertEqual(A.shape, (3, 3))
        self.assertEqual(out.shape, (3, 2))

    def test_mascara_causal(self):
        out, A = at.autoatencion(X, WQ, WK, WV, mascara=True)
        np.testing.assert_allclose(np.triu(A, 1), 0, atol=1e-12)
        np.testing.assert_allclose(A.sum(-1), 1)
        np.testing.assert_allclose(out, [[2, 0], [1.6351, 0.5474], [1.3856, 1.9345]], atol=1e-3)

    def test_permutar_filas_permuta_la_salida(self):
        perm = [2, 0, 1]
        out, _ = at.autoatencion(X, WQ, WK, WV)
        out_p, _ = at.autoatencion(X[perm], WQ, WK, WV)
        np.testing.assert_allclose(out_p, out[perm], atol=1e-9)

    def test_escala_por_raiz_de_dk(self):
        Q = np.array([[1.0, 0, 0, 0]]); K = np.array([[4.0, 0, 0, 0], [0, 0, 0, 0]]); V = np.eye(2)
        _, A = at.atencion(Q, K, V)
        np.testing.assert_allclose(A, [[np.exp(2) / (np.exp(2) + 1), 1 / (np.exp(2) + 1)]], atol=1e-6)


class TestMulticabeza(unittest.TestCase):
    def test_una_cabeza_con_wo_identidad_es_autoatencion(self):
        out1, _ = at.autoatencion(X, WQ, WK, WV)
        outm = at.multicabeza(X, [(WQ, WK, WV)], np.eye(2))
        np.testing.assert_allclose(outm, out1, atol=1e-9)

    def test_dos_cabezas_concatenan_y_proyectan(self):
        c1 = (WQ[:, :2], WK[:, :2], WV[:, :1]); c2 = (WQ[:, 2:], WK[:, 2:], WV[:, 1:])
        Wo = np.array([[1.0, 2.0], [0.0, 1.0]])
        esperado = np.concatenate([at.autoatencion(X, *c1)[0], at.autoatencion(X, *c2)[0]], axis=1) @ Wo
        np.testing.assert_allclose(at.multicabeza(X, [c1, c2], Wo), esperado, atol=1e-9)
        self.assertEqual(at.multicabeza(X, [c1, c2], Wo).shape, (3, 2))


class TestLayerNorm(unittest.TestCase):
    def test_valor_de_la_clase(self):
        np.testing.assert_allclose(at.layer_norm(np.array([[2.0, 0, 1, 1]])), [[1.4142, -1.4142, 0, 0]], atol=1e-3)

    def test_invariante_a_escala_y_corrimiento(self):
        x = np.array([[2.0, 0, 1, 1]])
        np.testing.assert_allclose(at.layer_norm(2 * x), at.layer_norm(x), atol=1e-4)
        np.testing.assert_allclose(at.layer_norm(x + 10), at.layer_norm(x), atol=1e-4)

    def test_por_fila(self):
        y = at.layer_norm(np.array([[1.0, 0, 1, 0], [0, 20, 0, 10], [300, 0, 100, 200]]))
        np.testing.assert_allclose(y.mean(-1), 0, atol=1e-6)
        np.testing.assert_allclose(y.var(-1), 1, atol=1e-3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
