from flask import Blueprint, render_template, request, session, redirect, url_for
from models.User import User, db

home_controller = Blueprint('home_controller', __name__)

@home_controller.route('/', methods=['GET'])
def index():
    if session.get('logged_in'):
        return render_template('home.html')
    else:
        return render_template('index.html', message="Hello!")
    
@home_controller.route('/logout', methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('home_controller.index'))

@home_controller.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            db.session.add(User(username=request.form['username'], password=request.form['password']))
            db.session.commit()
            return redirect(url_for('home_controller.login'))
        except:
            return render_template('index.html', message="User Already Exists")
    else:
        return render_template('register.html')


@home_controller.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        u = request.form['username']
        p = request.form['password']
        data = User.query.filter_by(username=u, password=p).first()
        if data is not None:
            session['logged_in'] = True
            return redirect(url_for('home_controller.index'))
        return render_template('index.html', message="Incorrect Details")
    