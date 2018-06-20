from flask import Flask, render_template
import dj_database_url
from models import Stats

app = Flask(__name__)
session = Session()


@app.route('/')
def index():

    HS1="159 pts- Tanks"
    HS2= "200 pts - Brickbreaker"
    HS3="400 pts- Space Invaders"
    most_played= "Brickbreaker"
    featured="Space Invaders"
    render_template("index.html", mp=most_played, hs_1=HS1, hs_2=HS2, hs_3=HS3, feat=featured)
@app.route("/games")
def games():
	render_template("games.html")

@app.route("/games/<game>")
def game(game):
	return "Game to be"
	
	
@app.route("/stats/rating", methods=["GET"])
def stats_rating():
	games = session.query(Stats).all()
	
@app.route("/stats/most_played", methods=["GET"])
def stats_most_played():
	games = session.query(Stats).all()
	
@app.route("/stats/rating", methods=["POST"])
def update_stats_rating():
	if not request.json:
		abort(404)
	game_id = request.json["id"]
	games = session.query(Stats).filter(Stats.id == game_id).first()
	games.rated = games.rated + 1
	session.commit()
	
@app.route("/stats/most_played", methods=["POST"])
def update_stats_most_played():
	if not request.json:
		abort(404)
	game_id = request.json["id"]
	games = session.query(Stats).filter(Stats.id == game_id).first()
	games.played = games.played + 1
	session.commit()
	
if __name__ == '__main__':
    app.run()
