from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_wtf.csrf import CSRFProtect
from config import config
from models.ModelUser import ModelUser
from models.entities.User import User

app=Flask(__name__)

csrf=CSRFProtect()
db = MySQL(app)
login_manager_app=LoginManager(app)

@login_manager_app.user_loader
def loard_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():    
    if request.method=='POST':        
        user = User(0, request.form['username'], request.form['password'])        
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash('Contraseña incorrecta')
                return render_template('auth/login.html')
        else:
            flash('Usuario no encontrado')
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home')
@login_required
def home():
    return render_template('home.html')

if __name__=='__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.run()