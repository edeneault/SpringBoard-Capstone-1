## Import App and needed modules ##
from app import app

from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g
from models import ( db, connect_db, User, Team, Athlete, Workout, Athlete_workout, Category, 
                    Equipment, Muscle, Exercise, Workout_exercise, Athlete_workout_exercise )
from utils import *
import requests

NEXT = "next"
NEXT_IMAGE = "next_image"

@app.route('/exercises/<int:page_num>')
def exercises_show(page_num):
    """ Show all exercises view and call on API for exercise data """
    
    # user_id = g.user.id

    ## API request for exercises - offset 5 every call ##
    # if NEXT in session:
    #     url = session[NEXT]  
    #     response = requests.get(url=url, timeout=1.25)
    #     response = response.json()
    #     session[NEXT] = response["next"]
    #     response = response["results"]
    # else:
    #     response = requests.get("https://wger.de/api/v2/exerciseinfo/?limit=5&language=2", timeout=1.25)
    #     response = response.json()
    #     session[NEXT] = response["next"]
    #     response = response["results"]


    ## API request for image - offset 20 every call ##
    # print(NEXT_IMAGE)
    
    # if NEXT_IMAGE in session:
        
    #     if session[NEXT_IMAGE] != None:
    #         url = session[NEXT_IMAGE] 
    #     else:
    #         url = "https://wger.de/api/v2/exerciseimage/?is_main=True"
     
    #     resp = requests.get(url=url, timeout=1.25)
      
    #     resp = resp.json()
    #     session[NEXT_IMAGE] = resp["next"]
    #     resp = resp["results"]
    #     print(resp)
    # else:
    #     resp = requests.get("https://wger.de/api/v2/exerciseimage/?is_main=True", timeout=1.25)
    #     resp = resp.json()
    #     session[NEXT_IMAGE] = resp["next"]
    #     resp = resp["results"]
    #     print(resp)

    # insert_to_db(response)
    # insert_images(resp)

    exercises = Exercise.query.paginate(per_page=21, page=page_num, error_out=True)
    print("********************************************")
    print(exercises.items[0].name)


    return render_template('/exercises/show_exercises.html',  exercises=exercises)


# @app.route('/thread/<int:page_num>')
# def thread(page_num):
#     threads = Thread.query.paginate(per_page=5, page=page_num, error_out=True)

#     return render_template('index.html', threads=threads)




@app.route('/exercises/exercise/<int:exercise_id>')
def exercise_show(exercise_id):
    """ Show exercise by ID """
    ALT_IMAGE= "https://w7.pngwing.com/pngs/165/675/png-transparent-black-person-lifting-barbell-illustration-computer-icons-physical-exercise-physical-fitness-personal-trainer-fitness-centre-muscle-building-routine-miscellaneous-logo-monochrome-thumbnail.png"
  
    # user_id = g.user

    # user = User.query.get_or_404(user_id)

    exercise = Exercise.query.get_or_404(exercise_id)

    image_id = exercise.wger_id
    print(image_id)

    # exercise.description = f"{exercise.description}"
    
    try:
        image = Image.query.filter(exercise.wger_id == Image.wger_id).first()
        print(image)
    except:
        image = ALT_IMAGE
    
     
    
    # snagging athletes in order from the database;
    # team.athletes won't be in order by default
    # athletes = (Athlete
    #             .query
    #             .filter(Athlete.team_id == team_id)
    #             .order_by(Athlete.created_on.desc())
    #             .all())

    return render_template('exercises/show_exercise.html', exercise=exercise, image=image, alt_image=ALT_IMAGE)


