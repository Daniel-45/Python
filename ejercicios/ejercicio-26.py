"""
Haz un pequeño programa para rellenar el tablero con las piezas correspondientes. 
Primero debes crear el tablero vacío y pon una letra significativa para poner en la posición de la figura de ajedrez. 
Por ejemplo TORRE (T), PEON (P), ALFIL (A), REINA (Q), REY (R), CABALLO (C).
"""

filas = 8
columnas = 8

matriz_ajedrez = []
peones = ["P","P","P","P","P","P","P","P"]
piezasBlancas = ["T","C","A","Q","R","A","C","T"]
piezasNegras = ["T","C","A","R","Q","A","C","T"]

for i in range(8):
    matriz_ajedrez.append(["#","#","#","#","#","#","#","#"])

def colocarPiezas(matriz_ajedrez):
    for i in range(filas):
        for j in range(columnas):
            if i == 0:
                matriz_ajedrez[i][j] = piezasBlancas[j]
            if i == 7:
                matriz_ajedrez[i][j] = piezasNegras[j]
            if i == 1 or i == 6:
                matriz_ajedrez[i][j] = peones[j]

colocarPiezas(matriz_ajedrez)

for i in range(filas):
    for j in range(columnas):
        print(matriz_ajedrez[i][j] + " ",end=" ")
    print("")
