from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS 
from dotenv import loadenv
import os

def create_app():
    app = Flask(__name__)

    load.dotenv()
    
    db = SQLAlchemy(app)
    cors = CORS(app)


    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flash_words.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    cors.init_app(app, resources={r"/*": {"origins": "*"}})

    # Import and register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app


    


