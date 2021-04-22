## Import App ##
from app import app
from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g
from models import ( db, connect_db, User, Team, Athlete, Workout, Athlete_workout, Category, 
                    Equipment, Muscle, Exercise, Workout_exercise, Athlete_workout_exercise )
# from utils import *


## ATHLETE ROUTES ##

@app.route('/athletes')
def athletes_show():
    """Show athletes profile."""
    user_id = g.user.id
    user = User.query.get_or_404(user_id)
    teams = Team.query.filter(user_id == Team.user_id)

    return render_template('/athletes/show_athletes.html', user=user, teams=teams)

@app.route('/athletes/<int:athlete_id>')
def athlete_show(athlete_id):
    """Show team profile."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")

    # user_id = g.user

    # user = User.query.get_or_404(user_id)

    athlete = Athlete.query.get_or_404(athlete_id)

    # snagging athletes in order from the database;
    # team.athletes won't be in order by default
    # athletes = (Athlete
    #             .query
    #             .filter(Athlete.team_id == team_id)
    #             .order_by(Athlete.created_on.desc())
    #             .all())

    return render_template('athletes/show_athlete.html', athlete=athlete)