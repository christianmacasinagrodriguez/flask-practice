from unicodedata import category
from xmlrpc.client import boolean
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, login_user, logout_user, current_user
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        emal = request.form.get('emal')
        password = request.form.get('password')

        user = User.query.filter_by(emal=emal).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password! Try again!', category='error')
                return render_template("login.html")
        else:
            flash('You are not yet registered!', category='error')
            return render_template("signup.html")

    return render_template("home.html", boolean=True)

@auth.route('/logout', methods=['POST', 'GET'])
#@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.lpage'))

@auth.route('/lpage', methods=['POST', 'GET'])
def lpage():
    return render_template("login.html")

@auth.route('/spage', methods=['POST', 'GET'])
def spage():
    return render_template("signup.html")

@auth.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        emal = request.form.get('emal')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(emal=emal).first()
        if user:
            flash('Email already exists!', category='error')
            return render_template("login.html")

        elif len(emal) < 4:
            pass
        elif len(first_name) < 2:
            pass
        elif password1 != password2:
            pass
        elif len(password1) < 7:
            pass
        else:
            #add user to the database
            new_user = User(emal=emal, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    return render_template("signup.html")
