"""
Ejercicio 5 – Dificultad media
Cree un programa que utilizando una función, solicite la edad de la persona e imprima todos los años que la persona ha cumplido según el siguiente formato de ejemplo. 
1, 2, 3, 4, 5
Y 
5, 4, 3, 2, 1

"""


def edad():
    age = int(input("Cuantos años tenes?\n"))
    cumples = []
    cumple_inv = [0]
    for i in range(1, age + 1):
        cumples += [i]
        cumple_inv.insert(0, i)

    cumple_inv.pop(age)

    return f"{cumples}\n{cumple_inv}"


print(edad())
