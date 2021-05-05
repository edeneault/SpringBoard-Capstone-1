## Import App ##
from app import app
from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g
from sqlalchemy.exc import IntegrityError
from models import ( db, connect_db, User, Team, Athlete, Workout, Athlete_workout, Category, 
                    Equipment, Muscle, Exercise, Workout_exercise, Athlete_workout_exercise )
from forms import AthleteForm, AthleteEditForm
from utils import *


## ATHLETE ROUTES ##

@app.route('/athletes')
def athletes_show():
    """Show athletes profile."""
    user_id = g.user.id
    user = get_user_by_ID(user_id)
    teams = get_teams_by_user_id(user_id)
    return render_template('/athletes/show_athletes.html', user=user, teams=teams)

@app.route('/athletes/<int:athlete_id>')
def athlete_show(athlete_id):
    """Show athlete profile."""
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")

    user_id = g.user.id

    athlete = get_athlete_by_athlete_id(athlete_id)
    user = get_user_by_ID(user_id)
    team = get_team_by_athlete_id(athlete)
    athlete_workouts = get_athlete_workouts(athlete_id, athlete)
    workouts = get_workouts_by_athlete_id()

    return render_template('athletes/show_athlete.html', workouts=workouts, athlete_workouts=athlete_workouts,
                                                                    team=team, athlete=athlete, user=user)

@app.route('/athletes/add', methods=["GET", "POST"])
def athlete_add():
    """ Add an Athlete: Show form if GET. If valid, add athlete and redirect to user page. """
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")
    
    user = g.user
    user_id = g.user.id
    teams = user.teams

    form = AthleteForm()
    teams = [(t.id, t.name) for t in teams]    
    form.team_id.choices = teams

    if form.validate_on_submit():
        try:
            athlete = add_athlete(form)
        except:
            flash("Something went wrong", "danger")
            return render_template('/athletes/athlete_add_form.html', form=form)

        return redirect(f"/athletes")

    else:
        return render_template('/athletes/athlete_add_form.html', form=form)




@app.route('/athletes/edit/<int:athlete_id>', methods=["GET", "POST"])
def athlete_edit(athlete_id):
    """ Edit an Athlete: Show form if GET. If valid, update athlete and redirect to user page. """
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")
    
    athlete = get_athlete_by_athlete_id(athlete_id)

    user = g.user
    teams = user.teams
 
    form = AthleteEditForm(obj=athlete)

    teams = [(t.id, t.name) for t in teams]
    form.team_id.choices = teams

    if form.validate_on_submit():
        try:
            edit_athlete(form, athlete)

        except IntegrityError:
            flash("Something went wrong", "danger")
            return render_template('/athletes/athlete_edit_form.html', form=form)

        return redirect(f"/athletes/{athlete.id}")

    else:
        return render_template('/athletes/athlete_edit_form.html', form=form, athlete=athlete)



@app.route('/athletes/delete/<int:athlete_id>', methods=["POST"])
def athlete_delete(athlete_id):
    """Delete an athlete."""
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    delete_athlete(athlete_id)

    return redirect("/athletes")