import spotipy
import spotipy.util as util
import requests 
import sys
spotify = spotipy.Spotify()
Client_id = '1a3a8ea947e0445f88fa68c4056d0e2a'
Client_secret = '5ed0d9e6382143d2882915ba397271e4'
scopes = 'playlist-read-private playlist-read-collaborative playlist-modify-public playlist-modify-private	streaming ugc-image-upload user-read-email user-top-read user-read-playback-state user-modify-playback-state user-read-currently-playing user-read-recently-played'

scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope = scope, client_id = Client_id, client_secret=Client_secret)

# if token != None:
#     sp = spotipy.Spotify(auth=token)
#     results = sp.current_user_saved_tracks()
#     for item in results['items']:
#         track = item['track']
#         print track['name'] + ' - ' + track['artists'][0]['name']
# else:
#     print "Can't get token for", username

# results = spotify.search(q='artist:' + 'Birdy', type='artist')
# print(results)