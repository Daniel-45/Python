"""
Escribe un programa que pida números al usuario, y calcula el mayor de los números introducidos. 
Cuando quiera acabar el usuario introduce -1. Utiliza el break para salir del bucle.
"""

print("Para salir introduce -1")

mayor = 0

while 1 == 1:
    numero = int(input('Introduce un número: '))
    if numero > mayor:
        mayor = numero
    if numero == -1:
        break
print('El número mayor de los números introducidos es:',mayor)

 
