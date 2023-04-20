from datetime import datetime
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

@app.get("/add")
def add_function():
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  return jsonify({"answer": a + b})

@app.route("/divide")
def divide():
	a = int(request.args.get("a"))
	b = int(request.args.get("b"))

	# if(b == 0):
	# 	return "This ain't Math", 400
	try:
		return f"{a/b}"
	except ZeroDivisionError:
		return "This ain't maths", 400

@app.route('/days_until')
def days_until():
    date_str = request.args.get('date')
    try:
        target_date = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return 'Invalid date format, use YYYY-MM-DD.', 404

    today = datetime.now().date()
    
    if target_date.date() < today:
        return 'The given date is in the past.', 400
    
    days_left = (target_date.date() - today).days
    print(date_str)
    
    return f"{days_left} days left."

@app.get('/days-to-gone')
def date_till():  
  date = datetime.strptime(request.args.get('date'), "%Y-%m-%d").date()
  now = datetime.now().date()
  date_diff = date - now
  return f'Be patient, just {date_diff} till {date}'

# Listen on a port
if __name__ == "__main__":
  app.run(debug=True, port=1234)