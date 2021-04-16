"""Seed file to make sample data for users and posts db."""

from models import db, User, Team, Athlete, Workout, Athlete_workout
from app import app
from datetime import datetime as dt
import datetime

## CREATE ALL TABLES ##
db.drop_all()
db.create_all()

## IF TABLE NOT EMPTY => EMPTY ##
User.query.delete()
Team.query.delete()

# SET DATE ##
curr_date = datetime.datetime.now().strftime('%Y-%m-%d')
print(curr_date)

## ADD USERS ##
coach1 = User(username="edeneault", password="password1", email="edeneault@gmail.com", first_name="Etienne", last_name="Deneault",
                image_url="https://miro.medium.com/max/3150/1*vx4SBuW5YM3s1Pxyk00mSQ.jpeg")
coach2 = User(username="msparks", password="password2", email="msparks@fakegmail.com", first_name="Matthew", last_name="Sparks")
coach3 = User(username="adeneault", password="password3", email="apjarova@gmail.com", first_name="Alexandra", last_name="Deneault",
                 image_url="https://iv1.lisimg.com/image/20508627/666full-alexandra-apjarova.jpg")

users = [coach1, coach2, coach3]

## ADD TEAMS ##

team_1_1 = Team(name="Volta", location="Las Vegas, NV, USA", discipline="acrobatics",
                user_id=1)
team_2_1 = Team(name="Fitness Coders", location="San Diego, NV, USA", discipline="brain gymnastics",
                user_id=1)
team_3_2 = Team(name="La Nouba", location="Orlando, FL, USA", discipline="acrobatics",
                user_id=2)
team_4_2 = Team(name="Seneca", location="Toronto, ONT, CAN", discipline="cycling",
                user_id=2)
team_5_3 = Team(name="ProRhytmics", location="Denver, CO, USA", discipline="Rhytmic Gymnastics",
                user_id=3)
team_6_3 = Team(name="AerialFusion", location="Austin, TX, USA", discipline="Aerial Arts",
                user_id=3)


teams = [team_1_1, team_2_1, team_3_2, team_4_2, team_5_3, team_6_3]

## ADD ATHLETES ##

# TEAM 1 #
athlete_1_1 = Athlete(first_name="Joe", last_name="Douglas", email="jdouglas@fakemail.com", position="Acro_Base",
                        height=70, weight=175.0, team_id=1)
athlete_2_1 = Athlete(first_name="Peter", last_name="Johnson", email="pjohnson@fakegmail.com", position="Acro_Base",
                        height=73, weight=185.0, team_id=1)
athlete_3_1 = Athlete(first_name="Lucille", last_name="Walker", email="lwalker@fakegmail.com", position="Acro_Flyer",
                        height=57, weight=95.0, team_id=1)
athlete_4_1 = Athlete(first_name="Alexandra", last_name="Zumin", email="azumin@fakegmail.com", position="Acro_Flyer",
                        height=58, weight=100.0, team_id=1)
athlete_5_1 = Athlete(first_name="John", last_name="Mgurk", email="jmagurk@fakegmail.com", position="Acro_Flyer",
                        height=62, weight=115.0, team_id=1)
athlete_6_1 = Athlete(first_name="Alanna", last_name="FireStorm", email="afirestorm@fakegmail.com", position="Acro_Dancer",
                        height=64, weight=114.0, team_id=1)

# TEAM 2 #
athlete_1_2 = Athlete(first_name="Sean", last_name="Soul", email="jsoul@fakemail.com", position="Full Stack",
                        height=80, weight=175.0, team_id=2)
athlete_2_2 = Athlete(first_name="Jordan", last_name="Ash", email="jash@fakegmail.com", position="Front-End",
                        height=73, weight=185.0, team_id=2)
athlete_3_2 = Athlete(first_name="Joshua", last_name="Lewis", email="jlewisr@fakegmail.com", position="Back-end",
                        height=57, weight=135.0, team_id=2)
athlete_4_2 = Athlete(first_name="Mack", last_name="Prairie", email="mprairie@fakegmail.com", position="Database Admin",
                        height=76, weight=170.0, team_id=2)
athlete_5_2 = Athlete(first_name="Pierre", last_name="Loyette", email="ployette@fakegmail.com", position="UX-UI Designer",
                        height=78, weight=165.0, team_id=2)
athlete_6_2 = Athlete(first_name="Mike", last_name="Jordan", email="mjordan@fakegmail.com", position="Project Manager",
                        height=77, weight=230.0, team_id=2)

# TEAM 3 #

athlete_1_3 = Athlete(first_name="Kayla", last_name="Lau", email="klow@fakemail.com", position="Tramp Wall",
                        height=70, weight=155, team_id=3)
athlete_2_3 = Athlete(first_name="Sam", last_name="Lake", email="slake@fakegmail.com", position="Acro-Character",
                        height=73, weight=125.0, team_id=3)
athlete_3_3 = Athlete(first_name="Alex", last_name="Men", email="amen@fakegmail.com", position="Aerialist",
                        height=57, weight=95.0, team_id=3)
athlete_4_3 = Athlete(first_name="Julia", last_name="More", email="jmore@fakegmail.com", position="Aerialist",
                        height=58, weight=100.0, team_id=3)
athlete_5_3 = Athlete(first_name="Janette", last_name="Pow", email="jpow@fakegmail.com", position="Trapeze Flyer",
                        height=62, weight=115.0, team_id=3)
athlete_6_3 = Athlete(first_name="Anna", last_name="Kilt", email="akilt@fakegmail.com", position="Power Track",
                        height=64, weight=114.0, team_id=3)

# TEAM 4 #

athlete_1_4 = Athlete(first_name="Emma", last_name="Lau", email="elau@fakemail.com", position="Road cyclist",
                        height=70, weight=155.0, team_id=4)
athlete_2_4 = Athlete(first_name="Zoe", last_name="Lake", email="zlake@fakegmail.com", position="Road cyclist",
                        height=73, weight=125.0, team_id=4)
athlete_3_4 = Athlete(first_name="Lisa", last_name="Men", email="lmen@fakegmail.com", position="Road cyclist",
                        height=57, weight=95.0, team_id=4)
athlete_4_4 = Athlete(first_name="Philip", last_name="More", email="lmore@fakegmail.com", position="Road cyclist",
                        height=58, weight=100.0, team_id=4)
athlete_5_4 = Athlete(first_name="Vincent", last_name="Pow", email="vpow@fakegmail.com", position="Road cyclist",
                        height=62, weight=115.0, team_id=4)
athlete_6_4 = Athlete(first_name="Anatoli", last_name="Kilt", email="aakilt@fakegmail.com", position="Road cyclist",
                        height=64, weight=114.0, team_id=4)

# TEAM 5 #

athlete_1_5 = Athlete(first_name="Qiqi", last_name="La", email="qla@fakemail.com", position="Rhytmic Gymnast",
                        height=70, weight=95, team_id=5)
athlete_2_5 = Athlete(first_name="Virginia", last_name="Lake", email="vlake@fakegmail.com", position="Rhytmic Gymnast",
                        height=73, weight=90.5, team_id=5)
athlete_3_5 = Athlete(first_name="Victoria", last_name="Men", email="vmen@fakegmail.com", position="Rhytmic Gymnast",
                        height=57, weight=95.0, team_id=5)
athlete_4_5 = Athlete(first_name="Marie", last_name="More", email="mmore@fakegmail.com", position="Rhytmic Gymnast",
                        height=58, weight=100.2, team_id=5)
athlete_5_5 = Athlete(first_name="Ella", last_name="Pow", email="epow@fakegmail.com", position="Rhytmic Gymnast",
                        height=62, weight=105.5, team_id=5)
athlete_6_5 = Athlete(first_name="Melanie", last_name="Kilt", email="mkilt@fakegmail.com", position="Rhytmic Gymnast",
                        height=64, weight=97.0, team_id=5)

# TEAM 6 #

athlete_1_6 = Athlete(first_name="Laura", last_name="La", email="qla@fakemail.com", position="Rhytmic Gymnast",
                        height=70, weight=95, team_id=6)
athlete_2_6 = Athlete(first_name="Louanne", last_name="Lake", email="vlake@fakegmail.com", position="Rhytmic Gymnast",
                        height=73, weight=90.5, team_id=6)
athlete_3_6 = Athlete(first_name="Lexa", last_name="Men", email="vmen@fakegmail.com", position="Rhytmic Gymnast",
                        height=57, weight=95.0, team_id=6)
athlete_4_6 = Athlete(first_name="Belle", last_name="More", email="mmore@fakegmail.com", position="Rhytmic Gymnast",
                        height=58, weight=100.2, team_id=6)
athlete_5_6 = Athlete(first_name="Maya", last_name="Pow", email="epow@fakegmail.com", position="Rhytmic Gymnast",
                        height=62, weight=105.5, team_id=6)
athlete_6_6 = Athlete(first_name="Olga", last_name="Kilt", email="okilt@fakegmail.com", position="Rhytmic Gymnast",
                        height=64, weight=97.0, team_id=6)


athletes = [ athlete_1_1, athlete_2_1, athlete_3_1, athlete_4_1, athlete_5_1, athlete_6_1,
             athlete_1_2, athlete_2_2, athlete_3_2, athlete_4_2, athlete_5_2, athlete_6_2,
             athlete_1_3, athlete_2_3, athlete_3_3, athlete_4_3, athlete_5_3, athlete_6_3,
             athlete_1_4, athlete_2_4, athlete_3_4, athlete_4_4, athlete_5_4, athlete_6_4,
             athlete_1_5, athlete_2_5, athlete_3_5, athlete_4_5, athlete_5_5, athlete_6_5,
             athlete_1_6, athlete_2_6, athlete_3_6, athlete_4_6, athlete_5_6, athlete_6_6  ]


## ADD WORKOUTS ##

workout_1 = Workout(name="Upper Body Strength", description="Workout targets upperbody strength")
workout_2 = Workout(name="Lower Body Strength", description="Workout targets lowerbody strength")
workout_3 = Workout(name="Core Strength", description="Workout targets core strength")
workout_4 = Workout(name="Lower Body Endurance", description="Tabata Style workout targets lowerbody endurance")
workout_5 = Workout(name="Upper Body Endurance", description="Tabata Style workout targets lowerbody endurance")
workout_6 = Workout(name="Core Body Endurance", description="Tabata Style workout targets lowerbody endurance")
workout_7 = Workout(name="Total Body", description="EMOM style workout for Total Body strength and endurance")
workout_8 = Workout(name="Hiit - hardcore", description="HiiT workout - a hardcore challenge")
workout_9 = Workout(name="Hiit - medium", description="HiiT workout - a medium challenge")
workout_10 = Workout(name="Hiit - starter", description="HiiT workout - a starter challenge")

workouts = [ workout_1,  workout_2, workout_3, workout_4, workout_5,
             workout_6, workout_7, workout_8, workout_9, workout_10 ]
                                                       


## ADD ATHLETE_WORKOUTS ##

athlete_workout_1_1 = Athlete_workout(rpe_avg=7, workout_id=1, athlete_id=1)
athlete_workout_2_1 = Athlete_workout(rpe_avg=7, workout_id=2, athlete_id=1)
athlete_workout_2_2 = Athlete_workout(rpe_avg=7, workout_id=2, athlete_id=2)
athlete_workout_3_2 = Athlete_workout(rpe_avg=7, workout_id=3, athlete_id=2)
athlete_workout_4_3 = Athlete_workout(rpe_avg=7, workout_id=4, athlete_id=3)
athlete_workout_5_3 = Athlete_workout(rpe_avg=7, workout_id=5, athlete_id=3)
athlete_workout_6_4 = Athlete_workout(rpe_avg=7, workout_id=6, athlete_id=4)
athlete_workout_7_4 = Athlete_workout(rpe_avg=7, workout_id=7, athlete_id=4)
athlete_workout_8_10 = Athlete_workout(rpe_avg=7, workout_id=8, athlete_id=10)
athlete_workout_9_10 = Athlete_workout(rpe_avg=7, workout_id=9, athlete_id=10)

athlete_workout_1_12 = Athlete_workout(rpe_avg=7, workout_id=1, athlete_id=12)
athlete_workout_2_12 = Athlete_workout(rpe_avg=7, workout_id=2, athlete_id=12)
athlete_workout_2_24 = Athlete_workout(rpe_avg=7, workout_id=2, athlete_id=24)
athlete_workout_3_24 = Athlete_workout(rpe_avg=7, workout_id=3, athlete_id=24)
athlete_workout_4_34 = Athlete_workout(rpe_avg=7, workout_id=4, athlete_id=34)
athlete_workout_5_34 = Athlete_workout(rpe_avg=7, workout_id=5, athlete_id=34)
athlete_workout_7_16 = Athlete_workout(rpe_avg=7, workout_id=7, athlete_id=16)
athlete_workout_8_15 = Athlete_workout(rpe_avg=7, workout_id=8, athlete_id=15)
athlete_workout_6_16 = Athlete_workout(rpe_avg=7, workout_id=6, athlete_id=16)
athlete_workout_9_27 = Athlete_workout(rpe_avg=7, workout_id=9, athlete_id=27)

athlete_workouts = [ athlete_workout_1_1, athlete_workout_2_1, athlete_workout_2_2, athlete_workout_3_2, 
                     athlete_workout_4_3, athlete_workout_5_3, athlete_workout_6_4, athlete_workout_7_4, 
                     athlete_workout_8_10, athlete_workout_9_10, athlete_workout_1_12, athlete_workout_2_12, 
                     athlete_workout_2_24, athlete_workout_3_24, athlete_workout_4_34, athlete_workout_5_34, 
                     athlete_workout_7_16, athlete_workout_8_15, athlete_workout_6_16, athlete_workout_9_27  ]

## ADD OBJECTS TO SESSION ##

db.session.add_all(users)
db.session.add_all(teams)
db.session.add_all(athletes)
db.session.add_all(workouts)

## COMMIT !IMPORTANT ##
db.session.commit()


## COMMIT AFTER CREATION OF ATHLETES AND WORKOUTS !IMPORTANT ##
db.session.add_all(athlete_workouts)
db.session.commit()
