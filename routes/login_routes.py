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

@app.before_request
def add_user_to_g():
    """If logged in, add curr user to Flask global."""
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
            user = do_register(form)
          
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
        user = do_authentification(form)

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