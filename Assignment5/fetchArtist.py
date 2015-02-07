import sys
import requests
import csv

def fetchArtistId(name):
    """Using the Spotify API search method, take a string that is the artist's name, 
    and return a Spotify artist ID.
    """
    url = 'https://api.spotify.com/v1/search?q=' + name + "&type=artist"
    req = requests.get(url)

    #checking for bad return value
    if not req.ok:
        print "error"
        return -1

    data = req.json() 	
    #in JSON, index to artists, then items, then 0 location in items array, 
    #then id in location 0.

    #use len() to determine length of the array 'items' to make sure that
    #the artist actually exists.


    if  len(data['artists']['items']) > 0 :
        return data['artists']['items'][0]['id']
    else:
        return -1
      


def fetchArtistInfo(artist_id):
    """Using the Spotify API, takes a string representing the id and
	`returns a dictionary including the keys 'followers', 'genres', 
    'id', 'name', and 'popularity'.
    """
   #create a new dictionary
    artist_info_dict = {}

    #keys for the dictionary
    #artist_info_dict['followers'] = #number of Spotify followers
    #artist_info_dict['genres'] = #list of Spotify genres associated w/ artist
    #artist_info_dict['id'] = #Spotify artist ID
    #artist_info_dict['name'] = #artist name
    #artist_info_dict['popularity'] = #Spotify's popularity-meter, an integer


    pass

print fetchArtistId('M83')





