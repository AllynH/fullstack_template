# server.py
from flask import Flask, render_template
import random

app = Flask(__name__, static_folder="../static/dist",
	template_folder="../static")

@app.route("/")
def index():
	""" Index page: """
	return render_template("index.html")

@app.route("/hello")
def hello():
	""" Return random Hello to browser """
	return get_hello

def get_hello():
	""" return random hello! """
	greeting_list = ['Dia dhuit', 'Ciao', 'hei', 'Salut', 'Hola', 'Hallo', 'Hej']
	return random.choice(greeting_list)

if __name__ == "__main__":
	app.run()
