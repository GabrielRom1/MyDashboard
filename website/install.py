#archivo para crear al primer admin 
from flask import Blueprint, render_template, redirect, url_for, request, flash, session, Flask, Request
from .models import Admin, generate_uuid, User
from flask import jsonify
from . import db

install = Blueprint('install', __name__)

@install.route('/finstall', methods = ['GET'])
def finstall():
    admin = Admin.query.first()
    if admin:
        return redirect(url_for('views.index'))
    
    return render_template('install.html')



@install.route('/install_post', methods = ['POST'])
def install_post():

    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    print(f"Nombre recibido: {name}")
    print(f"Email recibido: {email}")
    print(f"Password recibido: {password}")

    
    # cambiar lo de id para que sea un id unico
    first_Admin = Admin(name=name, email = email, password=password, id= generate_uuid() ) # Crear un nuevo usuario
    first_User = User(name=name, email = email, password=password, id= generate_uuid() ) # Crear un nuevo usuario

    # Agregar el usuario a la base de datos
    try:
        db.session.add(first_Admin)
        db.session.commit()  # Guardar cambios
        print("First admin added")

        db.session.add(first_User)
        db.session.commit()  # Guardar cambios
        print("First user added")


        return redirect(url_for('auth.login'))
    
    except Exception as e:
        print("Error")
        db.session.rollback()  # Revertir cambios si hay un error
        return "Error"



