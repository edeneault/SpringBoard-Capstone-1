from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime as dt
import datetime

bcrypt = Bcrypt()
db = SQLAlchemy()

# SET DATE ##

CURR_DATE = datetime.datetime.now().strftime('%Y-%m-%d')
HEIGHT_DEFAULT = 0
WEIGHT_DEFAULT = 0.0
RPE_DEFAULT = 0

# print(CURR_DATE)


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

    

    # @classmethod
    # def register(cls, username, pwd, first_name, last_name, email):
    #     """ Register user with Hashed passwor and return user. """
    #     hashed = bcrypt.generate_password_hash(pwd)

    #     hashed_utf8 = hashed.decode("utf8")
    #     user = cls(username=username, password=hashed_utf8,
    #                first_name=first_name, last_name=last_name, email=email)

    #     return user

    # @classmethod
    # def authenticate(cls, username, password):
    #     """ Class method to users existence and that the password is correct. """
    #     user = User.query.filter_by(username=username).first()
    #     if user and bcrypt.check_password_hash(user.password, password):
    #         return user
    #     else:
    #         return False

class Team(db.Model):
    """ Class to instantiate a Team class and methods"""
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    location = db.Column(db.Text, nullable=False)
    discipline = db.Column(db.Text, nullable=False)
    team_image_url = db.Column(db.Text, default="/static/images/default-pic.png")
    created_on = db.Column(db.DateTime, default=CURR_DATE)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='cascade'))

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


class Workout(db.Model):
    """ Class to instantiate a Workout class and methods"""
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)

    athlete_workouts = db.relationship("Athlete_workout", backref="workout", cascade="all, delete")

    def __repr__(self):
        return f"<Workout #{self.id}: {self.name}, {self.description}>"


class Athlete_workout(db.Model):
    """ Class to instantiate a Athlete_workout class and methods"""
    __tablename__ = "athlete_workouts"

    id = db.Column(db.Integer, primary_key=True)
    rpe_avg = db.Column(db.Integer, default=RPE_DEFAULT)
    workout_date = db.Column(db.DateTime, default=CURR_DATE)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id', ondelete='cascade'))
    athlete_id = db.Column(db.Integer, db.ForeignKey('athletes.id', ondelete='cascade')) 



    def __repr__(self):
        return f"<Athlete_workout #{self.id}: {self.rpe_avg}, {self.workout_date}, {self.workout_id}, {self.athlete_id}>"