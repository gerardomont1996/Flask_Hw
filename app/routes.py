
from app import app
from flask import render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required
from app.forms import RegisterForm, LoginForm
from app.models import User


@app.route('/register', methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        
        username = form.username.data
        password = form.password.data

    
        user_exists = User.query.filter(User.username == username).all()
        
        if user_exists:
            return redirect(url_for('register'))
        
        User(username=username, password=password)

        return redirect(url_for('home'))

    return render_template('register.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        
        username = form.username.data
        password = form.password.data
       
        user = User.query.filter_by(username=username).first()
        
        if not user or not user.check_password(password):
        
            print('That username and password is incorrect')
            return redirect(url_for('login'))
        
        login_user(user)
        print('User has been logged in')
        return redirect(url_for('index'))

    return render_template('login.html', form=form)
