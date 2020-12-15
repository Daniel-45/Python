"""
Calcula para una entrada de hora, minuto y duración de un evento la hora de finalización del mismo. 
Por ejemplo: Un evento comienza a las 12:57 y dura 59 minutos.
"""

h = int(input("Hora de inicio (horas): "))
m = int(input("Tiempo de inicio (minutos): "))
duracion = int(input("Duración del evento (minutos): "))

m += duracion
h += m // 60
m = m % 60

if(h>24):
    while(h>24):
        h-= 24

print("La salida esperada es:",h,":",m)
