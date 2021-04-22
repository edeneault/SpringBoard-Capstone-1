## Import App ##
from app import app
from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g
from models import ( db, connect_db, User, Team, Athlete, Workout, Athlete_workout, Category, 
                    Equipment, Muscle, Exercise, Workout_exercise, Athlete_workout_exercise )
# from utils import *


### TEAM ROUTES ###

@app.route('/teams')
def teams_show():
    """Show teams profile."""
    user_id = g.user.id
    print(user_id)
    user = User.query.get_or_404(user_id)

    # snagging messages in order from the database;
    # user.messages won't be in order by default
    teams = (Team
                .query
                .filter(Team.user_id == user_id)
                .order_by(Team.created_on.desc())
                .all())

    return render_template('/teams/show_teams.html', user=user, teams=teams)



@app.route('/teams/<int:team_id>')
def team_show(team_id):
    """Show team profile."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")

    # user_id = g.user

    # user = User.query.get_or_404(user_id)

    team = Team.query.get_or_404(team_id)

    # snagging athletes in order from the database;
    # team.athletes won't be in order by default
    athletes = (Athlete
                .query
                .filter(Athlete.team_id == team_id)
                .order_by(Athlete.created_on.desc())
                .all())

    return render_template('teams/show_team.html', team=team, athletes=athletes)