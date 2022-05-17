"""

Ejercicio 2
Escriba un programa que consulte al usuario por una oración y comente al usuario cuantas veces aparece la letra “a”. 

"""

oracion = input("Escriba una oracion: ")
veces = 0
for i in oracion:
    if i == "a":
        veces += 1

print(f"La letra 'a' aparecio {veces} veces")
