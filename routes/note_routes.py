from flask import Blueprint, request, jsonify, session
from models import db
from models.note import Note

note_bp = Blueprint('note_bp', __name__)

def get_current_user_id():
    return session.get('user_id')


@note_bp.route('/notes', methods=['GET'])
def get_notes():
    user_id = get_current_user_id()

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    pagination = Note.query.filter_by(user_id=user_id).paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    return jsonify({
        "items": [note.to_dict() for note in pagination.items],
        "page": pagination.page,
        "per_page": pagination.per_page,
        "total": pagination.total,
        "pages": pagination.pages
    }), 200


@note_bp.route('/notes', methods=['POST'])
def create_note():
    user_id = get_current_user_id()

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()

    title = data.get('title')
    content = data.get('content')

    if not title or not content:
        return jsonify({"error": "Title and content are required"}), 400

    note = Note(
        title=title,
        content=content,
        user_id=user_id
    )

    db.session.add(note)
    db.session.commit()

    return jsonify(note.to_dict()), 201


@note_bp.route('/notes/<int:id>', methods=['PATCH'])
def update_note(id):
    user_id = get_current_user_id()

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    note = Note.query.get(id)

    if not note:
        return jsonify({"error": "Note not found"}), 404

    if note.user_id != user_id:
        return jsonify({"error": "Forbidden"}), 403

    data = request.get_json()

    if 'title' in data:
        note.title = data['title']

    if 'content' in data:
        note.content = data['content']

    db.session.commit()

    return jsonify(note.to_dict()), 200


@note_bp.route('/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    user_id = get_current_user_id()

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    note = Note.query.get(id)

    if not note:
        return jsonify({"error": "Note not found"}), 404

    if note.user_id != user_id:
        return jsonify({"error": "Forbidden"}), 403

    db.session.delete(note)
    db.session.commit()

    return '', 204