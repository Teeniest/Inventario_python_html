from flask import Blueprint, render_template, request

auth = Blueprint('auth',__name__)

#Es necesario agregar el prefijo "/auth" para acceder a las sig. rutas: 
@auth.route("/login",methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", cuenta="Hola", boolean=True)

@auth.route("/log-out")
def logout():
    return render_template("logout.html")

@auth.route("/sign-up", methods=['GET','POST'])
def signup():
    return render_template("sign_up.html")
