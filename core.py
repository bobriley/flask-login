from flask import Flask
from models import db

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    
    db.init_app(app)

    with app.app_context():
        from models import User  # Moved import here to ensure db is initialized
        db.create_all()

    return app