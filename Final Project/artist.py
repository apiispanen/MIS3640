"""
The popularity of the artist: The value will be between 0 and 100, with 100 being the most popular. The artist's popularity is calculated from the popularity of all the artist's tracks.

"""
import requests
import pprint

Client_id = '1a3a8ea947e0445f88fa68c4056d0e2a'
Client_secret = '5ed0d9e6382143d2882915ba397271e4'
Token = 'Bearer BQBKw1vXJItaKWVfEHQwj0um1t78C4yrwQ2U9wmYFdLSYc2UmtB2xqhfD3NeLD5CezzNrEOnh1IVonv2d8xhhSShWIUiQTw2GPcSVY6Q-de0vkBZn0fUi5Koe0UoJVyVuYpGdHMiFPYbrmQJ9dmXCux6hq0TTMjC8K3M6D4'

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
    if len(b['artists']['items'])<1:
        return False
    else:
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

def history():
    a = open('history.txt', 'r')
    text_split = a.readlines()
    a = []
    for line in text_split:
        a.append(line[:line.find(':')]+', starting popularity:'+ line[line.find(':')+1:line.find(',')])
    
    return a 
        

aid='1vCWHaC5f2uS3yhpwWbIA6'

# print(history())
# print(popularity(aid))
# print(search('Katy Perry'))

# print(search('Avicii'))
# print(search('Loote'))
# print(search('Led Zeppelin'))

# print(search('The Lone Bellow'))