"""
Identifica el mayor de dos números enteros
"""

a = int(input("Introduce un número: "))
b = int(input("Introduce otro número: "))

if(a>b):
    print("El número",a,"es mayor que el número",b)
elif(a==b):
    print("El número",a,"y el número",b,"son iguales")
else:
    print("El número",b,"es mayor que el número",a)
