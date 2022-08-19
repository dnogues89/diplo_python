import unittest
from unittest.mock import patch

from src import controlador
from src.vista import Visual
from .doubles import *

class TestController(unittest.TestCase):
    @patch('builtins.input', lambda *args: 'abcde 123')
    def test_option1_al_agregar_modelo_y_cantidad_se_da__de_alta_en_repositorio(self):
        repositorio = RepositorioSpy()
        vista_que_retorna_opcion_1 = VistaMock(menu_value=1)
        app = controlador.Aplicacion(visual=vista_que_retorna_opcion_1, repositorio=repositorio)
        return_value = app.run()
        self.assertTrue(repositorio.alta_fue_invocado)
        self.assertTrue(return_value)

    @patch('builtins.input', lambda *args: 'abcde hola_dami')
    def test_option1_al_agregar_mal_el_modelo_y_o_cantidad_deberia_avisar_a_vista_que_hubo_error(self):
        repositorio = RepositorioSpy()
        vista_que_retorna_opcion_1 = VistaMock(menu_value=1)
        app = controlador.Aplicacion(visual=vista_que_retorna_opcion_1, repositorio=repositorio)
        return_value = app.run()
        self.assertTrue(return_value)
        self.assertTrue(vista_que_retorna_opcion_1.mostrar_error_fue_invocado)

    def test_option3_devuelve_toda_la_informacion_de_base_de_datos_a_la_vista(self):
        visual = VistaMock(menu_value=3)
        data_de_stock = [1, "abc", 123]
        repositorio = RepositorioMock(stubbed_data=data_de_stock)
        app = controlador.Aplicacion(visual=visual, repositorio=repositorio)
        return_value = app.run()
        self.assertTrue(visual.lista_fue_invocado)
        self.assertEqual(visual.lista_lista_recibida, data_de_stock)
        self.assertTrue(return_value)
