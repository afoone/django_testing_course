from re import A
from this import d
from unittest import TestCase
from testing_course.calc import suma, resta, multiplicacion, division

class TestSuma(TestCase):
    """
    testing de la suma  
    """
    def test_suma_correctamente(self):
        self.assertEqual(suma(2,2), 4)
        self.assertEqual(suma(2,3), 5)

    def test_suma_cero_si_solo_hay_un_parametro(self):
        self.assertEqual(suma(2), 2)
        self.assertEqual(suma(3), 3)

    def test_falla_si_hay_un_string(self):
        self.assertRaises(TypeError, suma, "2", 3)
        self.assertRaises(TypeError, suma, 2, "hola")


class TestDivision(TestCase):
    def test_division_correctamente(self):
        self.assertEqual(division(2,2), 1)
        self.assertEqual(division(2,3), 0.6666666666666666)

    def test_division_cero_salta_error(self):
        self.assertRaises(ZeroDivisionError, division, 2, 0)

    
# class TestDimeMesActual(TestCase):
#     def test_mes_actual_correctamente(self):
#         self.assertEqual(dime_mes_actual(), "septiembre")
        

# def  dime_mes_actual():
#     return dime_mes_fecha(datetime.now())

# def dime_mes_fecha(fecha):
#     pass

      

