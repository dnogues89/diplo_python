from distutils.core import setup
from pydoc import visiblename
import unittest
from unittest.mock import patch

from src import controlador
from src.modelo import Repositorio
from src.vista import Visual
from .doubles import *

class TestController(unittest.TestCase):
    def setUp(self):
        self.app = None
        self.repositorio = None
        self.vista = None

    def dada_una_aplicacion(self, menu_value: int, repositorio = RepositorioMock()):
        self.vista = VistaMock(menu_value=menu_value)
        self.repositorio = repositorio
        self.app = controlador.Aplicacion(visual=self.vista, repositorio=self.repositorio)

    @patch('builtins.input', lambda *args: 'abcde 123')
    def test_option1_al_agregar_modelo_y_cantidad_se_da__de_alta_en_repositorio(self):
        self.dada_una_aplicacion(menu_value=1)
        self.assertTrue(self.app.run())
        self.assertTrue(self.repositorio.alta_fue_invocado)

    @patch('builtins.input', lambda *args: 'abcde hola_dami')
    def test_option1_al_agregar_mal_el_modelo_y_o_cantidad_deberia_avisar_a_vista_que_hubo_error(self):
        self.dada_una_aplicacion(menu_value=1)
        self.assertTrue(self.app.run())
        self.assertTrue(self.vista.mostrar_error_fue_invocado)

    @patch('builtins.input', lambda *args: '1')
    def test_option2_devuelve_toda_la_informacion_de_base_de_datos_a_la_vista(self):
        self.dada_una_aplicacion(menu_value=2)
        self.assertTrue(self.app.run())
        self.assertTrue(self.vista.lista_fue_invocado)

    @patch('builtins.input', lambda *args: '1') # Id ingresado es '1'
    def test_option2_le_envia_a_dar_de_baja_al_repositorio_en_base_al_id_ingresado(self):
        self.dada_una_aplicacion(menu_value=2)
        self.assertTrue(self.app.run())
        self.assertTrue(self.repositorio.baja_fue_invocado)

    def test_option3_devuelve_toda_la_informacion_de_base_de_datos_a_la_vista(self):
        data_de_stock = [1, "abc", 123]
        repositorio = RepositorioMock(stubbed_data=data_de_stock)
        self.dada_una_aplicacion(menu_value=3, repositorio=repositorio)
        self.assertTrue(self.app.run())
        self.assertTrue(self.vista.lista_fue_invocado)
        self.assertEqual(self.vista.lista_lista_recibida, data_de_stock)
    
    @patch('builtins.input', lambda *args: '1 ABC 123')
    def test_option4_devuelve_toda_la_informacion_de_base_de_datos_a_la_vista_dos_veces(self):
        self.dada_una_aplicacion(menu_value=4)
        self.assertTrue(self.app.run())
        self.assertTrue(self.vista.lista_fue_invocado)
        self.assertEqual(self.vista.lista_fue_invocado_veces, 2)
    
    @patch('builtins.input', lambda *args: '1 ABC 123')
    def test_option4_al_ingresar_id_modelo_cantidad_se_modifica_en_repositorio(self):
        self.dada_una_aplicacion(menu_value=4)
        self.assertTrue(self.app.run())
        self.assertTrue(self.repositorio.modificar_fue_invocado)

    @patch('builtins.input', lambda *args: '1')
    def test_option4_al_ingresar_mal_la_info_de_stock_deberia_avisar_a_la_vista_que_hubo_error(self):
        self.dada_una_aplicacion(menu_value=4)
        self.assertTrue(self.app.run())
        self.assertTrue(self.vista.mostrar_error_fue_invocado)

    def test_option5_devuelve_false_y_le_avisa_a_la_vista_su_salida(self):
        self.dada_una_aplicacion(menu_value=5)
        self.assertFalse(self.app.run())
        self.assertTrue(self.vista.exit_fue_invocado)