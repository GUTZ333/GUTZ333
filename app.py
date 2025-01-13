from flask import Flask, flash, render_template, redirect, url_for, request
from sql_api import SqlSERVER
site = Flask(__name__)
@site.route("/")
def home():
    return render_template("index.html")

@site.route("/sign-up")
def signUp():
    return render_template("signUp.html")
@site.route("/sign-up/submit", methods=["POST"])
def submitSignUp():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    phone = request.form.get("phone")
    sql_instance = SqlSERVER()
    sql_instance.dataAccountAttributes(name=name, email=email, password=password, phone=phone)
    return sql_instance.SignUp(flash, redirect, url_for, render_template) 

@site.route("/sign-in")
def signIn():
    return render_template("signIn.html")
@site.route("/sign-in/submit", methods=["POST"])
def submitSignIn():
    email = request.form.get("email")
    password = request.form.get("password")
    sql_instance = SqlSERVER()
    sql_instance.dataAccountAttributes(email=email, password=password)
    return sql_instance.SignIn(flash, redirect, url_for, render_template)

if __name__ == "__main__":
    site.secret_key = 'super secret key'
    site.run()
    site.config["SESSION_TYPE"] = "filesystem"