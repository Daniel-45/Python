"""
Identifica el mayor de tres números enteros
"""

a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
c = int(input("Introduce el tercer número: "))
mayor = a
if(mayor < b):
    mayor = b
if(mayor < c):
    mayor = c
print("El mayor de los tres números es:",mayor)

if(mayor == b and mayor == c):
    print("Los números son iguales")
