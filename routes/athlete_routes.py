## Import App ##
from app import app
from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g
from models import ( db, connect_db, User, Team, Athlete, Workout, Athlete_workout, Category, 
                    Equipment, Muscle, Exercise, Workout_exercise, Athlete_workout_exercise )
from forms import AthleteForm
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

    athlete = Athlete.query.get_or_404(athlete_id)


    return render_template('athletes/show_athlete.html', athlete=athlete)


@app.route('/athletes/add', methods=["GET", "POST"])
def athlete_add():
    """ Add an Athlete: Show form if GET. If valid, update message and redirect to user page. """

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")
    
    user = g.user
    teams = user.teams
    print(teams)
    form = AthleteForm()

    teams = [(t.id, t.name) for t in teams]
    form.team_id.choices = teams
    print(teams)

    if form.validate_on_submit():
        try:
            athlete = Athlete(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                team_id= form.team_id.data,
                position=form.position.data,
                height=form.height.data,
                weight=form.weight.data,
                athlete_image_url=form.athlete_image_url.data,
                medical_status=form.medical_status.data
            )
            print(athlete)
            db.session.add(athlete)
            db.session.commit()
            print(athlete)

        except:
            flash("Something went wrong", "danger")
            return render_template('/athletes/athlete_add_form.html', form=form)

        return redirect(f"/users/{g.user.id}")

    else:
        return render_template('/athletes/athlete_add_form.html', form=form)
    return render_template('/athletes/athlete_add_form.html', form=form)

