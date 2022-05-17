"""
Ejercicio 5
Suponga que tiene una verdulería y carga la cantidad y el precio de lo comprado por un cliente. Realice un programa que tome de a uno la cantidad y el precio comprado por el cliente y al finalizar la compra retorne el monto total gastado. 

"""

cantidad = int(input("Coloque cuanta cantidad de verdura esta comprando: "))

monto = int(input("Coloque el precio por unidad: "))

precio_total = 0

for i in range(cantidad):
    precio_total += monto

print(f"El monto total a pagar es {precio_total}")

precio_total = 0
veces = 0
while veces < cantidad:
    precio_total += monto
    veces += 1

print(f"El monto total a pagar es {precio_total}")
