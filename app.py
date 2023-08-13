from flask import Flask, render_template, request, url_for, redirect, send_from_directory
from PasswordManager import PasswordManager as pm 

import json, bcrypt

app = Flask(__name__)

#Login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
    return render_template('./login.html')

#Chat page
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    return render_template('./index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context='adhoc')
