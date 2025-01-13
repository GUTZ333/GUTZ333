from flask import Flask, flash, render_template, redirect, url_for, request
from sql_api import SqlSERVER
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sign-up")
def signUp():
    return render_template("signUp.html")
@app.route("/sign-up/submit", methods=["POST"])
def submitSignUp():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    phone = request.form.get("phone")
    sql_instance = SqlSERVER()
    sql_instance.dataAccountAttributes(name=name, email=email, password=password, phone=phone)
    return sql_instance.SignUp(flash, redirect, url_for, render_template) 

@app.route("/sign-in")
def signIn():
    return render_template("signIn.html")
@app.route("/sign-in/submit", methods=["POST"])
def submitSignIn():
    email = request.form.get("email")
    password = request.form.get("password")
    sql_instance = SqlSERVER()
    sql_instance.dataAccountAttributes(email=email, password=password)
    return sql_instance.SignIn(flash, redirect, url_for, render_template)

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run()
    app.config["SESSION_TYPE"] = "filesystem"
