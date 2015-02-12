import sys
from fetchArtist import fetchArtistId, fetchArtistInfo
from fetchAlbums import fetchAlbumIds, fetchAlbumInfo
from csvUtils import writeArtistsTable, writeAlbumsTable
from barChart import plotBarChart

if __name__ == '__main__':
    artist_names = sys.argv[1:]
    print "input artists are ", artist_names
    # YOUR CODE HERE
    album_info_list = []
    artist_info_list = []
    for artist in artist_names:
    	artist_id = fetchArtistId(artist)
    	album_info_list.append(fetchAlbumInfo(fetchAlbumIds(fetchArtistId(artist))[0]))
    	artist_info_list.append(fetchArtistInfo(fetchArtistId(artist)))
    writeArtistsTable(artist_info_list)
    writeAlbumsTable(album_info_list)
    plotBarChart()
