from flask import Blueprint, render_template, redirect, url_for, request, session
from .models import Admin, User, Service, Appointment
from . import db
from datetime import datetime


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
def home():
    #!! login required

    if request.method == 'GET':
        print("EN EL GET DE HOME")
        if 'admin' in session:
            print("es admin")

    access = session.get('admin')
    

    return render_template('home.html', access=access)



@views.route('/settings', methods = ['GET'])
def settings():
    #!! login required

    if request.method == 'GET':
        print("Settings get")
        if not "admin" in session:
            print("cannot access")
        else:
            print("hello!!")
            return render_template('settings.html')
        

@views.route('/month', methods = ['GET'])
def month():
    if request.method == 'GET':
        print('month get')
    return "month"


