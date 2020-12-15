from flask import Flask, redirect, url_for, render_template, views
from datetime import datetime
import os
from flask import request, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = 'clave_secreta_flask'

# Conexión con la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'daniel' # Cambiar por tú usuario
app.config['MYSQL_PASSWORD'] = 'password' # Cambiar por tú password
app.config['MYSQL_DB'] = 'flask' # Cambiar por tú base de datos

mysql = MySQL(app)

# Context processors
# Actualizar CSS 
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.context_processor
def date_now():
    return {
        'now': datetime.utcnow()
    }

# Endpoints
@app.route('/')
def index():
    nombre = 'Daniel'
    return render_template('index.html', nombre=nombre)


@app.route('/informacion')
@app.route('/informacion/<string:nombre>/<string:apellidos>')
def informacion(nombre=None, apellidos=None):
    texto = ''

    if nombre != None and apellidos != None:
        texto = f'Hola, {nombre} {apellidos}'

    return render_template('informacion.html', texto=texto)

@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contacto(redireccion = None):
    if redireccion is not None:
        return redirect(url_for('informacion'))

    return render_template('contacto.html')

@app.route('/insertar-coche', methods=['GET', 'POST'])
def insertar_coche():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO coches VALUES(NULL, %s, %s, %s)", (marca, modelo, precio))
        cursor.connection.commit()

        flash("Registro insertado correctamente")

        return redirect(url_for('coches'))
    
    
    return render_template('formulario.html')

@app.route('/coches')
def coches():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches")
    coches = cursor.fetchall()
    cursor.close()

    return render_template('coches.html', coches=coches)

@app.route('/coche/<coche_id>')
def coche(coche_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches WHERE id=%s", (coche_id))
    coche = cursor.fetchall()
    cursor.close()

    return render_template('coche.html', coche=coche[0])

@app.route('/editar-coche/<coche_id>', methods=['GET', 'POST'])
def editar_coche(coche_id):
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']

        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE coches
            SET marca=%s,
                modelo=%s,
                precio=%s
            WHERE id=%s
        """, (marca, modelo, precio, coche_id))
        cursor.connection.commit()

        flash("Registro editado correctamente")

        return redirect(url_for('coches'))


    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches WHERE id=%s", (coche_id))
    coche = cursor.fetchall()
    cursor.close()

    return render_template('formulario.html', coche=coche[0])

@app.route('/eliminar-coche/<coche_id>')
def eliminar_coche(coche_id):
    cursor = mysql.connection.cursor()
    cursor.execute(f"DELETE FROM coches WHERE id={coche_id}")
    mysql.connection.commit()
    flash('El coche se ha eliminado correctamente')

    return redirect(url_for('coches'))

# Iniciar app
if __name__ == '__main__':
    app.run(debug=True)