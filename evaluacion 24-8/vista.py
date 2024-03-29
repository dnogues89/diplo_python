class Visual:
    def menu():
        print("\n\n")
        print("#" * 20 + " MENU " + "#" * 20)
        print("1 - Cargar Producto")
        print("2 - Eliminar Producto")
        print("3 - Consultar Producto")
        print("4 - Modificar Producto")
        print("5 - Finalizar")
        print("#" * 20 + " MENU " + "#" * 20)
        opcion = input("Coloque la opcion deseada: ")
        print("\n\n")
        return int(opcion)

    def lista(lista):
        print("\n\n")
        print("*" * 20 + "  -BASE DE DATOS-  " + "*" * 20)
        print("{:<8} {:<15} {:<10}".format("Id", "Modelo", "Cantidad"))
        for i in lista:
            id, modelo, cantidad = i
            print("{:<8} {:<15} {:<10}".format(id, modelo, cantidad))
        print("*" * 20 + "  -BASE DE DATOS-  " + "*" * 20)
        print("\n\n")

    def exit():
        print("Cerrando APP")
        print("BYE")


if __name__ == "__main__":
    pass
