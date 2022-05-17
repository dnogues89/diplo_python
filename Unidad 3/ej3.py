"""
Ejercicio 3
Escriba un programa que consulte al usuario por una oración y comente al usuario cuantas veces aparecen todas las vocales considerando 
minúsculas, mayúsculas y acentos.  

"""

vocales = "AaáEeéIiíOoóUuú"
contador = 0
frase = input("Escriba una frase :")

for i in frase:
    if vocales.find(i) >= 0:
        contador += 1

print(
    f" En la frase que pusiste hay {contador} vocales, contando Mayusculas y con tilde"
)
