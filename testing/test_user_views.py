"""User Views Tests."""
## Run the command in the line below in bash terminal ##
# python -m unittest -v  test_user_views.py #
print("------------------")
print("USER VIEWS TESTS")
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


class UseViewTestCase(TestCase):
    """Test views for users."""

    def setUp(self):
        """Create test client, add sample data."""

        db.drop_all()
        db.create_all()

        self.client = app.test_client()
        User.query.delete()
        Team.query.delete()

        # SET DATE ##
        curr_date = datetime.datetime.now().strftime('%Y-%m-%d')

        ## ADD USERS ##
        coach1 = User(username="coach_E", password="$2b$12$L/HD4t51NVFRvMI37MAmcO8Bw66XvpzPweAsiGlg29bdItUEVvtTS", email="edeneault@gmail.com", first_name="Etienne", last_name="Deneault",
                        image_url="https://miro.medium.com/max/3150/1*vx4SBuW5YM3s1Pxyk00mSQ.jpeg", 
                        header_image_url="https://images.unsplash.com/photo-1580237754794-0e26a1d7ee03?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1414&q=80")

        coach2 = User(username="coach_M", password="$2b$12$aMRinHJfFHPSZPJC/d2UuOgSSFd8ChPuHeI3rhaP.SW/cJuGG8rRy", email="msparks@fakegmail.com", first_name="Matthew", last_name="Sparks")
        coach3 = User(username="coach_A", password="p$2b$12$LEjxCuEgEfohtVqEwgzwjOzAmtLQSVguQYXDvpaIzvrfkY8/tqOqK", email="apjarova@gmail.com", first_name="Alexandra", last_name="Deneault",
                        image_url="https://iv1.lisimg.com/image/20508627/666full-alexandra-apjarova.jpg",
                        header_image_url="https://images.unsplash.com/photo-1519925610903-381054cc2a1c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1350&q=80")
        
        ## ADD TEAM s##
        team_1_1 = Team(name="Volta", location="Las Vegas, NV, USA", discipline="acrobatics",
        user_id=1)
        team_2_1 = Team(name="Fitness Coders", location="San Diego, NV, USA", discipline="brain gymnastics",
        user_id=1)

        self.teams = [team_1_1, team_2_1]        
        self.users = [coach1, coach2, coach3 ]
        db.session.add_all(self.teams)
        db.session.add_all(self.users)
        db.session.commit()
        self.user = User.query.get_or_404(1)
        self.user_id = self.user.id

        self.teams = get_teams_by_user_id(self.user_id)


    def tearDown(self):
        resp = super().tearDown()
        db.session.rollback()
        return resp


    def test_user_show(self):
        """ Test-1: can a user register?"""
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.user_id
 
            # print("----------user.id-------  ", self.user.id)
            resp = c.get(f"/users/{self.user_id}",follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("coach_E", str(resp.data))
            self.assertIn("Volta", str(resp.data) )

    def test_users_edit(self):
        """ Test-2: when logged-in, can the user edit their profile?"""

        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.user.id

        resp = c.post(f"/users/edit/{self.user_id}", data={ "first_name": "Etienne1",
                    "last_name": "Deneault1",
                    "email": "edit@mail.com",
                    "image_url": "https://miro.medium.com/max/3150/1*vx4SBuW5YM3s1Pxyk00mSQ.jpeg",
                    "header_image_url": "https://images.unsplash.com/photo-1580237754794-0e26a1d7ee03?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1414&q=80"
                    } )

        self.assertEqual(resp.status_code, 302)
        user = User.query.get_or_404(self.user_id)
        self.assertEqual(user.first_name, "Etienne1")
