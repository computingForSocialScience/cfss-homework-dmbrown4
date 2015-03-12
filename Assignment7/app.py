from flask import Flask, render_template, request, redirect, url_for
import pymysql

import MySQLdb
import unicodecsv
import datetime

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


dbname="playlists"
host="localhost"
user="root"
passwd=""
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')

app = Flask(__name__)


@app.route('/')
def make_index_resp():
    # this function just renders templates/index.html when
    # someone goes to http://127.0.0.1:5000/
    return(render_template('index.html'))


@app.route('/playlists/')
def make_playlists_resp():
    cur = db.cursor()
    cur.execute("""SELECT * FROM playlists;""")
    playlists=cur.fetchall()
    return render_template('playlists.html',playlists=playlists)


@app.route('/playlist/<listId>')
def make_playlist_resp(listId):
    cur = db.cursor()
    sql = """SELECT songOrder, artistName, albumName, trackName FROM songs 
        WHERE playlistId=%s ORDER BY songOrder;"""
    cur.execute(sql, listId)
    songs=cur.fetchall()
    return render_template('playlist.html',songs=songs)


@app.route('/addPlaylist/',methods=['GET','POST'])
def add_playlist():
    if request.method == 'GET':
        # This code executes when someone visits the page.
        return(render_template('addPlaylist.html'))
    elif request.method == 'POST':
        # this code executes when someone fills out the form
        artistName = request.form['artistName']
        # YOUR CODE HERE
        return(redirect("/playlists/"))








def createNewPlaylist(artist):
    writeEdgeList(fetchArtistId(artist), 2, 'edgeList.csv')
    master_DF_edgeList = readEdgeList('edgeList.csv')

# for i in sys.argv[2:]:
#     writeEdgeList(fetchArtistId(i), 2, 'edgeList.csv')
#     DF_edgeList = readEdgeList('edgeList.csv')
#     master_DF_edgeList = combineEdgeLists(master_DF_edgeList, DF_edgeList)


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

    #create tables within playlists database
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS playlists 
        (id INTEGER PRIMARY KEY AUTO_INCREMENT, rootArtist VARCHAR (128)) 
        ENGINE=MyISAM DEFAULT CHARSET=utf8;""")
    cur.execute("""CREATE TABLE IF NOT EXISTS songs 
        (id INTEGER PRIMARY KEY AUTO_INCREMENT, playlistId INTEGER, 
            songOrder INTEGER, artistName VARCHAR (128), albumName VARCHAR (128), 
            trackName VARCHAR (128)) ENGINE=MyISAM DEFAULT CHARSET=utf8;""")
    query = """INSERT INTO playlists (rootArtist) VALUES (%s)"""
    cur.execute(query,artist)
    #calling the last id to use later
    lastID = cur.lastrowid

    #opening csv made with random_node information
    f = open('playlist.csv')
    csv = unicodecsv.reader(f)
    header = True
    #setting song order count to 1
    songOrder=1
    #looping through csv file and creating a tuple for each row
    for i in csv:
        #print i
        i_tuple = (i[0], i[1], i[2])
        if header:
            header=False
            continue
        playlistId = lastID
        sql = """INSERT INTO songs (playlistId, songOrder, artistName, albumName, trackName)
         VALUES (%s, %s, %s, %s, %s)""" 
        cur.execute(sql, (playlistId, songOrder)+i_tuple)
        songOrder +=1
        
#createNewPlaylist("REO Speedwagon") 
#createNewPlaylist("Def Leppard")       


if __name__ == '__main__':
    app.debug=True
    app.run()   





