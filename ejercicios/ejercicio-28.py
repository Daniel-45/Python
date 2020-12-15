"""
Escribir una función que tome como argumento un año y devuelva True si es Bisiesto y False si no lo es.
"""

test_data = [1900,2000,2016,1987]
test_results = [False,True,True,False]

def bisiesto(year):
    resultado = False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        resultado = True
    return resultado


for i in range(len(test_data)):
    anio = test_data[i]
    print(anio,"->",end="")
    resultado = bisiesto(anio)
    if resultado == test_results[i]:
        if(resultado == True):
            print(" Ok. Es bisiesto")
        else:
            print(" Has fallado, no es bisiesto")
