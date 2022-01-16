from flask import Flask, render_template, redirect, url_for, request ,jsonify, json
from flask_pymongo import PyMongo
from bson.json_util import dumps, loads

app = Flask(__name__)

app.config["MONGO_URI"]= "mongodb+srv://cinmoy98:ci406898-@movies.4hmlw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
app.config['SECRET_KEY'] = "Donotexpose"
auth_code = "4092"

mongo  = PyMongo(app)

@app.route('/home', methods=['GET','POST'])
def home():
	if request.method == "POST":
		data = request.form
		movie = {
		'mname':data['mname'],
		'rdate':data['rdate'],
		'wlink':data['wlink'],
		'imdblink':data['imdblink'],
		'genre':data['genre'],
		'country':data['country'],
		'watched':data['watched'],
		'moviesorseries':data['moviesorseries'],
		'review':data['review'],
		'rating':data['rating'],
		'wdate':data['wdate']
		}
		if data['auth_code'] == auth_code:
			doc = mongo.db.movies.insert_one(movie)
			return redirect(url_for('dashboard'))
	return render_template('create.html')

@app.route('/', methods=['GET','POST'])
def dashboard():
	movies = mongo.db.movies.find()
	return render_template('movies.html', movies=movies)



if __name__ == '__main__':
	app.run(debug=True)