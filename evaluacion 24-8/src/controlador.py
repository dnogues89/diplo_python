from multiprocessing.sharedctypes import Value
from .vista import Visual
from .modelo import Repositorio
import re


class Aplicacion:
    def __init__(self, visual: Visual, repositorio: Repositorio):
        self.vista = visual
        self.repositorio = repositorio

    def run(self):
        patron = "[0-9]+"
        opcion = self.vista.menu()
        if re.match(patron, str(opcion)):
            if opcion == 1:
                self._dar_de_alta()

            if opcion == 2:
                self._dar_de_baja()

            if opcion == 3:
                self._mostrar_stock_completo()
                return True

            if opcion == 4:
                return self._modificar_stock()

            if opcion == 5:
                return self._exit()

        print("El numero ingresado es incorrecto")
        return True

    def _dar_de_alta(self):
        try:
            modelo, cantidad = input(
                "Ingresar Modelo y cantidad (Separado con un Espacio): "
            ).split(" ")    
            self.repositorio.alta(modelo, int(cantidad))
        except ValueError:
            self.vista.mostrar_error()
        return True

    def _dar_de_baja(self):
        self._mostrar_stock_completo()
        id = int(input("Ingresar el ID del producto a eliminar. "))
        self.repositorio.baja(id)
        return True

    def _modificar_stock(self):
        self._mostrar_stock_completo()
        try:
            id, modelo, cantidad = input(
                "Ingresar ID a moificar Modelo y cantidad (Separado con un Espacio): "
            ).split(" ")
            self.repositorio.modificar(int(id), modelo, int(cantidad))
            print("Modificacion realizada con exito")
            self._mostrar_stock_completo()
        except ValueError:
            self.vista.mostrar_error()
        return True

    def _exit(self):
        self.vista.exit()
        return False
    
    def _mostrar_stock_completo(self):
        lista = self.repositorio.consulta()
        self.vista.lista(lista)


if __name__ == "__main__":
    mi_app = Aplicacion()
    while mi_app.run():
        pass
