import bcrypt, firebase_admin
import firebase_admin
from firebase_admin import credentials, auth
from flask import request

class PasswordManager():

    def __init__():
        cred = credentials.Certificate("mstu5013-final-project-8a1a3-firebase-adminsdk-pf5co-29ebbcfa8e.json")
        firebase_admin.initialize_app(cred)

    #Taken from ChatGPT
    @staticmethod
    def authenticate_user(route_function):
        def wrapper(*args, **kwargs):
            id_token = request.cookies.get('idToken')  # Get the ID token from the user's cookies
            try:
                decoded_token = auth.verify_id_token(id_token)
                uid = decoded_token['uid']
                # You can now use 'uid' to identify the user and perform actions accordingly
                return route_function(*args, **kwargs)
            except:
                # Handle authentication errors
                return "Authentication required", 401
        return wrapper

        # Hashes the data during registration
    def text_encrypt(self, data):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(data.encode('utf-8'), salt)
        return hashed

    #Taken from https://www.geeksforgeeks.org/how-to-hash-passwords-in-python/
    # Hashes the data during registration
    def data_encrypt(self, data):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(data.encode('utf-8'), salt)
        return hashed

    # Simulates user registration
    def register_user(self, username, password):
        hashed_password = self.text_encrypt(password)
        # Store hashed_password and other user information in the database

    # Simulates user login
    def login_user(self, username, password):
        # Retrieve hashed_password from the database for the given username
        # For demonstration purposes, let's assume hashed_password is retrieved from the database
        hashed_password_from_db = b'$2b$12$Gazf71sqg01k58rBxW07iOoZJeCmhr4y2XOYIYRFrjzUcWUMRTUli'

        # Compare provided plain-text password with the stored hashed password
        provided_password = password.encode('utf-8')
        if bcrypt.checkpw(provided_password, hashed_password_from_db):
            print("Login successful")
        else:
            print("Login failed")
