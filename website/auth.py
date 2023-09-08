from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth',__name__)

#Es necesario agregar el prefijo "/auth" para acceder a las sig. rutas: 
@auth.route("/login",methods=['GET','POST'])
def login():
    
    return render_template("login.html", cuenta="Hola", boolean=True)

@auth.route("/log-out")
def logout():
    return render_template("logout.html")

@auth.route("/sign-up", methods=['GET','POST'])
def signup():
    #Añadiendo usuario a base de datos
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('primer nombre')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if len(email)<4:
            flash('Correo es menor a 4 caracteres', category='error')
        elif len(first_name)<2:
            flash('Nombre debe ser mayor a 2 caracteres', category='error')
        elif password != password2:
            flash('Las contraseñas no coinciden', category='error')
        elif len(password)<8:
            flash('La contraseña es menor a 8 caracteres', category='error')
        else:
            new_user = User(email=email, firstname=first_name, password=generate_password_hash(password, method='shas56'))
            db.session_add(new_user)
            db.session.commit()
            flash('Cuenta creada exitosamente', category='succes')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")
