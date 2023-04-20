from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

class Note:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
        self.created_at = datetime.now()
        self.updated_at = None

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

notes = []

@app.get("/notes")
def get_notes():
    query = request.args.get("query", "").lower()
    filtered_notes = [note for note in notes if query in note.title.lower() or query in note.content.lower()]
    page = request.args.get("page", 1)
    start_index = (int(page) - 1) * 10
    return jsonify([note.to_dict() for note in filtered_notes][start_index: start_index + 10])

@app.post("/notes")
def create_note():
    data = request.json
    title = data.get("title")
    content = data.get("content")

    if not title or not content:
        return jsonify({"message": "You need to provide a note title and content", "error": True}), 400

    id = len(notes) + 1
    note = Note(id, title, content)
    notes.append(note)
    
    return jsonify(note.to_dict()), 201

@app.get("/notes/<int:id>")
def get_note(id):
    for note in notes:
        if note.id == id:
            return jsonify(note.to_dict())
    return jsonify({"message": "Cannot find note with given id", "error": True}), 404

@app.put("/notes/<int:id>")
def update_note(id):
    for note in notes:
        if note.id == id:
            data = request.json
            note.title = data.get("title", note.title)
            note.content = data.get("content", note.content)
            note.updated_at = datetime.now()
            return jsonify(note.to_dict())
    return jsonify({"message": "Cannot find note with given id", "error": True}), 404

@app.delete("/notes/<int:id>")
def delete_note(id):
    for note in notes:
        if note.id == id:
            notes.remove(note)
            return "", 204
    return jsonify({"message": "Cannot find note with given id", "error": True}), 404

if __name__ == "__main__":
    app.run(debug=True)
