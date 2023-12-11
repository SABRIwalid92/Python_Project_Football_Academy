from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.offer import Offer
from flask_app.models.player import Player



@app.route('/players/<int:id>/add_stats')
def add_stats(id):
    redirect("/dashboard")



# @app.route('/offers/<int:id>')
# def one(id):
#     if 'player_id' in session:
#         offer = Offer.get_by_id({'id' : id})
#         player = Player.get_player_by_id({'id':session['player_id']})
#         return render_template('/view_offer.html', offer=offer,player=player)
#     return redirect('/')
