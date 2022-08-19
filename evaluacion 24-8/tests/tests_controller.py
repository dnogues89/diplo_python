from pydoc import visiblename
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
        self.assertTrue(app.run())
        self.assertTrue(repositorio.alta_fue_invocado)

    @patch('builtins.input', lambda *args: 'abcde hola_dami')
    def test_option1_al_agregar_mal_el_modelo_y_o_cantidad_deberia_avisar_a_vista_que_hubo_error(self):
        repositorio = RepositorioSpy()
        vista_que_retorna_opcion_1 = VistaMock(menu_value=1)
        app = controlador.Aplicacion(visual=vista_que_retorna_opcion_1, repositorio=repositorio)
        self.assertTrue(app.run())
        self.assertTrue(vista_que_retorna_opcion_1.mostrar_error_fue_invocado)

    @patch('builtins.input', lambda *args: '1')
    def test_option2_devuelve_toda_la_informacion_de_base_de_datos_a_la_vista(self):
        visual = VistaMock(menu_value=2)
        repositorio = RepositorioMock()
        app = controlador.Aplicacion(visual=visual, repositorio=repositorio)
        self.assertTrue(app.run())
        self.assertTrue(visual.lista_fue_invocado)

    @patch('builtins.input', lambda *args: '1') # Id ingresado es '1'
    def test_option2_le_envia_a_dar_de_baja_al_repositorio_en_base_al_id_ingresado(self):
        visual = VistaMock(menu_value=2)
        repositorio = RepositorioMock()
        app = controlador.Aplicacion(visual=visual, repositorio=repositorio)
        self.assertTrue(app.run())
        self.assertTrue(repositorio.baja_fue_invocado)

    def test_option3_devuelve_toda_la_informacion_de_base_de_datos_a_la_vista(self):
        visual = VistaMock(menu_value=3)
        data_de_stock = [1, "abc", 123]
        repositorio = RepositorioMock(stubbed_data=data_de_stock)
        app = controlador.Aplicacion(visual=visual, repositorio=repositorio)
        self.assertTrue(app.run())
        self.assertTrue(visual.lista_fue_invocado)
        self.assertEqual(visual.lista_lista_recibida, data_de_stock)
        

    def test_option5_devuelve_false_y_le_avisa_a_la_vista_su_salida(self):
        vista = VistaMock(menu_value=5)
        app = controlador.Aplicacion(visual=vista, repositorio=RepositorioMock())
        self.assertFalse(app.run())
        self.assertTrue(vista.exit_fue_invocado)