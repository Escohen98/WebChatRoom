from flask import Flask, render_template, request, redirect, url_for, redirect, session
from PasswordManager import PasswordManager as pm
from DatabaseHandler import Query as query
from ChatHandler import ChatHandler as ch
import json

app = Flask(__name__)
    
user_name = None
channel = "general"

# Login page
@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    # Pulls account info from form
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Gets hashed password and salt
        hashed_password, hashed_salt = pm.get_salt_password(password)

        # Creates account. If it already exists, checks if correct password
        if query.create_account(hashed_password, hashed_salt, username) or hashed_password == query.get_hashed_password(username):
            global user_name
            user_name = username
            return redirect(url_for("chat"))
        
         # Checks for display name. 
         # Technically there is no way to differentiated between password invalid or existing username
        if query.display_name_exists(username):
            message="Username already exists or invalid password."
        
    return render_template('./login.html', message=message)

# Chat page
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    global user_name
    global channel
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
            query.insert_message(query.get_user_id(user_name), query.get_channel_id(channel), message)
        

    # Gets channels from database
    channel_html = ch.get_channel_html(query)
    
    # Theoretically should never hit unless I force it to
    if channel_html == False:
        return redirect(url_for("fourohfour"))
    message_html = ch.get_message_html(query, user_name, channel)
    return render_template('./chat.html', rooms=channel_html, msgs=message_html, room="demo1")

@app.route('/bad')
def bad():
    return render_template('./bad.html')

@app.route("/fourohfour")
def fourohfour(): 
    return render_template('404.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
