from flask import Blueprint, render_template, redirect, url_for, request, session
from .models import Admin, User, Service, Appointment
from . import db
from datetime import datetime
from flask_login import login_required, current_user

#!! check flask-wtf

#se va a definir los blueprints, son un monton de rutas para poder dividir el codigo
views = Blueprint('views', __name__)


@views.route('/')
def index():
    admin = Admin.query.all()

    # 1, 0, None
    print("llego aqui")

    # si no hay nada en la db entonces a esa ruta
    if not admin:
        return redirect(url_for('install.finstall'))

    return render_template('index.html')


@views.route('/home' , methods = ['GET'])
@login_required
def home():
    if request.method == 'GET':
        print("EN EL GET DE HOME")
        if 'admin' in session:
            print("es admin")

    access = session.get('admin')
    
    
    return render_template('home.html', current_user=current_user)



@views.route('/settings', methods = ['GET'])
@login_required
def settings():
    if request.method == 'GET':
        print("Settings get")
        if not "admin" in session:
            print("cannot access")
            #!! o mandar a otro lado o modificar el html para user settings
        else:
            print("hello!!")
            return render_template('settings.html')
        

@views.route('/month', methods = ['GET'])
@login_required
def month():
    if request.method == 'GET':
        print('month get')
    return "month"


