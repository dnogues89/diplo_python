"""
Ejercicio 7
A partir del ejercicio 5 cree un programa que vaya agregando en un diccionario las compras realizadas.

"""
dicc_compra = {}
precio_total = 0
contador = 0
x = "si"


def carrito():
    verdura = input("Ingrese lo que esta comprando: ")

    cantidad = int(input("Coloque cuanta cantidad de verdura esta comprando: "))

    monto = int(input("Coloque el precio por unidad: "))

    precio_total = 0

    for i in range(cantidad):
        precio_total += monto

    compra = {"Item": verdura, "Cantidad": cantidad, "Costo": precio_total}
    return compra


while x.lower() == "si":
    contador += 1
    dicc_compra[contador] = carrito()

    x = input("Quisiera agregar compra (escriba si o no): ")

print(dicc_compra)
