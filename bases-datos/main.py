import mysql.connector

# Conexión a la base de datos
database = mysql.connector.connect(
    host = 'localhost',
    user = 'daniel', # Cambiar por tú usuario
    passwd  = 'password', # Cambiar por tú password
    database = 'python' # Cambiar por tú base de datos
)

# Cursor que permite ejecutar las consultas
cursor = database.cursor(buffered=True)

# Crear base de datos
# cursor.execute('CREATE DATABASE IF NOT EXISTS python')

"""
cursor.execute("SHOW DATABASES")

for bd  in cursor:
    print(bd)
"""

# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(20) not null,
    modelo varchar(20) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

"""
cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)
"""

"""
cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Insignia', 32850)")
cursor.execute("INSERT INTO vehiculos VALUES(null, 'Seat', 'Ibiza', 16360)")
cursor.execute("INSERT INTO vehiculos VALUES(null, 'Audi', 'A8', 101000)")
cursor.execute("INSERT INTO vehiculos VALUES(null, 'Mercedes-Benz', 'CLS', 81850)")
cursor.execute("INSERT INTO vehiculos VALUES(null, 'BMW', 'X6', 32850)")
cursor.execute("INSERT INTO vehiculos VALUES(null, 'Lexus', 'LC', 120000)")
cursor.execute("INSERT INTO vehiculos VALUES(null, 'Renault', 'Clio', 11000)")
database.commit()
"""


# Insertar multiples registros
"""
coches = [
    ('Seat', 'Leon', 26490),
    ('Toyota', 'Auris', 16450),
    ('Renault', 'Megane', 21175),
    ('Ford', 'Mondeo', 30825)
]

cursor.executemany("INSERT INTO vehiculos VALUES(null,%s,%s,%s)", coches)

database.commit()
"""

# Consultas
cursor.execute("SELECT * FROM vehiculos")
resultado = cursor.fetchall()

print('\n---------- VEHICULOS ----------\n')

for vehiculo in resultado:
    print('ID:', vehiculo[0])
    print('Marca:', vehiculo[1])
    print('Modelo:', vehiculo[2])
    print('Precio:', vehiculo[3])
    print()

"""
cursor.execute("SELECT marca, precio FROM vehiculos")
resultado = cursor.fetchall()

for vehiculo in resultado:
    print(vehiculo)
"""

print('------------ WHERE ------------\n')

cursor.execute("SELECT * FROM vehiculos WHERE precio <= 20000 AND marca = 'Seat'")
resultado = cursor.fetchall()

for vehiculo in resultado:
    print('ID:', vehiculo[0])
    print('Marca:', vehiculo[1])
    print('Modelo:', vehiculo[2])
    print('Precio:', vehiculo[3])
    print()


print('------- PRIMER REGISTRO -------\n')
cursor.execute("SELECT * FROM vehiculos")
vehiculo = cursor.fetchone()
print(vehiculo)

# Eliminar
# cursor.execute("DELETE FROM vehiculos")
"""
cursor.execute("DELETE FROM vehiculos WHERE modelo = 'Clio'")
database.commit()
print()
print(cursor.rowcount, "eliminados")
"""

# Actualizar
"""
cursor.execute("UPDATE vehiculos SET precio=16500 WHERE modelo='Ibiza'")
database.commit()
print()
print(cursor.rowcount, "actualizados")
"""