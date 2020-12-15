import os
import shutil

# Crear directorio
"""
if not os.path.isdir('./documentos'):
    os.mkdir('./documentos')
else:
    print('El directorio ya existe')
"""

# Copiar directorio
"""
rutaOriginal = './documentos'
rutaNueva = './documentos-copia'

shutil.copytree(rutaOriginal, rutaNueva)
"""

# Eliminar directorio
# os.rmdir('./documentos-copia')

# Listar contenido de un directorio
print('Contenido del directorio')

contenido = os.listdir('./ficheros')

# print(contenido)

for fichero in contenido:
    print('Fichero: ' + fichero)