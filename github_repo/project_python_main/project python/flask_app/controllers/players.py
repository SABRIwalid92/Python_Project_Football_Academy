from flask_app import app
from datetime import datetime
from flask import render_template, redirect, request, flash, session
from flask_app.models.offer import Offer
from flask_app.models.player import Player
from flask_app.models.user import User

@app.route("/create_player")
def stats():
    player = Player.get_player_by_id({"id":1})
    arr =player.test_skills_insert()
    return render_template("create_player.html" ,arr = arr, show = [0,"block","none","none"])

@app.route("/create_player2")
def stats2():
    player = Player.get_player_by_id({"id":1})
    arr = player.test_skills_insert()
    return render_template("create_player.html" ,arr = arr, show = [0,"none","block","none"])

@app.route("/create_player3")
def stats3():
    player = Player.get_player_by_id({"id":1})
    arr =player.test_skills_insert()
    return render_template("create_player.html" , arr = arr, show = [0,"none","none","block"])

@app.route('/players/4/add_stats', methods=['POST'])
def add_stats():
    date =  datetime.strptime((request.form)["birthdate"],"%Y-%m-%d").date()
    data = {**request.form, "age": Player.calculate_age(date), "id": 1}
    Player.add_stats(data)

    return redirect("/create_player2")

@app.route("/test")
def render():
    return render_template("test.html")


# @app.route('/offers/<int:id>')
# def one(id):
#     if 'player_id' in session:
#         offer = Offer.get_by_id({'id' : id})
#         player = Player.get_player_by_id({'id':session['player_id']})
#         return render_template('/view_offer.html', offer=offer,player=player)
#     return redirect('/')
