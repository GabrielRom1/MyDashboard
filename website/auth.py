
from flask import Blueprint,  render_template, request, jsonify, url_for, flash, session, redirect
from . import db
from .models import Admin, User
from flask_login import login_user
from flask_login import login_required, current_user
from .users import create_user


#se va a definir los blueprints, son un monton de rutas para poder dividir el codigo
auth = Blueprint('auth', __name__)

    #!! configurar login required


@auth.route('/login',  methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        print("EN EL GET DE LOGIN")
        render_template('login.html')

    if request.method == 'POST':
        print("EN EL POST DE LOGIN")

        email = request.form.get('email')
        password = request.form.get('password')
        
        admin = Admin.query.filter_by(email = email).first()
        user = User.query.filter_by(email = email).first()
        
        if admin:
            if password == user.password:
                print("admin password correct ")
                session['admin'] = True
            else:
                print("Password incorrect")
                flash("Incorrect password", 'danger')

                return "error en login post o admin con mal password"
        elif user:
            print(user.name)
            if password == user.password:
                print("user password correct ")
                session['user'] = True

        else:
            flash("No user", 'danger')
            return ("errorrrrrrr")
        
         # if the above check passes, then we know the user has the right credentials
        login_user(user)
        # login_user(user, remember=remember)

        return redirect(url_for('views.home'))
        

    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    #!! login required ??

    session.clear()
    return redirect(url_for('auth.login') )


@auth.route('/signup', methods = ['POST', 'GET'])
def signup():

    if request.method == 'GET':
        render_template('signup.html')
    elif request.method == 'POST':

        name = request.form.get('name')

        email = request.form.get('email')
        password = request.form.get('password')

        print(f"Nombre recibido: {name}")
        print(f"Email recibido: {email}")
        print(f"Password recibido: {password}")

        user = User(name=name, email = email, password=password ) # Crear un nuevo usuario

        try:
            db.session.add(user)
            db.session.commit()  # Guardar cambios

        except Exception as e:
            print("Error")
            db.session.rollback()  # Revertir cambios si hay un error
            return "Error"
        
        print("user created succesfully from signup")
        return redirect(url_for('auth.login'))
        

    # AQUI LEES EL FORM DEL USUARIO Y PONES EL USER EN LA TABLA DE USERS
    return render_template('signup.html')




