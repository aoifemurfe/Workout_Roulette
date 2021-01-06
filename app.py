import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env
from datetime import datetime


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/go_home")
def go_home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("create_workout", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "view_workouts", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/view_workouts/<username>", methods=["GET", "POST"])
def view_workouts(username):
    # get the username in session
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    workouts = mongo.db.workouts.find()
    if session["user"]:
        return render_template("view_workouts.html", 
        username=username, workouts=workouts)
    return redirect(url_for("login"))


@app.route("/search/<username>", methods=["GET", "POST"])
def search(username):
    # get the username in session
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    query = request.form.get("search")
    workouts = list(mongo.db.workouts.find({"$text": {"$search": query}}))
    return render_template("view_workouts.html", workouts=workouts, username=username)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get the username in session
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    workouts = mongo.db.workouts.find()
    total = mongo.db.workouts.aggregate([
                    {"$match": {"status": "on"}},
                    {"$group": {"_id": "$user" , "minutes": {"$sum": "$timing"}}}
                   ])
    burpees = mongo.db.workouts.aggregate([
                    {"$match": {"status": "on","$text": {"$search": "Burpees"}}},
                    {"$group": {"_id": "$user" , "count": { "$sum": "$count" }}}
                   ])
    push_ups = mongo.db.workouts.aggregate([
                    {"$match": {"status": "on","$text": {"$search": "Push Ups"}}},
                    {"$group": {"_id": "$user" , "count": { "$sum": "$count" }}}
                   ])
    air_squats = mongo.db.workouts.aggregate([
                    {"$match": {"status": "on","$text": {"$search": "Air Squats"}}},
                    {"$group": {"_id": "$user" , "count": { "$sum": "$count" }}}
                   ])
    lunges = mongo.db.workouts.aggregate([
                    {"$match": {"status": "on","$text": {"$search": "Lunges"}}},
                    {"$group": {"_id": "$user" , "count": { "$sum": "$count" }}}
                   ])
    shuttle_runs = mongo.db.workouts.aggregate([
                    {"$match": {"status": "on","$text": {"$search": "Shuttle Runs"}}},
                    {"$group": {"_id": "$user" , "count": { "$sum": "$count" }}}
                   ])  
    jumping_jacks = mongo.db.workouts.aggregate([
                    {"$match": {"status": "on","$text": {"$search": "Jumping Jacks"}}},
                    {"$group": {"_id": "$user" , "count": { "$sum": "$count" }}}
                   ])    
    plank = mongo.db.workouts.aggregate([
                    {"$match": {"status": "on","$text": {"$search": "Plank"}}},
                    {"$group": {"_id": "$user" , "count": { "$sum": "$count" }}}
                   ])       
    sit_ups = mongo.db.workouts.aggregate([
                    {"$match": {"status": "on","$text": {"$search": "Plank"}}},
                    {"$group": {"_id": "$user" , "count": { "$sum": "$count" }}}
                   ])  
    tricep_dips = mongo.db.workouts.aggregate([
                    {"$match": {"status": "on","$text": {"$search": "Tricep Dips"}}},
                    {"$group": {"_id": "$user" , "count": { "$sum": "$count" }}}
                   ])       
    mountain_climbers = mongo.db.workouts.aggregate([
                    {"$match": {"status": "on","$text": {"$search": "Mountain Climbers"}}},
                    {"$group": {"_id": "$user" , "count": { "$sum": "$count" }}}
                   ])      
    bear_crawl = mongo.db.workouts.aggregate([
                    {"$match": {"status": "on","$text": {"$search": "Bear Crawl"}}},
                    {"$group": {"_id": "$user" , "count": { "$sum": "$count" }}}
                   ]) 
    glute_bridges = mongo.db.workouts.aggregate([
                    {"$match": {"status": "on","$text": {"$search": "Glute Bridges"}}},
                    {"$group": {"_id": "$user" , "count": { "$sum": "$count" }}}
                   ]) 

    return render_template("profile.html", 
        username=username, workouts=workouts, total=total, burpees=burpees,push_ups=push_ups,air_squats=air_squats, lunges=lunges, shuttle_runs=shuttle_runs, jumping_jacks=jumping_jacks, plank=plank, sit_ups=sit_ups, tricep_dips=tricep_dips, mountain_climbers=mountain_climbers, bear_crawl=bear_crawl, glute_bridges=glute_bridges)


@app.route("/logout")
def logout():
    # remove user cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/create_workout", methods=["GET", "POST"])
def create_workout():
    if request.method == "POST":
        status = "on" if request.form.get("status") else "off"
        if request.form.get("interval") == "Medium - 45secs on, 15secs off": 
            timing = 45 
        elif request.form.get("interval") == "Hard - 60secs on, 0 secs off":
            timing = 60
        else:
            timing = 30
        logworkout = {
            "user": session["user"],
            "date": request.form.get("date"),
            "exercise_1": request.form.get("exercise_1"),
            "exercise_2": request.form.get("exercise_2"),
            "exercise_3": request.form.get("exercise_3"),
            "exercise_4": request.form.get("exercise_4"),
            "exercise_5": request.form.get("exercise_5"),
            "interval": request.form.get("interval"),
            "comment": request.form.get("comment"),
            "status": status,
            "timing": timing,
            "count": 1
        }
        mongo.db.workouts.insert_one(logworkout)
        flash("Workout Added Successfully")
        return redirect(url_for('view_workouts', username=session['user']))
    return render_template("create_workout.html")


@app.route("/edit_workout/<workouts_id>",methods=["GET", "POST"])
def edit_workout(workouts_id):
    if request.method == "POST":
        status = "on" if request.form.get("status") else "off"
        if request.form.get("interval") == "Medium - 45secs on, 15secs off": 
            timing = 45 
        elif request.form.get("interval") == "Hard - 60secs on, 0 secs off":
            timing = 60
        else:
            timing = 30
        updateworkout = {
            "user": session["user"],
            "date": request.form.get("date"),
            "exercise_1": request.form.get("exercise_1"),
            "exercise_2": request.form.get("exercise_2"),
            "exercise_3": request.form.get("exercise_3"),
            "exercise_4": request.form.get("exercise_4"),
            "exercise_5": request.form.get("exercise_5"),
            "interval": request.form.get("interval"),
            "comment": request.form.get("comment"),
            "status": status,
            "timing": timing,
            "count": 1
            
        }
        mongo.db.workouts.update({"_id": ObjectId(workouts_id)}, updateworkout)
        flash("Workout Updated Successfully")
        return redirect(url_for('view_workouts', username=session['user']))
    workouts = mongo.db.workouts.find_one({"_id": ObjectId(workouts_id)})
    return render_template("edit_workout.html", workouts=workouts)



# delete a workout on view workouts page
@app.route("/delete_workout/<workouts_id>")
def delete_workout(workouts_id):
    mongo.db.workouts.remove({"_id": ObjectId(workouts_id)})
    flash("Workout Removed Successfully")
    return redirect(url_for('view_workouts', username=session['user']))


# delete profile on profile page
@app.route("/delete_profile")
def delete_profile():
    mongo.db.workouts.remove({"user": session['user']})
    mongo.db.users.remove({"username": session['user']})
    session.pop("user")
    flash("Your Profile has been deleted")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)