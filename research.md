# SpringBoard - Capstone 1 - Ideas
###### by: Etienne Deneault

### Idea #1:

### Lightweight Athlete/Performance Artist Management System

###### Application Main Function

* Provide coaches and performance enhancement specialist with a lightweight system to manage their teams/athletes/performance artists.

###### Application Secondary Function
* Provide coaches and athletes quick access to the most useful tools for Day to Day use.

###### Problems Solved

* There are many athlete management systems avaialble in the market but most have a difficult barrier of access for coaches and smaller athletic organizations.  These "barriers" are due to the following: cost of access, complexity of implementation, complex tooling that generates a significant amount of work for the user/administrator.

* Many of the athlete mamagement systems do not offer easy access to features that coaches use on a daily basis.  The result of this issue is that coaches do not use the functionality available because in "real-world" time it is too difficult to integrate into their coaching workflows.

###### Application Features

*No Auth Access*
* Quick Access - *workout selector*
* Quick Access - *custom workout selector/builder*
* Quick Access - *workout timer example configurations:  HIIT Timer, Circuit/Tabata Timer, Round Timer*

*With Auth Access*

* Team/Athlete Managment Creation
* Team/Athlete Management Dashboard
* CRUD custom workouts to DB 
* CRUD training sessions to DB
* Quick Access - *training session plan*
* Quick Access - *training session athlete RPE logging (RPE: Rate of Perceived Exertion)

   

###### API

* API to be used is: <a style="color: CadetBlue" href="https://wger.de/en/software/api">WEGR</a>
    * >Public Endpoints: 
    daysofweek, equipment, exercise, exerciseinfo, exercisecategory, exercisecomment, exerciseimage, ingredient, ingredientinfo, ingredienttoweightunit, language, license, muscle, weightunit,setting-repetitionunit, setting-weightunit

    * >Private Endpoints: day, meal, mealitem, nutritionplan, schedule, schedulestep, set, setting, userprofile,weightentry, workout, workoutlog

##### Technologies
* Python/Flask, PostgreSQL, QLAlchemy, Heroku, Jinja, RESTful APIs, JavaScript, HTML, CSS, WTForms


## Idea #2:

### Science Fiction News Feed 

###### Application Main Function

* Provide users with a curated content feed related to Science Fiction.

###### Application Secondary Function
* Add sentiment analysis of content and CRUD capibily for users to save content
and share content with friends.


###### Problems Solved

* Curation of content.  A challenge encountered while browsing for new science fiction content, news and social media content is the lack of curation.  This content feed would provide a curation of the content fed to the stream using sentiment analysis.

###### Application Features

 No Auth Access
* News Feed with SciFi/NewTech news - Sort feature (Trending/Newest)
* Search of Articles in news feed database
* Sentiment Analysis of Article
* Submit for curation 

With Auth Access

* Become a Curator
* Review articles submitted for curation
* CRUD to "No Auth facing page" articles that are approved by curator

##### API

* API's to be used is: <a style="color: CadetBlue" href="http://demo.intellexer.com/">intellexer</a>, <a style="color: CadetBlue" href="https://newsapi.org/docs/client-libraries/python">NewsAPI</a>,  <a style="color: CadetBlue" href="https://currentsapi.services/en">Currents</a>
                        

##### Technologies
* Python/Flask, PostgreSQL, QLAlchemy, Heroku, Jinja, RESTful APIs, JavaScript, HTML, CSS, WTForms


