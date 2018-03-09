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
    return("")




if(__name__=="__main__"):
    app.run(debug=True)
