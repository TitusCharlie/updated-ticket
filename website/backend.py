from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
# from .models import Note
# from . import db
import json

backend = Blueprint('backend', __name__)


@backend.route('/login')
def edit_ticket():

    return "<h1>Admin portal</h1>"