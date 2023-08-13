from flask import Flask, render_template, request, url_for, redirect, send_from_directory

app = Flask(__name__)

#Login page
@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('./login.html')