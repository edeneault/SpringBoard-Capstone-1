import os

from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError
# import requests


from forms import LoginForm, RegisterForm
from models import ( db, connect_db, User, Team, Athlete, Workout, Athlete_workout, Category, 
                    Equipment, Muscle, Exercise, Workout_exercise, Athlete_workout_exercise )
from utils import *



CURR_USER_KEY = "curr_user"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgres:///gymhero'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")
app.config['WTF_CSRF_ENABLED'] = True
# toolbar = DebugToolbarExtension(app)

connect_db(app)
# db.create_all() 

# import declared routes
import login_routes



### TIMER ROUTE ###
@app.route('/timers')
def timers():
    """ Show timers homepage: """

    return render_template('timers.html')


### HOME ROUTE and ERROR ROUTE ###
@app.route('/')
def homepage():
    """Show homepage:

    - anon users: no messages
    - logged in: 100 most recent messages of followed_users
    """
    form = LoginForm()
    form1 = RegisterForm()
    # if g.user:
    #     following_id_user_id = [
    #         follow.id for follow in g.user.following] + [g.user.id]

    #     messages = (Message
    #                 .query
    #                 .filter(Message.user_id.in_(following_id_user_id))
    #                 .order_by(Message.timestamp.desc())
    #                 .limit(100)
    #                 .all())

    #     liked_msg_ids = [msg.id for msg in g.user.likes]

    return render_template('home.html', form=form, form1=form1)

    # else:
    #     return render_template('home-anon.html')


@app.errorhandler(404)
def page_not_found(e):
    """ Show 404 NOT FOUND page. """

    return render_template('404.html'), 404