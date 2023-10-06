import probabilidadsislineal as probabilidad
import unittest

class TestCibreriaComplejos(unittest.TestCase):
    def test_probabilidad(self):
        v=probabilidad.proba([3+5j, 6+3j, 1+0j], 1)
        self.assertAlmostEqual(v, 0.5625)
        v1=probabilidad.proba([2+1j, -3j, 4], 1)
        self.assertAlmostEqual(v1, 0.3)
    def test_transicion(self):
        v=probabilidad.transicion([3+5j, 6+3j, 1+0j], [2+1j, -3j, 4])
        self.assertAlmostEqual(v, 0.12247448713915893+0.5103103630798287j)
        v1=probabilidad.transicion([2+1j, -3j, 4], [3+5j, 6+3j, 1+0j])
        self.assertAlmostEqual(v1, 0.12247448713915893-0.5103103630798287j)
    def test_probabilidad_transicion(self):
        v=probabilidad.probabilidadtrans([3+5j, 6+3j, 1+0j], [2+1j, -3j, 4])
        self.assertAlmostEqual(v, 0.2754166666666666)
        v1=probabilidad.probabilidadtrans([1+1j, 3-3j, 2+6j], [2+1j, 3-5j, 2+3j])
        self.assertAlmostEqual(v1, 0.8237179487179488)
    def test_media_y_varianza(self):
        v=probabilidad.hervarmed([[2, 1+3j],[1-3j, 4]], [1,0])
        self.assertAlmostEqual(v, (2.0, 10.0))
        v1=probabilidad.hervarmed([[9, 0+8j],[1-3j, 4]], [0,1])
        self.assertAlmostEqual(v1, "Matriz no hermitiana")
    
if __name__ == '__main__':
    unittest.main()
