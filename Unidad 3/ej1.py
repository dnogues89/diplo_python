"""
Ejercicio 2:
Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan pasar tres parámetros. 
El programa debe tomar los parámetros e indicar en la terminal si son múltiplos de dos.
"""

import sys


len = len(sys.argv)
for i in range(1, len):
    if i % 2 == 0:
        print(f"{sys.argv[i]} es par")
    else:
        print(f"{sys.argv[i]} es impar")
