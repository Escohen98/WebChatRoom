import bcrypt, firebase_admin
import firebase_admin
from firebase_admin import credentials, auth, exceptions

class PasswordManager():

    def __init__(self):
        cred = credentials.Certificate("mstu5013-final-project-8a1a3-firebase-adminsdk-pf5co-29ebbcfa8e.json")
        firebase_admin.initialize_app(cred)

    #Logs the user in
    #If the user exists, checks if password is correct, otherwise creates a new account
    #Password is required.
    def login_handler(self, email, password):
        #Makes sure email and password are populated
        if email.strip() == "" or password.strip() == "":
            return "Please enter and email and password"
        elif len(password.strip()) < 6:
            return "Your password must be at least 6 characters."
        user_exists = self.check_user_exists(email, password)
        if user_exists == True: #Playing it safe b/c not binary
            return user_exists
        elif user_exists == 'NOT_FOUND': #e.code
            try:
                user = auth.create_user(
                    email=email.strip(),
                    password=password.strip()
                )
                return True
            except exceptions.FirebaseError as e:
                error_message = e.detail
                print(error_message)
                return "Error creating user"
        return "Something went wrong." #Interested to see how this could get hit
    
    def check_user_exists(self,email, password):
        try:
            #Checks if user exists
            existing_user = auth.get_user_by_email(email)
            if auth.verify_password(existing_user.uid, password):
                return True
            else: #Incorrect Password
                return "Incorrect password"
        except exceptions.FirebaseError as e:  #User does not exist, create a new one 
            print(e.code)
            return e.code