"""
Escribe y prueba una función que tome dos argumentos (año y mes) y devuelva el número de
días que tiene el par mes/año (realmente sólo afecta al mes de febrero de los años bisiestos).
Utiliza None si los argumentos que se le pasan no tienen sentido.
"""

anio = 0
mes = 0
correcto = False
numero_dias = 0
lista_meses = [0,0,0,0,0,0,0,0,0,0,0,0]
meses_lista = [0,0,0,0,0,0,0,0,0,0,0,0]

print("Introduce un año entre (1900-2020) y un mes para calcular el número de dias del mes")

def bisiesto(year):
    resultado = False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        resultado = True
    return resultado

def anioMesDia(anio,mes,dia):
    if(bisiesto(anio)):
        numero_dias = meses_lista[mes -1]
    else:
        numero_dias = lista_meses[mes -1]
    print("El mes tiene",numero_dias,"días")

for i in range(12):
    if i == 0 or i == 2 or i == 4 or i == 6 or i == 7 or i == 9 or i == 11:
        lista_meses[i] = 31
        meses_lista[i] = 31
    if i == 3 or i == 5 or i == 8 or i == 10:
        lista_meses[i] = 30
        meses_lista[i] = 30
    if i == 1: #Mes 1 es Febrero
        lista_meses[i] = 28
        meses_lista[i] = 29

while(not correcto):
    try:
        anio = int(input("Año: "))
        mes = int(input("Mes (número de mes): "))

        if anio < 1900 or anio > 2020 or mes <= 0 or mes > 12:
            print("ERROR!! Introduce valores correctos.")
        else:
            correcto = True
    except:
        print("ERROR!! Tienes que inroducir un valor numérico.")

def calculaDias(anio,mes):
    if(bisiesto(anio)):
        numero_dias = meses_lista[mes -1]
    else:
        numero_dias = lista_meses[mes -1]
    print("El mes tiene",numero_dias,"dias")

calculaDias(anio,mes)
