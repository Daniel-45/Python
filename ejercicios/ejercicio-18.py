"""
Escribe una lista con los números del 1 al 5. 
Solicita al usuario que reemplace el número del medio con un número entero que meta por teclado.
Elimina el último elemento de la lista. 
Escribe una línea de código que imprima la longitud de la lista.
En todos los pasos imprime los valores correspondientes de la lista.
"""

lista = [1,2,3,4,5]

print(lista)

lista[2] = int(input("Introduce un número: "))

print(lista)

del lista[len(lista)-1]

print(lista)

print("La longitud de la lista es:",len(lista))
