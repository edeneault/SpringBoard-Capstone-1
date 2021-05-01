## Import App ##
from app import app
from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g
from sqlalchemy.exc import IntegrityError
from models import ( db, connect_db, User, Team, Athlete, Workout, Athlete_workout, Category, 
                    Equipment, Muscle, Exercise, Workout_exercise, Athlete_workout_exercise )
from forms import AthleteForm, AthleteEditForm
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
    """Show athlete profile."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/home")

    athlete = Athlete.query.get_or_404(athlete_id)

    user_id = g.user.id
    user = User.query.get_or_404(user_id)

    team = Team.query.filter(Team.id == athlete.team_id)
  
    
    athlete_workouts = (Athlete_workout
            .query
            .filter(athlete_id == athlete.id)
            .all())


   
    workouts = db.session.query(Athlete_workout.id.label("athlete_workout_id"), Workout.name, Workout.description, Workout.id.label("workout_id"), Athlete.first_name, Athlete.last_name, 
                Athlete.athlete_image_url, Athlete.position, Athlete.medical_status, Athlete.team_id, Athlete.id ). \
                select_from(Workout). \
                join(Athlete_workout). \
                join(Athlete). \
                filter(Workout.id == Athlete_workout.workout_id). \
                all()


    return render_template('athletes/show_athlete.html', workouts=workouts, athlete_workouts=athlete_workouts,
                                                                    team=team, athlete=athlete, user=user)


@app.route('/athletes/add', methods=["GET", "POST"])
def athlete_add():
    """ Add an Athlete: Show form if GET. If valid, add athlete and redirect to user page. """

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

        return redirect(f"/athletes")

    else:
        return render_template('/athletes/athlete_add_form.html', form=form)




@app.route('/athletes/edit/<int:athlete_id>', methods=["GET", "POST"])
def athlete_edit(athlete_id):
    """ Edit an Athlete: Show form if GET. If valid, update athlete and redirect to user page. """

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")
    
    athlete = Athlete.query.get_or_404(athlete_id)

    user = g.user
    teams = user.teams
 
    form = AthleteEditForm(obj=athlete)

    teams = [(t.id, t.name) for t in teams]
    form.team_id.choices = teams
    print(teams)

    if form.validate_on_submit():
        try:
         
            athlete.first_name=form.first_name.data,
            athlete.last_name=form.last_name.data,
            athlete.email=form.email.data,
            athlete.team_id= form.team_id.data,
            athlete.position=form.position.data,
            athlete.height=form.height.data,
            athlete.weight=form.weight.data,
            athlete.athlete_image_url=form.athlete_image_url.data,
            athlete.medical_status=form.medical_status.data
          
            db.session.add(athlete)
            db.session.commit()
            flash(f"Succesfully updated TEAM profile {athlete.full_name}", 'success')

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

    
    athlete = Athlete.query.get(athlete_id)
    db.session.delete(athlete)
    db.session.commit()

    return redirect("/athletes")