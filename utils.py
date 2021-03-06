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


CATEGORY_OBJ = {"Abs": 1, "Arms": 2, "Back": 3,
                "Calves": 4, "Chest": 5, "Legs": 6, "Shoulders": 7}

EQUIPMENT_OBJ = {"Barbell": 1, "Bench": 2, "Dumbbell": 3, "Gym mat": 4, "Incline bench": 5, "Kettlebell": 6,
                 "none (bodyweight exercise)": 7, "Pull-up bar": 8, "Swiss Ball": 9, "SZ-Bar": 10}

MUSCLE_OBJ = {"Anterior deltoid": 1,  "Biceps brachii": 2, "Biceps femoris": 3, "Brachialis": 4, "Gastrocnemius": 5,
              "Gluteus maximus": 6, "Latissimus dorsi": 7, "Obliquus externus abdominis": 8, "Pectoralis major": 9,
              "Quadriceps femoris": 10, "Rectus abdominis": 11, "Serratus anterior": 12, "Soleus": 13, "Trapezius": 14,
              "Triceps brachii": 15}

CURR_USER_KEY = "curr_user"
NEXT = "next"
NEXT_IMAGE = "next_image"
ALT_IMAGE = "https://w7.pngwing.com/pngs/165/675/png-transparent-black-person-lifting-barbell-illustration-computer-icons-physical-exercise-physical-fitness-personal-trainer-fitness-centre-muscle-building-routine-miscellaneous-logo-monochrome-thumbnail.png"
WORKOUT = "workout_id"
athlete_workout_list = []


def ip6_force_disabled():
    """ force disable ipv6, use ipv4 """
    wger_request = socket.AF_INET
    if urllib3_cn.HAS_IPV4:
        wger_request = socket.AF_INET4
    return wger_request


urllib3_cn.ip6_force_disabled = ip6_force_disabled

## API CALL FUNCTIONS ##


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
        response = requests.get(
            "https://wger.de/api/v2/exerciseinfo/?limit=5&language=2", timeout=1.25)
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
        resp = requests.get(
            "https://wger.de/api/v2/exerciseimage/?is_main=True", timeout=1.25)
        resp = resp.json()
        session[NEXT_IMAGE] = resp["next"]
        resp = resp["results"]
        return resp


## SPECIAL GET IMAGES TO ACCESS WGER API PROVIDED IMAGES ##
def get_exercise_image(exercise_id, exercise):
    """ Function to get the image associated  
    with exercise if available in image table """

    try:
        image = Image.query.filter(exercise.wger_id == Image.wger_id).first()

    except:
        image = exercise.image_url

    return image


### GET QUERY FUNCTIONS ###

def get_teams_by_user_id(user_id):
    ''''get all teams by user_id '''
    teams = Team.query.filter(user_id == Team.user_id).order_by(
        Team.created_on.desc()).all()
    return teams


def get_athletes_by_team_id(team_id):
    ''' get all teams by user_id '''

    athletes = [a for a in Athlete.query.filter(Athlete.team_id == team_id)]
    return athletes


def get_select_categories():
    ''' get all categories for SelectField '''
    categories = [(c.id, c.category_name) for c in Category.query.all()]
    return categories


def get_category_by_id(category_id):
    ''' get category by ID '''
    category = Category.query.filter(Category.id == category_id).all()
    category = category[0]
    return category


def get_select_equipment():
    ''' get all equipment for SelectField '''
    equipment = [(e.id, e.equipment_name) for e in Equipment.query.all()]
    return equipment


def get_equipment_by_id(equipment_id):
    ''' get equipment by ID '''
    equipment = Equipment.query.filter(Equipment.id == equipment_id).all()
    equipment = equipment[0]

    return equipment


def get_select_muscles():
    ''' get all muscles for SelectField '''
    muscles = [(m.id, m.muscle_name) for m in Muscle.query.all()]
    return muscles


def get_muscle_by_id(muscle_id):
    ''' get muscle by ID '''
    muscle = Muscle.query.filter(Muscle.id == muscle_id).all()
    muscle = muscle[0]
    return muscle


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


def get_workout(workout_id):
    ''' get a workout by ID '''
    workout = Workout.query.get_or_404(workout_id)
    return workout


def get_workout_exercises(workout_id):
    ''' get exercises for a specific workout '''
    exercises = db.session.query(Workout.name, Exercise.name, Exercise.id, Exercise.image_url, Workout_exercise). \
        select_from(Workout). \
        join(Workout_exercise). \
        join(Exercise). \
        filter(Workout.id == Workout_exercise.workout_id, Workout.id == workout_id).\
        all()


def get_workout_assigned_athlete(workout_id, athlete_id):
    ''' get a workout assigned to athlete '''
    workout = Athlete_workout.query.filter(
        Athlete_workout.athlete_id == athlete_id, Athlete_workout.workout_id == workout_id).all()
    workout = workout[0]
    return workout


def get_exercises_paginated(page_num, category_id, muscle_id, equipment_id):
    ''' get all exercises paginated filtered by request categories '''
    exercises = Exercise.query. \
        filter(Exercise.category_id == category_id, Exercise.muscle_id == muscle_id, Exercise.equipment_id == equipment_id). \
        paginate(per_page=21, page=page_num, error_out=True)
    return exercises


def get_exercise_by_ID(exercise_id):
    ''' get exercise by exercise ID '''
    exercise = Exercise.query.get_or_404(exercise_id)
    return exercise


def get_workout_exercise(workout_id, exercise_id):
    '''get a specific workouts exercise '''
    workout_exercise = Workout_exercise.query.filter(
        Workout_exercise.exercise_id == exercise_id, Workout_exercise.workout_id == workout_id).all()
    workout_exercise = workout_exercise[0]
    return workout_exercise


def get_user_by_ID(user_id):
    ''' get user by ID'''
    user = User.query.get_or_404(user_id)
    return user


def get_teams_by_user_Id(user_id):
    ''' get teams for a specific user '''
    teams = Team.query.filter(user_id == Team.user_id)
    return teams


def get_all_athlete_workouts():
    ''' get all athlete_workouts '''
    workouts = db.session.query(Workout.name, Workout.description, Workout.id, Athlete.first_name, Athlete.last_name,
                                Athlete.athlete_image_url, Athlete.position, Athlete.medical_status, Athlete.team_id, Athlete.id). \
        select_from(Workout). \
        join(Athlete_workout). \
        join(Athlete).all()
    return workouts


def get_athletes():
    ''' get all athletes in database '''
    athletes = Athlete.query.all()
    return athletes


def get_athletes_by_user_Id(athletes, user_id):
    ''' get athletes filtered by user_id '''
    athletes = [(a.id, a.full_name)
                for a in athletes if a.team.user.id == user_id]
    return athletes


def get_team_by_team_id(team_id):
    ''' get a team with the team_id '''
    team = Team.query.get_or_404(team_id)
    return team


def get_athletes_by_team_id(team_id):
    ''' get all athletes from a specific team with team_id '''
    athletes = (Athlete
                .query
                .filter(Athlete.team_id == team_id)
                .order_by(Athlete.created_on.desc())
                .all())
    return athletes


def get_athlete_by_athlete_id(athlete_id):
    ''' get an athlete by the athlete_id '''
    athlete = Athlete.query.get_or_404(athlete_id)
    return athlete


def get_team_by_athlete_id(athlete):
    ''' get a athletes team by using the athlete_id '''
    team = Team.query.filter(Team.id == athlete.team_id)
    return team


def get_athlete_workouts(athlete_id, athlete):
    ''' get all athlete_workout references to athlete '''
    athlete_workouts = (Athlete_workout
                        .query
                        .filter(athlete_id == athlete.id)
                        .all())
    return athlete_workouts


def get_workouts_by_athlete_id():
    ''' get the workouts for the athlete '''
    workouts = db.session.query(Athlete_workout.id.label("athlete_workout_id"), Workout.name, Workout.description, Workout.id.label("workout_id"), Athlete.first_name, Athlete.last_name,
                                Athlete.athlete_image_url, Athlete.position, Athlete.medical_status, Athlete.team_id, Athlete.id). \
        select_from(Workout). \
        join(Athlete_workout). \
        join(Athlete). \
        filter(Workout.id == Athlete_workout.workout_id). \
        all()
    return workouts


## ADD TO DATABASE FUNCTIONS ##

def add_workout_exercise(exercise_id, workout_id):
    ''' add an exercise to workout '''
    workout_exercise = Workout_exercise(
        workout_id=workout_id, exercise_id=exercise_id)
    db.session.add(workout_exercise)
    db.session.commit()
    return flash(f"Successfully added exercise to workout {workout_id}", "success")


def add_workout_exercises(workout_exercises):
    ''' add all workout_exercises to workout '''

    db.session.add_all(workout_exercises)
    db.session.commit()
    return flash(f"Successfully added exercise to workout {workout_id}", "success")


def add_to_db(response):
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
            exercise = Exercise(wger_id=wger_id, name=name, description=description,
                                category_id=category, equipment_id=equipment, muscle_id=muscle)
            db.session.add(exercise)
            db.session.commit()
        except:
            continue


def add_images(resp):
    """ utility to collect all exercise images from API and input in table """
    NEXT_IMAGE = ""
    for i in range(0, 4):

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
                image = Image(
                    exercise_image_url=exercise_image_url, wger_id=wger_id)
                db.session.add(image)
                db.session.commit()

        else:
            resp = requests.get(
                "https://wger.de/api/v2/exerciseimage/?is_main=True", timeout=1.25)
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
                image = Image(
                    exercise_image_url=exercise_image_url, wger_id=wger_id)
                db.session.add(image)
                db.session.commit()

        time.sleep(5)


def add_assignment(form):
    ''' add assignment to athlete '''
    athlete_id = form.athlete.data
    workout_id = form.workout.data
    athlete_workout = Athlete_workout(
        workout_id=workout_id, athlete_id=athlete_id)
    db.session.add(athlete_workout)
    db.session.commit()
    athlete_workout_list.append(athlete_workout.id)
    session['athlete_workout_list'] = athlete_workout_list
    flash(f"Succesfully assigned WORKOUT {workout_id}", 'success')
    return athlete_id


def add_completed_athlete_workout_assignment(workout):
    ''' add completed athlete workout to db '''
    # TODO: send to db into completed assignments table
    db.session.delete(workout)
    db.session.commit()
    return flash(f"Succesfully COMPLETED WORKOUT {workout.id}", 'success')


def add_team(form):
    ''' add a new team '''
    team = Team(
        name=form.name.data,
        location=form.location.data,
        discipline=form.discipline.data,
        team_image_url=form.team_image_url.data,
        user_id=g.user.id
    )
    db.session.add(team)
    db.session.commit()
    return flash(f"Succesfully added new team - {team.name.upper()}", 'success')


def add_exercise(form):
    ''' add new exercise to db '''
    exercise = Exercise(
        name=form.name.data,
        description=form.description.data,
        default_reps=form.default_reps.data,
        image_url=form.image_url.data,
        category_id=form.category_id.data,
        equipment_id=form.equipment_id.data,
        muscle_id=form.muscle_id.data
    )
    db.session.add(exercise)
    db.session.commit()
    flash(f"Succesfully added new team - {exercise.name.upper()}", 'success')
    return exercise


def add_athlete(form):
    ''' add new athlete '''
    athlete = Athlete(
        first_name=form.first_name.data,
        last_name=form.last_name.data,
        email=form.email.data,
        team_id=form.team_id.data,
        position=form.position.data,
        height=form.height.data,
        weight=form.weight.data,
        athlete_image_url=form.athlete_image_url.data,
        medical_status=form.medical_status.data
    )
    db.session.add(athlete)
    db.session.commit()
    flash(
        f"Succesfully added new athlete - {athlete.full_name.upper()}", 'success')
    return athlete

## EDIT FROM DATABASE FUNCTIONS ##


def edit_user(form, user):
    ''' edit user insert into db '''
    user.first_name = form.first_name.data,
    user.last_name = form.last_name.data,
    user.email = form.email.data,
    user.image_url = form.image_url.data,
    user.header_image_url = form.header_image_url.data
    db.session.commit()
    return flash(f"Succesfully updated TEAM profile {user.full_name}", 'success')


def edit_team(form, team):
    ''' edit team insert into db '''
    team.name = form.name.data,
    team.location = form.location.data,
    team.discipline = form.discipline.data,
    team.team_image_url = form.team_image_url.data,
    team.user_id = g.user.id
    db.session.commit()
    return flash(f"Succesfully updated TEAM profile {team.name}", 'success')


def edit_exercise(form, exercise):
    ''' add exercise insert in db '''
    exercise.name = form.name.data,
    exercise.description = form.description.data,
    exercise.default_reps = form.default_reps.data,
    exercise.image_url = form.image_url.data,
    exercise.category_id = form.category_id.data,
    exercise.equipment_id = form.equipment_id.data,
    exercise.muscle_id = form.muscle_id.data
    db.session.commit()
    flash(
        f"Succesfully updated EXERCISE profile {exercise.name.upper()}", 'success')
    return exercise


def edit_athlete(form, athlete):
    '''  edit athlete insert into db '''
    athlete.first_name = form.first_name.data,
    athlete.last_name = form.last_name.data,
    athlete.email = form.email.data,
    athlete.team_id = form.team_id.data,
    athlete.position = form.position.data,
    athlete.height = form.height.data,
    athlete.weight = form.weight.data,
    athlete.athlete_image_url = form.athlete_image_url.data,
    athlete.medical_status = form.medical_status.data

    db.session.add(athlete)
    db.session.commit()
    flash(
        f"Succesfully updated ATHLETE profile {athlete.full_name}", 'success')
    return athlete


def edit_workkout(form):
    ''' edit a workout name and description '''


# DELETE FROM DATABASE FUNCTIONS

def delete_exercise_workout(workout_exercise, exercise, workout):
    ''' delete exercise from a workout '''
    db.session.delete(workout_exercise)
    db.session.commit()
    return flash(f"Succesfully deleted exercise {exercise.id} from workout {workout.id}", 'success')


def delete_workout(workout):
    ''' delete entire workout '''
    db.session.delete(workout)
    db.session.commit()
    return flash(f"Succesfully deleted WORKOUT {workout.name.upper()}", 'success')


def delete_athlete_workout_assignment(workout):
    ''' delete completed athlete workout '''
    db.session.delete(workout)
    db.session.commit()
    return flash(f"Succesfully DELETED WORKOUT {workout.id}", 'success')


def delete_team(team_id):
    ''' delete a team '''
    team = Team.query.get(team_id)
    db.session.delete(team)
    db.session.commit()
    return flash(f"Succesfully deleted team {team.name}", 'success')


def delete_exercise(exercise_id):
    ''' delete an exercise '''
    exercise = Exercise.query.get_or_404(exercise_id)
    db.session.delete(exercise)
    db.session.commit()
    return flash(f"Succesfully deleted EXERCISE profile {exercise.name.upper()}", 'success')


def delete_athlete(athlete_id):
    ''' delete athlete '''
    athlete = Athlete.query.get(athlete_id)
    db.session.delete(athlete)
    db.session.commit()
    return flash(f"Succesfully deleted ATHLETE profile {athlete.full_name.upper()}", 'success')


## LOGIN FUNCTIONS ##

def do_logout():
    """Logout user."""
    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


def do_login(user):
    """Log in user."""
    session[CURR_USER_KEY] = user.id


def do_register(form):
    ''' register new user '''
    user = User.register(
        username=form.username.data,
        password=form.password.data,
        email=form.email.data,
        first_name=form.first_name.data,
        last_name=form.last_name.data,
        image_url=form.image_url.data or User.image_url.default.arg,
        header_image_url=form.header_image_url.data or User.header_image_url.default.arg
    )

    db.session.add(user)
    db.session.commit()
    return user


def do_authentification(form):
    ''' authenticate user '''
    user = User.authenticate(form.username.data,
                             form.password.data)
    return user
