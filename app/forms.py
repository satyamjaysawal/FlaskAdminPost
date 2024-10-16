# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo

# Common field length limits for username and passwords
USERNAME_LEN = 150
PASSWORD_MIN_LEN = 6
PASSWORD_MAX_LEN = 128
POST_TITLE_LEN = 150
COMMENT_CONTENT_LEN = 500

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=USERNAME_LEN)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=USERNAME_LEN)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=PASSWORD_MIN_LEN, max=PASSWORD_MAX_LEN)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=PASSWORD_MIN_LEN, max=PASSWORD_MAX_LEN)])
    confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Change Password')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=POST_TITLE_LEN)])
    content = TextAreaField('Content', validators=[DataRequired(), Length(min=1)])
    submit = SubmitField('Add Post')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired(), Length(min=1, max=COMMENT_CONTENT_LEN)])
    submit = SubmitField('Add Comment')

class AdminLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=USERNAME_LEN)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=PASSWORD_MIN_LEN, max=PASSWORD_MAX_LEN)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Admin Login')
