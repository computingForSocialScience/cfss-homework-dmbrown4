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



#readCSV("permits_hydepark.csv")[0][42]
#index into list , then index into tuple for zip code

def zip_code_barchart():
	tplelist = readCSV("permits_hydepark.csv")
	zip_list = []
	for tple in tplelist:
		if tple[28] != "":
			zip_list.append(tple[28])
		if tple[35] != "":
			zip_list.append(tple[35])
		if tple[42] != "":
			zip_list.append(tple[42])
		if tple[49] != "":
			zip_list.append(tple[49])
		if tple[56] != "":
			zip_list.append(tple[56])
		if tple[63] != "":
			zip_list.append(tple[63])
		if tple[70] != "":
			zip_list.append(tple[70])
		if tple[77] != "":
			zip_list.append(tple[77])
		if tple[84] != "":
			zip_list.append(tple[84])
		if tple[91] != "":
			zip_list.append(tple[91])
		if tple[98] != "":
			zip_list.append(tple[98])
		if tple[105] != "":
			zip_list.append(tple[105])
		if tple[112] != "":
			zip_list.append(tple[112])
		if tple[119] != "":
			zip_list.append(tple[119])
		if tple[126] != "":
			zip_list.append(tple[126])

	print zip_list
	
zip_code_barchart()		
		
