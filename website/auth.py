from flask import Blueprint, render_template, request, flash, redirect, url_for
# from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from flask_mysqldb import MySQL as mysqldb
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

mydb =mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "crud"
)

mycursor = mydb.cursor()


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        select_query = "SELECT * FROM accounts WHERE email=%s AND password=%s"

        email = request.form['email']
        password = request.form['password']

        # print(request.form(email))

        # user = User.query.filter_by(email=email).first()
        # user = mycursor.execute(f"SELECT * FROM accounts WHERE email={email}")
        user = mycursor.execute(select_query, (email), (password))
        selected_row = mycursor.fetchone()
        if selected_row:
            if email == True:
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    # return render_template("login.html", user=current_user)
    return render_template("login.html", accounts=current_user)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form['firstName' + 'lastName']
        password = request.form['password1']
        email = request.form['email']
        # phone = request.form['phone']
        # password2 = request.form.get('password2')

        # user = User.query.filter_by(email=email).first()
        curr = mycursor.execute(f"SELECT * FROM accounts WHERE email = {email}")
        user = curr.fetchall()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        # elif password1 != password2:
        #     flash('Passwords don\'t match.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # new_user = User(email=email, first_name=first_name, password=generate_password_hash(
            #     password1, method='sha256'))
            cur = mysqldb.connection.cursor()
            cur.execute("INSERT INTO accounts (id, name, email, phone, password) VALUES (%s, %s, %s)", (30, name, email, '080699', password))
            # print(table)
            mysqldb.connection.commit()
            # login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign-up.html", user=current_user)

# @auth.route('/insert', methods = ['POST'])
# def insert():
#     if request.method == "POST":
#         flash("Data Inserted Successfully")
#         name = request.form['name']
#         password = request.form['password1']
#         email = request.form['email']
#         phone = request.form['phone']
#         cur = mysqldb.connection.cursor()
#         cur.execute("INSERT INTO accounts (name, password1, email, phone) VALUES (%s, %s, %s, %s)", (name, password, email, phone))
#         mysqldb.connection.commit()
#         return redirect(url_for('Index'))
