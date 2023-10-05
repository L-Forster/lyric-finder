from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from time import sleep
import random

"""
Get Lyrics from webpage
"""
name = "The Wicker Man"
name_format = name
#name = str(input("Enter Song Name: "))
name = name.replace(" ","")
name = name.lower()


artist = "Iron Maiden"
artist_format = artist
#artist = str(input("Enter Artist: "))
artist = artist.replace(" ","")
artist = artist.lower()


##Finding the artist##
artist_url = "https://www.azlyrics.com/i/" + artist + ".html"
#artist_page = urlopen(artist_url)
 

#artist_start = artist_data.find(' start of song list ') 
#artist_end = artist_data.find(" end of song list ")
r = requests.get(artist_url)
soup = BeautifulSoup(r.content, "html.parser")

i=0
songs = []
for link in soup.find_all('a', href=True):
    try:
        temp = str(link['href'])
        print("TEMP ",temp[2])
        if temp[1] ==  "l":
            songs.append(temp)
            print("Appending..")
    except:
        pass
    i+=1
print(songs)
# creating txt files


count = 0
for i in range(0,len(songs)):
    count += 1
    song = songs[i]
    url = "https://www.azlyrics.com/" + song
#    print("Removing HTML",url)
#    url = url + artist + "/" + name + ".html"
#    print("Adding Name",url)
    size = len(song)
    file = open(r"INSERT LOCATION"+song[:size-5]+".txt", "w")
    
    
    
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    start_index = html.find("<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->")
    end_index = html.find("<!-- MxM banner -->")
    lyric_data = html[start_index+135:end_index-22]
    
    lyric_data = lyric_data.replace("<br>","\n")
    file.write(lyric_data)
    file.close()
#    print(name_format + "\n")
#    print(artist_format + "\n" + "\n")
    print(lyric_data)
    if count%20 == 0:
        sleep(5)
    rest = random.randint(0,20)
    rest = rest   
    sleep(rest)
    
