from src import controlador
import unittest
from unittest.mock import patch


class VistaMock:
    def __init__(self, menu_value: int):
        self.value = menu_value
        self.mostrar_error_fue_invocado = False

    def menu(self):
        return self.value

    def mostrar_error(self):
        self.mostrar_error_fue_invocado = True

class RepositorioSpy:
    def __init__(self):
        self.alta_fue_invocado = False

    def alta(self, modelo, cantidad):
        self.alta_fue_invocado = True


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