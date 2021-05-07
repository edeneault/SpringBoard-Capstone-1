"""Team Views Tests."""
## Run the command in the line below in bash terminal ##
# python -m unittest -v  test_team_views.py #
print("------------------")
print("TEAM VIEWS TESTS")
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

       
        self.teams = [team_1_1, team_2_1]      
        self.athletes = [athlete_1_1, athlete_2_1]   
        
        db.session.add(self.user)
        db.session.add_all(self.teams)
        db.session.add_all(self.athletes)
        
        db.session.commit()
        self.user = User.query.get_or_404(1)
        self.user_id = self.user.id
        
        self.teams = get_teams_by_user_id(self.user_id)


    def tearDown(self):
        resp = super().tearDown()
        db.session.rollback()
        return resp


    def test_teams_show(self):
        """ Test: can a user see his teams?"""
        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.user_id
 
            resp = c.get(f"/teams")

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Volta", str(resp.data))
            self.assertIn("Fitness Coders", str(resp.data) )
    
    def test_team_show(self):
        """ Test: can a user see each team individually?"""
        with self.client as c:
            with c.session_transaction() as sess:
                print(self.user_id)
                sess[CURR_USER_KEY] = self.user_id

            self.team = self.teams[0]
            self.team_id = self.team.id
            athletes = get_athletes_by_team_id(self.team_id)
            
            resp = c.get(f"/teams/{self.team_id}")
       
            self.assertEqual(resp.status_code, 200)
            self.assertIn(f'<h5 class="d-inline teams-fa-color fs-3 mx-auto">Volta', str(resp.data))
           

    def test_teams_add(self):
        """when logged-in, can the user add a team?"""

        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.user.id

        resp = c.post(f"/teams/add", data={ "name": "testname",
                    "location": "testlocation",
                    "discipline": "testdiscipline",
                    "team_image_url": "https://miro.medium.com/max/3150/1*vx4SBuW5YM3s1Pxyk00mSQ.jpeg",
                    "user_id": f"{self.user_id}"
                    } )

        self.assertEqual(resp.status_code, 302)
        team = Team.query.get_or_404(3)
        self.assertEqual(team.name, "testname")

    
    def test_teams_edit(self):
        """when logged-in, can the user edit a team?"""

        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.user.id

        self.team_id = 2

        resp = c.post(f"/teams/edit/{self.team_id}", data={ "name": "testname1",
                    "location": "testlocation",
                    "discipline": "testdiscipline",
                    "team_image_url": "https://miro.medium.com/max/3150/1*vx4SBuW5YM3s1Pxyk00mSQ.jpeg",
                    "user_id": f"{self.user_id}"
                    } )

        self.assertEqual(resp.status_code, 302)
        team = Team.query.get_or_404(2)
        self.assertEqual(team.name, "testname1")

    def test_teams_delete(self):
        """when logged-in, can the user delete a team?"""

        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.user.id

        self.team_id = 2

        resp = c.post(f"/teams/delete/{self.team_id}")

        self.assertEqual(resp.status_code, 302)
        team = Team.query.get(2)
        self.assertIsNone(team)
