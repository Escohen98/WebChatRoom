from flask import Flask, render_template, request, redirect, url_for, redirect, session
from PasswordManager import PasswordManager as pm
from DatabaseHandler import Query as query
from ChatHandler import ChatHandler as ch
import json

app = Flask(__name__)

try:
    # Load the secret key from config.json
    with open("config.json", "r") as file:
        config = json.load(file)
        app.secret_key = config.get("session_key", "default_fallback_key")  # fallback key if not found in config

except Exception as e:
    print("Failed to get session key")
    print("Idk, I guess I should shut down the program?")
    import sys
    sys.exit()   

    # Login page
@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    # Pulls account info from form
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()
        
        # Everything happening below is so ridiculously redundant and unnecessary
        # Pretty much using a copout because this is becoming a lot...

        # Gets hashed password and salt for a new user
        hashed_password, salt = pm.get_salt_password(password)

        # boolean -> Account exists or not
        new_user = query.create_account(hashed_password, salt, username)

        if not new_user:
            # Getting the salt and hashed_password stored in the database for the given user.
            db_hashed_password, db_salt = query.get_hashed_password(username)

            # The entered password with the salt associated with the user who is logging in
            existing_hashed_password = pm.get_salt_password(password, db_salt)[0]

        # Creates account. If it already exists, checks if correct password
        if new_user or db_hashed_password == existing_hashed_password:
            session['user_name'] = username.strip()
            return redirect(url_for("chat"))
        
         # Checks for display name. 
         # Technically there is no way to differentiated between password invalid or existing username
        if query.display_name_exists(username):
            message="Username already exists or invalid password."
        
    return render_template('./login.html', message=message)

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    user_name = session.get('user_name', None)
    channel = session.get('channel', 'general')  # Defaulting to 'general'
    
    # No bypass hackers. Boo.
    if user_name == None:
        return redirect(url_for("bad"))
    
    if request.method == 'POST':
        button_value = request.form.get('submit-button')
        
        if button_value == 'submit-channel':
            channel_name = request.form.get('channel-name')
            query.create_channel(channel_name)
        
        elif button_value == 'send-message':
            message = request.form.get('chat-message')
            query.insert_message(query.get_channel_id(channel), query.get_user_id(user_name), message)
        
        elif button_value == 'change-channel':
            channel_name = request.form.get(f"unique-id-{channel}")
            session['channel'] = channel_name

        # Redirect to chat after processing the POST request
        return redirect(url_for('chat'))

    # This part executes for GET requests. Fetch the latest state from the database and render it.
    channel_html = ch.get_channel_html(query, channel)
    if channel_html == False:
        return redirect(url_for("fourohfour"))
    message_html = ch.get_message_html(query, user_name, channel)
    return render_template('./chat.html', rooms=channel_html, msgs=message_html, room=channel, username=user_name)

@app.route('/bad')
def bad():
    return render_template('./bad.html')

@app.route("/fourohfour")
def fourohfour(): 
    return render_template('404.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
