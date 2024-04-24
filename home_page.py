# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)

# route decorator binds a function to a URL
@app.route('/')
def home_page():
   return 'Hello world from Flask!'

@app.route('/environment1')
def environment1():
   return 'First environment page '