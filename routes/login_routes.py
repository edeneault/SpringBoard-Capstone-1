## Import App ##
from app import app
from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g
from sqlalchemy.exc import IntegrityError
from datetime import datetime as dt
import datetime
from forms import LoginForm, RegisterForm
from models import ( db, connect_db, User, Team, Athlete, Workout, Athlete_workout, Category, 
                    Equipment, Muscle, Exercise, Workout_exercise, Athlete_workout_exercise )
from utils import *

CURR_USER_KEY = "curr_user"


### REGISTER - LOGIN - LOGOUT ###

def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]

def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id

@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])
     

    else:
        g.user = None

@app.route('/users/register', methods=["GET", "POST"])
def register_user():
    """Handle user register."""

    form = RegisterForm()
    if form.validate_on_submit():
        try:
            user = User.register(
                username=form.username.data,
                password=form.password.data,
                email=form.email.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                image_url=form.image_url.data or User.image_url.default.arg,
                header_image_url=form.header_image_url.data or User.header_image_url.default.arg
            )
            
            db.session.add(user)
            db.session.commit()
          
        except IntegrityError:
            flash("Username already taken", 'danger')
            return render_template('/users/login_user_form.html', form=form)

        do_login(user)
        flash("Welcome to GYM HERO, ADD your first Team to gwt started", "info")
        return redirect("/")

    else:
        return render_template('users/register_user_form.html', form=form)
    return render_template('/users/register_user_form.html', form=form)


@app.route("/users/login", methods=['GET', 'POST'])
def login_user():
    """ Login View and Handle Login """

    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.authenticate(form.username.data,
                                 form.password.data)

        if user:
            do_login(user)
            flash(f"Hello, {user.username}!", "success")
            return redirect(f"/users/{user.id}")
        else:
            form.username.errors = ["Invalid username/password."]
            flash("Invalid credentials.", 'danger')
            return render_template("users/login_user_form.html", form=form)

    return render_template("/users/login_user_form.html", form=form)


@app.route('/logout')
def logout_user():
    """Handle logout of user."""
    flash(f"Logged Out. Goodbye!", "success")
    do_logout()
    return redirect("/")