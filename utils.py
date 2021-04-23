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


# def get_thumbnail_images():
#     """ Function to get all thumbnail images from API """
#     resp = requests.get(f"https://wger.de/api/v2/exerciseimage/{exercise_id}/thumbnails/", timeout=2)
#     resp = resp.json()
    
#     if resp == []:
#         image_url = "/media/exercise-images/192/Bench-press-1.png"
#     else:
#         image_url = resp["thumbnail"]["url"] 



CATEGORY_OBJ = { "Abs": 1, "Arms": 2, "Back": 3, "Calves": 4, "Chest": 5, "Legs": 6, "Shoulders": 7 }

EQUIPMENT_OBJ = {   "Barbell": 1, "Bench": 2, "Dumbbell": 3, "Gym mat": 4, "Incline bench": 5, "Kettlebell": 6,
                    "none (bodyweight exercise)": 7, "Pull-up bar": 8, "Swiss Ball": 9, "SZ-Bar": 10 }

MUSCLE_OBJ = {  "Anterior deltoid": 1,  "Biceps brachii": 2, "Biceps femoris": 3, "Brachialis": 4, "Gastrocnemius": 5,
                "Gluteus maximus": 6, "Latissimus dorsi": 7, "Obliquus externus abdominis": 8, "Pectoralis major": 9,
                "Quadriceps femoris": 10, "Rectus abdominis": 11, "Serratus anterior": 12, "Soleus": 13, "Trapezius": 14,
                 "Triceps brachii": 15 }





def ip6_force_disabled():
    """ force disable ipv6, use ipv4 """
    wger_request = socket.AF_INET
    if urllib3_cn.HAS_IPV4:
        wger_request = socket.AF_INET4 
    return wger_request

urllib3_cn.ip6_force_disabled = ip6_force_disabled

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


def insert_images():
    """ utility to collect all exercise images from API and input in table """
    NEXT_IMAGE = ""
    for i in range(0,3):

        if NEXT_IMAGE != "":
            url = NEXT_IMAGE

            # url = "https://wger.de/api/v2/exerciseimage/?is_main=True"
        
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
                # try:
                image = Image(exercise_image_url=exercise_image_url, wger_id=wger_id)
                db.session.add(image)
                db.session.commit()
                # except:
                #     continue
        
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
                # try:
                image = Image(exercise_image_url=exercise_image_url, wger_id=wger_id)
                db.session.add(image)
                db.session.commit()
                # except:
                #     continue
        time.sleep(5)


    # else:
    #     resp = requests.get("https://wger.de/api/v2/exerciseimage/?is_main=True", timeout=1.25)
    #     resp = resp.json()
    #     NEXT_IMAGE = resp["next"]
    #     resp = resp["results"]
    #     print(resp)
    
    
    
     
# insert_images()
    
 ## API request for image - offset 20 every call ##
    # print(NEXT_IMAGE)
    
    # if NEXT_IMAGE:
        
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
    #     NEXT_IMAGE = resp["next"]
    #     resp = resp["results"]
    #     print(resp)



    















# import aiohttp
# import asyncio
# import time

# start_time = time.time()


# async def get_exercise(session, url):
#     async with session.get(url) as resp:
#         exercise = await resp.json()
#         return exercise

# async def main():

#     async with aiohttp.ClientSession() as session:

#         url = f'https://wger.de/api/v2/exerciseinfo/?language=2'
#         response = asyncio.ensure_future(get_exercise(session, url))

#         result = await response
#         return result

# result = asyncio.run(main())
# # print(result)

# exercise1 = result["results"][5]

# name = exercise1["name"]
# description = exercise1["description"]
# muscles = exercise1["muscles"]
# equipment =  exercise1["equipment"]

# new_exercise = { "name": name, "description": description, "muscles": muscles, "equipment": equipment }

# print()
# print()
# print(new_exercise)
# print("--- %s seconds ---" % (time.time() - start_time))



# def parse_exercise_resp(result):


# import logging

# import http.client
# http.client.HTTPConnection.debuglevel = 1

# # You must initialize logging, otherwise you'll not see debug output.
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True

# requests.get("https://wger.de/api/v2/exercise")