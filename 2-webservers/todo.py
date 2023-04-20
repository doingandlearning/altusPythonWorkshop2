from flask import Flask

app = Flask(__name__)

class Todo:
  def __init__(self, id, title, completed=False):
    self.id = id
    self.title = title
    self.completed = completed

  def to_dict(self):
    return {"id": self.id, "title": self.title, "completed": self.completed}

todos = []

# CRUD

@app.get("/todos")
def get_todos():
  pass

@app.post("/todos")
def post_todos():
  pass

@app.get("/todos/<int:id>")
def get_single_todo(id):
  pass

@app.put("/todos/<int:id>")
def update_single_todo(id):
  pass

@app.delete("/todos/<int:id>")
def delete_single_todo(id):
  pass

if __name__ == "__main__":
  app.run(debug=True, port=7337)