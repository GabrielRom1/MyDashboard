
from flask import Blueprint,  render_template, request, jsonify, url_for, flash, session, redirect
from . import db
from .models import Admin, User


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

                return "error en login post"
        elif user:
            print(user.name)
            if password == user.password:
                print("user password correct ")
                session['user'] = True


        else:
            flash("No user", 'danger')
            return ("errorrrrrrr")

        return redirect(url_for('views.home'))
        

    return render_template('login.html')


@auth.route('/logout')
def logout():
    #!! login required ??

    session.clear()
    return redirect(url_for('auth.login') )


@auth.route('/sign-up', methods = ['POST', 'GET'])
def sign_up():

    if request.method == 'GET':
        render_template('signup.html')

    # AQUI LEES EL FORM DEL USUARIO Y PONES EL USER EN LA TABLA DE USERS
    return render_template('signup.html')




