## Import App ##
from app import app
from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g
from models import ( db, connect_db, User, Team, Athlete, Workout, Athlete_workout, Category, 
                    Equipment, Muscle, Exercise, Workout_exercise, Athlete_workout_exercise )
from forms import (WorkoutForm, AddCategoryToWorkoutForm, AddMuscleToWorkoutForm, AddEquipmentToWorkoutForm,
                    WorkoutFormStep2)
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
                filter(Workout.id == Workout_exercise.workout_id, Workout.id == workout_id).all()

   

  


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
        print("*************** in validate ***************")
        
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
        print("*************** workout ***************")
        print(workout)
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
    print("*************** in select ***************")
    print(workout)
    form2.categories.category.choices = [(c.id, c.category_name) for c in Category.query.all()] 
    form2.muscles.muscle.choices = [(m.id, m.muscle_name) for m in Muscle.query.all()] 
    form2.equipment.equipment.choices = [(e.id, e.equipment_name) for e in Equipment.query.all()] 

   
    exercises = db.session.query(Workout.name, Exercise.name, Workout_exercise). \
            select_from(Workout). \
            join(Workout_exercise). \
            join(Exercise). \
            filter(Workout.id == Workout_exercise.workout_id, Workout.id == workout_id).all()

    if form2.validate_on_submit():
        print("*************** in validate ***************")

        category = form2.categories.data
        muscle = form2.muscles.data
        equipment = form2.equipment.data

        print(category, muscle, equipment)
        
        print("************redirecting**********")
        return redirect('workouts/workout_show_exercises.html', category=category, muscle=muscle, equipment=equipment, 
                                                                        form=form, form2=form2, workout=workout,  exercises=exercises)
  
    return render_template('workouts/workout_select_categories.html', form=form, form2=form2, workout=workout, exercises=exercises)
    


@app.route('/workouts/add/select/exercises/<int:page_num>', methods=["GET", "POST"])
def workout_exercises_show(page_num):
    """ Show all filterd workout exercises view and call on API for exercise data """

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

     ### 3RD PARTY WGER API CALLS - UNCOMMENT TO ACTIVATE##
    # exercises_api_request
    # exercise_images_api_request()

    # insert_to_db(response)
    # insert_images(resp)

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


   
    print("**********************************************************")
    # print(category["category"])
    # exercises = Exercise.query.paginate(per_page=21, page=page_num, error_out=True)

    
    
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
    print("**********in workout_exercise_add*************")
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




    