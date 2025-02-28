from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    """Creates and configures the Flask app."""
    app = Flask(__name__)

    # Configure the database (SQLite for simplicity)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productdb.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize the database
    db.init_app(app)

    # Import and register Blueprints
    from app.views import views_bp
    from app.auth import auth_bp
    from app.admin import admin_bp

    app.register_blueprint(views_bp, url_prefix='/views')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    # Create database tables if they don’t exist
    with app.app_context():
        db.create_all()

    return app

