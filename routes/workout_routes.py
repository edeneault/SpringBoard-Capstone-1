## Import App ##
from app import app
from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g
from models import ( db, connect_db, User, Team, Athlete, Workout, Athlete_workout, Category, 
                    Equipment, Muscle, Exercise, Workout_exercise, Athlete_workout_exercise )
# from utils import *

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

    exercises = db.session.query(Workout.name, Exercise.name, Workout_exercise). \
                select_from(Workout). \
                join(Workout_exercise). \
                join(Exercise). \
                filter(Workout.id == Workout_exercise.workout_id, Workout.id == workout_id).all()

    print(exercises)

    return render_template('workouts/show_workout.html', exercises=exercises, workout=workout)