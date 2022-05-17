"""

Ejercicio9
A partir del ejerció 7 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada
Pregunta: Considera que es más fácil guardar la información en listas o en diccionarios


"""
"""
Ejercicio8
A partir del ejerció 6 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada

"""


def alta(producto):
    compra[producto] = {
        "Item": input("Ingrese el producto: "),
        "Cantidad": int(input("Ingrese la cantidad: ")),
    }
    return


def baja(item):
    compra.pop(item)
    return


def consulta():
    if len(compra) == 0:
        print("El carrito esta vacio")
    else:
        print(compra)
    return


def modificar(item):
    compra[item] = {
        "Item": input("Ingrese el producto: "),
        "Cantidad": int(input("Ingrese la cantidad: ")),
    }
    return


compra = {}
producto = 0


while True:
    opcion = int(
        input(
            "Seleccione la opcion deseada\n1 Consulta de pedido\n2 Modificar pedido\n3 Nuevo Pedido\n4 Eliminar Pedido\n5 Finalizar\n"
        )
    )

    if opcion == 1:
        consulta()

    if opcion == 2:
        item = int(input("Indique el Item a modificar "))
        modificar(item)

    if opcion == 3:
        producto += 1
        alta(producto)

    if opcion == 4:
        item = int(input("Indique item a eliminar: "))
        baja(item)

    if opcion == 5:
        break
