
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


        # data = request.get_json()
    
        # # Procesa los datos
        # email = data.get('email', 'No email provided')
        email = request.form.get('email')
        password = request.form.get('password')
        # password = data.get('password', 'No password provided')
        
        admin = Admin.query.filter_by(email = email).first()
        user = Admin.query.filter_by(email = email).first()
        
        if admin:
            print(admin.name)
            if password == admin.password:
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
        if create_user(True):
            print("user created succesfully from signup")
            return redirect(url_for('auth.login'))
        else:
            print("error when signup create user")


    # AQUI LEES EL FORM DEL USUARIO Y PONES EL USER EN LA TABLA DE USERS
    return render_template('signup.html')




