from flask_app import app
from flask import request, render_template, session, redirect
from flask_app.models.offer import Offer
from flask_app.models.trainer import Trainer
from flask_app.models.scout import Scout
from flask_app.models.player import Player


@app.route("/offers_trainers")
def offers_trainers():
    if "user_id" not in session:
        return redirect("/index")
    loggedin_user = Trainer.get_user_by_id({"id": session["user_id"]})
    return render_template(
        "go_to_offers_trainer.html",
        offers=Offer.get_all(),
        get_trainer=Trainer.get_user_by_id,
        loggedin_user=loggedin_user,
    )


@app.route("/offers_players")
def offers_players():
    if "user_id" not in session:
        return redirect("/index")
    loggedin_user = Player.get_user_by_id({"id": session["user_id"]})
    return render_template(
        "go_to_offers_player.html",
        offers=Offer.get_all(),
        get_trainer=Trainer.get_user_by_id,
        loggedin_user=loggedin_user,
    )


@app.route("/offers_scouts")
def offers_scouts():
    if "user_id" not in session:
        return redirect("/index")
    loggedin_user = Scout.get_user_by_id({"id": session["user_id"]})
    return render_template(
        "go_to_offers_scout.html",
        offers=Offer.get_all(),
        get_trainer=Trainer.get_user_by_id,
        loggedin_user=loggedin_user,
    )


@app.route("/offers/new")
def new():
    if "user_id" in session:
        return render_template("new.html")
    return redirect("/")


@app.route("/offers/create", methods=["POST"])
def create():
    # if not Offer.validation(request.form):
    #     return redirect('/offers/new')

    data = {**request.form, "trainer_id": int(session["user_id"])}
    db_return = Offer.create(data)
    return redirect("/trainers/dashboard")


# @app.route("/offers/<int:id>")
# def one(id):
#     if "trainer_id" in session:
#         offer = Offer.get_by_id({"id": id})
#         # trainer = Trainer.get_by_id({'id':session['trainer_id']})
#         return render_template("view.html", offer=offer)
#     return redirect("/")


@app.route("/offers/edit/<int:id>")
def edit(id):
    session["offer_id"] = id
    offer = Offer.get_by_id({"id": id})
    return render_template("edit.html", offer=offer)


@app.route("/offers/update", methods=["post"])
def update():
    # if not Offer.validation(request.form):
    #     return redirect(f'/offers/edit/{ session["offer_id"]}')
    data = {**request.form, "id": session["offer_id"]}
    Offer.edit(data)
    return redirect("/trainers/dashboard")


@app.route("/offers/delete/<int:id>")
def delete(id):
    if "user_id" in session:
        Offer.delete({"id": id})
        return redirect("/trainers/dashboard")
    return redirect("/index")
