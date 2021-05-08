## Import App ##
from app import app
from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g
from sqlalchemy.exc import IntegrityError
from models import ( db, connect_db, User, Team, Athlete, Workout, Athlete_workout, Category, 
                    Equipment, Muscle, Exercise, Workout_exercise, Athlete_workout_exercise )
from forms import (WorkoutForm, WorkoutFormStep2, WorkoutEditForm, WorkoutExerciseEditForm, 
                    AddCategoryToWorkoutForm, AddEquipmentToWorkoutForm, AddMuscleToWorkoutForm,
                    AthleteWorkoutAssignForm, WorkoutSelectForm)
from utils import *

WORKOUT = "workout_id"
athlete_workout_list = []

## WORKOUT ROUTES ##

@app.route('/workouts', methods=["GET", "POST"] )
def workouts_show():
    """ Show all workouts view """
    if g.user:
        user_id = g.user.id

    workouts = get_workouts()
    workouts1 = get_select_workouts(workouts)
    exercises = get_workouts_exercises()

    form = WorkoutSelectForm()
    form.workouts.choices = workouts1
    
    if form.validate_on_submit():
            
        workout = form.workouts.data
        return redirect(f"/workouts/{workout}")

    return render_template('/workouts/show_workouts.html', workouts=workouts, exercises=exercises, form=form, workouts1=workouts1)


@app.route('/workouts/<int:workout_id>')
def workout_show(workout_id):
    """ Show workout view """ 
    if g.user:
        user_id = g.user.id

    workout = get_workout(workout_id)
    exercises = get_workout_exercises(workout_id)

    return render_template('workouts/show_workout.html', exercises=exercises, workout=workout)


@app.route('/workouts/add', methods=["GET", "POST"])
def workout_add():
    """ Add a workout. """
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")
    
    form2 = WorkoutFormStep2()
    form= WorkoutForm()

    form2.categories.category.choices = get_select_categories()
    form2.muscles.muscle.choices = get_select_muscles()
    form2.equipment.equipment.choices = get_select_equipment()

    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        workout = Workout(name=name, description=description)
        db.session.add(workout)
        db.session.commit()
        session[WORKOUT] = workout.id
        workout_id = workout.id
        flash(f"Successfully added work out", "success")

        exercises = get_workout_exercises(workout_id)

        return render_template('workouts/workout_select_categories.html', form=form, form2=form2, description=description,
                                                                             name=name, workout=workout, exercises=exercises)
    else:
        errors = form.errors
    return render_template('workouts/workout_add_form.html',form=form, errors=errors)


@app.route('/workouts/add/select/', methods=["GET", "POST"])
def workout_select():
    """ Select Categories of exercises. """
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")
        
    form= WorkoutForm()
    form2= WorkoutFormStep2()

    workout_id = session[WORKOUT] 
    workout = Workout.query.get_or_404(workout_id)

    form2.categories.category.choices = get_select_categories()
    form2.muscles.muscle.choices = get_select_muscles()
    form2.equipment.equipment.choices = get_select_equipment()

    exercises = get_workout_exercises(workout_id)

    if form2.validate_on_submit():
        category = form2.categories.data
        muscle = form2.muscles.data
        equipment = form2.equipment.data

        return redirect('workouts/workout_show_exercises.html', category=category, muscle=muscle, equipment=equipment, 
                                                                        form=form, form2=form2, workout=workout,  exercises=exercises)
  
    return render_template('workouts/workout_select_categories.html', form=form, form2=form2, workout=workout, exercises=exercises)
    

@app.route('/workouts/add/select/exercises/<int:page_num>', methods=["GET", "POST"])
def workout_exercises_show(page_num):
    """ Show all filterd workout exercises view and call on API for exercise data """

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    ########################################################
    ### 3RD PARTY WGER API CALLS - UNCOMMENT TO ACTIVATE ###
    ### BETWEEN HASH LINES                               ###
    ########################################################
    
    # exercises_api_request
    # exercise_images_api_request()

    # add_to_db(response)
    # add_images(resp)
    
    ######################################################

    form= WorkoutForm()
    form2= WorkoutFormStep2()

    workout_id = session[WORKOUT] 
    workout = get_workout(workout_id)

    form2.categories.category.choices = get_select_categories()
    form2.muscles.muscle.choices = get_select_muscles()
    form2.equipment.equipment.choices = get_select_equipment()
   
    category_id= form2.categories.data["category"]
    category = get_category_by_id(category_id)
   
    muscle_id = form2.muscles.data["muscle"]
    muscle = get_muscle_by_id(muscle_id)
 
    equipment_id = form2.equipment.data["equipment"]
    equipment = get_equipment_by_id(equipment_id)

    exercises = get_exercises_paginated(page_num, category_id, muscle_id, equipment_id)
 
    if len(exercises.items) < 1:
        flash(f"no exercise found matching search parameters.", "warning")
        return redirect("/workouts/add/select/")

    return render_template('workouts/workout_show_exercises.html', form=form, form2=form2, exercises=exercises, 
                                                                    category=category, muscle=muscle, equipment=equipment, workout=workout)
 
@app.route('/workouts/add/select/exercises/all/<int:page_num>', methods=["GET", "POST"])
def workout_exercises_show_all(page_num):
    """ Show all filterd workout exercises view and call on API for exercise data """

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    

    form= WorkoutForm()
    form2= WorkoutFormStep2()

    workout_id = session[WORKOUT] 
    workout = get_workout(workout_id)

    form2.categories.category.choices = get_select_categories()
    form2.muscles.muscle.choices = get_select_muscles()
    form2.equipment.equipment.choices = get_select_equipment()
   
    category_id= form2.categories.data["category"]
    category = get_select_categories()
   
    muscle_id = form2.muscles.data["muscle"]
    muscle = get_select_muscles()
 
    equipment_id = form2.equipment.data["equipment"]
    equipment = get_select_equipment()
    # exercises = get_exercises_paginated(page_num, category_id, muscle_id, equipment_id)
    all_exercises = Exercise.query.paginate(per_page=21, page=page_num, error_out=True)
 
    if len(all_exercises.items) < 1:
        flash(f"no exercise found matching search parameters.", "warning")
        return redirect("/workouts/add/select/")

    return render_template('workouts/workout_show_exercises_all.html', form=form, form2=form2, all_exercises=all_exercises,
                                                                    category=category, muscle=muscle, equipment=equipment, workout=workout)


@app.route('/workouts/add/select/exercises/add/<int:exercise_id>', methods=["GET", "POST"])
def workout_exercises_add(exercise_id):
    """ Add exercise to workout """
    print("**************", exercise_id)
    workout_id = session[WORKOUT] 
    add_workout_exercise(exercise_id, workout_id)
    
    return redirect(f"/workouts/add/select/")


@app.route('/workouts/add/select/exercises/add/complete/<int:workout_id>', methods=["GET", "POST"])
def workout_complete(workout_id):
    """  Workout builder completed - redirect to workout and update session """
    session["workout_id"] = None

    return redirect(f"/workouts/{workout_id}") 


@app.route('/workouts/edit/<int:workout_id>', methods=["GET", "POST"])
def workout_edit(workout_id):
    """ Edit exercise to workout """
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")
    
    workout = get_workout(workout_id)
    workout_exercises = get_workout_exercises(workout_id)
    session[WORKOUT] = workout.id
    workout_id = workout.id
  
    form= WorkoutEditForm(obj=workout)
    form2= WorkoutExerciseEditForm(obj=workout)

    if form.validate_on_submit():
        try:
            workout.name = form.name.data
            workout.description = form.description.data
            db.session.add(workout)
            db.session.commit()
            flash(f"Successfully edited work out", "success")
            form2= WorkoutFormStep2()
            form2.categories.category.choices = get_select_categories()
            form2.muscles.muscle.choices = get_select_muscles()
            form2.equipment.equipment.choices = get_select_equipment()
  
            exercises = get_workout_exercises(workout_id)

            return render_template('/workouts/workout_edit_form.html',  form=form, form2=form2, workout=workout, exercises=exercises )
        except IntegrityError:
            flash("Problem updating.", 'danger')
            return render_template('/workouts/workout_edit_form.html', form=form)

    return render_template('/workouts/workout_edit_form.html',  form=form,  workout=workout)


    
    
   

@app.route('/workouts/edit/delete/<int:workout_id>/<int:exercise_id>', methods=["GET", "POST"])
def workout_exercises_edit_delete(exercise_id, workout_id):
    """ Add exercise to workout """
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    exercise = get_exercise_by_ID(exercise_id)
    workout = get_workout(workout_id)

    workout_exercise = get_workout_exercise(workout_id, exercise_id)
    
    delete_exercise_workout(workout_exercise, exercise, workout)
        
    return redirect(f'/workouts/edit/{workout_id}' )


@app.route('/workouts/delete/<int:workout_id>', methods=["POST"])
def workout_delete(workout_id):
    """Delete a workout."""
    
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    workout = get_workout(workout_id)
    delete_workout(workout)
    return redirect(f"/workouts")


@app.route('/workouts/athletes')
def athlete_workouts_show():
    """ Show all athlete workouts view filtered for user """

    if g.user:
        user_id = g.user.id
    
    user_id = g.user.id
    user = get_user_by_ID(user_id)
    teams = get_teams_by_user_Id(user_id)
    workouts = get_all_athlete_workouts()

    return render_template('/workouts/show_athlete_workouts.html', workouts=workouts, 
                                                                    teams=teams, user=user)


@app.route('/workouts/athletes/assign', methods=["GET", "POST"] )
def athlete_workouts_assign():
    """ Assign workout to Athlete """
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    user_id = g.user.id
    
    form = AthleteWorkoutAssignForm()
    athletes = get_athletes() 
    athletes = get_athletes_by_user_Id(athletes, user_id)

    form.athlete.choices = athletes
    form.workout.choices = [(w.id, w.name) for w in Workout.query.all()] 

    if form.validate_on_submit():
        athlete_id = add_assignment(form)
        return redirect(f'/athletes/{athlete_id}' )

    return render_template('/workouts/assign_athlete_workout_form.html', form=form)


@app.route('/workouts/athletes/assign/completed/<int:athlete_id>/<int:workout_id>', methods=["GET", "POST"] )
def athlete_workouts_completed(workout_id, athlete_id):
    """ Remove Competed Athlete Workout """
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")
  
    user_id = g.user.id

    workout = get_workout_assigned_athlete(workout_id, athlete_id)
    add_completed_athlete_workout_assignment(workout)
    return redirect(f'/athletes/{athlete_id}' )
    
    
@app.route('/workouts/athletes/delete/<int:workout_id>/<int:athlete_id>', methods=["POST"])
def athlete_workout_delete(workout_id, athlete_id):
    """Delete a workout."""
    
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    workout = get_workout_assigned_athlete(workout_id, athlete_id)
    delete_athlete_workout_assignment(workout)
    return redirect(f'/athletes/{athlete_id}' )
