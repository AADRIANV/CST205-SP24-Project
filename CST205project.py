# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)

# route decorator binds a function to a URL
@app.route('/')
def home_page():
   return render_template('index.html')


@app.route('/biome1')
def environment1():
   return 'First biome page'

@app.route('/about us')
def environment2():
   return 'this is a project created by Adrian Villalpando, Jocy Cortez-Arellano, Issac Espinoza, Ronaldo Chagolla-Bonilla' 