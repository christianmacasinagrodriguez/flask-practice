from flask import Blueprint, flash, render_template, request, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Note
import json
from .store import Tinda
from .models import User

views = Blueprint('views', __name__)

@views.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category='success')

    return render_template("home.html", user=current_user, tinda=Tinda)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Note Deleted!', category='success')
    return jsonify({})