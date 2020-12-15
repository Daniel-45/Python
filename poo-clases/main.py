from coche import Coche

coches = []

coche1 = Coche('Audi', 'A8', 'Negro', 340, 260, 5, 4)
coche2 = Coche('Audi', 'A4', 'Azul', 280, 220, 5, 4)
coche3 = Coche('Seat', 'Ibiza', 'Gris', 180, 220, 5, 4)
coche4 = Coche('Reanult', 'Clio', 'Blanco', 150, 200, 5, 4)
coche5 = Coche('Toyota', 'Auris', 'Gris', 200, 230, 5, 4)
coche6 = Coche('Mercedes', 'Clase A', 'Negro', 340, 260, 5, 4)

coches = [coche1, coche2, coche3, coche4, coche5, coche6]

for coche in coches:
    print(coche.mostrarDatos())

# Detectar tipado
print('\n------ Tipo de dato ------')
if (type(coche1)) == Coche:
    print('El objeto es un coche')
else:
    print('El objeto no es un coche')