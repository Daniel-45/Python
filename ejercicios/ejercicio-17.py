"""
Tenemos a un niño que hace construcciones con bloques de madera. 
Siempre construye una pirámide que se apila siguiendo una regla: 
cada capa tiene un bloque más que la capa de arriba. 
De forma que con 6 bloques hacemos una pirámide de tres alturas. 
Tú tienes que ayudarle y leer un número de bloques que hay en la caja y generar la altura de la pirámide máxima que puedes construir con esos bloques. 
Las alturas tienen que ser completas, no pueden dejarse a medias.
"""

contador1 = 0
contador2 = 1
alturas = 0

numero_bloques = int(input("Introduce el número de bloques: "))

while contador2 <= numero_bloques:
    contador1 = contador1 + contador2
    contador2 += 1
    if numero_bloques >= contador1:
        alturas += 1

print("Con",numero_bloques,"bloques, hago",alturas,"alturas")
