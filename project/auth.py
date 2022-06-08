from flask import Flask, Blueprint, redirect, render_template, request, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(email=email).first()

        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login'))

        # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=remember)
        return redirect(url_for('todo.hello_world'))

    return render_template('login.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        # filter takes two possitional arguments while filter_by takes one
        # checks for unique email and name
        user = User.query.filter((User.email == email)
                                 | (User.name == name)).first()

        if user:  # if a user with that email already exists
            flash('Email or Name already exists')
            return redirect(url_for('auth.signup'))

        # creating new user and hashing password
        new_user = User(email=email,  password=generate_password_hash(
            password, method='sha256'), name=name)

        # adding user to database
        db.session.add(new_user)
        db.session.commit()

    return render_template('signin.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
