import json
from youtube_dl import YoutubeDL
from pyglet.media import Source, Player, load
import pyglet

opt = [
    {'1' : 'Show all songs'},
    {'2' : 'Show show detail'},
    {'3' : 'Play a song'},
    {'4' : 'Search and download a song'},
    {'5' : 'Exit'}
]

songList = [] 
dataList = []

while True:
    for i in opt:
        for key, value in i.items():
            print(key, '.', value)
    option = int(input("Your choice: "))

    if option == 1:
        with open('data.json', encoding = 'utf-8') as data:
            song = json.loads(data.read())
        if song == []:
            print("Empty list.")
        else:
            for index, music in enumerate(song):
                print(index + 1, ' - ', music['title'])

    elif option == 2:
        with open('data.json', encoding = 'utf-8') as data:
            song = json.loads(data.read())
        for index, music in enumerate(song):
            print(index + 1, ' - ', music['title'])
        detail = int(input("Index of the song: "))

        found = False
        songFound = {}
        for i in range(len(song)):
            if i == detail - 1:
                found = True
                songFound = song[detail - 1]
        
        if found == True:
            print(songFound['id'], " ", songFound['webpage_url'])
        else:
            print("Not found")

    elif option == 3:
        with open('data.json', encoding = 'utf-8') as data:
            song = json.loads(data.read())
        for index, music in enumerate(song):
            print(index + 1, " - ", music['title'])

        if song == []:
            print("Empty list")
        else:
            play = int(input("Song to play: "))
            mp3File = song[play - 1]['id'] + '.mp3'

            player = Player()
            source = load(mp3File)
            player.queue(source)
            player.play()
            while True:
                interact = (input("play, pause or stop:"))
                if interact == "play":
                    player.play()
                elif interact == "pause":
                    player.pause()
                elif interact == "stop":
                    player.pause()
                    break
    
    elif option == 4:
        with open('data.json', encoding = 'utf-8') as data:
            song = json.loads(data.read())
        
        dataList = song

        search = input("Search song: ")

        optionsExtract = {
            'default_search' : 'ytsearch4'
        }

        ydl = YoutubeDL(optionsExtract)
        searched = ydl.extract_info(search, download = False)
        songList = searched['entries']

        optionsDownload = {
            'outtmpl' : '%(id)s',
            'postprocessors' : [{
                'key' : 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '192'
            }]
        }

        for index, music in enumerate(songList):
            print(index + 1, " - ", music['title'])
        
        download = int(input("Choose the song to down: "))

        ydl1 = YoutubeDL(optionsDownload)
        downloaded = ydl1.extract_info(songList[download - 1]['id'], download = True)

        dataList.append(downloaded)
        with open('data.json', 'w')as data:
            json.dump(dataList, data)
    
    elif option == 5:
        break

