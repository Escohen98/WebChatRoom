import bcrypt, firebase_admin
import firebase_admin, json
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
            #Create new user
            #Display name is first part of email
            try:
                user = auth.create_user(
                    email=email.strip(),
                    password=password.strip(),
                    display_name=email.strip().split("@")[0]
                )

                user_json = json.dumps({email.strip(): {"password": password.strip(), "display_name": email.strip().split("@")[0]}})
                with open('accounts.json')

                return True
            except exceptions.FirebaseError as e:
                error_message = e.detail
                print(error_message)
                return "Error creating user"
        return "Something went wrong." #Interested to see how this could get hit
    
    def check_user_exists(self,email, password):
        try:
            #Checks if user exists
            existing_user = auth.get_user_by_email(email) #Does firebase not require password verification?
            if self.verify_user_password(existing_user.uid, password):
                return True
            else: #Incorrect Password
                return "Incorrect password"
        except exceptions.FirebaseError as e:  #User does not exist, create a new one 
            print(e.code)
            return e.code
        
    #Apparently can be used to verify the password is correct
    #Does this by attempting to login
    #If it works, return user if not, return false
    def signed_in(self, user, email, password):
        try:
            # Sign in with email and password to verify
            #user = auth.sign_in_with_email_and_password(uid, password)
            # If successful, Firebase will return user data
            # credential = auth.email_auth_provider.credential(
            #     email,
            #     password
            # )
            # #Tries to authenticate user
            # user.reauthenticate_with_credential(credential)
            return True
        except exceptions.FirebaseError as e:
            print("crap")
            return False
        
    def verify_user_password(self, uid, password):
        try:
            # Sign in with email and password to verify
            user = auth.sign_in_with_email_and_password(uid, password)
            # If successful, Firebase will return user data
            return True
        except exceptions.FirebaseError as e:
            return False
        
    #Because I don't wanna Firebase
    def register_user(username, password):
        salt = bcrypt.gensalt()
        hashed_salt = bcrypt.hashpw(salt, bcrypt.gensalt())  # Hashing the salt itself
        salted_password = password.encode('utf-8') + hashed_salt
        hashed_password = bcrypt.hashpw(salted_password, bcrypt.gensalt())
        # Store hashed_password and hashed_salt along with other user information