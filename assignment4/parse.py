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

#PART 3.1

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


#Part 3.2

#readCSV("permits_hydepark.csv")[0][42]
#index into list , then index into tuple for zip code

def zip_code_barchart():
	tplelist = readCSV("permits_hydepark.csv")
	zip_list = []
	zip_count_dict = {}

	#looping over tplelist and adding zipodes to zip_list
	for tple in tplelist:
		if tple[28] != "":
			zip_list.append(int(tple[28][0:5]))
			#adding zipcode form tuple
			#[0:5] only adds the first 5 characters
			#(this makes sure no zipcodes have a "-" in them)
		if tple[35] != "":
			zip_list.append(int(tple[35][0:5]))
		if tple[42] != "":
			zip_list.append(int(tple[42][0:5]))
		if tple[49] != "":
			zip_list.append(int(tple[49][0:5]))
		if tple[56] != "":
			zip_list.append(int(tple[56][0:5]))
		if tple[63] != "":
			zip_list.append(int(tple[63][0:5]))
		if tple[70] != "":
			zip_list.append(int(tple[70][0:5]))
		if tple[77] != "":
			zip_list.append(int(tple[77][0:5]))
		if tple[84] != "":
			zip_list.append(int(tple[84][0:5]))
		if tple[91] != "":
			zip_list.append(int(tple[91][0:5]))
		if tple[98] != "":
			zip_list.append(int(tple[98][0:5]))
		if tple[105] != "":
			zip_list.append(int(tple[105][0:5]))
		if tple[112] != "":
			zip_list.append(int(tple[112][0:5]))
		if tple[119] != "":
			zip_list.append(int(tple[119][0:5]))
		if tple[126] != "":
			zip_list.append(int(tple[126][0:5]))
		
	#make a dictionary of the zipcode counts by looping over zip list
	#key = zipcode (zp)
	#value = zipcode count
	for zp in zip_list:
		zip_count_dict[zp]=0
	for zp in zip_list:
		if zp in zip_count_dict:	
			zip_count_dict[zp] +=1	
	

	#print zip_list
	#print zip_count_dict
	#print zip_count_dict.keys()
	
	zips_in_illinois={}
	for zipcode in zip_count_dict.keys():
		if zipcode>=60000:
			zips_in_illinois[zipcode]=zip_count_dict[zipcode]

	
	#make histogram
	import numpy as np
	import matplotlib.pyplot as plt
	
	N=len(zip_count_dict)
	x = zips_in_illinois.keys()
	y = zips_in_illinois.values()

	width = 0.35

	fig, ax = plt.subplots()
	rects1 = ax.bar(x, y, width, color='b', yerr=y)
	
	ax.set_ylabel('Zip Code Count')
	ax.set_xlabel('Zip Codes')
	ax.set_title('Contractor Zip Codes')

	plt.show()



zip_code_barchart() > Zip_Code_Histogram.jpg


#Questions for Wednesday:
#1. Get matplotlib to work
#2. make sure I understand question 3.3 and how to answer it
#3. make sure I can commit new versions of my hw
		
