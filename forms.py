"""Forms for flask-feedback."""

from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional
from flask_wtf import FlaskForm


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
        render_kw={"placeholder": "username", "class": "form-control mt-2"}
    )
    last_name = StringField(
        "Last Name",
        validators=[InputRequired(), Length(max=30)],
        render_kw={"placeholder": "username", "class": "form-control mt-2"}
    )


# class FeedbackForm(FlaskForm):
#     """ Add feedback form. """

#     title = StringField(
#         "Title",
#         validators=[InputRequired(), Length(max=100)]
#     )
#     content = StringField(
#         "Content",
#         validators=[InputRequired()]
#     )


# class DeleteForm(FlaskForm):
#     """ Delete form - only use to create delete-POST method route """
