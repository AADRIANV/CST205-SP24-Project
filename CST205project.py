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


@app.route('/birdwatch')
def bird_watch():
   return render_template('bird_watch.html')

@app.route('/about us')
def about_us():
   return render_template('about_us.html')