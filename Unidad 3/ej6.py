"""
Ejercicio 6
A partir del ejercicio 5 cree un programa que vaya agregando en una lista las compras realizadas.

"""
lista_compra = []
precio_total = 0
x = "si"


def carrito(lista_compra):
    verdura = input("Ingrese lo que esta comprando: ")

    cantidad = int(input("Coloque cuanta cantidad de verdura esta comprando: "))

    monto = int(input("Coloque el precio por unidad: "))

    precio_total = 0

    for i in range(cantidad):
        precio_total += monto

    lista_compra += [verdura, cantidad, precio_total]


while x.lower() == "si":
    carrito(lista_compra)
    x = input("Quisiera agregar compra (escriba si o no): ")

print(lista_compra)
