## Import App ##
from app import app
from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g
from sqlalchemy.exc import IntegrityError
from forms import TeamForm, TeamEditForm
from models import ( db, connect_db, User, Team, Athlete, Workout, Athlete_workout, Category, 
                    Equipment, Muscle, Exercise, Workout_exercise, Athlete_workout_exercise )
from utils import *


### TEAM ROUTES ###

@app.route('/teams')
def teams_show():
    """Show teams profile."""
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")

    user_id = g.user.id
    user = get_user_by_ID(user_id)
    teams = get_teams_by_user_id(user_id)

    return render_template('/teams/show_teams.html', user=user, teams=teams)

@app.route('/teams/<int:team_id>')
def team_show(team_id):
    """Show team profile."""
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")

    team = get_team_by_team_id(team_id)

    athletes = get_athletes_by_team_id(team_id)

    return render_template('teams/show_team.html', team=team, athletes=athletes)


@app.route('/teams/add', methods=["GET", "POST"])
def team_add():
    """ Add a team: Show form if GET. If valid, update message and redirect to user page. """
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")
        
    form = TeamForm()

    if form.validate_on_submit(): 
        try:
            team = add_team(form)
        except IntegrityError:
            form.name.errors = ["Team Name already taken"]
            return render_template('/teams/team_add_form.html', form=form , user=g.user)

        return redirect(f"/users/{g.user.id}")

    else:
        return render_template('/teams/team_add_form.html', form=form, user=g.user)
    return render_template('/teams/team_add_form.html', form=form, user=g.user)


@app.route('/teams/edit/<int:team_id>', methods=["GET", "POST"])
def team_edit(team_id):
    """ Add a team: Show form if GET. If valid, update message and redirect to user page. """

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    team = get_team_by_team_id(team_id)
    form = TeamEditForm(obj=team)

    if form.validate_on_submit():
        try:
            edit_team(form, team)
        except IntegrityError:
            flash("Problem updating.", 'danger')
            return render_template('/teams/edit_team_form.html', form=form)

        return redirect(f"/users/{g.user.id}")

    else:
        return render_template('/teams/edit_team_form.html', form=form, user=g.user)


@app.route('/teams/delete/<int:team_id>', methods=["POST"])
def team_delete(team_id):
    """Delete a team."""
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    delete_team(team_id)

    return redirect(f"/users/{g.user.id}")