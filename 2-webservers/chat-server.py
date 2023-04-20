from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "some super key"
socketio = SocketIO(app, logger=True)

@app.get("/chat/<username>")
def get_chat_page(username):
  return render_template("chat.html", username=username)