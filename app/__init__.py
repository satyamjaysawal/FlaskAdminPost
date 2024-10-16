# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from werkzeug.security import generate_password_hash
import os

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'login'

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Set secret key from environment variable or fallback to a default
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'shivam-secret-key')  # Change this for production!
    
    # Define the database URI and instance path for writable storage
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(app.instance_path, 'app.db'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Ensure the instance path exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass  

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()  # Create database tables

        # Create default admin user if it doesn't exist
        from .models import User  # Import User model here to avoid circular import
        default_username = 'user'
        default_password = 'password'
        
        # Check if the admin user already exists
        admin_user = User.query.filter_by(username=default_username).first()
        if not admin_user:
            admin_user = User(username=default_username, is_admin=True)  # Set is_admin to True
            admin_user.set_password(default_password)  # Hash the password
            db.session.add(admin_user)
            db.session.commit()
            print(f"Default admin user created: {default_username}")

    return app
