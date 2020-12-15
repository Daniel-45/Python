"""
Vamos a registrar las temperaturas de una estación meteorológica durante todo un mes. 
Para ello a cada hora en punto tomamos la temperatura. Supón un mes estándar de 31 días.
Programa un método para determinar los siguiente:
1. La temperatura media mensual al mediodía. Supón que la primera que tomas es la de las 00:00 de la noche.
2. Calcula la temperatura más alta del mes.
3. Cuenta los días más calurosos, cuando la temperatura al mediodía fue de más de 20ºC.
"""

import random

acumulador = 0
dias_mas_calurosos = 0
temperatura_mas_alta = 0
# temperatura por cada hora del dia
thd = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# temperatura máxima del día por cada día en un mes
temperatura_max_dia_mes = [thd,thd,thd,thd,thd,thd,thd,thd,thd,thd,thd,
thd,thd,thd,thd,thd,thd,thd,thd,thd,thd,thd,thd,thd,thd,thd,thd,thd,thd,thd,thd]

def dia():
    for i in range(24):
        thd[i] = (random.randrange(8,47))
    return thd

for i in range(31):
    temperatura_max_dia_mes[i] = dia()

for i in range(31):
    for j in range(24):
        if temperatura_max_dia_mes[i][j] > temperatura_mas_alta:
            temperatura_mas_alta = temperatura_max_dia_mes[i][j]

for i in range(31):
    acumulador = acumulador + temperatura_max_dia_mes[i][12]
    if temperatura_max_dia_mes[i][12] > 20:
        dias_mas_calurosos = dias_mas_calurosos + 1

media = acumulador / 31

print("La temperatura media del mes a mediodía es: " + str(media) + "º")
print("La temperatura mas alta del mes ha sido: " + str(temperatura_mas_alta) +"º")
print("Este mes el numero de dias con temperatura superior a 20º ha sido:", dias_mas_calurosos)
