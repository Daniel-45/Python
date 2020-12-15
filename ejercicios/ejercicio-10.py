"""
Comprueba que el año que te pasa el usuario por línea de comandos es o no bisiesto.
Ten también en cuenta que si el año es inferior a 1582 que es cuando se introdujo el calendario gregoriano, 
debe aparecer un mensaje indicando que no está en el período del calendario gregoriano
"""

MAXIMO = 1582

anio = int(input("Introduce un año: "))

salida = "Año normal"

if(anio >= MAXIMO):

    if(anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)):
        salida = "Año bisiesto"
else:
    salida = "No esta en el periodo del calendario Gregoriano"

print(salida)
