from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api
from middleware import with_header_auth

app = Flask(__name__)
api = Api(app)

class TodoApi(Resource):
  def get(self, todo_id=None):
    if not todo_id:
      return todos
    else:
      for todo in todos:
        if todo.id == id:
          return todo.to_dict()
  
  def post(self):
    data = request.json
    id = len(todos) + 1 # Get it from the database!!
    title = data.get("title")

    if not title:
      return jsonify({"message": "Whoops! You need to send a title.", "error": True}), 400

    todo = Todo(id, title)
    todos.append(todo)
    return todo.to_dict()

api.add_resource(TodoApi, "/other-todos")

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
  # reponse.headers["content-type"] = "application/json"
  response = make_response({"test": "test"})
  return response

@app.post("/todos")
@with_header_auth
def post_todos():
  data = request.json
  id = len(todos) + 1 # Get it from the database!!
  title = data.get("title")

  if not title:
    return jsonify({"message": "Whoops! You need to send a title.", "error": True}), 400

  todo = Todo(id, title)
  todos.append(todo)
  return jsonify(todo.to_dict()), 201

# @app.route("/todos/<int:id>", methods=["DELETE", "PUT", "GET"])
# def single_todo(id):
#   if request.method == "GET":
#     pass
#   elif request.method == "PUT":
#     pass
#   elif request.method == "DELETE":
#     pass
#   else:
#     pass


@app.get("/todos/<int:id>")
def get_single_todo(id):
  for todo in todos:
    if todo.id == id:
      return jsonify(todo.to_dict())
  return jsonify({"message": "We don't have a todo with that id", "error": True}), 404

@app.put("/todos/<int:id>")
def update_single_todo(id):
  for todo in todos:
    if todo.id == id:
      data = request.json
      todo.title = data.get("title", todo.title)
      todo.completed = data.get("completed", todo.completed)
      return jsonify(todo.to_dict())
  return jsonify({"message": "We don't have a todo with that id", "error": True}), 404  

@app.delete("/todos/<int:id>")
def delete_single_todo(id):
  for todo in todos:
    if todo.id == id:
      todos.remove(todo)
      return "", 204
  return jsonify({"message": "We don't have a todo with that id", "error": True}), 404  

if __name__ == "__main__":
  app.run(debug=True, port=7337)