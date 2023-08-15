# Originally meant to be used for Firebase, but Firebase was getting on my nerves,
# so I'm switching to SQLite because I know how to use it.
# This means I'm also hashing the passwords myself on the back-end which is what is going on here. 

import bcrypt
from DatabaseHandler import Query as query

class PasswordManager():
        
    # Because I don't wanna Firebase
    # Hashes the given password and returns the hashed_password and hashed_salt
    def get_salt_password(password):
        salt = bcrypt.gensalt()
        hashed_salt = bcrypt.hashpw(salt, bcrypt.gensalt())  # Hashing the salt itself
        salted_password = password.encode('utf-8') + hashed_salt
        hashed_password = bcrypt.hashpw(salted_password, bcrypt.gensalt())
        return hashed_password, hashed_salt
        