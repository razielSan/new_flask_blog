import os
import shutil

from flask import Blueprint, render_template, flash, redirect, url_for

from blog.user.forms import RegistrationForm, LoginForm
from blog.models import User
from blog import bcrypt, db


users = Blueprint("users", __name__)


@users.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    print(form.username.data, form.email.data)
    print(form.validate_on_submit(), 1)
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        print(user, 1111)
        db.session.add(user)
        db.session.commit()


        full_path = os.path.join(os.getcwd(), "static", "profile_pics", user.username)

        if not os.path.exists(full_path):
            os.mkdir(full_path)


        shutil.copy(f"{os.getcwd()}/static/profile_pics/default.jpg", full_path)
        flash("Ваш аккаунт был созданн вы можете войти на блог", "success")
        return redirect(url_for("users.login"))

    return render_template("register.html", form=form, title="Регистрация", legend="Регистрация")
        

@users.route('/login', methods=['GET', 'POST'])
def login():
    return 'hello'