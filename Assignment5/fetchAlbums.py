import requests
from datetime import datetime

import fetchArtist


def fetchAlbumIds(artist_id):
    """Using the Spotify API, take an artist ID and 
    returns a list of album IDs in a list
    """
    url = 'https://api.spotify.com/v1/artists/' + artist_id + '/albums?market=US&albumtype=album'
    req = requests.get(url)

    data = req.json()

    #checking for bad return value
    if not req.ok:
        print "error : " + data['error']['message']
        return "error : " + data['error']['message']

    albums = []
    for item in data['items']:
    	albums.append(item['id'])

    return albums    

   


def fetchAlbumInfo(album_id):
    """Using the Spotify API, take an album ID 
    and return a dictionary with keys 'artist_id', 'album_id' 'name', 'year', popularity'
    """
    pass




artist_id = fetchArtist.fetchArtistId('Beatles')
print fetchAlbumIds(artist_id)


