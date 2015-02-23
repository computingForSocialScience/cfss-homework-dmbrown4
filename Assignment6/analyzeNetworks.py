from artistNetworks import *

import sys
import requests
import csv
import pandas as pd
import networkx as nx
import numpy as np


def readEdgeList(filename):
	# takes one argument (filename of a csv) and reads an edge list from
	# that CSV. It will only return data from the first two columns of the 
	# CSV.

	DataFrame = pd.read_csv(filename)
	#return(DataFrame.columns)

	if len(DataFrame.columns)!=2:
		print "Error: too many columns"
		DataFrame_2cols = pd.read_csv(filename, usecols=(1,2))
		return DataFrame_2cols
	else:	
		return DataFrame

#print readEdgeList('Edge_List_1.csv')	
#print readEdgeList('albums.csv')	


def	degree(edgeList, in_or_out):
	# takes 2 arguments (1. an edge list as returned by 'readEdgeList()' and
	# 2. a string that is either 'in' or 'out'). Function returns the in-degree
	# or out-degree for all nodes in a given edge list.

	if in_or_out == 'in':
		return edgeList['Artist'].value_counts()
	elif in_or_out == 'out':
		return edgeList['Related Artist'].value_counts()
	else:
		print "Error: invalid argument. must enter either 'in' or 'out'"	


			
#print degree(readEdgeList('Edge_List_1.csv'), "out")


def combineEdgelists(edgeList1, edgeList2):
	# Takes two data frames as arguments and combines them into into
	# one long edge list. Returned data frame has no duplicate rows.

	combined_edgeList = pd.concat([edgeList1, edgeList2])
	clean_edgeList = combined_edgeList.drop_duplicates()

	return clean_edgeList

#print combineEdgelists(readEdgeList('Edge_List_1.csv'), readEdgeList('Edge_List_2.csv'))	


def pandasToNetworkX(edgeList):
	# Creates a NetworkX Digraph from an edge list in a pandas data frame.

	G = nx.DiGraph()
	EdgeList = readEdgeList(edgeList)
	for Artist, Related_Artist in EdgeList.to_records(index=False):
 		G.add_edge(Artist, Related_Artist)

		#circularLayout = nx.layout.circular_layout(G)
		#nx.draw(G, pos=circularLayout, with_labels=False)
		nx.draw(G, with_labels=False)
	#plt.show() # display
	return G

#pandasToNetworkX('Edge_List_1.csv')	


def randomCentralNode(inputDiGraph):
	# Takes a Networkx DiGraph and returns a single node from the network.
	#pass in entire DiGraph and returns a dictionary mapping nodes to
	#eigenvector centrality.
	eigen_dict = nx.eigenvector_centrality(inputDiGraph)
	normalized_eigen_dict = {}
	value_sum = 0

	for node in eigen_dict:
		value_sum += eigen_dict[node]

	for node in eigen_dict:
		normalized_eigen_dict[node] = eigen_dict[node]/value_sum

	random_node = np.random.choice(normalized_eigen_dict.keys(), p=normalized_eigen_dict.values())
	return random_node

print randomCentralNode(pandasToNetworkX('Edge_List_1.csv'))










