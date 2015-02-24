from artistNetworks import *
from analyzeNetworks import *
from fetchArtist import *
from fetchAlbums import *


import sys
import requests
import csv
import pandas as pd
import networkx as nx
import numpy as np
import io


# Takes any number of artist names as command-line arguments and 
# which writes a file called `playlist.csv` that lists 30 songs 
# (as given by artist name, album name, and track name).

#depth of 2
#fetch networks for each artist
#combine related-artist networks
#sample 30 artists from combined network using randomCentralNode




for i in sys.argv[1:]:
	writeEdgeList(fetchArtistId(i), 2, 'edgeList.csv')
	master_DF_edgeList = readEdgeList('edgeList.csv')

for i in sys.argv[2:]:
	writeEdgeList(fetchArtistId(i), 2, 'edgeList.csv')
	DF_edgeList = readEdgeList('edgeList.csv')
	master_DF_edgeList = combineEdgeLists(master_DF_edgeList, DF_edgeList)


#making a list of 30 nodes from combined edge list
random_node_list = []
DG = pandasToNetworkX(master_DF_edgeList)
for x in range(0,30):
	random_node = randomCentralNode(DG)
	random_node_list.append(random_node)




random_album_dict = {}
random_albumID_list = []
random_song_dict = {}
random_artist_name_dict = {}




#getting album and song info using Spotify urls
for random_node in random_node_list:
	url1 = 'https://api.spotify.com/v1/artists/' + random_node + '/albums'
	req = requests.get(url1)
	data1 = req.json()
	random_album_dict[random_node] = data1['items'][0]['name']
	random_albumID_list.append(data1['items'][0]['id'])
	for albumID in random_albumID_list:
		url2 = 'https://api.spotify.com/v1/albums/' + albumID + '/tracks'
		req = requests.get(url2)
		data2 = req.json()
		#random_song_dict[albumID] = data2['items'][0]['name']
		#random_song_dict[data2['items'][0]['artists'][0]['id']] = data2['items'][0]['name']
		random_song_dict[random_node] = data2['items'][0]['name']
		random_artist_name_dict[random_node] = data2['items'][0]['artists'][0]['name']

# dict_list = []
# dict_list.append(random_album_dict)
# dict_list.append(random_song_dict)

f = open('playlist.csv','w', encoding = 'utf-8')
f.write(u'artist_name,album_name,track_name\n')

for random_node in random_node_list:
    f.write(u'"' + random_artist_name_dict[random_node] + '","' + random_album_dict[random_node] + '","' + random_song_dict[random_node] + '" \n')
f.close() 



# fetchArtistId(name)
# getRelatedArtists(artist_id)
# getDepthEdges(artist_id, depth)
# getEdgeList(artist_id, depth)
# writeEdgeList(artist_id, depth, filename)
# readEdgeList(filename)

# combineEdgeLists(edgeList1, edgeList2)

# pandasToNetworkX(edgeList)
# randomCentralNode(inputDiGraph)
