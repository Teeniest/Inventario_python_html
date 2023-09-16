from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from .models import Productos
from . import db
import json, sqlite3
from .__init__ import DB_NAME

views = Blueprint('views', __name__)

@views.route('/')
def home():
        return render_template("home.html", user=current_user)

@views.route('/inventario', methods=['GET', 'POST'])
@login_required
def inventario():
    if request.method == 'POST':
        cant = request.form.get('inventario_cantidad')
        nom = request.form.get('inventario_nombre')
        des = request.form.get('inventario_descripcion')
        p_ant = request.form.get('inventario_p_anterior')
        p_min = request.form.get('inventario_p_minimo')
        cad = request.form.get('inventario_fechacad')
        cat = request.form.get('inventario_cat')

        if len(nom)>100:
            flash('Error: nombre supera los 100 caracteres', category='error')    
        elif len(des)>100:
            flash('Error: descripción supera los 1000 caracteres', category='error')
        elif len(cad)>20:
            flash('Error: fecha de caducidad supera los 20 caracteres', category='error')
        elif len(cat)>100:
            flash('Error: categoría supera los 100 caracteres', category='error') 
        #elif cant==None:
        #    pass   
        else:
            #pass
            new_item=Productos(cantidad=cant, nombre=nom, descripcion=des, 
                               precio_anterior=p_ant, precio_minimo=p_min, caducidad=cad, 
                               categoria=cat,user_id=current_user.id)
            db.session.add(new_item)
            db.session.commit()
            flash('Objeto agregado', category='success')
    return render_template("inventario.html", user=current_user)

@views.route('/notas', methods=['GET', 'POST'])
@login_required
def notas():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note)<1:
            flash('Note is too short', category='error')
        else:
            new_note=Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Nota añadida', category='success')
    return render_template("notas.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

@views.route('/borrar-prod', methods=['POST'])
def borrar_prod():
    prod = json.loads(request.data)
    prod_id = prod['prodId']
    prod = Productos.query.get(prod_id)
    if prod:
        if prod.user_id == current_user.id:
            db.session.delete(prod)
            db.session.commit()
    return jsonify({})