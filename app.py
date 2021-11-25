from flask import Flask, request, render_template, redirect, url_for
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)

# Conection to db:
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sickomode'
app.config['MYSQL_DB'] = 'uman'
db= MySQL(app)

# Routes:
@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST': # Supongo que esta wea es capaz de agarrar info de un formulario
        details = request.json
        nombre = details['Nombre']
        correo = details['Correo']
        password = details['Password']
        direccion = details['Direccion']
        telefono = details['Telefono']
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM Usuario WHERE Correo = %s;", [correo,])
        if cur.fetchone() is not None:
            return ("Usuario ya se encuentra registrado")
        else:
            curs = db.connection.cursor()
            cur.execute("INSERT INTO Usuario(Nombre, Correo, Password, Direccion, Telefono, ID_Rol) VALUES (%s, %s, %s, %s, %s, %s)", (nombre, correo, password, direccion, telefono, "1"))
            db.connection.commit()
            curs.close()
            return("Registro exitoso")

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST': 
        details = request.json
        correo = details['Correo']
        password = details['Password']
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM Usuario WHERE Correo = %s;", [correo,])
        confirm = cur.fetchone()
        cur.close()
        if confirm is not None:
            if confirm[3] == password:
                return "Credenciales correctas"
            else:
                return "Credenciales incorrectas"
        else:
            return "Credenciales incorrectas"
        # Tiene que haber una forma mas correcta de testear si las credencales son correctas

@app.route('/item/<int:id>', methods = ['GET'])
def producto(id):
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM Productos WHERE ID_Producto = %s", [id,])
    infoProducto = cur.fetchone()
    cur.close()
    # Terminar con el agregado al carrito, necesito ver el front end


if __name__ == "__main__":
    app.run(debug=True)