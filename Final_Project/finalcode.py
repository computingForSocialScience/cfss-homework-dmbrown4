from flask import Flask, render_template, request, redirect, url_for
import pymysql

import MySQLdb
import unicodecsv
import datetime

import sys
import requests
import csv
import pandas as pd
import networkx as nx
import numpy as np
import io

from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__)

dbname="gazetteer"
host="localhost"
user="root"
passwd=""
db=pymysql.connect(db=dbname, host=host, user=user, passwd=passwd)
#db=pymysql.connect(db=dbname, host=host, user=user, passwd=passwd, charset="utf8")

@app.route('/')
def make_index_resp():
    # this function just renders templates/index.html when
    # someone goes to http://127.0.0.1:5000/
    return(render_template('index.html'))



GoogleMaps(app)

@app.route('/sitemap/')
def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=34.3436733,
        lng=62.2023147,
        markers=[(34.3436733,62.2023147)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=34.3436733,
        lng=62.2023147,
        markers={'http://maps.google.com/mapfiles/ms/icons/green-dot.png':[(34.3436733,62.2023147)],
                 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png':[(34.3436733,62.2023147)]}
    )
    return render_template('map.html', mymap=mymap, sndmap=sndmap)



@app.route('/archsites/')
def make_archsite_resp():
    cur = db.cursor()
    cur.execute("""SELECT id, siteName FROM heratsites;""")
    heratsites=cur.fetchall()
    return render_template('archsites.html',heratsites=heratsites)
# """For this part of my code I was able to render a web page with a list of links
# for each of the artists in my database. However, I have not been able to figure out
# how to link the playlist information to the link itself. Whenever I try to SELECT from
# both the playlists and songs tables I get an error saying that there is too much information
# to unpack. I have fiddled with my code for a while to fix this but cannot find out exactly
# what is triggering this error. I understand that ultimately playlists.html would include
# a line like <li><a href="/playlist/{{playlistId}}">{{ id}}.{{ rootArtist}}</a></li> that
# links to the playlist pages using the playlist.html. However, because I have been
# unable to fix this Unpacking Error I have left the code like this so that the playlist
# links send you to an empty playlist rather than an error page."""    


@app.route('/archsites/<id>')
def make_archsites_resp(id):
    cur = db.cursor()
    sql = """SELECT id, siteName, aoi, aoiSubarea, mineralProximity, roadProximity, threatLevel FROM heratsites 
        WHERE id=%s;"""
    cur.execute(sql, id)
    heratsites=cur.fetchall()
    return render_template('playlist.html',heratsites=heratsites)




'''
def populate_tables():
#populate table in gazetteer database
    cur = db.cursor()
    f = open('Herat_database.csv')
    #opening csv made from archaeological data
    csv = unicodecsv.reader(f)
    header = True
    #looping through csv file and creating a tuple for each row
    for i in csv:
        #print i
        i_tuple = (i[1], i[2], i[3], i[4], i[5], i[6])
        if header:
            header=False
            continue
        sql = """INSERT INTO heratsites (siteName, aoi, aoiSubarea, mineralProximity, roadProximity, threatLevel)
         VALUES (%s, %s, %s, %s, %s, %s)""" 
        cur.execute(sql, i_tuple)
'''        
     

#populate_tables()

if __name__ == '__main__':
    app.debug=True
    app.run()   

