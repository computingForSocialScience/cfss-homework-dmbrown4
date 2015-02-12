#Importing unicosecsv and matplotlib.pyplot as csv and plt
import unicodecsv as csv
import matplotlib.pyplot as plt

def getBarChartData():
    f_artists = open('artists.csv')
    f_albums = open('albums.csv')
    #Opening two csv files as f_artists and f_albums

    artists_rows = csv.reader(f_artists)
    albums_rows = csv.reader(f_albums)
    #This reads over the csv files and assigning information to the 
        #variables artists_rows and album_rows

    artists_header = artists_rows.next()
    albums_header = albums_rows.next()
    #.next() is an interator method that is pulling the next item in the files artists_rows and
        #albums_rows and assigning them to variables

    artist_names = []
    #Creating an empty dictionary
    
    decades = range(1900,2020, 10)
    #Generating a list of numbers from 1900-2020 for intervals of 10 representing decades
    decade_dict = {}
    #Creating an empty dictionary
    for decade in decades:
        decade_dict[decade] = 0
    #Assigning the key 'decade' in decade_dictionary to the value 0 using a for loop.

    for artist_row in artists_rows:
        if not artist_row:
            continue
        artist_id,name,followers, popularity = artist_row
        artist_names.append(name)
    #This generates a list of artist names by looping over artist_rows and adding the name
        #information from artist_row (which has been  assigned to the artist_id, name, followers, 
        #and popularity information from artist_rows).     

    for album_row  in albums_rows:
        if not album_row:
            continue
        artist_id, album_id, album_name, year, popularity = album_row
        for decade in decades:
            if (int(year) >= int(decade)) and (int(year) < (int(decade) + 10)):
                decade_dict[decade] += 1
                break
    #This keeps a count of the number of albums that were released in each decade within the 
        #decade_dict dictionary by looping the year information in album_rows (which was assigned
        #the variable album_row) and determining which decade that year falls into. This is done
        #with a for loop. The for loop loops through the decades list and asks if
        #the integer value of the album year is greater than or equal to the integer value of
        #a decade item from the list and less than that decade value plus 10 years. If so, then 1
        #is added to the value corresponding to that decade item in the decade_dict dictionary.      

    x_values = decades
    #Creating a list called x_values that contains the information from the list decades.
    y_values = [decade_dict[d] for d in decades]
    #Creating a list called y_values that cotains the the values from decade_dict that 
        #correpsond to the items from the decades list.
    return x_values, y_values, artist_names
    #Returns the lists x_values, y_values, and artist_names.

def plotBarChart():
    x_vals, y_vals, artist_names = getBarChartData()
    #Calls the function getBarChartData from above and assigns the three returned lists from this
        #function equal to the variables x_vals, y_vals, and artist_names.
    
    fig , ax = plt.subplots(1,1)
    ax.bar(x_vals, y_vals, width=10)
    #Sets the x and y axis data equal to x_vals and y_vals an sets the width of the 
        #bars equal to 10.
    ax.set_xlabel('decades')
    #x-axis label  = decades
    ax.set_ylabel('number of albums')
    #y-axis label = number of albums
    ax.set_title('Totals for ' + ', '.join(artist_names))
    #title = 'Totals for ________' where the artist names fill in the blank
    plt.show()
    #plot the bar chart

if __name__ == '__main__':
    getBarChartData()
    plotBarChart()

    
