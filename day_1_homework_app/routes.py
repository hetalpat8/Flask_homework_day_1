# Import the app variable from the init 
from day_1_homework_app import app 

# Import specific packages from flask
from flask import render_template

# Default Home Route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/fav')
def favRoute():
    artists = ['B.B. King','Billie Ellish','Rihanna','The Weekend','Fleetwood Mac']
    return render_template('fav.html',list_artists = artists)


