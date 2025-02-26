from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecomstore_db.db'
    app.config['SECRET_KEY'] = '3ac59e5abebccf45a46282ee'
    
    db.init_app(app)
    csrf.init_app(app)

    from .auth import auth_bp
    from .admin import admin_bp
    from .views import views_bp
    from .delivery import delivery_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(delivery_bp, url_prefix="/delivery")
    app.register_blueprint(views_bp, url_prefix="/")

    with app.app_context():
        db.create_all()

    return app
