import sqlite3

"""
Ejecutar python sqlite.py
"""

# Conexión
conexion = sqlite3.connect("test.db")

# Crear cursor - permite ejecutar las consultas
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(30),
    descripcion TEXT,
    precio INT(10)
);
""")

# Guardar cambios
conexion.commit()

# Insertar datos
"""
cursor.execute("INSERT INTO productos VALUES (null, 'PC Workstation', 'Intel Core i7-9700K/32GB/2TB+500GB SSD/RTX2060S', 2000)")

cursor.execute("INSERT INTO productos VALUES (null, 'PC Gamming', ' Core i7-9700K/32GB/1TB+250GBSSD/RTX2070S', 1900)")

cursor.execute("INSERT INTO productos VALUES (null, 'PC Basic', 'AMD Ryzen 5 3600/8GB/1TB+500SSD/GTX1650', 650)")

conexion.commit()
"""

# Eliminar registros
"""
cursor.execute("DELETE FROM productos")
conexion.commit()
"""

# Insertar multiples registros
"""
productos = [
    ('PC Workstation', 'Intel Core i7-9700K/32GB/2TB+500GB SSD/RTX2060S', 2000),
    ('PC Gamming', ' Core i7-9700K/32GB/1TB+250GBSSD/RTX2070S', 1900),
    ('PC Basic', 'AMD Ryzen 5 3600/8GB/1TB+500SSD/GTX1650', 650)
]

cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)

conexion.commit()
"""

# Consultas
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()

"""
for producto in productos:
    print(producto)
"""

for producto in productos:
    print('ID:',producto[0])
    print('Nombre:', producto[1])
    print('Descripcion:', producto[2])
    print('Precio:', producto[3])
    print()

cursor.execute("SELECT nombre, precio FROM productos")
producto = cursor.fetchone()
print(producto)

# Update
"""
cursor.execute("UPDATE productos SET nombre='PC Workstation', precio=810 WHERE id=4")
conexion.commit()
"""

# Where
cursor.execute("SELECT * FROM productos WHERE precio >= 800")
productos = cursor.fetchall()

print('\n---------- WHERE ----------')

for producto in productos:
    print('ID:',producto[0])
    print('Nombre:', producto[1])
    print('Descripcion:', producto[2])
    print('Precio:', producto[3])
    print()

# Cerrar conexión
conexion.close()