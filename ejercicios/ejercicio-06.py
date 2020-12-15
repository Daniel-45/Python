"""
Escribir el código necesario para evaluar los resultados de cuatro operaciones aritméticas básicas. 
"""

numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
resto = numero1 % numero2

print(f'Suma: {numero1} + {numero2} = {suma}')
print(f'Resta: {numero1} - {numero2} = {resta}')
print(f'Multiplicacion: {numero1} * {numero2} = {multiplicacion}')
print(f'Division: {numero1} / {numero2} = {division}')
print(f'Resto: {numero1} % {numero2} = {resto}')
