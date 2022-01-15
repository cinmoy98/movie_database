from flask import Flask, render_template, redirect, url_for, request,jsonify, json
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"]= "mongodb+srv://cinmoy98:ci406898-@movies.4hmlw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
app.config['SECRET_KEY'] = "Donotexpose"

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
		print(movie)
		doc = mongo.db.movies.insert_one(movie)
	return render_template('create.html')





if __name__ == '__main__':
	app.run(debug=True)