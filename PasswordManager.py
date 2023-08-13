import bcrypt

class PasswordManager():

    #Taken from https://www.geeksforgeeks.org/how-to-hash-passwords-in-python/
    #Hashes the data

    # Hashes the data during registration
    def data_encrypt(data):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(data.encode('utf-8'), salt)
        return hashed

    # Simulates user registration
    def register_user(username, password):
        hashed_password = text_encrypt(password)
        # Store hashed_password and other user information in the database

    # Simulates user login
    def login_user(username, password):
        # Retrieve hashed_password from the database for the given username
        # For demonstration purposes, let's assume hashed_password is retrieved from the database
        hashed_password_from_db = b'$2b$12$Gazf71sqg01k58rBxW07iOoZJeCmhr4y2XOYIYRFrjzUcWUMRTUli'

        # Compare provided plain-text password with the stored hashed password
        provided_password = password.encode('utf-8')
        if bcrypt.checkpw(provided_password, hashed_password_from_db):
            print("Login successful")
        else:
            print("Login failed")

# Simulating registration and login
register_user("user123", "secretpassword")
login_user("user123", "secretpassword")
