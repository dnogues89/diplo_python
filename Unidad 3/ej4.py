"""
Ejercicio 4
Escriba un programa que solicite la edad de la persona e imprima todos los años que la persona ha cumplido. 

"""

edad = int(input("Ingrese su edad: "))
cumpleanos = 0

while cumpleanos < edad:
    cumpleanos += 1

print(f"Usted tuvo {cumpleanos} cumpleaños")

cumpleanos = 0

for i in range(edad):
    cumpleanos += 1

print(f"Usted tuvo {cumpleanos} cumpleaños")
