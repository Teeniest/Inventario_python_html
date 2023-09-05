from flask import Blueprint, render_template

auth = Blueprint('auth',__name__)

#Es necesario agregar el prefijo "/auth" para acceder a las sig. rutas: 
@auth.route("/login")
def login():
    return render_template("login.html", cuenta="Hola", boolean=True)

@auth.route("/log-out")
def logout():
    return render_template("logout.html")

@auth.route("/sign-up")
def signup():
    return render_template("sign_up.html")
