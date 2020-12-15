"""
Busca un elemento dentro de una lista.
"""

miLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(miLista)

if 5 in miLista:

    print("El número 5 esta en la lista")

else:

    print("El número 5 no esta en la lista")

print("El número de elementos de la lista es", len(miLista))

print("El número 5 esta en la posición (índice)",miLista.index(5),"de la lista")
