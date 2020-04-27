from flask import Flask
from flask import request
import sys
import random

app = Flask(__name__)

@app.route("/spotify/callback", methods=['GET', 'POST'])
def spotify_callback(request):
    print ("hello there!!")
    display_name = request.args.get('display_name')
    access_code = request.args.get('access_code')
    app.logger.warning('testing warning log')
    print (request.headers, file=sys.stderr)
    return 'Hello'

if __name__ == '__main__':
    import requests
    import pprint
    import spotipy
    import spotipy.util as util

    spotify_object = spotipy.oauth2.SpotifyOAuth(username='12102312236', scope='user-library-read',
    client_id='a9cb3719fa8049baa76f4c1dfc2285ea',
    client_secret='a2c294ac68e04b72a1dea3eec69f4e8b',
    redirect_uri="http://127.0.0.1:5000/spotify/callback/")
    access_token = spotify_object.get_access_token()['access_token']
    spc = spotipy.client.Spotify(auth=access_token)
    print (spc.current_user())
    url = "https://api.spotify.com/v1/me/shows"
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token }
    params = {'limit': '50'}
    r = requests.get(url, headers=headers, params=params)
    for item in r.json()['items']:
        print (item['show']['name'], item['show']['id'], item['show']['images'][2]['url'])

    app.debug = True
    app.run(host='127.0.0.1', port=5000)
