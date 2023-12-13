from lib2to3.pytree import _Results
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
from flask_app.models.user import User


EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


class Scout:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.type = data["type"]

    # ? ==== CREATE A scout ====
    @classmethod
    def create(cls, data):
        data = {**data, "type" : "scouts"}
        return   User.create(data)

    # ? === GET scouts BY ID
    @classmethod
    def get_user_by_id(cls, data):
        data ={**data, "type" : "scouts"}
        
        return User.get_user_by_id(data)

    # ? === READ ONE (GET BY EMAIL)
    @classmethod
    def get_by_email(cls, data):
        data = {**data, "type" : "scouts"}
        
        return  User.get_by_email(data)
#  scouts VALIDATE =========
    @staticmethod
    def validate(data):
        is_valid = True

        if len(data["first_name"]) < 1:
            is_valid = False
            flash("first_name Required !", "reg")
        if len(data["last_name"]) < 1:
            is_valid = False
            flash("last_name Required !", "reg")
        if len(data["email"]) < 1:
            flash("email Required !", "reg")
            is_valid = False
        elif not EMAIL_REGEX.match(data["email"]):
            flash("Invalid email address", "reg")
            is_valid = False
        else:
            # data_for_email = {"email": data["email"]}
            potential_user = Scout.get_by_email(data)
            if potential_user:
                is_valid = False
                flash("email already taken, hopefully by you! ", "reg")
        if len(data["password"]) < 1:
            is_valid = False
            flash("password Required", "reg")
        elif not data["password"] == data["confirm_password"]:
            is_valid = False
            flash("passwords don't match!", "reg")
        return is_valid
