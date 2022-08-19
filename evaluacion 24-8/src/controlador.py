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
                try:
                    modelo, cantidad = input(
                        "Ingresar Modelo y cantidad (Separado con un Espacio): "
                    ).split(" ")    
                    self.repositorio.alta(modelo, int(cantidad))
                except ValueError:
                    self.vista.mostrar_error()
                return True

            if opcion == 2:
                self._mostrar_stock_completo()
                id = int(input("Ingresar el ID del producto a eliminar. "))
                self.repositorio.baja(id)
                return True

            if opcion == 3:
                self._mostrar_stock_completo()
                return True

            if opcion == 4:
                lista = self.repositorio.consulta()
                self.vista.lista(lista)
                id, modelo, cantidad = input(
                    "Ingresar ID a moificar Modelo y cantidad (Separado con un Espacio): "
                ).split(" ")
                self.repositorio.modificar(int(id), modelo, int(cantidad))
                print("Modificacion realizada con exito")
                lista = self.repositorio.consulta()
                self.vista.lista(lista)
                return True

            if opcion == 5:
                self.vista.exit()
                return False

        print("El numero ingresado es incorrecto")
        return True
    
    def _mostrar_stock_completo(self):
        lista = self.repositorio.consulta()
        self.vista.lista(lista)


if __name__ == "__main__":
    mi_app = Aplicacion()
    while mi_app.run():
        pass
