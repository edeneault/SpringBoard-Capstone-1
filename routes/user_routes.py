## Import App ##
from app import app
from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g
from sqlalchemy.exc import IntegrityError
from forms import LoginForm, RegisterForm, UserEditForm
from models import ( db, connect_db, User, Team, Athlete, Workout, Athlete_workout, Category, 
                    Equipment, Muscle, Exercise, Workout_exercise, Athlete_workout_exercise )
from utils import *

### USER ROUTES ###

@app.route('/users/<int:user_id>')
def users_show(user_id):
    """Show user profile."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    user = get_user_by_ID(user_id)

    teams = get_teams_by_user_id(user_id)
 
    return render_template('users/show_user.html', user=user, teams=teams)


@app.route('/users/edit/<int:user_id>', methods=["GET", "POST"])
def users_edit(user_id):
    """Show edit profile."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    user = get_user_by_ID(user_id)

    form = UserEditForm(obj=user)

    if form.validate_on_submit():
        try:
            edit_user(form, user)

        except IntegrityError:
            flash("Problem updating.", 'danger')
            return render_template('/users/user_edit_form.html', form=form, user_id=g.user.id, team=team)

        return redirect(f"/users/{g.user.id}")

    else:
        return render_template('/users/user_edit_form.html', form=form)
