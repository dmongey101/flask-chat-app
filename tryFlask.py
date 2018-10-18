from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


messages = [
    {
     'text': "Hi",
     'author': 'richard'
    },
    {
     'text': "Hi you too.",
     'author': 'tony'
    }
    ]

@app.route("/")
def login():
    return render_template("login.html")
    
@app.route("/login", methods = ["POST"])
def do_login():
    username = request.form["username"]
    return redirect("/chat/" + username)

@app.route("/chat/<username>")
def show_chat(username):
    return render_template("chat.html", messages=messages, username = username)

@app.route("/chat/<username>/add", methods = ["POST"])
def add_message(username):
    message = request.form["msg"]
    message_dict = {
        'author': username,
        'text': message
    }
    messages.append(message_dict)
    return redirect("/chat/" + username)


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
