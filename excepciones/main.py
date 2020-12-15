# Capturar excepciones y manejar errores en código suceptible a fallos/errores
"""
try:
    nombre = input('Introduce tú nombre: ')

    if len(nombre) > 3:
        nombreUsuario = 'Hola, ' + nombre

    print(nombreUsuario)
except:
    print('El nombre debe tener mínimo tres caracteres')
"""

"""
Crear una lista con 9 numeros enteros
- Recorrer la lista y mostrar
- Hacer función que recorra listas de numeros y devuelva un string
- Mostrar lista orden inverso
- Ordenar y mostrar la lista
- Mostrar la longitud de la lista
- Buscar un elemento que el usuario pida por teclado
"""

# Crear lista
numeros = [46, 1300, 47, 1500, 48, 1700, 67, 2000, 97]

# Funcion que recorre listas de numeros y devuelve string
def mostrarLista(lista):
    resultado = ''

    for elemento in lista:
        resultado += str(elemento)
        resultado += ' '

    return resultado

print('\n-------------- Función recorre listas --------------\n')
print(mostrarLista(numeros))


# Recorrer y mostrar lista
print('\n------------- Recorrer y mostrar lista -------------\n')

for numero in numeros:
    print(numero)

# Mostrar lista orden inverso
print('\n----------- Mostrar lista orden inverso ------------\n')
numeros.reverse()
print(numeros)

# Ordenar la lista
print('\n------------ Ordenar y mostrar la lista ------------\n')
numeros.sort()
print(numeros)


# Mostrar longitud de la lista
print('\n---------- Mostrar longitud de la lista ------------\n')
print('La longitud de la lista es de ' + str(len(numeros)) + ' elementos')

# Buscar un elemento que el usuario pida por teclado
print('\n--------- Buscar un elemento de la lista -----------\n')

try:
    elemento = int(input('Introduce un número: '))

    comprobar = isinstance(elemento, int)

    while not comprobar or elemento <= 0:
        elemento = int(input('Introduce un número: '))
    else:
        print(f'Has introducido el número {elemento}')

        busqueda = numeros.index(elemento)

        print(f'El número buscado esta en la lista, es el indice {busqueda}')
except Exception as e:
    print('Ha ocurrido un error:', type(e).__name__)


# Multiples excepciones
"""
try:
    numero = int(input('\nIntroduce un número para elevar al cuadrado: '))
    print(f'El cuadrado  de {numero} es: ' + str(numero*numero))
except TypeError:
    print('Tienes que convertir la cadena a entero en el codigo')
except ValueError:
    print('Tienes que introducir un numero entero')
"""

# Excepciones personalizadas o lanzar excepcion
"""
try:
    nombre = input('\nIntroduce tú nombre: ')
    edad = int(input('Introduce tú edad: '))

    if edad < 1 or edad > 110:
        raise ValueError('La edad introducida no es real')
    elif len(nombre) < 3:
        raise ValueError('El nombre tiene que tener minimo tres caracteres')
    else:
        print(f'Hola, {nombre}')
except ValueError:
    print('Introduce los datos correctamente!!')
"""