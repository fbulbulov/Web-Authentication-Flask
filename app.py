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
    email=StringField('username', Email(message='Invalid email'), Length(max=40))
    username=StringField('username',validators=[InputRequired(), Length(min=3, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=6, max=20)])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return '<h1>'+form.username.data+' '+form.password.data + '</h1>'
    return render_template('login.html', form=form)

@app.route('/singup', methods=['GET', 'POST'])
def singup():
    form=RegisterForm()
    if form.validate_on_submit():
        return '<h1>'+form.username.data+' '+form.email.data + ' ' + form.password.data + '</h1>'
    return render_template('singup.html', form=form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)