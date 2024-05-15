import requests
from flask import Flask, render_template, current_app
from flask_bootstrap import Bootstrap5
import requests
import API_KEY_INFO



# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)

def get_weather_info():
   city = 'Marina'
   api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
   response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})

# route decorator binds a function to a URL
@app.route('/')
def home_page():

   API_KEY = API_KEY_INFO.ninjaAPIKey
   animalarray = ['sea otter', 'seagull', 'Ruby-Throated Hummingbird','sea lion', 'Mountain Lion','Humpback Whale']
   responseArray = []
   for name in animalarray:
      api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
      responseArray.append(requests.get(api_url, headers={'X-Api-Key': API_KEY}).json())

   print("JSON", responseArray)

   response = requests.get(api_url, headers={'X-Api-Key': API_KEY})

   return render_template('index.html',animal=responseArray)


@app.route('/birdwatch')
def bird_watch():
   search_url = 'https://www.googleapis.com/youtube/v3/search'
   video_url = 'https://www.googleapis.com/youtube/v3/videos'
   search_param = {
      'key' : 'AIzaSyBnrbxuMZrF7mSIyELpEioYxxHBv6odRA8',
      'q' : 'learn flask',
      'part' : 'snippet',
      'maxResluts' : 3,
      'type' : 'video'

      }

   r = requests.get(search_url,params=search_param)

   results= r.json()['items']
 
   video_ids = []
   for result in results:
    video_ids.append(result['id']['videoId'])
    
    video_params = {
       'key' : 'AIzaSyBnrbxuMZrF7mSIyELpEioYxxHBv6odRA8',
       'id' : ','.join(video_ids), 
       'part': 'snippet,contentDetails',
       'maxResluts' : 3

    }
   r = requests.get(video_url, params= video_params)
    
   results = r.json()['items']
   for result in results:
      video_data = {
         'id': result['id'],
         'url' : f'https://www.youtube.com/watch?v={ result['id'] }',
         'thumbnail' : result['snippet']['thumbnails']['high']['url'],
         'duration' : result['contentDetails']['duration'],
         'title' : result['snippet']['title']

      }
   

   return render_template('bird_watch.html')

@app.route('/about us')
def about_us():
   return render_template('about_us.html')

if __name__ == '__main__':
   app.run(debug=True)