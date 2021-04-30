## Import App ##
from app import app
from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g
from sqlalchemy.exc import IntegrityError
from forms import LoginForm, RegisterForm
from models import ( db, connect_db, User, Team, Athlete, Workout, Athlete_workout, Category, 
                    Equipment, Muscle, Exercise, Workout_exercise, Athlete_workout_exercise )
# from utils import *

### USER ROUTES ###

@app.route('/users/<int:user_id>')
def users_show(user_id):
    """Show user profile."""

    user = User.query.get_or_404(user_id)

    # snagging messages in order from the database;
    # user.messages won't be in order by default
    teams = (Team
                .query
                .filter(Team.user_id == user_id)
                .order_by(Team.created_on.desc())
                .all())

    return render_template('users/show_user.html', user=user, teams=teams)


