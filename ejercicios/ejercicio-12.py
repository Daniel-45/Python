
"""
Un mago ha creado un juego en el que hay que adivinar un número secreto del 1 al 100. 
Los que no adivinen el número entrarán en un bucle infinito como castigo divino.
Como ayudante de mago ayúdale a implementar el código con estos requisitos que te ha
pedido el mago explícitamente:
- Debes pedir al público que introduzca un número.
- Usa un bucle while
- Comprueba si el número pensado por el mago es el que el público ha escogido y si no
es así saca un mensaje de aviso "Estás cayendo en mi bucle…". 
Si coincide debe imprimirse en pantalla y el mago dirá las palabras "Esta vez lo has conseguido… Estás libre"
- Limita si quieres a dos cifras porque el mago tiene que trabajar el fin de semana y si nono cobra ni él ni tú.
"""
import random

numero_secreto = random.randint(1,99)

# print("Numero secreto:",numero_secreto)

n = 0

print("Adivina el número secreto")

while (n < 0 or n != numero_secreto):
    try:
        n = int(input("Introduce un numero del 1 al 99: "))
        if n != numero_secreto:
            print("Estas cayendo en mi bucle...")
        else:
            print("Esta vez lo has conseguido... Estas libre")
    except:
        print("Tienes que introducir un numero entero")
