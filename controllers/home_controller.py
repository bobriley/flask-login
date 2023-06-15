from flask import Blueprint, render_template, request, session, redirect, url_for

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
    return redirect(url_for('index'))
    