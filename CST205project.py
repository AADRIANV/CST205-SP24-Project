
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import requests
import API_KEY_INFO



# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)

# route decorator binds a function to a URL
@app.route('/')
def home_page():

   API_KEY = API_KEY_INFO.ninjaAPIKey
   animalarray = ['sea otter', 'seagull', 'Ruby-Throated Hummingbird','sea lion', 'Humpback Whale']
   responseArray = []
   for name in animalarray:
      api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
      responseArray.append(requests.get(api_url, headers={'X-Api-Key': API_KEY}).json())

   print("JSON", responseArray)

   response = requests.get(api_url, headers={'X-Api-Key': API_KEY})

   return render_template('index.html',animal=responseArray)


@app.route('/birdwatch')
def bird_watch():
   return render_template('bird_watch.html')

@app.route('/about us')
def about_us():
   return render_template('about_us.html')

if __name__ == '__main__':
   app.run(debug=True)