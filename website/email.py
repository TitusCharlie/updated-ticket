from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask import Flask
from flask_mail import Mail, Message


email = Blueprint('email', __name__)



@email.route('/email', methods=['POST'])
def send_email():

    to_you = request.form['recipient']
    from_me = request.form['sender']
    the_message = request.form['message']

    msg = Message(the_message, sender=from_me, recipients=to_you)
    msg.body = the_message
    msg.html = the_message
    
    Mail.send(msg)
    return 'Email sent!'