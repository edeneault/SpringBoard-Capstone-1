# import os

# from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g
# from flask_debugtoolbar import DebugToolbarExtension
# from sqlalchemy.exc import IntegrityError
# from datetime import datetime as dt
# import datetime
# import requests

# from utils import *
# from forms import LoginForm, RegisterForm
# from models import (connect_db, db, User, Team, Athlete, Workout, Athlete_workout, Exercise, Category, 
#                     Equipment, Muscle, Workout_exercise, Athlete_workout_exercise)
# from pprint import pprint
# import json
# import urllib.request


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