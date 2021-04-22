## Import App ##
from app import app
from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g

from models import ( db, connect_db, User, Team, Athlete, Workout, Athlete_workout, Category, 
                    Equipment, Muscle, Exercise, Workout_exercise, Athlete_workout_exercise )
# from utils import *
import requests

NEXT = "next"

CATEGORY_OBJ = { "Abs": 1, "Arms": 2, "Back": 3, "Calves": 4, "Chest": 5, "Legs": 6, "Shoulders": 7 }

EQUIPMENT_OBJ = {   "Barbell": 1, "Bench": 2, "Dumbbell": 3, "Gym mat": 4, "Incline bench": 5, "Kettlebell": 6,
                    "none (bodyweight exercise)": 7, "Pull-up bar": 8, "Swiss Ball": 9, "SZ-Bar": 10 }

MUSCLE_OBJ = {  "Anterior deltoid": 1,  "Biceps brachii": 2, "Biceps femoris": 3, "Brachialis": 4, "Gastrocnemius": 5,
                "Gluteus maximus": 6, "Latissimus dorsi": 7, "Obliquus externus abdominis": 8, "Pectoralis major": 9,
                "Quadriceps femoris": 10, "Rectus abdominis": 11, "Serratus anterior": 12, "Soleus": 13, "Trapezius": 14,
                 "Triceps brachii": 15 }


@app.route('/exercises')
def exercises_show():
    """ Show all exercises view """
    
    user_id = g.user.id

    response = requests.get("https://wger.de/api/v2/exerciseinfo/?language=2", timeout=2)

    response = response.json()

    session[NEXT] = response["next"]

    response = response["results"]

    

    exercises_resp = []

    for exercise in response:
        name = exercise["name"]
        description = exercise["description"]
        category = exercise["category"]["name"]
        if not exercise["equipment"]:
           equipment = 1
        else:
            equipment = exercise["equipment"][0]["name"]

        if not exercise["muscles"]:
           muscle = 1
        else:
            muscle = exercise["muscles"][0]["name"]   

        for cat in CATEGORY_OBJ.keys():
            if cat == category:
                category = CATEGORY_OBJ.get(cat, 1)

        for equip in EQUIPMENT_OBJ.keys():
            if equip == equipment:
                equipment = EQUIPMENT_OBJ.get(equip, 7)
        
        for musl in MUSCLE_OBJ.keys():
            if musl == muscle:
                muscle = MUSCLE_OBJ.get(musl, 11)

        # equipment = ( equip["name"] for equip in exercise["equipment"] if equip == equipment )
        try:
            exercise = Exercise(name=name, description=description, category_id=category, equipment_id=equipment, muscle_id=muscle)
            db.session.add(exercise)
            db.session.commit()
        except:
            continue



        # exercises_resp.append(exercise)
     


    exercises = Exercise.query.all()

    return render_template('/exercises/show_exercises.html',  exercises=exercises)


