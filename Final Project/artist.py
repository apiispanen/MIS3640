"""
The popularity of the artist: The value will be between 0 and 100, with 100 being the most popular. The artist's popularity is calculated from the popularity of all the artist's tracks.

"""
import requests
import pprint

Client_id = '1a3a8ea947e0445f88fa68c4056d0e2a'
Client_secret = '5ed0d9e6382143d2882915ba397271e4'
Token = 'Bearer BQBWJExDJWGVtBBq6Gtbqdq_dEUPxHJ_ysMvaJc-3K2fExldgxkbQ0-CQGNaZixAq2i03mf5seARLaDtBwepfFkNNl_cnYK5OdvOORQG8trlDl-aZzGBqBwgRZLK_nHGTqXh_Viklwo4xyBdPdaEgT0ipI7uetTmrwny'

'''
Produces the popularity data from Spotify based on an artist search term.

'''

def search(name):
    headers = {'Authorization':Token}
    url = 'https://api.spotify.com/v1/search'
    name = name.replace(' ', '+')
    params = {'q':name, 'type':'artist'}
    a = requests.get(url, headers = headers, params =params)
    b = a.json()
    popularity = b['artists']['items'][0]['popularity']
    return popularity

'''
Based on an artist ID, return the popularity of the artist. 

'''

def popularity(artistID):
    id = artistID
    url = 'https://api.spotify.com/v1/artists/'+id
    headers = {'Authorization':Token}
    a = requests.get(url, headers = headers )
    return a.json()['popularity']


aid='1vCWHaC5f2uS3yhpwWbIA6'

# print(popularity(aid))
# print(search('Katy Perry'))

# print(search('Avicii'))
# print(search('Loote'))
# print(search('Led Zeppelin'))

# print(search('The Lone Bellow'))