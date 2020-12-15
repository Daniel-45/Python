"""
Escribe un pequeño programa que, utilizando listas y/o segmentos calcules el número mayor de una lista.
"""

import random

numeros= int(input("Introduce cuantos números aleatorios quieres en la lista: "))

miLista = [random.randint(0,100) for _ in range(numeros)]

print("Los elementos de la lista son:",miLista)

print("El número mas alto de la lista es:", max(miLista))
