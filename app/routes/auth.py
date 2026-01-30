from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from app.models.users import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        useremail = request.form.get('useremail')
        password = request.form.get('password')

        user = User.query.filter_by(email=useremail).first()

        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            flash('Login successful', 'success')
            return redirect(url_for('cafes.home'))
        else:
            flash('Invalid email or password', 'danger')

    return render_template('login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        useremail = request.form.get('useremail')
        password = request.form.get('password')
        c_password = request.form.get('c_password')

        if password != c_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('auth.register'))

        existing_user = User.query.filter_by(email=useremail).first()
        if existing_user:
            flash('Email already registered', 'danger')
            return redirect(url_for('auth.register'))

        hashed_password = generate_password_hash(password)

        new_user = User(
            name=username,
            email=useremail,
            password_hash=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        flash('Successfully registered. Please login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')
