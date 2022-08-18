from vista import Visual
from modelo import Repositorio
import re


class Aplicacion:
    def run(self):
        patron = "[0-9]+"
        opcion = Visual.menu()
        if re.match(patron, str(opcion)):

            if opcion == 1:
                modelo, cantidad = input(
                    "Ingresar Modelo y cantidad (Separado con un Espacio): "
                ).split(" ")
                Repositorio.alta(modelo, int(cantidad))
                return True

            if opcion == 2:
                lista = Repositorio.consulta()
                Visual.lista(lista)
                id = int(input("Ingresar el ID del producto a eliminar. "))
                Repositorio.baja(id)
                return True

            if opcion == 3:
                lista = Repositorio.consulta()
                Visual.lista(lista)
                return True

            if opcion == 4:
                lista = Repositorio.consulta()
                Visual.lista(lista)
                id, modelo, cantidad = input(
                    "Ingresar ID a moificar Modelo y cantidad (Separado con un Espacio): "
                ).split(" ")
                Repositorio.modificar(int(id), modelo, int(cantidad))
                print("Modificacion realizada con exito")
                lista = Repositorio.consulta()
                Visual.lista(lista)
                return True

            if opcion == 5:
                Visual.exit()
                return False

        print("El numero ingresado es incorrecto")
        return True


if __name__ == "__main__":
    mi_app = Aplicacion()
    while mi_app.run():
        pass
