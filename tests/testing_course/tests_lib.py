from unittest import TestCase
from testing_course.lib import es_un_saludo

mockFrase1 = "hola"
mockFrase2 = "adios"
mockFrase3 = "hola adios"
mockFrase4 = "este tiene que fallar"
mockFrase5 = "lkdsafjlkdsajflkdsfja"


class TestSaludo(TestCase):
    def tests_funciona_correctamente(self):
        self.assertTrue(es_un_saludo(mockFrase1))
        self.assertTrue(es_un_saludo(mockFrase2))
        # self.assertTrue(es_un_saludo(mockFrase3))
        self.assertFalse(es_un_saludo(mockFrase4))
        self.assertFalse(es_un_saludo(mockFrase5))