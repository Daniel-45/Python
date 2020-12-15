"""
Mejora el código anterior del  y asigna las consonantes a una palabra nueva palabra_sin_vocales. 
Imprime el resultado en la pantalla.
"""

palabra_sin_vocales = ""

palabra = input("Introduce una palabra: ").upper()

for letra in palabra:
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        palabra_sin_vocales += letra
print(palabra_sin_vocales)
