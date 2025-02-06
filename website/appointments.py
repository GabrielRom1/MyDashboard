from flask import Blueprint, render_template, redirect, url_for, request, session
from .models import Admin, User, Service, Appointment
from . import db
from datetime import datetime
from flask_login import login_required, current_user


appointments = Blueprint('appointments', __name__)



    


@appointments.route('/delete_appointments', methods = ['GET'])
@login_required
def delete_appintments():

    if session.get('admin'):
        print("se puede")
    
    pass





@appointments.route('/create_appointment', methods = ['GET', 'POST'])
@login_required
def create_appointment():

    if session.get('admin'):

        if request.method == 'GET':
            clients = User.query.all()
            services = Service.query.all()
            
            return render_template('form_appointment.html', clients = clients, services=services, create = True)

        elif request.method == 'POST':
            name = request.form.get('name')
            date = request.form.get('date')
            hour = request.form.get('hour')
            client = request.form.get('client')
            service = request.form.get('service')
            tip = request.form.get('tip')

            print(service)
            print(name)

            
            user = User.query.filter_by(name=client).first() #!!ojo cambiar a algo que no se repita
            service_obj = Service.query.filter_by(name=service).first()
            print(service_obj)
            if user and service:

                # cambiar lo de id para que sea un id unico
                appointment = Appointment( date=date, hour=hour, user_id=user.id, service_id=service_obj.id, name=name) 
            # 
            # Agregar el usuario a la base de datos
            try:
                db.session.add(appointment)
                db.session.commit()  # Guardar cambios
                
                return redirect(url_for("appointments.view_appointments"))
                
            except Exception as e:
                print("Error")
                db.session.rollback()  # Revertir cambios si hay un error
                print(e)
                return "Error"
    
    return "access denied"


@appointments.route('/view_appointments', methods = ['GET'])
@login_required
def view_appointments():
    
    if session.get('admin'):
        appointment_list = Appointment.query.all()
        if not appointment_list:
            print("users empty")
        
        else:
            print(appointment_list)

        return render_template('appointments.html', appointment_list = appointment_list)

    else:
        return ("access to view users denied")






@appointments.route('/edit_appointment/<appointment_id>', methods = ['GET', 'POST'])
@login_required
def edit_appointment(appointment_id):
    pass





