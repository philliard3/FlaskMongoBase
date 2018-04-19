from flask import Flask, render_template, request, session, json, redirect, url_for, Response
import pymongo
import bson
import datetime

# establish database
client = pymongo.MongoClient()

# database of user accounts
userdb = client.accounttesting.users

app = Flask(__name__)
app.secret_key = "change this string"


@app.route("/")
@app.route("/home")
@app.route("/index")
def homepage():
    return(render_template("homepage.html"))

@app.route("/register")
def register_page():
    return (render_template("register.html"))

@app.route("/login")
def login_page():
    return (render_template("login.html"))


if(__name__=="__main__"):
    app.run(debug=True)
    '''
    print(userdb.insert_one({"potato": 1}))
    print(userdb.find_one({"potato":1}))
    print(list(userdb.find()))
    userdb.remove()
    print(userdb.find_one({"potato":1}))
    '''
