import os

from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g
from sqlalchemy.exc import IntegrityError
from datetime import datetime as dt
import datetime
import requests
import socket
import requests.packages.urllib3.util.connection as urllib3_cn
import re
import time
from models import (connect_db, db, User, Team, Athlete, Workout, Athlete_workout, Exercise, Category, 
                    Equipment, Muscle, Workout_exercise, Athlete_workout_exercise, Image)


CATEGORY_OBJ = { "Abs": 1, "Arms": 2, "Back": 3, "Calves": 4, "Chest": 5, "Legs": 6, "Shoulders": 7 }

EQUIPMENT_OBJ = {   "Barbell": 1, "Bench": 2, "Dumbbell": 3, "Gym mat": 4, "Incline bench": 5, "Kettlebell": 6,
                    "none (bodyweight exercise)": 7, "Pull-up bar": 8, "Swiss Ball": 9, "SZ-Bar": 10 }

MUSCLE_OBJ = {  "Anterior deltoid": 1,  "Biceps brachii": 2, "Biceps femoris": 3, "Brachialis": 4, "Gastrocnemius": 5,
                "Gluteus maximus": 6, "Latissimus dorsi": 7, "Obliquus externus abdominis": 8, "Pectoralis major": 9,
                "Quadriceps femoris": 10, "Rectus abdominis": 11, "Serratus anterior": 12, "Soleus": 13, "Trapezius": 14,
                 "Triceps brachii": 15 }

NEXT = "next"
NEXT_IMAGE = "next_image"
ALT_IMAGE= "https://w7.pngwing.com/pngs/165/675/png-transparent-black-person-lifting-barbell-illustration-computer-icons-physical-exercise-physical-fitness-personal-trainer-fitness-centre-muscle-building-routine-miscellaneous-logo-monochrome-thumbnail.png"




def ip6_force_disabled():
    """ force disable ipv6, use ipv4 """
    wger_request = socket.AF_INET
    if urllib3_cn.HAS_IPV4:
        wger_request = socket.AF_INET4 
    return wger_request

def exercises_api_request():
    """ Request exercise data from wger API """
     ###### API request for exercises - offset 5 every call ######
    if NEXT in session:
        url = session[NEXT]  
        response = requests.get(url=url, timeout=1.25)
        response = response.json()
        session[NEXT] = response["next"]
        response = response["results"]
        return response
    else:
        response = requests.get("https://wger.de/api/v2/exerciseinfo/?limit=5&language=2", timeout=1.25)
        response = response.json()
        session[NEXT] = response["next"]
        response = response["results"]
        return response

def exercise_images_api_request():
    """ Request exercise image data from wger API """

     ###### API request for image - offset 20 every call ######
    # print(NEXT_IMAGE)
    
    if NEXT_IMAGE in session:
        
        if session[NEXT_IMAGE] != None:
            url = session[NEXT_IMAGE] 
        else:
            url = "https://wger.de/api/v2/exerciseimage/?is_main=True"
     
        resp = requests.get(url=url, timeout=1.25)
      
        resp = resp.json()
        session[NEXT_IMAGE] = resp["next"]
        resp = resp["results"]
        return resp
    else:
        resp = requests.get("https://wger.de/api/v2/exerciseimage/?is_main=True", timeout=1.25)
        resp = resp.json()
        session[NEXT_IMAGE] = resp["next"]
        resp = resp["results"]
        return resp

def insert_to_db(response):
    """ Function to insert retrieved API data into the database """
    for exercise in response:
        wger_id = exercise["id"]
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
        ## Insert into exercise table ##
        try:
            exercise = Exercise(wger_id=wger_id, name=name, description=description, category_id=category, equipment_id=equipment, muscle_id=muscle)
            db.session.add(exercise)
            db.session.commit()
        except:
            continue


def insert_images(resp):
    """ utility to collect all exercise images from API and input in table """
    NEXT_IMAGE = ""
    for i in range(0,4):

        if NEXT_IMAGE != "":
            url = NEXT_IMAGE

            resp = requests.get(url=url, timeout=1.25)
            resp = resp.json()
            NEXT_IMAGE = resp["next"]
            resp = resp["results"]
            print("**************  if   *****************")
            print(NEXT_IMAGE)
            print(resp)
            for exercise in resp:
                print(exercise)
                exercise_image_url = exercise["image"]
                wger_id = exercise["image"]
                ## Extract wger exercice id (wger_id) from url address ##
                wger_id = str(wger_id)
                wger_id = re.findall('\d{1,}', wger_id)
                wger_id = int(wger_id[0])
                ## Insert into images table ##
                image = Image(exercise_image_url=exercise_image_url, wger_id=wger_id)
                db.session.add(image)
                db.session.commit()

        else:
            resp = requests.get("https://wger.de/api/v2/exerciseimage/?is_main=True", timeout=1.25)
            resp = resp.json()
            print("**************  resp['next']   *****************")
            print(resp["next"])
            NEXT_IMAGE = resp["next"]
            resp = resp["results"]
            print("**************  else   *****************")
            print(NEXT_IMAGE)
            print(resp)

            for exercise in resp:
                print(exercise)
                exercise_image_url = exercise["image"]
                wger_id = exercise["image"]
                ## Extract wger exercice id (wger_id) from url address ##
                wger_id = str(wger_id)
                wger_id = re.findall('\d{1,}', wger_id)
                wger_id = int(wger_id[0])
                ## Insert into images table ##
                image = Image(exercise_image_url=exercise_image_url, wger_id=wger_id)
                db.session.add(image)
                db.session.commit()

        time.sleep(5)
   
### UNCOMMENT TO SEED images TABLE ###    
# insert_images()
    
 
def get_exercise_image(exercise_id, exercise):
    """ Function to get the image associated  
    with exercise if available in image table """

    try:
        image = Image.query.filter(exercise.wger_id == Image.wger_id).first()
    
    except:
        image = exercise.image_url 
    
    return image
    

### QUERY FUNCTIONS ###

def get_teams_by_user_id(user_id):
    ''''get all teams by user_id '''
    teams = Team.query.filter(user_id == Team.user_id)
    return teams

def get_athletes_by_team_id(team_id):
    ''' get all teams by user_id '''

    athletes = [a for a in Athlete.query.filter(Athlete.team_id == team_id)]
    return athletes

def get_select_categories():
    ''' get all categories for SelectField '''

    categories = Category.query.all() 
    categories = [ (c.id, c.category_name) for c in categories]
    return categories

def get_select_equipment():
    ''' get all equipment for SelectField '''

    equipment = Equipment.query.all() 
    equipment = [ (e.id, e.equipment_name) for e in equipment]
    return equipment

def get_select_muscles():
    ''' get all muscles for SelectField '''

    muscles = Muscle.query.all() 
    muscles = [ (m.id, m.muscle_name) for m in muscles]
    return muscles

def get_workouts():
    ''' get all workouts '''
    workouts = Workout.query.all()
    return workouts

def get_select_workouts(workouts):
    ''' get all workouts for SelectField '''
    workouts = [(w.id, w.name) for w in workouts] 
    return workouts

def get_workouts_exercises():
    ''' get all exercises for workouts '''
    exercises = db.session.query(Workout.name, Exercise.name, Workout_exercise). \
            select_from(Workout). \
            join(Workout_exercise). \
            join(Exercise). \
            filter(Workout.id == Workout_exercise.workout_id). \
            all()
    return exercises






urllib3_cn.ip6_force_disabled = ip6_force_disabled





