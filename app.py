from flask import Flask, render_template, request, redirect, url_for, redirect, send_from_directory
from PasswordManager import PasswordManager

import json, bcrypt

app = Flask(__name__)
user_email = "" #need this to be global to store which user it is
user_pass = ""
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
    return render_template('./chat.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
