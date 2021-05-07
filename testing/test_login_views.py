"""Login Views Tests."""
## Run the command in the line below in bash terminal ##
# python -m unittest -v  test_login_views.py #
print("------------------")
print("LOGIN VIEWS TESTS")
print("------------------")

import os

from unittest import TestCase
from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g

from models import ( db, connect_db, User, Team, Athlete, Workout, Athlete_workout, Category, 
                    Equipment, Muscle, Exercise, Workout_exercise, Athlete_workout_exercise, CURR_DATE )
from bs4 import BeautifulSoup
from utils import *


CURR_USER_KEY = "curr_user"

## Set os environment to use the test database ##

os.environ['DATABASE_URL'] = "postgresql:///gymhero-test"

## Import App ##

from app import app, CURR_USER_KEY
from utils import *

## Create Tables ##

db.create_all()

# Don't have WTForms use CSRF at all, since it's a pain to test

app.config['WTF_CSRF_ENABLED'] = False
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True


class TeamViewTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        db.drop_all()
        db.create_all()
        
        self.client = app.test_client()
        User.query.delete()
        Team.query.delete()
        Workout.query.delete()
        Exercise.query.delete()
        # SET DATE ##
        curr_date = datetime.datetime.now().strftime('%Y-%m-%d')

        ## ADD USERS ##
        self.user = User(username="coach_E", password="$2b$12$L/HD4t51NVFRvMI37MAmcO8Bw66XvpzPweAsiGlg29bdItUEVvtTS", email="edeneault@gmail.com", first_name="Etienne", last_name="Deneault",
                        image_url="https://miro.medium.com/max/3150/1*vx4SBuW5YM3s1Pxyk00mSQ.jpeg", 
                        header_image_url="https://images.unsplash.com/photo-1580237754794-0e26a1d7ee03?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1414&q=80")
        
        ## ADD TEAMS ##
        team_1_1 = Team(name="Volta", location="Las Vegas, NV, USA", discipline="acrobatics",
        user_id=1)
        team_2_1 = Team(name="Fitness Coders", location="San Diego, NV, USA", discipline="brain gymnastics",
        user_id=1)

        ## ADD ATHLETES ##

        athlete_1_1 = Athlete(first_name="Joe", last_name="Douglas", email="jdouglas@fakemail.com", position="Acro_Base",
                        height=70, weight=175.0, team_id=1)
        athlete_2_1 = Athlete(first_name="Peter", last_name="Johnson", email="pjohnson@fakegmail.com", position="Acro_Base",
                        height=73, weight=185.0, team_id=1)

       ## ADD WORKOUTS ##

        workout_1 = Workout(name="Upper Body Strength", description="Workout targets upperbody strength")
        workout_2 = Workout(name="Lower Body Strength", description="Workout targets lowerbody strength")

        ## ADD ATHLETE_WORKOUTS ##

        athlete_workout_1_1 = Athlete_workout(rpe_avg=7, workout_id=1, athlete_id=1)
        athlete_workout_2_1 = Athlete_workout(rpe_avg=7, workout_id=2, athlete_id=1)
        athlete_workout_2_2 = Athlete_workout(rpe_avg=7, workout_id=2, athlete_id=2)
        athlete_workout_3_2 = Athlete_workout(rpe_avg=7, workout_id=2, athlete_id=2)

        ## EXERCISES ##

        exercise_1 = Exercise(name="flat bench press", 
            description="On you bench press rack of choice, set-up in flat configuration, use a barbell to press up and down, make sure to have a spotter.",
            wger_id=192, category_id=5, equipment_id=1, muscle_id=1)
        exercise_2 = Exercise(name="Air Squat", 
            description="Perform a squat with no resistance, make sure stance is slightly wider then shoulder width and feet are turned out.",
            wger_id=111, category_id=6, equipment_id=7, muscle_id=2)
        exercise_3 = Exercise(name="push up", 
            description="Assume a support position, perform a push up, make sure to engage your core while performing each repetition.",
            wger_id=182, category_id=5, equipment_id=7, muscle_id=1)
        exercise_4 = Exercise(name="crunches", 
            description="Sit and lay back on a swiss ball, position feet slightly wider then shoulder width, perform a half-crunch fully engaging the core.",
            wger_id=91, category_id=1, equipment_id=9, muscle_id=3)

        ## CATEGORIES ##

        category_1 = Category(category_name="Abs")
        category_2 = Category(category_name="Arms")
        category_3 = Category(category_name="Back")
        category_4 = Category(category_name="Calves")
        category_5 = Category(category_name="Chest")
        category_6 = Category(category_name="Legs")
        category_7 = Category(category_name="Shoulders")

        self.categories = [ category_1, category_2, category_3, category_4, category_5, category_6, category_7 ]


        ## EQUIQMENT ##

        equipment_1 = Equipment(equipment_name="Barbell")
        equipment_2 = Equipment(equipment_name="Bench")
        equipment_3 = Equipment(equipment_name="Dumbbell")
        equipment_4 = Equipment(equipment_name="Gym mat")
        equipment_5 = Equipment(equipment_name="Incline bench")
        equipment_6 = Equipment(equipment_name="Kettlebell")
        equipment_7 = Equipment(equipment_name="none (bodyweight exercise)")
        equipment_8 = Equipment(equipment_name="Pull-up bar")
        equipment_9 = Equipment(equipment_name="Swiss Ball")
        equipment_10 = Equipment(equipment_name="SZ-Bar")

        self.equipment = [ equipment_1, equipment_2, equipment_3, equipment_4, equipment_5,
                    equipment_6, equipment_7, equipment_8, equipment_9, equipment_10 ]

        ## MUSCLES ##

        muscle_1 = Muscle(muscle_name="Anterior deltoid")
        muscle_2 = Muscle(muscle_name="Biceps brachii")
        muscle_3 = Muscle(muscle_name="Biceps femoris")
        muscle_4 = Muscle(muscle_name="Brachialis")
        muscle_5 = Muscle(muscle_name="Gastrocnemius")
        muscle_6 = Muscle(muscle_name="Gluteus maximus")
        muscle_7 = Muscle(muscle_name="Latissimus dorsi")
        muscle_8 = Muscle(muscle_name="Obliquus externus abdominis")
        muscle_9 = Muscle(muscle_name="Pectoralis major")
        muscle_10 = Muscle(muscle_name="Quadriceps femoris")
        muscle_11 = Muscle(muscle_name="Rectus abdominis")
        muscle_12 = Muscle(muscle_name="Serratus anterior")
        muscle_13 = Muscle(muscle_name="Soleus")
        muscle_14 = Muscle(muscle_name="Trapezius")
        muscle_15 = Muscle(muscle_name="Triceps brachii")

        ## WORKOUT_EXERCISE ##

        workout_exercise_1_1 = Workout_exercise( workout_id=1, exercise_id=1 )
        workout_exercise_1_2 = Workout_exercise( workout_id=1, exercise_id=2 )
        workout_exercise_2_3 = Workout_exercise( workout_id=2, exercise_id=3 )
        workout_exercise_2_4 = Workout_exercise( workout_id=2, exercise_id=4 )

        self.workout_exercises = [ workout_exercise_1_1, workout_exercise_1_2, workout_exercise_2_3, workout_exercise_2_4,]

        self.muscles = [ muscle_1, muscle_2, muscle_3, muscle_4, muscle_5,
                    muscle_6, muscle_7, muscle_8, muscle_9, muscle_10,
                    muscle_11, muscle_12, muscle_13, muscle_14, muscle_15 ]

        self.teams = [team_1_1, team_2_1]      
        self.athletes = [athlete_1_1, athlete_2_1]   
        self.workouts = [ workout_1,  workout_2]
        self.exercises = [ exercise_1, exercise_2, exercise_3, exercise_4]
        self.athlete_workouts = [ athlete_workout_1_1, athlete_workout_2_1, athlete_workout_2_2, athlete_workout_3_2]
        
        db.session.add(self.user)
        db.session.add_all(self.teams)
        db.session.add_all(self.athletes)
        db.session.add_all(self.workouts)
        db.session.add_all(self.exercises)
        db.session.add_all(self.categories)
        db.session.add_all(self.equipment)
        db.session.add_all(self.muscles)


        db.session.commit()
       
        db.session.add_all(self.athlete_workouts)
        db.session.commit()

        db.session.add_all(self.workout_exercises)
        db.session.commit()
        
        self.user = User.query.get_or_404(1)
        self.user_id = self.user.id
        
        self.teams = get_teams_by_user_id(self.user_id)
        self.workouts = get_workouts()

    def tearDown(self):
        resp = super().tearDown()
        db.session.rollback()
        return resp


    def test_users_register(self):
        """ Test: can a user register?"""
        with self.client as c:
            
            
            
            # user = {"username": "coach_Test", "password": "password", "email": "edeneault@gmail.com", "first_name": "Etienne", "last_name": "Deneault",
            #             "image_url": "https://miro.medium.com/max/3150/1*vx4SBuW5YM3s1Pxyk00mSQ.jpeg", 
            #             "header_image_url": "https://images.unsplash.com/photo-1580237754794-0e26a1d7ee03?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1414&q=80"}
            
            # do_register(user)
 
            resp = c.post(f"/users/register", data= {"username": "coach_Test", "password": "password", "email": "edeneault@gmail.com", "first_name": "Etienne", "last_name": "Deneault",
                        "image_url": "https://miro.medium.com/max/3150/1*vx4SBuW5YM3s1Pxyk00mSQ.jpeg", 
                        "header_image_url": "https://images.unsplash.com/photo-1580237754794-0e26a1d7ee03?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1414&q=80"},
                        follow_redirects=True )

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<li class="nav-item"><a id="logout-link" class="nav-link tes2 ps-4" href="/logout ">LOGOUT</a></li>', str(resp.data))

    # def test_exercises_show_logged_out(self):
    #     """ Test: can a logged-out user see all the exercises?"""
    #     with self.client as c:
    #         self.page_num = 1
 
    #         resp = c.get(f"/exercises/{self.page_num}")

    #         self.assertEqual(resp.status_code, 200)
    #         self.assertIn('<a class="nav-link ps-4" href="/exercises/1">EXERCISES</a></li>', str(resp.data))

    # def test_exercise_show_logged_in(self):
    #     """ Test: can a logged-out user see a specific exercise? """
    #     with self.client as c:
    #         with c.session_transaction() as sess:
    #             sess[CURR_USER_KEY] = self.user_id
           
    #         self.exercise = get_exercise_by_ID(1)
    #         self.exercise_id = self.exercise.id
            
    #         resp = c.get(f"/exercises/exercise/{self.exercise_id}",follow_redirects=True )
       
    #         self.assertEqual(resp.status_code, 200)
    #         self.assertIn(f'<h1 class="d-inline teams-fa-color display-5 px-1">Exercise</h1>', str(resp.data))
    
    # def test_exercise_show_logged_out(self):
    #     """ Test: can a logged-out user see a specific exercise? """
    #     with self.client as c:
           
    #         self.exercise = get_exercise_by_ID(1)
    #         self.exercise_id = self.exercise.id
            
    #         resp = c.get(f"/exercises/exercise/{self.exercise_id}",follow_redirects=True )
       
    #         self.assertEqual(resp.status_code, 200)
    #         self.assertIn(f'<h1 class="d-inline teams-fa-color display-5 px-1">Exercise</h1>', str(resp.data))

    # def test_exercises_add_logged_in(self):
    #     """when logged-in, can the user add a exercise?"""

    #     with self.client as c:
    #         with c.session_transaction() as sess:
    #             sess[CURR_USER_KEY] = self.user.id

    #         resp = c.post(f"/exercises/add", data={ "name": "testname",
    #                                                 "description": "testdescription",
    #                                                 "default_reps": 7,
    #                                                 "image_url": None,
    #                                                 "category_id": 1,
    #                                                 "muscle_id": 1,
    #                                                 "equipment_id": 1
    #                                                 },follow_redirects=True )

    #         self.assertEqual(resp.status_code, 200)
    #         exercise = Exercise.query.get_or_404(5)
    #         self.assertEqual(exercise.name, "testname")     


    # def test_exercises_add_logged_out(self):
    #     """when logged-out, can the user add a exercise?"""

    #     with self.client as c:
    #         resp = c.post(f"/exercises/add", data={ "name": "testname",
    #                                                 "description": "testdescription",
    #                                                 "default_reps": 7,
    #                                                 "image_url": None,
    #                                                 "category_id": 1,
    #                                                 "muscle_id": 1,
    #                                                 "equipment_id": 1
    #                                                 },follow_redirects=True )

    #         self.assertEqual(resp.status_code, 200)
    #         exercise = Exercise.query.get(5)
    #         self.assertIsNone(exercise)

    
    # def test_exercises_edit_logged_in(self):
    #     """when logged-in, can the user edit an exercise?"""

    #     with self.client as c:
    #         with c.session_transaction() as sess:
    #             sess[CURR_USER_KEY] = self.user.id

    #         self.exercise_id = 4

    #         resp = c.post(f"/exercises/edit/{self.exercise_id}", data={ "name": "testname1",
    #                                                     "description": "testdescription",
    #                                                     "default_reps": 7,
    #                                                     "image_url": None,
    #                                                     "category_id": 1,
    #                                                     "muscle_id": 1,
    #                                                     "equipment_id": 1
    #                                                     }, follow_redirects=True )

    #         self.assertEqual(resp.status_code, 200)
    #         exercise = Exercise.query.get(4)
    #         self.assertEqual(exercise.name, "testname1")

    # def test_exercises_edit_logged_out(self):
    #     """when logged-out, can the user edit an exercise?"""
    #     with self.client as c:
    #         self.exercise_id = 4

    #         resp = c.post(f"/exercises/edit/{self.exercise_id}", data={ "name": "testname2",
    #                                                     "description": "testdescription",
    #                                                     "default_reps": 7,
    #                                                     "image_url": None,
    #                                                     "category_id": 1,
    #                                                     "muscle_id": 1,
    #                                                     "equipment_id": 1
    #                                                     }, follow_redirects=True )

    #         self.assertEqual(resp.status_code, 200)
    #         exercise = Exercise.query.get(4)
    #         self.assertNotEqual(exercise.name, "testname2")

    # def test_exercises_delete_logged_in(self):
    #     """when logged-in, can the user delete an exercise?"""

    #     with self.client as c:
    #         with c.session_transaction() as sess:
    #             sess[CURR_USER_KEY] = self.user.id

    #         self.exercise_id = 2

    #         resp = c.post(f"/exercises/delete/{self.exercise_id}", follow_redirects=True )

    #         self.assertEqual(resp.status_code, 200)
    #         exercise = Exercise.query.get(2)
    #         self.assertIsNone(exercise)

    # def test_exercises_delete_logged_out(self):
    #     """when logged-out, can the user delete an exercise?"""

    #     with self.client as c:
            

    #         self.exercise_id = 2

    #         resp = c.post(f"/exercises/delete/{self.exercise_id}", follow_redirects=True )

    #         self.assertEqual(resp.status_code, 200)
    #         self.assertIn(f'href="/users/register">REGISTER NOW!</a>', str(resp.data))     