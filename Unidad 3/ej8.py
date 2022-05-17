"""
Ejercicio8
A partir del ejerció 6 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada

"""
compra = []


def alta():
    item = input("Ingrese el producto: ")
    cantidad = int(input("Ingrese la cantidad: "))

    return item, cantidad


def baja(ind):
    compra.pop(ind)
    return


def consulta(compra):
    if len(compra) == 0:
        print("El carrito esta vacio")
    else:
        for i in compra:
            print(compra.index(i), i)
    return


def modificar(ind):
    compra.pop(ind)

    return alta()


producto = 0
corriendo_scrip = "si"

while corriendo_scrip == "si":
    opcion = int(
        input(
            "\n\nSeleccione la opcion deseada\n1 Consulta de pedido\n2 Modificar pedido\n3 Nuevo Pedido\n4 Eliminar Pedido\n5 Finalizar\n\nOpcion: "
        )
    )

    if opcion == 1:
        consulta(compra)

    if opcion == 2:
        ind = int(input("Indique el Item a modificar "))
        modificar(ind)
        if len(compra) == 0:
            compra = [alta()]
        else:
            compra = [[compra], [alta()]]

    if opcion == 3:
        if len(compra) == 0:
            compra = [alta()]
        else:
            compra = [[compra], [alta()]]

    if opcion == 4:
        ind = int(input("Indique item a eliminar: "))
        baja(ind)

    if opcion == 5:
        break
