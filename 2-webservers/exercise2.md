In this follow-up exercise, you will create a simple note-taking application that uses the same concepts from the Todo app. This will provide opportunities to practice the skills you've learned and extend them with additional features.

1. Create a Note class with the following attributes:

- id (integer)
- title (string)
- content (string)
- created_at (datetime)
- updated_at (datetime, optional)

2. Implement the following RESTful API endpoints for the Note app:

- GET /notes: Retrieve all notes.
- POST /notes: Create a new note.
- GET /notes/`<int:id>`: Retrieve a specific note by ID.
- PUT /notes/`<int:id>`: Update a note by ID.
- DELETE /notes/`<int:id>`: Delete a note by ID.

3. Add filtering capabilities to the GET /notes endpoint to allow users to search for notes by title or content.

4. Implement a simple pagination system for the GET /notes endpoint to limit the number of notes returned per request.

5. Add a timestamp feature to automatically update the updated_at attribute when a note is modified.

Here is a brief outline to get you started:

```python

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

class Note:
    # Add constructor and to_dict methods

notes = []

@app.get("/notes")
def get_notes():
    # Retrieve all notes with optional filtering

@app.post("/notes")
def create_note():
    # Create a new note

@app.get("/notes/<int:id>")
def get_note(id):
    # Retrieve a specific note by ID

@app.put("/notes/<int:id>")
def update_note(id):
    # Update a note by ID

@app.delete("/notes/<int:id>")
def delete_note(id):
    # Delete a note by ID

if __name__ == "__main__":
    app.run(debug=True)
```