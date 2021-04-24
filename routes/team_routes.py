## Import App ##
from app import app
from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g
from forms import TeamForm
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

    print(teams)

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


@app.route('/teams/add', methods=["GET", "POST"])
def team_add():
    """ Add a team: Show form if GET. If valid, update message and redirect to user page. """

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")
        

    form = TeamForm()

    if form.validate_on_submit():
        try:
            team = Team(
                name=form.name.data,
                location=form.location.data,
                discipline=form.discipline.data,
                team_image_url=form.team_image_url.data,
                user_id = g.user.id
            )
            db.session.add(team)
            db.session.commit()
            print(team)

        except IntegrityError:
            form.username.errors = ["Team Name already taken"]
            return render_template('/teams/team_add_form.html', form=form , user=g.user)

        return redirect(f"/users/{g.user.id}")

    else:
        return render_template('/teams/team_add_form.html', form=form, user=g.user)
    return render_template('/teams/team_add_form.html', form=form, user=g.user)