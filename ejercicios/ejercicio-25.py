"""
Crea una lista de 10 números con algunos duplicados. Escribe un programa que elimine los duplicados de la lista.
"""

lista = [31,31,29,26,23,2,19,19,2,8]

print("Los elementos de la lista original son:",lista)

lista = set([31,31,29,26,23,2,19,19,2,8])

print("Los elementos de la lista sin duplicados son:",lista)
