### GYM HERO - Lightweight Athlete/Performance Artist Management System
###### by: Etienne Deneault

Designed as Capstone project for the SpringBoard Software Engineering Bootcamp, GYM HERO is a lightweight *Athlete Management Web Application*.  There are many athlete management systems avaialble in the market but most have a difficult barrier of access for coaches and smaller athletic organizations.  These "barriers" are due to the following: cost of access, complexity of implementation, complex tooling that generates a significant amount of work for the user/administrator.  

 Many of the athlete mamagement systems do not offer easy access to features that coaches use on a daily basis.  The result of this issue is that coaches do not use the functionality available because in "real-world" time it is difficult to integrate into their coaching workflows.

<figure class="video_container">
 <video controls loop class="col-sm-12 border" width="640" height="360" muted>
                    <source src="https://res.cloudinary.com/gym-hero/video/upload/v1620253316/gifs/Athlete-management_kc5nge.mp4" type="video/mp4">
 </video>
</figure>


###### Application Main Function

* Provide coaches and performance enhancement specialist with a lightweight system to manage their teams/athletes/performance artists.

###### Application Secondary Function
* Provide coaches and athletes quick access to the most useful tools for Day to Day use. Workouts and Timers.

###### Problems Solved

* There are many athlete management systems avaialble in the market but most have a difficult barrier of access for coaches and smaller athletic organizations.  These "barriers" are due to the following: cost of access, complexity of implementation, complex tooling that generates a significant amount of work for the user/administrator.

* Many of the athlete mamagement systems do not offer easy access to features that coaches use on a daily basis.  The result of this issue is that coaches do not use the functionality available because in "real-world" time it is too difficult to integrate into their coaching workflows.

###### Target Users

* The target user fir the application are Coaches working with smaller team organizations or a coach with a "single" or "few" athletes in individual sports

###### Application Features

*No Auth Access*
* Quick Access - *workout selector* 
* Quick Access - *workout timer example configurations*
    * Timers built with dynamic javasript **OOP class Timer extended classes HiitTimer, RoundTimer, CircuitTimer**

*With Auth Access*

* Team/Athlete Managment (CRUD Teams, Athletes, Exercises, Workouts)
* Team/Athlete Management Dashboard - Team Data view and basic analysis (RPE, workload over time)
* CRUD workouts 
* CRUD Timers
* CRUD training sessions
* CRUD training plans


   

###### API

* API to be used is: <a style="color: CadetBlue" href="https://wger.de/en/software/api">WEGR</a>
    * >Public Endpoints to be used: 
     exercise, exerciseinfo, exercisecategory, muscle, exercisecomment, exerciseimage, muscle, exerciseinfo, equipment


###### ATHLETE WORKOUT DATABASE SCHEMA 

<img src="Database-Design-Capstone-1.png"
     alt="DATABASE"
     style="float: left; margin-right: 10px;" />

* additional tables will be needed for medical_status, timers and training_plans.

###### API ENDPOINTS / ROUTES PLAN

###### Base
    * GET /homepage
    * 404 error_handler

###### No Auth - Timers and Workouts
    * GET /timers
        * GET /timers/id
    * GET /workouts
        * GET /workouts/id
        
    ***Authentification / Authorization***
    * GET / POST /register
    * GET / POST /login
    * GET /logout

###### With Auth 
    * GET /dashboard

###### Users
    * GET /users/username
    * GET /users/logout
    * GET / POST /users/username/add_team

###### Teams 
    * GET / POST teams
    * GET teams/id
    * GET / POST teams/id/edit
    * GET / POST teams/id/delete

###### Athletes

    * GET /POST athletes
    * GET athletes/id
    * GET / POST athletes/id/edit
    * GET / POST athletes/id/delete

###### Exercises
    * GET / POST exercises
    * GET exercises/id
    * GET / POST exercises/id/edit
    * GET / POST exercises/id/delete

###### With Auth - Timers and Workouts
    * POST timers
    * GET / POST exercises/id/edit
    * GET / POST exercises/id/delete
    * POST workouts
    * GET / POST workouts/id/edit
    * GET / POST workouts/id/delete

##### Additional Routes for workouts, workouts_sesssions and training plans needed as well.

##### Technologies
* Python/Flask, PostgreSQL, QLAlchemy, Heroku, Jinja, RESTful APIs, JavaScript, HTML, CSS, WTForms, Bcryt



<p style="color: red;">INFO:  Documentation and Testing in Progress</p>
<p style="color: dark-gray;">Kindly start an issue to help me dedug the application and implement new features.</p>


