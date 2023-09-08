from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth',__name__)

#Es necesario agregar el prefijo "/auth" para acceder a las sig. rutas: 
@auth.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Acceso a cuenta correcto', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Contraseña incorrecta, vuelve a intentar.', category='error')
        else:
            flash('El usuario no existe',category='error')
    return render_template("login.html", user=current_user)

@auth.route("/log-out")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("/sign-up", methods=['GET','POST'])
def signup():
    #Añadiendo usuario a base de datos
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('primer nombre')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('El correo ya fue registrado','category='error')
        elif len(email)<4:
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
            login_user(user, remember=True)
            flash('Cuenta creada exitosamente', category='succes')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html",user=current_user)
