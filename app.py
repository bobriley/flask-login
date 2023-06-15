from flask import Flask, url_for, render_template, request, redirect, session
from controllers.home_controller import home_controller
from models.User import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db.init_app(app)

app.register_blueprint(home_controller)

if(__name__ == '__main__'):
    app.secret_key = "ThisIsNotASecret:p"
    
    with app.app_context():
        db.create_all()

    app.run()
