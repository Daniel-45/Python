"""
Pedir al usuario una palabra al usuario y escribir sólo las consonantes en mayúscula de la palabra en columna.
"""

VOCALES = "A E I O U"

palabra = input("Introduce una palabra: ").upper()

for letra in palabra:
    if letra in VOCALES:
        continue
    else:
        print(letra)
