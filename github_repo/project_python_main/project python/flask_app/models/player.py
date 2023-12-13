from random import randint
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models.user import User
from datetime import date
from random import randint





class Player(User):
    def __init__(self, data):
        super().__init__(data)
        self.age = data['age']
        self.weight = data['weight']
        self.height = data['height']
        self.position = data['position']
        self.foot = data['foot']
        self.stamina = data['stamina']
        self.kicking = data['kicking']
        self.speed = data['speed']
        self.physique = data['physique']
        self.technique = data['technique']
        self.reflex = data['reflex']
        self.energy = data['energy']
        self.injury = data['injury']
        self.trainer_id = data['trainer_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.page = 0
        # self.poster = user.User.get_by_id({"id": self.user_id})


    @classmethod
    def create(cls, data):
        data = {**data, "type" : "players"}
        return   User.create(data)
    
    @classmethod
    def get_player_by_id(cls, data):
        data ={**data, "type" : "players"}
        
        return User.get_user_by_id(data)
    
    @classmethod
    def get_by_email(cls, data):
        data = {**data, "type" : "players"}
        
        return  User.get_by_email(data)
    
    @classmethod
    def add_stats(cls,data):
        query = f"""
                UPDATE players SET age=%(age)s, weight=%(weight)s, height=%(height)s, foot=%(foot)s, position=%(position)s
                WHERE players.id = %(id)s;
                """

        return connectToMySQL(DATABASE).query_db(query, data)
    
    def test_skills_insert(self):
        arr = Player.skills_calc(self.position)
        query = f"""
                UPDATE players SET stamina={arr[0]}, kicking={arr[1]}, speed={arr[2]}, physique={arr[3]}, technique={arr[4]}, reflex={arr[5]}
                WHERE players.id ={self.id};
                """

        connectToMySQL(DATABASE).query_db(query)
        return arr
    
    @classmethod
    def get_all_players(cls):
        query = "SELECT *FROM players;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_players = []
        for row in results:
            all_players.append(cls(row))
        return all_players


    
    @staticmethod
    def calculate_age(birthdate):
        today = date.today()
        return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    

    @staticmethod
    def skills_calc(position):
        if position == "Forward":
            arr=[randint(40,60), randint(70,90),randint(70,90), randint(50,70), randint(70,90), randint(10,30)]
        elif position == "Center":
            arr=[randint(70,90), randint(60,80),randint(50,70), randint(60,80), randint(60,80), randint(10,30)]
        elif position == "Defense":
            arr=[randint(70,90), randint(50,70), randint(40,60),randint(60,80), randint(40,60), randint(10,30)]
        elif position == "Goalkeeper":
            arr=[randint(40,60), randint(50,70),randint(30,50), randint(50,70), randint(30,50), randint(70,90)]
        else:
            arr = [0,0,0,0,0,0]
        
        return arr