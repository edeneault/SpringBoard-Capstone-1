## Import App and needed modules ##
from app import app

from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g
from sqlalchemy.exc import IntegrityError
from models import ( db, connect_db, User, Team, Athlete, Workout, Athlete_workout, Category, 
                    Equipment, Muscle, Exercise, Workout_exercise, Athlete_workout_exercise )
from forms import ExerciseForm, ExerciseEditForm
from utils import *
import requests

NEXT = "next"
NEXT_IMAGE = "next_image"
ALT_IMAGE= "https://w7.pngwing.com/pngs/165/675/png-transparent-black-person-lifting-barbell-illustration-computer-icons-physical-exercise-physical-fitness-personal-trainer-fitness-centre-muscle-building-routine-miscellaneous-logo-monochrome-thumbnail.png"

@app.route('/exercises/<int:page_num>')
def exercises_show(page_num):
    """ Show all exercises view and call on API for exercise data """
    
    ### 3RD PARTY WGER API CALLS - UNCOMMENT TO ACTIVATE##

    ### ONLY RUN resp = exercise_images_api_request() ONCE! it will make 5 requests, it may fail on the last request ###
    # response = exercises_api_request()
    # resp = exercise_images_api_request()

    # insert_to_db(response)
    # insert_images(resp)

    exercises = Exercise.query.paginate(per_page=21, page=page_num, error_out=True)

    return render_template('/exercises/show_exercises.html',  exercises=exercises)


@app.route('/exercises/exercise/<int:exercise_id>')
def exercise_show(exercise_id):
    """ Show exercise by ID """
    exercise = get_exercise_by_ID(exercise_id)
    image_id = exercise.wger_id
    image = get_exercise_image(exercise_id, exercise)

    return render_template('exercises/show_exercise.html', exercise=exercise, image=image, alt_image=ALT_IMAGE)



@app.route('/exercises/add', methods=["GET", "POST"])
def exercise_add():
    """ Add an exercise. """

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")
    
    user = g.user
    page_num = 1
    exercises = Exercise.query.paginate(per_page=21, page=page_num, error_out=True)

    categories = get_select_categories()
    equipment = get_select_equipment()
    muscles = get_select_muscles()

    form = ExerciseForm()
    form.category_id.choices = categories
    form.equipment_id.choices = equipment
    form.muscle_id.choices = muscles


    if form.validate_on_submit():
        try:
            exercise = add_exercise(form)

        except:
            flash("Something went wrong", "danger")
            return render_template('/exercises/exercise_add_form.html', form=form)

        return redirect(f"/exercises/exercise/{exercise.id}")

    else:
        return render_template('/exercises/exercise_add_form.html', form=form, exercises=exercises)
    return render_template('/exercises/exercise_add_form.html', form=form)



@app.route('/exercises/edit/<int:exercise_id>', methods=["GET", "POST"])
def exercise_edit(exercise_id):
    """ Edit an exercise. """

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")
    
    user = g.user
    categories = get_select_categories()
    equipment = get_select_equipment()
    muscles = get_select_muscles()
    exercise = get_exercise_by_ID(exercise_id)
    image = get_exercise_image(exercise_id, exercise)

    form = ExerciseEditForm(obj=exercise)
    form.category_id.choices = categories
    form.equipment_id.choices = equipment
    form.muscle_id.choices = muscles

    if form.validate_on_submit():
        try:
            edit_exercise(form, exercise)
        except IntegrityError:
            flash("Problem updating.", 'danger')
            return redirect(f"/exercises/show_exercise/{exercise.id}")
        return render_template(f"/exercises/show_exercise.html", form=form, image=image, exercise=exercise)

    else:
        return render_template('/exercises/exercise_edit_form.html', form=form, exercise=exercise, image=image)


@app.route('/exercises/delete/<int:exercise_id>', methods=["POST"])
def exercise_delete(exercise_id):
    """Delete an exercise."""
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    delete_exercise(exercise_id)
    
    return redirect(f"/exercises/1")
