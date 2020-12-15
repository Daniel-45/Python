"""
Calcular números pares e impares. 
"""

pares = 0
impares = 0

numero = int(input("Introduce un numero o escribe 0 para terminar: "))

while numero != 0:
    if numero % 2 == 0:
        pares+=1
    else:
        impares+=1
    numero = int(input("Introduce un numero o escribe 0 para terminar: "))

print("El contador de los numeros pares es:",pares)
print("El contador de los numeros impares es:",impares)
