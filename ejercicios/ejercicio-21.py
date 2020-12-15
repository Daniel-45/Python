
"""
Haz una versión interactiva del método de ordenación de la burbuja.
Pide al usuario que diga primero cuántos elementos va a meter en la lista. 
Después intdroducir los valores uno a uno, transformalos en float y realiza la ordenación. 
"""

numero_elementos = int(input("Introduce el numero de elementos de la lista: "))
contador = 0
lista = []

while contador < numero_elementos:
    lista.append(float(input("Introduce el elemento " + str(contador+1) + ": ")))
    contador+=1

print("Los elementos de la lista son:", lista)

for i in range(0,len(lista)-1):
    for z in range(len(lista)-1,i,-1):
        if lista[z]<lista[z-1]:
            lista[z-1],lista[z]=lista[z],lista[z-1]

print("Los elementos ordenados de la lista son:", lista)
