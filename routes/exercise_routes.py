## Import App and needed modules ##
from app import app

from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g
from models import ( db, connect_db, User, Team, Athlete, Workout, Athlete_workout, Category, 
                    Equipment, Muscle, Exercise, Workout_exercise, Athlete_workout_exercise )
from forms import LoginForm, RegisterForm, TeamForm, AthleteForm, ExerciseForm
from utils import *
import requests

NEXT = "next"
NEXT_IMAGE = "next_image"

@app.route('/exercises/<int:page_num>')
def exercises_show(page_num):
    """ Show all exercises view and call on API for exercise data """
    
    ###### API request for exercises - offset 5 every call ######
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


    ###### API request for image - offset 20 every call ######
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



@app.route('/exercises/exercise/<int:exercise_id>')
def exercise_show(exercise_id):
    """ Show exercise by ID """
    ALT_IMAGE= "https://w7.pngwing.com/pngs/165/675/png-transparent-black-person-lifting-barbell-illustration-computer-icons-physical-exercise-physical-fitness-personal-trainer-fitness-centre-muscle-building-routine-miscellaneous-logo-monochrome-thumbnail.png"
  
    exercise = Exercise.query.get_or_404(exercise_id)
    image_id = exercise.wger_id

    try:
        image = Image.query.filter(exercise.wger_id == Image.wger_id).first()
    
    except:
        image = exercise.image_url

    return render_template('exercises/show_exercise.html', exercise=exercise, image=image, alt_image=ALT_IMAGE)



@app.route('/exercises/add', methods=["GET", "POST"])
def exercise_add():
    """ Add an exercise. """

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")
    
    user = g.user

    categories = Category.query.all() 
    categories = [ (c.id, c.category_name) for c in categories]

    equipment = Equipment.query.all() 
    equipment = [ (e.id, e.equipment_name) for e in equipment]

    muscles = Muscle.query.all() 
    muscles = [ (m.id, m.muscle_name) for m in muscles]

    form = ExerciseForm()
    form.category_id.choices = categories
    form.equipment_id.choices = equipment
    form.muscle_id.choices = muscles


    if form.validate_on_submit():
        try:
            exercise = Exercise(
                name=form.name.data,
                description=form.description.data,
                default_reps=form.default_reps.data,
                image_url=form.image_url.data,
                category_id= form.category_id.data,
                equipment_id= form.equipment_id.data,
                muscle_id= form.muscle_id.data
                
            )
            print(exercise)
            db.session.add(exercise)
            db.session.commit()
            print(exercise)

        except:
            flash("Something went wrong", "danger")
            return render_template('/exercises/exercise_add_form.html', form=form)

        return redirect(f"/exercises/exercise/{exercise.id}")

    else:
        return render_template('/exercises/exercise_add_form.html', form=form)
    return render_template('/exercises/exercise_add_form.html', form=form)