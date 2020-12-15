"""
Calcular el llamado impuesto sobre la renta personal utilizando la siguiente regla:
- Si el ingreso del ciudadano no es superior a 85.528 thalers, el impuesto es igual al 18% de los
ingresos menos 556 thalers y 2 céntimos (esto era la llamada desgravación fiscal)
- Si el ingreso es superior a esta cantidad, el impuesto es igual a 14,839 thalers y 2 céntimos,
más el 32% del excedente sobre 85,528 thalers.
Tú tarea es escribir una calculadora de impuestos.
Debe aceptar un valor de coma flotante: el ingreso.
A continuación, debe imprimir el impuesto calculado, redondeado a thalers completos.
Si el impuesto calculado es menor que cero, solo significa que no hay ningún impuesto (el impuesto es igual a cero). 
Tenga esto en cuenta durante sus cálculos.
"""

MAXIMO = 85528
impuesto = 0
cantidad = float(input("Introduce tus ingresos: "))

if(cantidad < MAXIMO):
    impuesto = (cantidad * 0.18) - 556.02
else:
    impuesto = 14839.02 + (cantidad - MAXIMO) * 0.32

if(impuesto < 0):
    impuesto = 0

print("El impuesto es:", round(impuesto,1),"thalers")
