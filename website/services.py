from flask import Blueprint, render_template, redirect, url_for, request, session
from .models import Admin, User, Service, Appointment
from . import db
from datetime import datetime
from flask_login import login_required, current_user

services = Blueprint('services', __name__)


@services.route('/create_service', methods = ['GET', 'POST'])
@login_required
def create_service():

    if session.get('admin'):

        if request.method == 'GET':
            print('create get')
            return render_template('form_service.html', create = 1)
        
        if request.method == 'POST':
            
            print("create post")
            name = request.form.get('name')
            price = request.form.get('price')
            cost = request.form.get('cost')

            category = request.form.get('category')

            print(name)
            print(price)
            print(cost)
            print(category)

            # Convertir la cadena a un objeto datetime
    
            new_service = Service(name=name, price=price, cost=cost, category=category)
            db.session.add(new_service)
            db.session.commit()  # Guardar cambios

            print("Service", name, "Added")

            return redirect(url_for('services.create_service'))
        
    return "create_services"


@services.route('/view_services', methods = ['GET'])
@login_required
def view_services():

    if session.get('admin'):

        services = Service.query.all()

        if not services:
            print("empty services")
        else:
            print(services)

        return render_template( 'view_services.html', services_list = services)

@services.route('/edit_service/<service_id>', methods = ['GET', 'POST'])
@login_required
def edit_service(service_id):

    if session.get('admin'):
        if request.method == 'GET':
            return render_template('form_service.html', service_id=service_id,create = 0)
        
        service = Service.query.filter_by(id=service_id).first()

        if request.method == 'POST':
            print("edit post")
            name = request.form.get('name')
            price = request.form.get('price')
            cost = request.form.get('cost')

            category = request.form.get('category')

            # Modificar el campo
            service.name = name
            service.price = price
            service.cost = cost
            service.category = category

            # Guardar cambios en la base de datos
            try:
                db.session.flush()

                db.session.commit()
                return redirect(url_for("services.view_services"))
            except Exception as e:
                db.session.rollback()  # Revertir cambios si hay un error
                return e

    return "edit page" + service_id

    
@services.route('/delete_service/<service_id>', methods = ['GET', 'POST'])
@login_required
def delete_service(service_id):

    if session.get('admin'):

        print(service_id)

        service = Service.query.filter_by(id=service_id).first()

        if service:
            print("delete", service)
            db.session.delete(service)
            db.session.commit()

        else:
            return ("error")

        return redirect(url_for("services.view_services"))

