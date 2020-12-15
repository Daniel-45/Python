"""
Escribe y prueba una función que tome tres argumentos (año, mes y día del mes) y devuelva el
día correspondiente del año o None si algún argumento no es válido. 
Reutiliza código si lo necesitas y añade algún caso de prueba.
"""

anio = 0
mes = 0
correcto = False
numero_dias = 0
lista_meses = [0,0,0,0,0,0,0,0,0,0,0,0]
meses_lista = [0,0,0,0,0,0,0,0,0,0,0,0]

print("Introduce un año entre (1900-2020) y el valor numerico de un mes del año")

def bisiesto(year):
    resultado = False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        resultado = True
    return resultado

def diaMes(anio,mes,dia):
    acumulador = 0
    if(bisiesto(anio) == True):
        for i in range(mes):
            if i == mes-1:
                acumulador = acumulador + dia
            else:
                acumulador = acumulador + meses_lista[i]
    else:
        for i in range(mes):
            if i == mes-1:
                acumulador = acumulador + dia
            else:
                acumulador = acumulador + lista_meses[i]
    return acumulador

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
        mes = int(input("Mes (numero de mes): "))
        dia = int(input("Dia: "))

        if  anio < 1900 or anio > 2020 or mes <= 0 or mes > 12 or dia <=0 or ((bisiesto(anio) == True) and (dia > meses_lista[mes-1]) or ((bisiesto(anio) == False) and dia > lista_meses[mes-1])):
            correcto = False
        else:
            correcto = True

        if anio < 1900 or anio > 2020 or mes <= 0 or mes > 12 or dia < 1 or dia > 31:
            print("ERROR!! Introduce valores correctos.")
        else:
            correcto = True
    except:
        print("ERROR!! Tienes que inroducir un valor numerico.")

print("Para la fecha",str(dia) + "/" + str(mes) + "/" + str(anio),"es el dia",diaMes(anio,mes,dia),"del año",anio)
