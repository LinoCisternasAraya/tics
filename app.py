from flask import Flask, request, render_template, redirect, url_for
from flask_mysqldb import MySQL
from flask_cors import CORS


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Contraseña'
app.config['MYSQL_DB'] = 'uman'
db= MySQL(app)




if __name__ == "__main__":
    app.run(debug=True)