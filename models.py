from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime as dt
import datetime

bcrypt = Bcrypt()
db = SQLAlchemy()



# SET DATE AND DEFAULTS ##

CURR_DATE = datetime.datetime.now().strftime('%Y-%m-%d')
HEIGHT_DEFAULT = 0
WEIGHT_DEFAULT = 0.0
RPE_DEFAULT = 0
REPS_DEFAULT = 7



def connect_db(app):
    """ Connect to database. """
    db.app = app
    db.init_app(app)


class User(db.Model):
    """ Class to instantiate a User class and methods """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    image_url = db.Column(db.Text, default="/static/images/default-pic.png")
    header_image_url = db.Column(db.Text, default="/static/images/warbler-hero.jpg")
    created_on = db.Column(db.DateTime, nullable=False, default=CURR_DATE)

    teams = db.relationship("Team", backref="user", cascade="all, delete")

    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {self.email}, {self.first_name}, {self.last_name}, {self.image_url}, {self.header_image_url}, {self.created_on}>"

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"

    @property
    def friendly_date(self):
        """Return nicely-formatted date."""

        return self.created_on.strftime("%a %b %-d  %Y")

    @classmethod
    def register(cls, username, password, first_name, last_name, email, image_url, header_image_url):
        """ Register user with Hashed passwor and return user. """
        hashed = bcrypt.generate_password_hash(password)

        hashed_utf8 = hashed.decode("utf8")
        user = cls(username=username, password=hashed_utf8,
                   first_name=first_name, last_name=last_name, email=email, image_url=image_url, header_image_url=header_image_url)

        return user

    @classmethod
    def authenticate(cls, username, password):
        """ Class method to users existence and that the password is correct. """
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False

class Team(db.Model):
    """ Class to instantiate a Team class and methods"""
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    location = db.Column(db.Text, nullable=False)
    discipline = db.Column(db.Text, nullable=False)
    team_image_url = db.Column(db.Text, default="/static/images/default-pic.png")
    created_on = db.Column(db.DateTime, default=CURR_DATE)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='cascade'))

    
    
    athletes = db.relationship("Athlete", backref="team", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Team #{self.id}: {self.name}, {self.location}, {self.discipline}, {self.team_image_url}, {self.created_on}>"

    

class Athlete(db.Model):
    """ Class to instantiate a Athlete class and methods"""
    __tablename__ = "athletes"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50))
    position = db.Column(db.String(30), nullable=False)
    height = db.Column(db.Integer, default=HEIGHT_DEFAULT)
    weight = db.Column(db.Float, default=WEIGHT_DEFAULT)
    athlete_image_url = db.Column(db.Text, default="/static/images/default-pic.png")
    medical_status = db.Column(db.Text, default="Full Duty")
    created_on = db.Column(db.DateTime, default=CURR_DATE)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id', ondelete='cascade'))

    athlete_workouts = db.relationship("Athlete_workout", backref="athlete", cascade="all, delete")
    
    def __repr__(self):
        return f"<Athlete #{self.id}: {self.first_name}, {self.last_name}, {self.email}, {self.position}, {self.height}, {self.weight}, {self.athlete_image_url}, {self.medical_status}, {self.created_on}>"

    @property
    def full_name(self):
        """Return full name of athlete."""

        return f"{self.first_name} {self.last_name}"
    
    @property
    def friendly_date(self):
        """Return nicely-formatted date."""

        return self.created_on.strftime("%a %b %-d  %Y")


class Workout(db.Model):
    """ Class to instantiate a Workout class and methods"""
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    athlete_workouts = db.relationship("Athlete_workout", backref="workout")
    workout_exercises = db.relationship("Workout_exercise", backref="workout")

    def __repr__(self):
        return f"<Workout #{self.id}: {self.name}, {self.description}>"


class Athlete_workout(db.Model):
    """ Class to instantiate a Athlete_workout class and methods"""
    __tablename__ = "athlete_workouts"

    id = db.Column(db.Integer, primary_key=True)
    rpe_avg = db.Column(db.Integer, default=RPE_DEFAULT)
    workout_date = db.Column(db.DateTime, default=CURR_DATE)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
    athlete_id = db.Column(db.Integer, db.ForeignKey('athletes.id')) 

    athlete_workout_exercise = db.relationship("Athlete_workout_exercise", backref="athlete_workout", cascade="all, delete")

    def __repr__(self):
        return f"<Athlete_workout #{self.id}: {self.rpe_avg}, {self.workout_date}, {self.workout_id}, {self.athlete_id}>"

class Category(db.Model):
    """ Class to instantiate a Category class and methods"""
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<Category #{self.id}: {self.category_name}>"


class Equipment(db.Model):
    """ Class to instantiate a Equipment class and methods"""
    __tablename__ = "equipment"

    id = db.Column(db.Integer, primary_key=True)
    equipment_name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Category #{self.id}: {self.equipment_name}>"


class Muscle(db.Model):
    """ Class to instantiate a Muscle class and methods"""
    __tablename__ = "muscles"

    id = db.Column(db.Integer, primary_key=True)
    muscle_name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.Text, default="/static/images/default-pic.png")

    def __repr__(self):
        return f"<Category #{self.id}: {self.muscle_name}, {self.image_url}>"


class Exercise(db.Model):
    """ Class to instantiate a Exercise class and methods"""
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    default_reps = db.Column(db.Integer, default=REPS_DEFAULT)
    image_url = db.Column(db.Text, default="/static/images/default-pic.png")
    wger_id = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
    muscle_id = db.Column(db.Integer, db.ForeignKey('muscles.id')) 


    categories = db.relationship("Category", backref="exercise")
    equipment = db.relationship("Equipment", backref="exercise")
    muscles = db.relationship("Muscle", backref="exercise")

    workout_exercises = db.relationship("Workout_exercise", backref="exercise", cascade="all, delete")

    def __repr__(self):
        return f"<Exercise #{self.id}: {self.name}, {self.description}, {self.default_reps}, {self.image_url}, {self.category_id}, {self.equipment_id}, {self.muscle_id}>"


class Workout_exercise(db.Model):
    """ Class to instantiate a Workout_exercise class and methods"""
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id', ondelete='cascade'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id', ondelete='cascade')) 

    athlete_workout_exercise = db.relationship("Athlete_workout_exercise", backref="workout_exercise", cascade="all, delete")

    def __repr__(self):
        return f"<Athlete_workout #{self.id}: {self.workout_id}, {self.exercise_id}>"



class Athlete_workout_exercise(db.Model):
    """ Class to instantiate a Athlete_workout_exercise class and methods"""
    __tablename__ = "athlete_workouts_exercises"

    id = db.Column(db.Integer, primary_key=True)
    athlete_workout_id = db.Column(db.Integer, db.ForeignKey('athlete_workouts.id', ondelete='cascade'))
    workout_exercise_id = db.Column(db.Integer, db.ForeignKey('workout_exercises.id', ondelete='cascade')) 

    def __repr__(self):
        return f"<Athlete_workouts_exercise#{self.id}: {self.athlete_workout_id}, {self.workout_exercise_id}>"


class Image(db.Model):
    """ Class to instantiate a Image class and methods"""
    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True)
    exercise_image_url = db.Column(db.Text, nullable=False)
    wger_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Image #{self.id}: {self.exercise_image_url }, {self.wger_id }>"


class Assignment_log(db.Model):
    """Class to track Assigment status"""

    id = db.Column(db.Integer, primary_key=True)
    athlete_workout_id = db.Column(db.Integer, nullable=False)
    is_completed = db.Column(db.Boolean, default=False, nullable=False)

     
    def __repr__(self):
        return f"<Assigment_log #{self.id}: {self.athlete_workout_id }, {self.is_completed}>"
