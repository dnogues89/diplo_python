"""
Ejercicio 1 (Este es el ejercicio 2 de la unidad 1 pero implementando if/else):
Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si son múltiplos de dos. Utilice la estructura if/else

"""


import sys

if int(sys.argv[1]) % 2 == 0:
    print("El numero ", sys.argv[1], " es par")
else:
    print("El numero ", sys.argv[1], " es impar")

if int(sys.argv[2]) % 2 == 0:
    print("El numero ", sys.argv[2], " es par")
else:
    print("El numero ", sys.argv[2], " es impar")

if int(sys.argv[3]) % 2 == 0:
    print("El numero ", sys.argv[3], " es par")
else:
    print("El numero ", sys.argv[3], " es impar")
