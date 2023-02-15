from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
# from .models import Note
import mysql.connector
import json

views = Blueprint('views', __name__)

mydb =mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "crud"
)

mycursor = mydb.cursor()


@views.route('/index', methods=['POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        

        print(email, first_name, last_name)
        print(request.form)
    return render_template('index.html')


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
     
    if request.method == 'POST': 
        
        note = request.form.get('note')#Gets the note from the HTML 


        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            # new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            mycursor.execute("INSERT INTO accounts(note) VALUES (%s)", (note))
            # db.session.add(new_note) #adding the note to the database 
            mycursor.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=(current_user))


# @views.route('/delete-note', methods=['POST'])
# def delete_note():  
#     note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
#     noteId = note['noteId']
#     note = Note.query.get(noteId)
#     if note:
#         if note.user_id == current_user.id:
#             # mycursor.delete(note)
#             mycursor.commit()

#     return jsonify({})
