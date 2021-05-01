"""Forms for flask-feedback."""

from wtforms import StringField, PasswordField, IntegerField, FloatField, SelectField, TextAreaField, Form, FieldList, FormField
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional
from flask_wtf import FlaskForm
from sqlalchemy.exc import IntegrityError


class LoginForm(FlaskForm):
    """ Login form. """

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1, max=20)],
        render_kw={ "class": "form-control mt-2"}
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=6, max=55)],
        render_kw={ "class": "form-control mt-2"}
    )


class RegisterForm(FlaskForm):
    """ User registration form. """

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1, max=20)],
        render_kw={"class": "form-control mt-2"}
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=6, max=55)],
        render_kw={ "class": "form-control mt-2"}
    )
    email = StringField(
        "Email",
        validators=[InputRequired(), Email(), Length(max=50)],
        render_kw={"class": "form-control mt-2"}
    )
    first_name = StringField(
        "First Name",
        validators=[InputRequired(), Length(max=30)],
        render_kw={"class": "form-control mt-2"}
    )
    last_name = StringField(
        "Last Name",
        validators=[InputRequired(), Length(max=30)],
        render_kw={"class": "form-control mt-2"}
    )
    image_url = StringField('(Optional) Image URL', render_kw={"class": "form-control mt-2"} )
    header_image_url = StringField('(Optional) Team Image URL', render_kw={"class": "form-control mt-2"})



class UserEditForm(FlaskForm):
    """ User edit Form """
    first_name = StringField(
        "First Name",
        validators=[InputRequired(), Length(max=30)],
        render_kw={"class": "form-control mt-2"}
    )
    last_name = StringField(
        "Last Name",
        validators=[InputRequired(), Length(max=30)],
        render_kw={"class": "form-control mt-2"}
    )
    email = StringField(
        "Email",
        validators=[InputRequired(), Email(), Length(max=50)],
        render_kw={"class": "form-control mt-2"}
    )
    image_url = StringField('(Optional) Image URL', render_kw={"class": "form-control mt-2"} )
    header_image_url = StringField('(Optional) Team Image URL', render_kw={"class": "form-control mt-2"})


class TeamForm(FlaskForm):
    """ Team form. """

    name = StringField(
        "Name",
        validators=[InputRequired(), Length(max=50)],
        render_kw={"class": "form-control mt-2", "placeholder": "name"}
    )

    location = StringField(
        "Location",
        validators=[InputRequired(), Length(max=30)],
        render_kw={"class": "form-control mt-2", "placeholder": "location"}
    )

    discipline = StringField(
        "Discipline-Sport",
        validators=[InputRequired(), Length(max=30)],
        render_kw={"class": "form-control mt-2", "placeholder": "Discipline-Sport"}
    )

    team_image_url = StringField(
        '(Optional) Header Image URL',
        render_kw={"class": "form-control mt-2", "placeholder": "Header Image URL"}
    )

class TeamEditForm(FlaskForm):
    """ Team form. """

    name = StringField(
        "Name",
        validators=[InputRequired(), Length(max=30)],
        render_kw={"class": "form-control mt-2", "placeholder": "name"}
    )

    location = StringField(
        "Location",
        validators=[InputRequired(), Length(max=30)],
        render_kw={"class": "form-control mt-2", "placeholder": "location"}
    )

    discipline = StringField(
        "Discipline-Sport",
        validators=[InputRequired(), Length(max=30)],
        render_kw={"class": "form-control mt-2", "placeholder": "Discipline-Sport"}
    )

    team_image_url = StringField(
        '(Optional) Header Image URL',
        render_kw={"class": "form-control mt-2", "placeholder": "Header Image URL"}
    )


class AthleteForm(FlaskForm):
    """ Athlete form. """

    first_name = StringField(
        "First Name",
        validators=[InputRequired(), Length(max=30)],
        render_kw={"class": "form-control mt-2", "placeholder": "first name"}
    )

    last_name = StringField(
        "Last Name",
        validators=[InputRequired(), Length(max=30)],
        render_kw={"class": "form-control mt-2", "placeholder": "last name"}
    )

    email = StringField(
        "Email",
        validators=[InputRequired(), Email(), Length(max=50)],
        render_kw={"class": "form-control mt-2", "placeholder": "email"}
    )

    team_id = SelectField('Athlete Team',
        render_kw={"class": "form-control mt-2", "placeholder": "email"}, 
        coerce=int)
 
    position = StringField(
        "Position",
        validators=[InputRequired(), Length(max=30)],
        render_kw={"class": "form-control mt-2", "placeholder": "position"}
    )

    height = IntegerField(
        "height:",
        validators=[InputRequired(), NumberRange(min=1, max=107)],
        render_kw={"class": "form-control mt-2", "placeholder": "height total inches (ex: 86)"}
    )
    
    weight = FloatField(
        "weight:",
        validators=[InputRequired()],
        render_kw={"class": "form-control mt-2", "placeholder": "weight total kg (ex: 56)"}
    )

    athlete_image_url = StringField(
        '(Optional) Athlete Image URL',
        render_kw={"class": "form-control mt-2", "placeholder": "Athlete Image URL"}
    )

    medical_status = StringField(
        '(Optional) medical status',
        render_kw={"class": "form-control mt-2", "placeholder": "example: Full Duty"}
    )

class AthleteEditForm(FlaskForm):
    """ Athlete form. """

    first_name = StringField(
        "First Name",
        validators=[InputRequired(), Length(max=30)],
        render_kw={"class": "form-control mt-2", "placeholder": "first name"}
    )

    last_name = StringField(
        "Last Name",
        validators=[InputRequired(), Length(max=30)],
        render_kw={"class": "form-control mt-2", "placeholder": "last name"}
    )

    email = StringField(
        "Email",
        validators=[InputRequired(), Email(), Length(max=50)],
        render_kw={"class": "form-control mt-2", "placeholder": "email"}
    )

    team_id = SelectField('Athlete Team',
        render_kw={"class": "form-control mt-2", "placeholder": "email"}, 
        coerce=int)
 
    position = StringField(
        "Position",
        validators=[InputRequired(), Length(max=30)],
        render_kw={"class": "form-control mt-2", "placeholder": "position"}
    )

    height = IntegerField(
        "height:",
        validators=[InputRequired(), NumberRange(min=1, max=107)],
        render_kw={"class": "form-control mt-2", "placeholder": "height total inches (ex: 86)"}
    )
    
    weight = FloatField(
        "weight:",
        validators=[InputRequired()],
        render_kw={"class": "form-control mt-2", "placeholder": "weight total kg (ex: 56)"}
    )

    athlete_image_url = StringField(
        '(Optional) Athlete Image URL',
        render_kw={"class": "form-control mt-2", "placeholder": "Athlete Image URL"}
    )

    medical_status = StringField(
        '(Optional) medical status',
        render_kw={"class": "form-control mt-2", "placeholder": "example: Full Duty"}
    )

class ExerciseForm(FlaskForm):
    """ Exercise form. """
    
    name = StringField(
        "Name",
        validators=[InputRequired(), Length(max=30)],
        render_kw={"class": "form-control mt-2", "placeholder": "name"}
    )

    description = TextAreaField(
        "Description",
        validators=[InputRequired(), Length(max=600)],
        render_kw={"class": "form-control mt-2", "placeholder": " exercise description"}
    )

    default_reps = IntegerField(
        "Reps:",
        validators=[InputRequired(), NumberRange(min=1, max=300)],
        render_kw={"class": "form-control mt-2", "placeholder": "number of reps"}
    )

    image_url = StringField(
        '(Optional) Exercise Image URL',
        render_kw={"class": "form-control mt-2", "placeholder": "Exercise Image URL"}
    )

    category_id = SelectField('Category',
        render_kw={"class": "form-select mt-2", "placeholder": "category"}, 
        coerce=int)

    equipment_id = SelectField('Equipment',
        render_kw={"class": "form-select mt-2", "placeholder": "equipment"}, 
        coerce=int)
    
    muscle_id = SelectField('Muscle',
        render_kw={"class": "form-select mt-2", "placeholder": "primary muscle"}, 
        coerce=int)

class ExerciseEditForm(FlaskForm):
    """ Exercise Edit form. """
    
    name = StringField(
        "Name",
        validators=[InputRequired(), Length(max=30)],
        render_kw={"class": "form-control mt-2", "placeholder": "name"}
    )

    description = TextAreaField(
        "Description",
        validators=[InputRequired(), Length(max=600)],
        render_kw={"class": "form-control mt-2", "placeholder": " exercise description"}
    )

    default_reps = IntegerField(
        "Reps:",
        validators=[InputRequired(), NumberRange(min=1, max=300)],
        render_kw={"class": "form-control mt-2", "placeholder": "number of reps"}
    )

    image_url = StringField(
        '(Optional) Exercise Image URL',
        render_kw={"class": "form-control mt-2", "placeholder": "Exercise Image URL"}
    )

    category_id = SelectField('Category',
        render_kw={"class": "form-select mt-2", "placeholder": "category"}, 
        coerce=int)

    equipment_id = SelectField('Category',
        render_kw={"class": "form-select mt-2", "placeholder": "category"}, 
        coerce=int)
    
    muscle_id = SelectField('Category',
        render_kw={"class": "form-select mt-2", "placeholder": "category"}, 
        coerce=int)


class AddCategoryToWorkoutForm(FlaskForm):
    """ Add exercise to workout form. """
    
    category = SelectField(
        render_kw={"class": "form-select mt-2 me-2",}, 
        coerce=int)

class AddMuscleToWorkoutForm(FlaskForm):
    """ Add exercise to workout form. """
    
    muscle = SelectField(
        render_kw={"class": "form-select mt-2 me-2",}, 
        coerce=int)

class AddEquipmentToWorkoutForm(FlaskForm):
    """ Add exercise to workout form. """
    
    equipment = SelectField(
        render_kw={"class": "form-select mt-2 me-2",}, 
        coerce=int)

class WorkoutForm(FlaskForm):
    """ Workout Add form. """

    name = StringField(
        "Name",
        validators=[InputRequired(), Length(max=100)],
        render_kw={"class": "form-control bg-light bg-gradient mt-2", "placeholder": "workout name"}
    )

    description = TextAreaField("Description",
        validators=[InputRequired(), Length(max=500)],
        render_kw={"class": "form-control bg-light bg-gradient mt-2", "placeholder": "workout description"}
    )

class WorkoutFormStep2(FlaskForm):
    """ Step2 for """
    categories = FormField(AddCategoryToWorkoutForm)

    muscles = FormField(AddMuscleToWorkoutForm)

    equipment = FormField(AddEquipmentToWorkoutForm)


class WorkoutSelectForm(FlaskForm):
    """ Workout Select form. """

    workouts = SelectField('Workouts',
        render_kw={"class": "form-select mt-2"}, 
        coerce=int)
    

class WorkoutEditForm(FlaskForm):
    """ Workout Add form. """

    name = StringField(
        "Name",
        validators=[InputRequired(), Length(max=100)],
        render_kw={"class": "form-control bg-light bg-gradient mt-2", "placeholder": "workout name"}
    )

    description = TextAreaField("Description",
        validators=[InputRequired(), Length(max=500)],
        render_kw={"class": "form-control bg-light bg-gradient mt-2", "placeholder": "workout description"}
    )

   

class WorkoutEditFormStep2(FlaskForm):
    """ Step2 for """

    default_reps = IntegerField(
            "Reps:",
            validators=[InputRequired(), NumberRange(min=1, max=300)],
            render_kw={"class": "form-control mt-2", "placeholder": "number of reps"}
        )

class WorkoutExerciseEditForm(FlaskForm):
    """ Exercise Edit form. """
    
    name = StringField(
        "Name",
        validators=[InputRequired(), Length(max=30)],
        render_kw={"class": "form-control mt-2", "placeholder": "name"}
    )

    description = TextAreaField(
        "Description",
        validators=[InputRequired(), Length(max=600)],
        render_kw={"class": "form-control mt-2", "placeholder": " exercise description"}
    )

    default_reps = IntegerField(
        "Reps:",
        validators=[InputRequired(), NumberRange(min=1, max=300)],
        render_kw={"class": "form-control mt-2", "placeholder": "number of reps"}
    )

    image_url = StringField(
        '(Optional) Exercise Image URL',
        render_kw={"class": "form-control mt-2", "placeholder": "Exercise Image URL"}
    )

    category_id = SelectField('Category',
        render_kw={"class": "form-select mt-2", "placeholder": "category"}, 
        coerce=int)

    equipment_id = SelectField('Equipment',
        render_kw={"class": "form-select mt-2", "placeholder": "equipment"}, 
        coerce=int)
    
    muscle_id = SelectField('muscle',
        render_kw={"class": "form-select mt-2", "placeholder": "muscle"}, 
        coerce=int)
    

class AthleteWorkoutAssignForm(FlaskForm):
    """ Exercise Edit form. """

    athlete = SelectField('Athlete',
        render_kw={"class": "form-select mt-2", "placeholder": "athlete"}, 
        coerce=int)
    
    workout = SelectField('Workout',
        render_kw={"class": "form-select mt-2", "placeholder": "workout"}, 
        coerce=int)
