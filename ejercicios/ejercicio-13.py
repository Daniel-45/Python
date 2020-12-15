"""
Para contar segundos a veces se utiliza la palabra Mississipi para calcular el tiempo mejor.
"un Mississipi, dos Mississipi, tres Mississipi" son más o menos, diciéndolo en voz alta unos 3 segundos.
Es una forma de calcular el tiempo bien y no hacer trampa cuando se cuentan los números al jugar al escondite.
"""

import time

tiempo_espera = 1
contador = 0

while contador < 5:
    contador += 1
    print(contador,"Mississipi")
    time.sleep(tiempo_espera)

print("Preparado o no, allá voy!")
