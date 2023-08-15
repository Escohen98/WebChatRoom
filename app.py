from flask import Flask, render_template, request, redirect, url_for, redirect, session
from PasswordManager import PasswordManager as pm
from DatabaseHandler import Query as query
from ChatHandler import ChatHandler as ch

app = Flask(__name__)

user_name = None
channel = "general"

#Login page
@app.route('/', methods=['GET', 'POST'])
def login():

    #Pulls account info from form
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        username = request.form.get('username')

        #Checks for display name
        if query.display_name_exists(username):
            return render_template('./login.html', message="Username already exists.")

        #Gets hashed password and salt
        hashed_password, hashed_salt = pm.get_salt_password(username, password)

        #Creates account. If it already exists, checks if correct password
        if query.create_account(email, hashed_password, hashed_salt, username) or hashed_password == query.get_hashed_password(email):
            session['user_name'] = username
            return redirect(url_for("chat"))
    return render_template('./login.html', message="Invalid password.")

#Chat page
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    #No bypass hackers. Boo.
    if user_name == None:
        return redirect(url_for("bad"))
    #Demo purposes only.
    channel_html = ch.get_channel_html(query)
    
    #Theoretically should never hit 
    if channel_html == False:
        return redirect(url_for("fourohfour"))
    messages = query.fetch_messages()
    messages = [
        "<div id='chat-bubble' class='user'>\
            <h2>You</h2>\
            <p class='msg-box'>Hi</p>\
        </div>", 
        "<div id='chat-bubble' class='other'>\
            <h2>Bot</h2>\
            <p class='msg-box'>Hello</p>\
        </div>"
    ]
    return render_template('./chat.html', rooms=channels, msgs=messages, room="demo1")

@app.route('/bad')
def bad():
    return render_template('./bad.html')

@app.route("/fourohfour")
def fourohfour(): 
    return render_template('404.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
