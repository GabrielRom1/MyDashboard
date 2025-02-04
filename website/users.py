from flask import Blueprint, render_template, redirect, url_for, request, session
from .models import Admin, User, Service, Appointment
from . import db
from datetime import datetime
from flask_login import login_required, current_user



users = Blueprint('users', __name__)


@users.route('/view_users',  methods=['GET', 'POST'])
@login_required
def view_users():

    if session.get('admin'):
        user_list = User.query.all()
        if not user_list:
            print("users empty")
        
        else:
            print(user_list)

        return render_template('users.html', user_list = user_list)

    else:
        return ("access to view users denied")


@users.route('/create_user', methods = ['GET', 'POST'])
@login_required
# maybe login required is problematic due to the import function on signup 
def create_user(from_signup = None):

    if not session.get('admin') and from_signup == None:
        print("unauthorized user tried to create a user")
        return ("unauthorized user tried to create other user")


    if request.method == "POST":

        name = request.form.get('name')

        email = request.form.get('email')
        password = request.form.get('password')
        
        #!! add a field of "make admin or not" and use an exception to make it works with signup

        print(f"Nombre recibido: {name}")
        print(f"Email recibido: {email}")
        print(f"Password recibido: {password}")

    
        # cambiar lo de id para que sea un id unico
        user = User(name=name, email = email, password=password ) # Crear un nuevo usuario
        # 
        # Agregar el usuario a la base de datos
        try:
            db.session.add(user)
            db.session.commit()  # Guardar cambios
            if not from_signup:
                return redirect(url_for("users.view_users"))
            else:
                return True
            # return jsonify({'success': True, 'message': 'Usuario registrado con éxito',  'redirect_url': url_for('auth.login')}), 201
        
        except Exception as e:
            print("Error")
            db.session.rollback()  # Revertir cambios si hay un error
            return "Error"
            # return jsonify({'success': False, 'message': str(e)}), 500
        
    elif request.method == 'GET':
        return render_template('form_user.html', create = 0)



@users.route('/edit_user/<user_id>', methods = ['GET', 'POST'])
@login_required
def edit_user(user_id):
    if request.method == 'GET':
        return render_template('form_user.html', user_id=user_id,create = 0)
    
    user = User.query.filter_by(id=user_id).first()

    if request.method == 'POST':
        print("edit post")
        name = request.form.get('name')

        email = request.form.get('email')

        passw = request.form.get('password')

         # Modificar el campo
        user.name = name
        user.email = email
        user.password = passw

        # Guardar cambios en la base de datos
        try:
            db.session.flush()

            db.session.commit()
            return redirect(url_for("services.view_services"))
        except Exception as e:
            db.session.rollback()  # Revertir cambios si hay un error
            return e

    return "edit page" + user_id

    if request.method == 'GET':
        return render_template('form_service.html', create = 0)


    print("llego al edit")

    return "edit page" + user_id


@users.route('/delete_user/<user_id>')
@login_required
def delete_user(user_id):
    print(user_id)
    if session.get('admin'):
        user = User.query.filter_by(id=user_id).first()

        if user:
            print("delete", user)
            db.session.delete(user)
            db.session.commit()

        else:
            return ("error")

        return redirect(url_for("users.view_users"))
    else:
        return ("access denied to delete user")
    