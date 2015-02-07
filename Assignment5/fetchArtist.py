import sys
import requests
import csv

def fetchArtistId(name):
    """Using the Spotify API search method, take a string that is the artist's name, 
    and return a Spotify artist ID.
    """
    url = 'https://api.spotify.com/v1/search?q=' + name + "&type=artist"
    req = requests.get(url)

    data = req.json()

    #checking for bad return value
    if not req.ok:
        print "error : " + data['error']['message']
        return "error : " + data['error']['message']

     	
    #in JSON, index to artists, then items, then 0 location in items array, 
    #then id in location 0.

    #use len() to determine length of the array 'items' to make sure that
    #the artist actually exists.
    if  len(data['artists']['items']) > 0 :
        return data['artists']['items'][0]['id']
    else:
        return 'error: artist does not exist'
      


def fetchArtistInfo(artist_id):
    """Using the Spotify API, takes a string representing the id and
	`returns a dictionary including the keys 'followers', 'genres', 
    'id', 'name', and 'popularity'.
    """

    url = 'https://api.spotify.com/v1/artists/' + artist_id
    req = requests.get(url)

    data = req.json() 

    if not req.ok:
        print "error : " + data['error']['message']
        return {}

    
   

   #create a new dictionary
    artist_info_dict = {}
    #keys for the dictionary
    artist_info_dict['followers'] = data['followers']['total'] #number of Spotify followers
    artist_info_dict['genres'] = data['genres']#array of Spotify genres associated w/ artist
    artist_info_dict['id'] = artist_id
    artist_info_dict['name'] = data['name']
    artist_info_dict['popularity'] = int(data['popularity']) #Spotify's popularity-meter, an integer

    return artist_info_dict







