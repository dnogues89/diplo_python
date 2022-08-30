import os
import subprocess


class Visual:
    def menu(self):
        print("\n\n")
        print("#" * 20 + " MENU " + "#" * 20)
        print("1 - Cargar Producto")
        print("2 - Eliminar Producto")
        print("3 - Consultar Producto")
        print("4 - Modificar Producto")
        print("5 - Finalizar")
        print("#" * 20 + " MENU " + "#" * 20)
        opcion = self.input_data_msg("Coloque la opcion deseada: ")
        print("\n\n")
        return int(opcion)

    def lista(self, lista):
        print("\n\n")
        print("*" * 20 + "  -BASE DE DATOS-  " + "*" * 20)
        print("{:<8} {:<15} {:<10}".format("Id", "Modelo", "Cantidad"))
        for i in lista:
            id, modelo, cantidad = i
            print("{:<8} {:<15} {:<10}".format(id, modelo, cantidad))
        print("*" * 20 + "  -BASE DE DATOS-  " + "*" * 20)
        print("\n\n")

    def exit(self):
        print("Cerrando APP")
        print("BYE")

    def mostrar_error(self):
        os.system("clear")
        print("Hubo un problema en el ingreso de datos")

    def input_data_msg(self, msg: str):
        return input(msg)

    def limpiar_consola(self):
        subprocess.run("clear")


if __name__ == "__main__":
    pass
