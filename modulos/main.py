"""
Modulos: son funcionalidades ya hechas para reutilizar
Se pueden utilizar modulos propios del lenguaje
Tambien se pueden crear modulos propios
"""

# Mi módulo

"""
import modulo

print(modulo.calculadora(100, 4))
"""

# Módulo fechas

"""
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)

formato_fecha = fecha_completa.strftime('%d/%m/%Y - %H:%M:%S')

print(formato_fecha)
"""

# Módulo matemáticas

"""
import math

print('Raiz cuadrada de 8:', math.sqrt(8))
print('Redondeo alto:', math.ceil(8.23653))
print('Redondeo bajo:', math.floor(8.23653))
print('Numero PI:', math.pi)
"""

# Modulo random
import random

print('Numero aleatorio entre 0 y 100:', random.randint(1,49))