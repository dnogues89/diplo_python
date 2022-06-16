import re

patron = "^[0-9]+"
hola = "hola"

print(re.match(patron, str(hola)))
