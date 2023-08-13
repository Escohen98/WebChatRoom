from flask import Flask, render_template, request, url_for, redirect, send_from_directory
#from firebase_admin import db
import json

app = Flask(__name__)
#ref = db.reference("/") #Firebase instructions taken from https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/

#Login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        email = request.form.get('email')
    return render_template('./login.html')

#Chat page
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    return render_template('./index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context='adhoc')
