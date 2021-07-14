from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtform import Stringfield, Passwordfield, BooleanField

app=Flas(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/singup')
def login():
    return render_template('singup.html')

@app.route('/dashboard')
def login():
    return render_template('dashboard.html')

if __name__=="__main__":
    app.run(debug=True)