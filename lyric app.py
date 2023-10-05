from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from time import sleep
import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


file = open(r"loCATION/ironmaiden/killers.txt", "r")


window = tk.Tk()
window.title("Find Lyrics")
window_width = 600
window_height = 400

# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.resizable(False,False)
# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

data = ["The wicker man", "Iron Maiden"]

def search_clicked():
    global l1
    l1 = [k for k in data if song_search.get() in k]
    try:
        label.after(1000, label.destroy())
    except:
        pass
    label = ttk.Label(text="Song Results:")
    label.pack(fill=tk.X, padx=5, pady=5)
    print(l1)
    # create a combobox
    global selected_song
    selected_song = tk.StringVar()
    song_cb = ttk.Combobox(window, textvariable=selected_song)
    
    # get first 3 letters of every month name
    song_cb['values'] = [l1[m] for m in range(0,len(l1))]
    
    # song_cb typing a value
    song_cb['state'] = 'readonly'
    
    # place the widget
    song_cb.pack(fill=tk.X, padx=5, pady=5)
    song_cb.bind('<<ComboboxSelected>>', song_changed)
    
def song_changed(event):
    """ handle the month changed event """
    showinfo(
        title='Result',
        message=f'You selected {selected_song.get()}!'
    )




song_search = tk.StringVar()

# Sign in frame
search = ttk.Frame(window)
search.pack(padx=10, pady=10, fill='x')


# email
name_label = ttk.Label(search, text="Song Name:")
name_label.pack(fill='x', expand=True)

name_entry = ttk.Entry(search, textvariable=song_search)
name_entry.pack(fill='x', expand=True)
name_entry.focus()


# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


search_button = ttk.Button(search, text="Search", command=search_clicked)
search_button.pack(fill='x', expand=True, pady=10)



window.mainloop()


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
    print("AA")
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

