"""Seed file to make sample data for users and posts db."""

from models import (db, User, Team, Athlete, Workout, Athlete_workout, Exercise, Category, 
                    Equipment, Muscle, Workout_exercise, Athlete_workout_exercise)
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
                image_url="https://miro.medium.com/max/3150/1*vx4SBuW5YM3s1Pxyk00mSQ.jpeg", 
                header_image_url="https://images.unsplash.com/photo-1580237754794-0e26a1d7ee03?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1414&q=80")

coach2 = User(username="msparks", password="password2", email="msparks@fakegmail.com", first_name="Matthew", last_name="Sparks")
coach3 = User(username="adeneault", password="password3", email="apjarova@gmail.com", first_name="Alexandra", last_name="Deneault",
                 image_url="https://iv1.lisimg.com/image/20508627/666full-alexandra-apjarova.jpg",
                 header_image_url="https://images.unsplash.com/photo-1519925610903-381054cc2a1c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1350&q=80")
coach4 = User(username="beachcoach", password="BeachCoach", email="beach@coach.com", first_name="Laura", last_name="Summers",
                image_url="https://iv1.lisimg.com/image/20508627/666full-alexandra-apjarova.jpg",
                header_image_url="https://images.unsplash.com/photo-1519925610903-381054cc2a1c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1350&q=80" )
users = [coach1, coach2, coach3, coach4]

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
exercise_5 = Exercise(name="concentration curl", 
    description="Using dumbells, sit on a bench, one arm at a time, position your arm against your leg and perform a curl.",
    wger_id=74, category_id=2, equipment_id=3, muscle_id=4)


exercises = [ exercise_1, exercise_2, exercise_3, exercise_4, exercise_5 ]


## CATEGORIES ##

category_1 = Category(category_name="Abs")
category_2 = Category(category_name="Arms")
category_3 = Category(category_name="Back")
category_4 = Category(category_name="Calves")
category_5 = Category(category_name="Chest")
category_6 = Category(category_name="Legs")
category_7 = Category(category_name="Shoulders")

categories = [ category_1, category_2, category_3, category_4, category_5, category_6, category_7 ]


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

equipment = [ equipment_1, equipment_2, equipment_3, equipment_4, equipment_5,
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

muscles = [ muscle_1, muscle_2, muscle_3, muscle_4, muscle_5,
             muscle_6, muscle_7, muscle_8, muscle_9, muscle_10,
             muscle_11, muscle_12, muscle_13, muscle_14, muscle_15 ]

## WORKOUT_EXERCISE ##

workout_exercise_1_1 = Workout_exercise( workout_id=1, exercise_id=1 )
workout_exercise_1_2 = Workout_exercise( workout_id=1, exercise_id=2 )
workout_exercise_2_3 = Workout_exercise( workout_id=2, exercise_id=3 )
workout_exercise_2_4 = Workout_exercise( workout_id=2, exercise_id=4 )
workout_exercise_2_5 = Workout_exercise( workout_id=2, exercise_id=5 )
workout_exercise_3_1 = Workout_exercise( workout_id=2, exercise_id=1 )
workout_exercise_3_3 = Workout_exercise( workout_id=3, exercise_id=3 )
workout_exercise_3_2 = Workout_exercise( workout_id=3, exercise_id=2 )
workout_exercise_4_5 = Workout_exercise( workout_id=4, exercise_id=5 )
workout_exercise_4_4 = Workout_exercise( workout_id=4, exercise_id=4 )
workout_exercise_4_2 = Workout_exercise( workout_id=4, exercise_id=2 )

workout_exercise_5_1 = Workout_exercise( workout_id=5, exercise_id=1 )
workout_exercise_5_2 = Workout_exercise( workout_id=5, exercise_id=2 )
workout_exercise_5_3 = Workout_exercise( workout_id=5, exercise_id=3 )
workout_exercise_6_4 = Workout_exercise( workout_id=6, exercise_id=4 )
workout_exercise_6_5 = Workout_exercise( workout_id=6, exercise_id=5 )
workout_exercise_6_1 = Workout_exercise( workout_id=6, exercise_id=1 )
workout_exercise_7_3 = Workout_exercise( workout_id=7, exercise_id=3 )
workout_exercise_7_4 = Workout_exercise( workout_id=7, exercise_id=2 )
workout_exercise_7_5 = Workout_exercise( workout_id=7, exercise_id=5 )
workout_exercise_8_1 = Workout_exercise( workout_id=8, exercise_id=1 )
workout_exercise_8_2 = Workout_exercise( workout_id=8, exercise_id=2 )

workout_exercise_8_5 = Workout_exercise( workout_id=8, exercise_id=5 )
workout_exercise_9_4 = Workout_exercise( workout_id=9, exercise_id=4)
workout_exercise_9_4 = Workout_exercise( workout_id=9, exercise_id=1 )
workout_exercise_9_2 = Workout_exercise( workout_id=9, exercise_id=2 )
workout_exercise_10_4 = Workout_exercise( workout_id=10, exercise_id=4 )
workout_exercise_10_5 = Workout_exercise( workout_id=10, exercise_id=5 )

workout_exercises = [ workout_exercise_1_1, workout_exercise_1_2, workout_exercise_2_3, workout_exercise_2_4,
workout_exercise_2_5, workout_exercise_3_1, workout_exercise_3_3,  workout_exercise_3_2,  workout_exercise_4_5, 
workout_exercise_4_4, workout_exercise_4_2, workout_exercise_5_1, workout_exercise_5_2, workout_exercise_5_3, 
workout_exercise_6_4, workout_exercise_6_5, workout_exercise_6_4, workout_exercise_6_5, workout_exercise_7_3, 
workout_exercise_7_4, workout_exercise_7_5, workout_exercise_8_1, workout_exercise_8_2, workout_exercise_8_5, 
workout_exercise_9_4, workout_exercise_9_2, workout_exercise_10_4, workout_exercise_10_5 ]


## ATHLETE_WORKOUT_EXERCISES ##

athlete_workout_exercise_1 = Athlete_workout_exercise( athlete_workout_id=1, workout_exercise_id =1  )
athlete_workout_exercise_2 = Athlete_workout_exercise( athlete_workout_id=2, workout_exercise_id =2  )
athlete_workout_exercise_3 = Athlete_workout_exercise( athlete_workout_id=3, workout_exercise_id =3  )
athlete_workout_exercise_4 = Athlete_workout_exercise( athlete_workout_id=4, workout_exercise_id =4  )
athlete_workout_exercise_5 = Athlete_workout_exercise( athlete_workout_id=5, workout_exercise_id =5  )
athlete_workout_exercise_6 = Athlete_workout_exercise( athlete_workout_id=6, workout_exercise_id =6  )
athlete_workout_exercise_7 = Athlete_workout_exercise( athlete_workout_id=7, workout_exercise_id =7  )
athlete_workout_exercise_8 = Athlete_workout_exercise( athlete_workout_id=8, workout_exercise_id =8  )
athlete_workout_exercise_9 = Athlete_workout_exercise( athlete_workout_id=9, workout_exercise_id =9  )
athlete_workout_exercise_10 = Athlete_workout_exercise( athlete_workout_id=10, workout_exercise_id=10  )
athlete_workout_exercise_11 = Athlete_workout_exercise( athlete_workout_id=11, workout_exercise_id =11  )
athlete_workout_exercise_12 = Athlete_workout_exercise( athlete_workout_id=12, workout_exercise_id =12  )
athlete_workout_exercise_13 = Athlete_workout_exercise( athlete_workout_id=13, workout_exercise_id =13  )
athlete_workout_exercise_14 = Athlete_workout_exercise( athlete_workout_id=14, workout_exercise_id =14  )
athlete_workout_exercise_15 = Athlete_workout_exercise( athlete_workout_id=15, workout_exercise_id =15  )
athlete_workout_exercise_16 = Athlete_workout_exercise( athlete_workout_id=16, workout_exercise_id =16  )
athlete_workout_exercise_17 = Athlete_workout_exercise( athlete_workout_id=17, workout_exercise_id =17  )
athlete_workout_exercise_18 = Athlete_workout_exercise( athlete_workout_id=18, workout_exercise_id =18  )
athlete_workout_exercise_19 = Athlete_workout_exercise( athlete_workout_id=19, workout_exercise_id =19  )
athlete_workout_exercise_20 = Athlete_workout_exercise( athlete_workout_id=20, workout_exercise_id =20  )

athlete_workout_exercises = [ athlete_workout_exercise_1, athlete_workout_exercise_2, athlete_workout_exercise_3, athlete_workout_exercise_4,
                              athlete_workout_exercise_5, athlete_workout_exercise_6, athlete_workout_exercise_7, athlete_workout_exercise_8,
                              athlete_workout_exercise_9, athlete_workout_exercise_10, athlete_workout_exercise_11, athlete_workout_exercise_12,
                              athlete_workout_exercise_13, athlete_workout_exercise_14, athlete_workout_exercise_15, athlete_workout_exercise_16,
                              athlete_workout_exercise_17, athlete_workout_exercise_18, athlete_workout_exercise_19, athlete_workout_exercise_20 ]

## ADD OBJECTS TO SESSION ##

db.session.add_all(users)
db.session.add_all(teams)
db.session.add_all(athletes)
db.session.add_all(workouts)
db.session.add_all(exercises)
db.session.add_all(categories)
db.session.add_all(equipment)
db.session.add_all(muscles)

## COMMIT !IMPORTANT ##
db.session.commit()


## COMMIT AFTER CREATION OF ATHLETES AND WORKOUTS !IMPORTANT ##
db.session.add_all(athlete_workouts)
db.session.commit()

## COMMIT AFTER CREATION OF EXERCISES AND WORKOUTS !IMPORTANT ## 
db.session.add_all(workout_exercises)
db.session.commit()

## COMMIT AFTER CREATION OF workout_exercises AND athlete_workouts !IMPORTANT ## 
db.session.add_all(athlete_workout_exercises)
db.session.commit()