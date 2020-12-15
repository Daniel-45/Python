"""
Haz un programa que simule el sorteo de la Bonoloto
"""

import random
contador = 0
aciertos = 0
mis_numeros = []
numeros_sorteo = 6
#sorteo = [31,29,26,23,19,2]
sorteo = [random.randint(1,49) for _ in range(numeros_sorteo)]

print("Introduce tus numeros de la BonoLoto")
while contador < 6:
    try:
        numero = int(input("Introduce un numero: "))
        if numero < 1 or numero > 49:
            print("Tienes que introducir un numero del 1 al 49")
            numero = int(input("Introduce un numero: "))
        else:
            mis_numeros.append(numero)
            contador += 1
    except:
        print("Tienes que introducir un numero!!")
print("Tus numeros de la BonoLoto son:", mis_numeros)
print("Los numeros del sorteo de la BonoLoto son:",sorteo)

for i in mis_numeros:
    if i in sorteo:
        aciertos += 1

if aciertos == 6:
    print("Has gando el primer premio de la BonoLoto")
else:
    print("Has acertado", aciertos, "numeros del sorteo")
