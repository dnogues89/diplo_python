from src.controlador import Aplicacion
from src.vista import Visual
from src.modelo import Repositorio

mi_app = Aplicacion(visual=Visual(), repositorio=Repositorio())
while mi_app.run():
    pass