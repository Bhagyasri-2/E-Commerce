# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import db  # ✅ Import db correctly

def create_app():
    """Creates and configures the Flask app."""
    app = Flask(__name__)

    # Configure the database (SQLite for simplicity)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productdb.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database
    db.init_app(app)  # ✅ Ensure db is initialized before queries

    # Import Blueprints for different sections of the app
    from app.views import views_bp
    from app.auth import auth_bp
    from app.admin import admin_bp

    # Register the Blueprints with URL prefixes
    app.register_blueprint(views_bp, url_prefix='/views')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    # Create database tables within app context (for the models to be created)
    with app.app_context():
        db.create_all()

    return app

