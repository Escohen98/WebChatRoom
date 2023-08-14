from flask import Flask, render_template, request, redirect, url_for, redirect, send_from_directory
from PasswordManager import PasswordManager

import json, bcrypt

app = Flask(__name__)
user = None
pm = PasswordManager()

#Login page
@app.route('/', methods=['GET', 'POST'])
def login():
    response=""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        response = pm.login_handler(email, password)   
        if response == True:
            user_email = email
            user_pass = password
            return redirect(url_for("chat"))
    return render_template('./login.html', message=response)

#Chat page
@app.route('/chat', methods=['GET', 'POST'])
def chat():

    #Demo purposes only.
    channels = [
        "<div class='channel' id='demo1' name='demo1'>\
            <button type='button'><p class='chat-text'>demo1</p></button>\
        </div>",
        "<div class='channel' id='demo2' name='demo1'>\
            <button type='button'><p class='chat-text'>demo2</p></button>\
        </div>"
    ]

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
