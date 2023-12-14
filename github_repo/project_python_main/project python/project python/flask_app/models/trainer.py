from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re


EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


class Trainer:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # ? ==== CREATE A Trainer ====
    @classmethod
    def create(cls, data):
        query = f"""
                INSERT INTO  trainers (first_name, last_name, email, password)
                VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
                """

        return connectToMySQL(DATABASE).query_db(query, data)

    # ? === GET trainers BY ID
    @classmethod
    def get_user_by_id(cls, data):
        query = f"""
                    SELECT * FROM trainers 
                    WHERE  id = %(id)s;
                    
                """
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False

        return cls(result[0])  # type: ignore

    # ? === READ ONE (GET BY EMAIL)
    @classmethod
    def get_by_email(cls, data):
        query = f"""
                    SELECT * FROM trainers 
                    WHERE  email = %(email)s;
                    
                """

        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False

        return cls(result[0])  # type: ignore

    #  trainers VALIDATE =========
    @staticmethod
    def validate(data):
        is_valid = True

        if len(data["first_name"]) < 3:
            is_valid = False
            flash("first_name Required !", "reg")
        if len(data["last_name"]) < 3:
            is_valid = False
            flash("last_name Required !", "reg")
        if len(data["email"]) < 3:
            flash("email Required !", "reg")
            is_valid = False
        elif not EMAIL_REGEX.match(data["email"]):
            flash("Invalid email address", "reg")
            is_valid = False
        else:
            # data_for_email = {"email": data["email"]}
            potential_user = Trainer.get_by_email(data)
            if potential_user:
                is_valid = False
                flash("email already taken, hopefully by you! ", "reg")
        if len(data["password"]) < 8:
            is_valid = False
            flash("password Required", "reg")
        elif not data["password"] == data["confirm_password"]:
            is_valid = False
            flash("passwords don't match!", "reg")
        return is_valid
