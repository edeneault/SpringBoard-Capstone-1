## Import App ##
from app import app
from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g
from sqlalchemy.exc import IntegrityError
from models import ( db, connect_db, User, Team, Athlete, Workout, Athlete_workout, Category, 
                    Equipment, Muscle, Exercise, Workout_exercise, Athlete_workout_exercise )
from forms import (WorkoutForm, WorkoutFormStep2, WorkoutEditForm, WorkoutExerciseEditForm, 
                    AddCategoryToWorkoutForm, AddEquipmentToWorkoutForm, AddMuscleToWorkoutForm,
                    AthleteWorkoutAssignForm)
from utils import *

WORKOUT = "workout_id"

## WORKOUT ROUTES ##

@app.route('/workouts')
def workouts_show():
    """ Show all workouts view """

    if g.user:
        user_id = g.user.id

    workouts = Workout.query.all()
    exercises = db.session.query(Workout.name, Exercise.name, Workout_exercise). \
                select_from(Workout). \
                join(Workout_exercise). \
                join(Exercise). \
                filter(Workout.id == Workout_exercise.workout_id). \
                all()

    return render_template('/workouts/show_workouts.html', workouts=workouts, exercises=exercises)


@app.route('/workouts/<int:workout_id>')
def workout_show(workout_id):
    """ Show workout view """
   
    workout = Workout.query.get_or_404(workout_id)
    exercises = db.session.query(Workout.name, Exercise.name, Exercise.id, Exercise.image_url, Workout_exercise). \
                select_from(Workout). \
                join(Workout_exercise). \
                join(Exercise). \
                filter(Workout.id == Workout_exercise.workout_id, Workout.id == workout_id).\
                all()

    return render_template('workouts/show_workout.html', exercises=exercises, workout=workout)


@app.route('/workouts/add', methods=["GET", "POST"])
def workout_add():
    """ Add a workout. """

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")
    
    form2 = WorkoutFormStep2()
    form= WorkoutForm()

    form2.categories.category.choices = [(c.id, c.category_name) for c in Category.query.all()] 
    form2.muscles.muscle.choices = [(m.id, m.muscle_name) for m in Muscle.query.all()] 
    form2.equipment.equipment.choices = [(e.id, e.equipment_name) for e in Equipment.query.all()] 

    if form.validate_on_submit():

        name = form.name.data
        description = form.description.data
        workout = Workout(name=name, description=description)
        db.session.add(workout)
        db.session.commit()
        session[WORKOUT] = workout.id
        workout_id = workout.id

        exercises = db.session.query(Workout.name, Exercise.name, Workout_exercise). \
                select_from(Workout). \
                join(Workout_exercise). \
                join(Exercise). \
                filter(Workout.id == Workout_exercise.workout_id, Workout.id == workout_id).all()

        flash(f"Successfully added work out", "success")
        return render_template('workouts/workout_select_categories.html', form=form, form2=form2, description=description,
                                                                             name=name, workout=workout, exercises=exercises)
    else:
        errors = form.errors
    return render_template('workouts/workout_add_form.html',form=form, errors=errors)


@app.route('/workouts/add/select/', methods=["GET", "POST"])
def workout_select():
    """ Select Categories of exercises. """
    
    form= WorkoutForm()
    form2= WorkoutFormStep2()

    workout_id = session[WORKOUT] 
    workout = Workout.query.get_or_404(workout_id)

    form2.categories.category.choices = [(c.id, c.category_name) for c in Category.query.all()] 
    form2.muscles.muscle.choices = [(m.id, m.muscle_name) for m in Muscle.query.all()] 
    form2.equipment.equipment.choices = [(e.id, e.equipment_name) for e in Equipment.query.all()] 

    exercises = db.session.query(Workout.name, Exercise.name, Workout_exercise). \
            select_from(Workout). \
            join(Workout_exercise). \
            join(Exercise). \
            filter(Workout.id == Workout_exercise.workout_id, Workout.id == workout_id).all()

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
    ### BETWEEN HASH LINES TO ACTIVATE                   ###
    ########################################################
    
    # exercises_api_request
    # exercise_images_api_request()

    # insert_to_db(response)
    # insert_images(resp)
    
    ######################################################

    form= WorkoutForm()
    form2= WorkoutFormStep2()

    workout_id = session[WORKOUT] 
    workout = Workout.query.get_or_404(workout_id)
    print(f"workout{workout}")

    form2.categories.category.choices = [(c.id, c.category_name) for c in Category.query.all()] 
    form2.muscles.muscle.choices = [(m.id, m.muscle_name) for m in Muscle.query.all()] 
    form2.equipment.equipment.choices = [(e.id, e.equipment_name) for e in Equipment.query.all()] 
   
    cat= form2.categories.data["category"]
    category = Category.query.filter(Category.id == cat).all() 
    category = category[0]
 
    mus = form2.muscles.data["muscle"]
    muscle = Muscle.query.filter(Muscle.id == mus).all() 
    muscle = muscle[0]

    equip = form2.equipment.data["equipment"]
    equipment = Equipment.query.filter(Equipment.id == equip).all() 
    equipment = equipment[0]

    exercises = Exercise.query. \
            filter(Exercise.category_id == cat, Exercise.muscle_id == mus, Exercise.equipment_id == equip ). \
            paginate(per_page=21, page=page_num, error_out=True)
    
    if len(exercises.items) < 1:
        flash(f"no exercise found matching search parameters.", "warning")
        return redirect("/workouts/add/select/")

    return render_template('workouts/workout_show_exercises.html', form=form, form2=form2, exercises=exercises, 
                                                                    category=category, muscle=muscle, equipment=equipment, workout=workout)
 


@app.route('/workouts/add/select/exercises/add/<int:exercise_id>', methods=["GET", "POST"])
def workout_exercises_add(exercise_id):
    """ Add exercise to workout """

    workout_id = session[WORKOUT] 
    
    workout_exercise = Workout_exercise(workout_id=workout_id, exercise_id=exercise_id)
    db.session.add(workout_exercise)
    db.session.commit()
    
    flash(f"Successfully added exercise to workout {workout_id}", "success")
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

    workout = Workout.query.get_or_404(workout_id)
    session[WORKOUT] = workout.id
    form= WorkoutEditForm(obj=workout)
    form2= WorkoutExerciseEditForm()

    categories = Category.query.all() 
    categories = [ (c.id, c.category_name) for c in categories]

    equipment = Equipment.query.all() 
    equipment = [ (e.id, e.equipment_name) for e in equipment]

    muscles = Muscle.query.all() 
    muscles = [ (m.id, m.muscle_name) for m in muscles]

    form2= WorkoutFormStep2()
    form2.categories.category.choices = [(c.id, c.category_name) for c in Category.query.all()] 
    form2.muscles.muscle.choices = [(m.id, m.muscle_name) for m in Muscle.query.all()] 
    form2.equipment.equipment.choices = [(e.id, e.equipment_name) for e in Equipment.query.all()] 
  
    exercises = db.session.query(Workout.name, Exercise.name, Workout_exercise). \
            select_from(Workout). \
            join(Workout_exercise). \
            join(Exercise). \
            filter(Workout.id == Workout_exercise.workout_id, Workout.id == workout_id).all()
    
    return render_template('/workouts/workout_edit_form.html',  form=form, form2=form2, workout=workout, exercises=exercises )


@app.route('/workouts/edit/delete/<int:workout_id>/<int:exercise_id>', methods=["GET", "POST"])
def workout_exercises_edit_delete(exercise_id, workout_id):
    """ Add exercise to workout """

    exercise = Exercise.query.get_or_404(exercise_id)
    workout = Workout.query.get_or_404(workout_id)

    workout_exercise = Workout_exercise.query.filter(Workout_exercise.exercise_id == exercise_id, Workout_exercise.workout_id == workout_id).all()
    workout_exercise = workout_exercise[0]
    db.session.delete(workout_exercise)
    db.session.commit()
    flash(f"Succesfully deleted exercise {exercise.id} from workout {workout.id}", 'success')
    return redirect(f'/workouts/edit/{workout_id}' )


@app.route('/workouts/delete/<int:workout_id>', methods=["POST"])
def workout_delete(workout_id):
    """Delete a workout."""
    
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    workout = Workout.query.get_or_404(workout_id)
    db.session.delete(workout)
    db.session.commit()
    flash(f"Succesfully deleted WORKOUT {workout.name.upper()}", 'success')
    return redirect(f"/workouts")


@app.route('/workouts/athletes')
def athlete_workouts_show():
    """ Show all athlete workouts view filtered for user """

    if g.user:
        user_id = g.user.id
    
    user_id = g.user.id
    user = User.query.get_or_404(user_id)
    teams = Team.query.filter(user_id == Team.user_id)
    # athletes = Athlete.query.filter(user_id == Athlete.team.user)



    workouts = db.session.query(Workout.name, Workout.description, Workout.id, Athlete.first_name, Athlete.last_name, 
                Athlete.athlete_image_url, Athlete.position, Athlete.medical_status, Athlete.team_id, Athlete.id ). \
                select_from(Workout). \
                join(Athlete_workout). \
                join(Athlete).all()
                # filter(Workout.id == Athlete_workout.workout_id, Athlete.id == Athlete_workout.athlete_id). \
                

    # workouts = Athlete_workout.query.filter( athlete.id == athlete_workout.athlete_id).all()



    print(workouts)
    

    return render_template('/workouts/show_athlete_workouts.html', workouts=workouts, 
                                                                    teams=teams, user=user)


@app.route('/workouts/athletes/assign', methods=["GET", "POST"] )
def athlete_workouts_assign():
    """ Assign workout to Athlete """

    if g.user:
        user_id = g.user.id
    
    form = AthleteWorkoutAssignForm()
  
    
    athletes = Athlete.query.all() 
    athletes = [ (a.id, a.full_name) for a in athletes]

    workouts = Workout.query.all() 
    workouts = [ (w.id, w.name) for w in workouts]

    print("**********************workouts list****************")
    print(workouts[0])

    form.athlete.choices = [(a.id, a.full_name) for a in Athlete.query.all()] 
    form.workout.choices = [(w.id, w.name) for w in Workout.query.all()] 
    if form.validate_on_submit():
        athlete_id = form.athlete.data
        print(f'**********************{athlete_id}**************')
        print(f'**********************{athlete_id}**************')
        print(f'**********************{athlete_id}**************')
        workout_id = form.workout.data
        print(f'**********************{workout_id}*************')
        print(f'**********************{workout_id}**************')
        print(f'**********************{workout_id}**************')
        athlete_workout = Athlete_workout( workout_id=workout_id, athlete_id=athlete_id)
        db.session.add(athlete_workout)
        db.session.commit()

        flash(f"Succesfully assigned WORKOUT {workout_id}", 'success')
        return redirect(f'/athletes/{athlete_id}' )

    return render_template('/workouts/assign_athlete_workout_form.html', form=form)
    
@app.route('/workouts/athletes/delete/<int:workout_id>/<int:athlete_id>', methods=["POST"])
def athlete_workout_delete(workout_id, athlete_id):
    """Delete a workout."""
    
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    workout = Athlete_workout.query.filter(Athlete_workout.athlete_id == athlete_id, Athlete_workout.workout_id == workout_id ).all()
    workout = workout[0]
    db.session.delete(workout)
    db.session.commit()
    flash(f"Succesfully deleted WORKOUT {workout.id}", 'success')
    return redirect(f'/athletes/{athlete_id}' )


@app.route('/workouts/athletes/completed/<int:workout_id>/<int:athlete_id>', methods=["POST"])
def athlete_workout_completed(workout_id, athlete_id):
    """Mark athlete workout as completed. Remove Workout from assigments."""