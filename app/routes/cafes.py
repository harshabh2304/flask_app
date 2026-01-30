from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from app import db
from app.models.cafes import Cafe

cafes_bp=Blueprint('cafes',__name__)

@cafes_bp.route('/home',methods=["GET"])
def home():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    cafes=Cafe.query.all()
    return render_template('home.html',cafes=cafes)

@cafes_bp.route('/add',methods=["GET","POST"])
def add():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    if request.method == "POST":
        name=request.form.get('name')
        location=request.form.get('location')
        power_socket=request.form.get('power_socket')
        rating=request.form.get('rating')
        opening_time=request.form.get('opening_time')

        if power_socket == 'yes':
            power_socket=True

        else:
            power_socket=False

        if name and location and opening_time and rating is not None:
            
            if not rating.isdigit():
                flash('Rating must be a number', 'danger')
                return redirect(url_for('cafes.add'))
            
            rating=int(rating)

            if rating < 1 or rating > 5:
                flash('Rating must be between 1 and 5', 'danger')
                return redirect(url_for('cafes.add'))


            new_cafe=Cafe(
            name=name,
            location=location,
            power_socket=power_socket,
            rating=rating,
            opening_time=opening_time
            )
            db.session.add(new_cafe)
            db.session.commit()
            flash('cafe added Successfully','success')
            return redirect(url_for('cafes.home'))

        else:
            flash('enter the all detials','danger')
            return redirect(url_for('cafes.add'))
              
    return render_template("add.html")

@cafes_bp.route('/logout')
def logout():
    session.pop('user_id',None)
    flash('logged out','info')
    return redirect(url_for('auth.login'))