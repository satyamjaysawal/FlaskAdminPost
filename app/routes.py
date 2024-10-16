# app/routes.py

from flask import render_template, redirect, url_for, flash, request, current_app as app
from flask_login import login_user, login_required, logout_user, current_user
from . import db
from .models import User, Post, Comment
from .forms import LoginForm, RegistrationForm, PostForm, CommentForm, ChangePasswordForm, AdminLoginForm

# Public Route - Home
@app.route('/')
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()  # Get all posts
    form = CommentForm()  # Create the form instance
    return render_template('posts.html', posts=posts, form=form)

# User Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Logged in successfully!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        flash('Invalid username or password', 'danger')

    return render_template('login.html', form=form)

# Admin User Update Route
@app.route('/admin/update', methods=['GET', 'POST'])
@login_required
def update_admin():
    if not current_user.is_admin:  # Check if the current user is an admin
        flash('Access denied.', 'danger')
        return redirect(url_for('index'))

    form = AdminLoginForm()  # Assuming you have AdminLoginForm defined
    admin_user = User.query.filter_by(username='user').first()  # Assuming 'user' is the admin username

    if form.validate_on_submit():
        if admin_user:
            # Update existing admin user
            admin_user.username = form.username.data
            admin_user.set_password(form.password.data)  # Update password
            db.session.commit()
            flash('Admin user updated successfully!', 'success')
        else:
            # Create the admin user if it doesn't exist
            new_user = User(username=form.username.data)
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash('Default admin user created successfully!', 'success')

        return redirect(url_for('update_admin'))  # Redirect to the same page after processing

    # Prepopulate the form with existing admin user details if they exist
    if admin_user:
        form.username.data = admin_user.username

    return render_template('update_admin.html', form=form)

# Admin Login Route
@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = AdminLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data) and user.is_admin:
            login_user(user, remember=form.remember.data)
            flash('Admin login successful!', 'success')
            return redirect(url_for('admin_dashboard'))
        flash('Invalid admin credentials', 'danger')
    
    return render_template('admin_login.html', form=form)

# User Logout Route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

# User Registration Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('Username already exists.', 'danger')
            return redirect(url_for('register'))
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# Change Password Route
@app.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.check_password(form.old_password.data):
            current_user.set_password(form.new_password.data)
            db.session.commit()
            flash('Your password has been updated.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Old password is incorrect.', 'danger')
    return render_template('change_password.html', form=form)

# Add Comment Route
@app.route('/add_comment/<int:post_id>', methods=['POST'])
@login_required
def add_comment(post_id):
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(content=form.content.data, author=current_user, post_id=post_id)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added.', 'success')
    else:
        flash('Failed to add comment.', 'danger')
    return redirect(url_for('index'))

# Admin Dashboard Route
@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash('Access denied.', 'danger')
        return redirect(url_for('index'))
    
    users = User.query.all()  # Get all users for the admin dashboard
    return render_template('dashboard.html', users=users)

# Add Post (Admin Only)
@app.route('/admin/add_post', methods=['GET', 'POST'])
@login_required
def add_post():
    if not current_user.is_admin:
        flash('Access denied.', 'danger')
        return redirect(url_for('index'))
    
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        flash('Post added successfully.', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_post.html', form=form)

# View Comments (Admin Only)
@app.route('/admin/comments')
@login_required
def view_comments():
    if not current_user.is_admin:
        flash('Access denied.', 'danger')
        return redirect(url_for('index'))
    
    comments = Comment.query.order_by(Comment.timestamp.desc()).all()  # Get all comments
    return render_template('comments.html', comments=comments)
