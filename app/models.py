# app/models.py

from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each user
    username = db.Column(db.String(150), unique=True, nullable=False)  # User's username
    password_hash = db.Column(db.String(128), nullable=False)  # Hashed password
    is_admin = db.Column(db.Boolean, default=False)  # Flag to indicate if user is admin
    comments = db.relationship('Comment', backref='author', lazy=True)  # Relationship with comments

    def set_password(self, password):
        """Hash the password and set the password hash."""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check if the provided password matches the hashed password."""
        return check_password_hash(self.password_hash, password)

# Post Model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each post
    title = db.Column(db.String(150), nullable=False)  # Title of the post
    content = db.Column(db.Text, nullable=False)  # Content of the post
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Time the post was created
    comments = db.relationship('Comment', backref='post', lazy=True)  # Relationship with comments

# Comment Model
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each comment
    content = db.Column(db.Text, nullable=False)  # Content of the comment
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Time the comment was created
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Linked to User
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)  # Linked to Post

# Form for submitting comments
class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])  # Content input for the comment
    submit = SubmitField('Submit')  # Submit button

# User Loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.query.get(int(user_id))
