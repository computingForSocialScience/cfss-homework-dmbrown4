import csv
import sys

def readCSV(filename):
    '''Reads the CSV file `filename` and returns a list
    with as many items as the CSV has rows. Each list item 
    is a tuple containing the columns in that row as stings.
    Note that if the CSV has a header, it will be the first
    item in the list.'''
    with open(filename,'r') as f:
        rdr = csv.reader(f)
        lines = list(rdr)
    return(lines)

    #open opens the file in reading mode as 'f'
    #assigning rdr to output of looping over f
    #list returns a list of tuples from rdr


### enter your code below
#print readCSV("permits_hydepark.csv")[0][128]

#print readCSV("permits_hydepark.csv")[0][129]

#'''
#-128 AND 129 are the location of the latitude and longitude
#- used [][] to index first into list and then into the tuple.
#'''

def get_avg_latlng():
	tplelist = readCSV("permits_hydepark.csv")
	lat_sum = 0.
	lng_sum = 0.
	#designated 0 is a float
	for tple in tplelist:
		lat_sum += float(tple[128])
		lng_sum += float(tple[129])
	#need to use float intead of int becasue of the decimals	
	lat_avg = lat_sum/len(tplelist)	
	lng_avg = lng_sum/len(tplelist)
	print "Latituge Average", lat_avg, "Longitude Average", lng_avg

get_avg_latlng()
#need to this at the end to call the function.