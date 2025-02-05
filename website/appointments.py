from flask import Blueprint, render_template, redirect, url_for, request, session
from .models import Admin, User, Service, Appointment
from . import db
from datetime import datetime
from flask_login import login_required, current_user


appointments = Blueprint('appointments', __name__)

@appointments.route('/view_appointments', methods = ['GET'])
@login_required
def view_appointments():


    


@appointments.route('/delete_appointments', methods = ['GET'])
@login_required
def delete_appintments():

    if session.get('admin'):
        print("se puede")
    
    pass



@appointments.route('/create_appointment', methods = ['GET'])
@login_required
def create_appintment():

    if session.get('admin'):
        print("se puede")
    
    pass





