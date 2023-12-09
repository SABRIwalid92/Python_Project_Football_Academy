from flask_app import app
from flask import render_template, redirect, request, flash, session
# from flask_app.models.user_model import User
from flask_app.models.trainer_model import Trainer
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

# ========== LOGIN / REGISTER PAGE - VIEW ============


@app.route("/")
def index():
    
    return render_template("index.html",d_login="d-none",d_reg="")


# REGISTER - method - ACTION
@app.route("/trainers/register", methods=["POST"])
def trainer_register():
    # print(f"\n\n\n\n\n\n\n\n\n {request.form}")
    trainer_one= Trainer.validate(request.form)
    print(f"\n\n\n\n///////////////,{trainer_one}")
    if not trainer_one  :
    
        
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

    
    data = {**request.form, "password": pw_hashed}
    print(f"\n\n\n\n**********************")
    # save user in DB
    trainer_id = Trainer.create(data)
    print(f"\n\n\n\n===============")

    session["trainer_id"] = trainer_id
    return redirect("/dashboard")


# Login - method - ACTION
@app.route("/trainers/login", methods=["POST"])
def trainer_login():
    data = {"email": request.form["email"]}
    user_in_db = Trainer.get_by_email(data)
    # if email not found
    if not user_in_db:
        flash("invalid credentials", "log")
        return redirect("/")
    # now check the password
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("invalid credentials", "log")
        return redirect("/")

    # * if all is good
    print(f"===> id = {user_in_db.id}")
    session["user_id"] = user_in_db.id
    return redirect("/dashboard")
    
    
    
    
    
    
    # Display Route - Dashboard
@app.route("/dashboard")
def dash():
    # ! Route Guard
    if "trainer_id" not in session:
        return redirect("/")
    data = {"id": session["trainer_id"]}
    loggedin_user = Trainer.get_user_by_id(data)
    session["user_email"] = "a@a.com"
    # all_arbortrarys=Trainer.get_all_()
    return render_template("trainer.html", loggedin_user=loggedin_user)
    
    
    
@app.route("/login")
def login():
    
    return render_template("index.html",d_login= "",d_reg="d-none")