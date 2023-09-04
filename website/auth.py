from flask import Blueprint

auth = Blueprint('auth',__name__)

#Es necesario agregar el prefijo "/auth" para acceder a las sig. rutas: 
@auth.route("/login")
def login():
    return "<p>Login</p>"

@auth.route("/log-out")
def logout():
    return "<p>Logout</p>"

@auth.route("/sign-up")
def signup():
    return "<p>Sign up</p>"
