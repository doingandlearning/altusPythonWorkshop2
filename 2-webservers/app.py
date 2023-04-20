from flask import Flask, request, jsonify, Response, make_response

# Hello, world!
app = Flask(__name__)

# Create a route
@app.route("/")
def hello_world():
  api_key = request.headers.get("x-api-key")

  if api_key == "super-secret-password":
    return "Time for coffee (if there are no questions)"
  else:
    resp = Response()
    resp.headers["x-coffee-time"] = 'now'
    return jsonify({"message": "now"}), 404



@app.route("/goodbye")
def goodbye_world():
  response = make_response(jsonify({"message": "Goodbye cruel, world!"}))
  response.headers["x-other-message"] = "It's not that bad!"
  return response

@app.route("/hello/<name>")
def say_hello(name):
  response = request.args.get("response")
  return f"Hello {name}, how are you? {response}"

@app.route("/", methods=["POST"])
def post_hello():
  return "You used the POST method"

@app.patch("/")
def patch_hello():
  return "You used the PATCH method"

# Listen on a port
if __name__ == "__main__":
  app.run(debug=True, port=1234)