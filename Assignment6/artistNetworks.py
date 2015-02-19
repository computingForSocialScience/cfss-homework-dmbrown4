from barChart import *
from fetchAlbums import *
from fetchArtist import *
from csvUtils import *

import sys
import requests
import csv
import pandas as pd


def getRelatedArtists(artist_id):
    """Using the Spotify API, take an artist ID and 
    returns a list of related artists in a list
    """
    url = 'https://api.spotify.com/v1/artists/' + artist_id + '/related-artists'
    req = requests.get(url)

    data = req.json()

    #checking for bad return value
    if not req.ok:
        print "error : " + data['error']['message']
        return "error : " + data['error']['message']

    related_artists = []
    for artist in data['artists']:
    	related_artists.append(artist['id'])

    return related_artists  

#if __name__ == '__main__':
	#print getRelatedArtists('43ZHCT0cAZBISjO8DG9PnE')  


def getDepthEdges(artist_id, depth):
	"""proxy function that takes two arguments, an artist ID and an
	integer 'depth' and returns a list of tuples representing the pairs of
	related artists."""
	return _getDepthEdges(artist_id, depth,[])

def _getDepthEdges(artist_id, depth,list_of_artists):
	"""that takes three arguments, an artist ID, an
	integer 'depth', and a list of already generated artist associations (in the form of tuples) 
	and returns a new list of tuples representing the pairs of related artists WITHOUT duplicates.
	"""	
	if depth == 0:
		return []

	related_artists = getRelatedArtists(artist_id)

	tpl_list = []

	for related_artist in related_artists: 
		tpl_list.append((artist_id, related_artist)) 
		list_of_artists.append(artist_id)
		'''created a list of artists that have already been inputted into the function
		'''
		if related_artist not in list_of_artists:
			tpl_list = tpl_list + _getDepthEdges(related_artist, depth-1,list_of_artists)

	return tpl_list

def checkTplList_undirected(tpl_list):
	"""checks if there are duplicates for undirected network. if there are then it prints an error
	"""
	for tpl in tpl_list:
		tpl2 = (tpl[1],tpl[0])
		if tpl2 in tpl_list:
			print 'duplicate found' , tpl, tpl2

def checkTplList_directed(tpl_list):
	"""checks if there are duplicates. if there are then it prints an error
	"""
	for tpl in tpl_list:
		count = 0
		for tpl2 in tpl_list:
			if tpl == tpl2:
				count += 1
				if count == 2:
					print "duplicate", tpl


def printTplList(tpl_list):
	"""prints tuples in tpl_list in a more readable format
	"""
	for tpl in tpl_list:
		print tpl
	
# tpl_list = getDepthEdges('7CyeXFnOrfC1N6z4naIpgo',3)
# printTplList(tpl_list)
# checkTplList_directed(tpl_list)


#checkTplList2([(1,2),(3,4),(1,2),(1,3)])

def getEdgeList(artist_id, depth):
	'''
	wrapper function that calls getEdgeList(artist_id, depth) and 
	returns the result as a Pandas DataFrame with one row for 
	each edge.
	'''
	EdgeList = pd.DataFrame(getDepthEdges(artist_id, depth))
	return EdgeList

#print getEdgeList('7CyeXFnOrfC1N6z4naIpgo',2)

def writeEdgeList(artist_id, depth, filename):
	''' Takes 3 arguments (artist ID, depth value, and a filename 
		for the output), and generates an edge list based on the 
		parameters 'artist_id' and 'depth' and sends them to a csv
		specified by the 'filename' parameter.
	'''
	EdgeListCSV = getEdgeList(artist_id, depth).to_csv(filename, index=False, header=['Artist','Related Artist'])
	return EdgeListCSV
	

writeEdgeList('7CyeXFnOrfC1N6z4naIpgo',2,'Edge_List_2.csv')	




