## Import App ##
from app import app
from flask import Flask, render_template, request, flash, redirect, session,  jsonify, g
from forms import LoginForm, RegisterForm

### REGISTER - LOGIN - LOGOUT ###
@app.route('/forms/register', methods=['GET', 'POST'])
def register_user():
    """ Register View and Handle Register """

    # if "username" in session:
    #     return redirect(f"/users/{session['username']}")

    # form = RegisterForm()

    # if form.validate_on_submit():
    #     username = form.username.data
    #     password = form.password.data
    #     first_name = form.first_name.data
    #     last_name = form.last_name.data
    #     email = form.email.data

    #     user = User.register(username, password, first_name, last_name, email)
    #     db.session.add(user)
    #     db.session.commit()
    #     session['username'] = user.username
    #     flash(f"Succesfully Registered: {first_name} {last_name}")
    #     return redirect(f"/users/{user.username}")

    # else:
        # return render_template('/forms/register_user_form.html', form=form)
    return render_template('/forms/register_user_form.html')

@app.route('/users/signup', methods=["GET", "POST"])
def signup():
    """Handle user signup.

    Create new user and add to DB. Redirect to home page.

    If form not valid, present form.

    If the there already is a user with that username: flash message
    and re-present form.
    """

    form = RegisterForm()

    # if form.validate_on_submit():
    #     try:
    #         user = User.signup(
    #             username=form.username.data,
    #             password=form.password.data,
    #             email=form.email.data,
    #             image_url=form.image_url.data or User.image_url.default.arg,
    #             header_image_url=form.header_image_url.data or User.header_image_url.default.arg,
    #             bio=form.bio.data or User.bio.default.arg,
    #             location=form.location.data or User.location.default.arg,
    #         )
    #         db.session.commit()

    #     except IntegrityError:
    #         flash("Username already taken", 'danger')
    #         return render_template('users/signup.html', form=form)

    #     do_login(user)

    #     return redirect("/")

    # else:
    #     return render_template('users/signup.html', form=form)
    return render_template('/users/register_user_form.html', form=form)


@app.route("/users/login", methods=['GET', 'POST'])
def login_user():
    """ Login View and Handle Login """
    # if "username" in session:
    #     return redirect(f"/users/{session['username']}")

    form = LoginForm()
   

    # if form.validate_on_submit():
    #     username = form.username.data
    #     password = form.password.data

    #     user = User.authenticate(username, password)
    #     if user:
    #         session['username'] = user.username
    #         return redirect(f"/users/{user.username}")
    #     else:
    #         form.username.errors = ["Invalid username/password."]
    #         return render_template("forms/login_user_form.html", form=form)

    return render_template("/users/login_user_form.html", form=form, form1=form1)