from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models.user import User
from datetime import date





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
        # self.poster = user.User.get_by_id({"id": self.user_id})




    @classmethod
    def add_stats(cls,data):
        query = f"""
                UPDATE players SET age=%(age)s, weight=%(weight)s, height=%(height)s, foot=%(foot)s, position=%(position)s
                WHERE players.id = %(id)s;
                """

        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_all_players(cls):
        query = "SELECT *FROM players;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_players = []
        for row in results:
            all_players.append(cls(row))
        return all_players


    @classmethod
    def get_player_by_id(cls, data):
        query = """
        SELECT * FROM players 
        WHERE id = %(id)s;"""
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])
    
    @staticmethod
    def calculate_age(birthdate):
        today = date.today()
        return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))