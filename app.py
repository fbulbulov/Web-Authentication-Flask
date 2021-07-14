from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app=Flask(__name__)
app.config['SECRET_KEY']="Secret_key"
Bootstrap(app)

class LoginForm(FlaskForm):
    username=StringField('username',validators=[InputRequired(), Length(min=3, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=6, max=20)])
    remember= BooleanField('remember me')

class RegisterForm(FlaskForm):
    email=StringField('email', validators[InputRequired(), Email(message='invalid email', length=(max=30)])
    username=StringField('username',validators=[InputRequired(), Length(min=3, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=6, max=20)])
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/singup')
def singup():
    return render_template('singup.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__=="__main__":
    app.run(debug=True)