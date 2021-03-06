from flask import Flask, render_template, request, redirect, url_for
import os

# modulo Base de datos

# Iniciando FLASK
app = Flask(__name__)
app.secret_key = 'E86xBi9k!y'

# RUTAS 
@app.route('/', methods=['GET', 'POST'])
def inicio():
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run("0.0.0.0", port=port, debug=True)