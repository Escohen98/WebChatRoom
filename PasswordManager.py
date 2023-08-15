import bcrypt
from DatabaseHandler import Query as query

class PasswordManager():
        
    #Because I don't wanna Firebase
    def get_salt_password(username, password):
        salt = bcrypt.gensalt()
        hashed_salt = bcrypt.hashpw(salt, bcrypt.gensalt())  # Hashing the salt itself
        salted_password = password.encode('utf-8') + hashed_salt
        hashed_password = bcrypt.hashpw(salted_password, bcrypt.gensalt())
        return hashed_password, hashed_salt
        