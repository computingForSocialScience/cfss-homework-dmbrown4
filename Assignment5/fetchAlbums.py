import requests
from datetime import datetime

from fetchArtist import *


def fetchAlbumIds(artist_id):
    """Using the Spotify API, take an artist ID and 
    returns a list of album IDs in a list
    """
    url = 'https://api.spotify.com/v1/artists/' + artist_id + '/albums?market=US&album_type=album'
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
    url = 'https://api.spotify.com/v1/albums/' + album_id
    req = requests.get(url)

    data = req.json() 

    if not req.ok:
        print "error : " + data['error']['message']
        return {}


   #create a new dictionary
    album_info_dict = {}
    #keys for the dictionary
    album_info_dict['artist_id'] = data['artists'][0]['id']
    album_info_dict['album_id'] = album_id
    album_info_dict['name'] = data['name']
    album_info_dict['year'] = data['release_date'][0:4]
    album_info_dict['popularity'] = int(data['popularity']) #Spotify's popularity-meter, an integer

    return album_info_dict


if __name__ == '__main__':
    fetchAlbumInfo(fetchAlbumIds(fetchArtistId('Sia'))[0])

#artist_id = fetchArtistId('Beatles')
#print fetchAlbumIds(artist_id)


