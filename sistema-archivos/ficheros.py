from io import open
import pathlib
import  shutil
import os
import os.path

# Abrir un archivo
"""
ruta = str(pathlib.Path().absolute()) + '/fichero-texto.txt'
archivo = open(ruta, "a+")
"""

# Escribir
# archivo.write('Hola mundo desde Python\n')

# Cerrar el archivo
# archivo.close()

# Abrir un archivo
ruta = str(pathlib.Path().absolute()) + '/ficheros/fichero-texto.txt'
archivoLectura = open(ruta, "r")


# Leer contenido del archivo
contenido = archivoLectura.read()
print(contenido)

# Leer contenido y guardar en una lista
"""
lista = archivoLectura.readlines()
archivoLectura.close()

for frase in lista:
    print(frase)
"""

# Copiar archivos
"""
rutaOriginal = str(pathlib.Path().absolute()) + '/fichero-texto.txt'
rutaNueva = str(pathlib.Path().absolute()) + '/ficheros/fichero-copia.txt'
# print(rutaNueva)
shutil.copyfile(rutaOriginal, rutaNueva)
"""

# Mover archivo
"""
rutaOriginal = str(pathlib.Path().absolute()) + '/fichero-texto.txt'
rutaNueva = str(pathlib.Path().absolute()) + '/ficheros'
shutil.move(rutaOriginal, rutaNueva)
"""

# Eliminar archivos
"""
rutaNueva = str(pathlib.Path().absolute()) + '/ficheros/fichero-copia.txt'
os.remove(rutaNueva)
"""

# Comprobar si existe
"""
print(os.path.abspath('./ficheros'))

if os.path.isfile('./ficheros/fichero-copia.txt'):
    print('El fichero existe')
else:
    print('El fichero no existe')
"""
