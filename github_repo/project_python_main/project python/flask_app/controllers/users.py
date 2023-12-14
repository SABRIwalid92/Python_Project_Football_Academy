from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.player import Player
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

# ========== LOGIN / REGISTER PAGE - VIEW ============


@app.route("/")
def home():
    
    return render_template("home.html")


@app.route("/index")
def index():
    
    return render_template("index.html",d_login="d-none",d_reg="")



# REGISTER - method - ACTION
@app.route("/users/register", methods=["POST"])
def user_register():
    user_one= User.validate(request.form)
    if not user_one  :

        return redirect("/")
    # 1 . hash the password
    pw_hashed = bcrypt.generate_password_hash(request.form["password"])
    # 2 . get the data dict ready with the new hashe pw to create a User
    # data = {
    #     "first_name": request.form["first_name"],
    #     "last_name": request.form["last_name"],
    #     "email": request.form["email"],
    #     "confirm": request.form["confirm_password"],
    #     "password": pw_hashed,
    # }

    
    data = {**request.form,"password": pw_hashed}
    # save user in DB
    user_id = User.create(data)    


    session["user_id"] = user_id
    session["type"] = data["type"]
    return redirect(f"/{session["type"]}/{session["user_id"]}/dashboard")


# Login - method - ACTION
@app.route("/users/login", methods=["POST"])
def user_login():
    # data = {"type": request.form["type"], "email": request.form["email"]}
    user_in_db = User.get_by_email({"email" : request.form["email"]})
    # if email not found
    if not user_in_db:
        flash("invalid credentials", "log")
        return redirect("/login")
    # now check the password
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("invalid credentials", "log")
        return redirect("/login")

    # * if all is good
    print(f"===> id = {user_in_db.id}")
    session["user_id"] = user_in_db.id
    session["type"] = user_in_db.type
    return redirect(f"/{session["type"]}/{session["user_id"]}/dashboard")
    
    
    
    
    
    
    # Display Route - Dashboard
@app.route(f"/<string:type>/<int:id>/dashboard")
def dash(type,id):
    # ! Route Guard
    if "user_id" not in session:
        return redirect("/")
    data = {"id": session["user_id"]}
    loggedin_user = User.get_user_by_id(data)
    
    loggedin_user = Player.create(loggedin_user)
    print(f"\n\n\n\n\n\n\n\n\n\n\n\nlogeedin{loggedin_user}")    

    # loggedin_user = Player.get_player_by_id({"id" : loggedin_user})

    # if loggedin_user.type == "players":
    if loggedin_user.page == 2:
        return redirect("/create_player2")
    elif loggedin_user.page == 3:
        return redirect("/create_player3")
    elif loggedin_user.page == 4:
        render_template("players_dashboard.html", loggedin_user=loggedin_user)
    else :
        return redirect("/create_player")
    return render_template(f"{loggedin_user.type}_dashboard.html", loggedin_user=loggedin_user)
    
    
    
@app.route("/login")
def login():
    
    return render_template("index.html",d_login= "",d_reg="d-none")

# ! ------- LOGOUT -------- action
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

