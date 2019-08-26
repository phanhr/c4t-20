from __future__ import unicode_literals
import youtube_dl
from pygame import mixer # Load the required library
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
	

check = True
while check:
    choice = input('''pick one of these options:
    1. Show all songs
    2. Show detail of a song
    3. Play a song
    4. Search and download songs
    5. Exit
    Enter: ''')

    if choice == "1":
        import json
        with open("songList.json", 'r+', encoding='utf8') as json_file:
            data = json.load(json_file)
        if len(data)==0:
            print("Song list is empty")
        else:
            for k,v in enumerate(data):
                for value in data[k].keys():
                    print(k+1,'.',value)
    elif choice == "2":
        ydl_opts = {
            'default_search' : "ytsearch5",
            'quiet' : True
        }
        ydl = youtube_dl.YoutubeDL(ydl_opts) 
        songSearch = input("Enter name of song: ")
        search_results = ydl.extract_info(songSearch, download=False)
        import json
        with open('seach.json','w',encoding='utf8') as json_file:
            json.dump(search_results,json_file)
        videos = search_results["entries"]
        for position,video in enumerate(videos):
            print(position+1,'.', video["title"],'-',video["id"],'-',video["uploader"])
        videoChoice = int(input("enter choice position: "))
        if videos[videoChoice-1]["webpage_url"]==search_results["webpage_url"]:
            showUp = {
            "ID": search_results["id"],
            "TITLE" : search_results["title"],
            "CREATOR" : search_results["creator"],
            "DURATION": search_results["duration"]
        }
        else:
            info = ydl.extract_info(videos[videoChoice-1]["webpage_url"], download=False)

            import json
            with open('info.json', 'w',encoding="utf8") as json_file:
                json.dump(info, json_file)
            showUp = {
                "ID": info["id"],
                "TITLE" : info["title"],
                "CREATOR" : info["creator"],
                "DURATION": info["duration"]
            }
        for k,v in showUp.items():
            print(k,'-',v)
        

    elif choice == "3":
        import json
        with open("songList.json", 'r+', encoding='utf8') as json_file:
            data = json.load(json_file)
        if len(data)==0:
            print("Song list is empty")
        else:
            for k,v in enumerate(data):
                for key in data[k].keys():
                    print(k+1,'.',key)
        name = input("Enter song's position: ")
        fileName = list(data[int(name)-1].values())[0]
        mixer.init(44100,-16, 300, 1024)
        mixer.music.load(fileName)
        mixer.music.play()
        while True:
            key = input("pause, continue or stop?")
            if key == "pause":
                mixer.music.pause()
            elif key == "continue":
                mixer.music.unpause()
            elif key == "stop":
                mixer.music.stop()
                break
    elif choice == "4": 
        ydl_opts = {
            'default_search': 'ytsearch5',
            'quiet': True,
            'outtmpl': '%(id)s', # lấy tên file down về là id của video, lấy id làm tên file để tiện quản lí
        'postprocessors': [{
        'key': 'FFmpegExtractAudio', # Tách lấy audio
        'preferredcodec': 'mp3', # Format ưu tiên là mp3
        'preferredquality': '192', # Chất lượng bitrate

    }]
        }
        ydl = youtube_dl.YoutubeDL(ydl_opts)
        songSearch = input("enter name of song: ")
        search_results=ydl.extract_info(songSearch, download=False)
        import json
        with open("search.json","w",encoding="utf8") as json_file:
            json.dump(search_results, json_file)
        videos = search_results["entries"]
        for position,video in enumerate(videos):
            print(position+1,'.',video["title"]," - ", video["id"],"-",video["uploader"])
        videoChoice = int(input("Enter choice position: "))
        search_results = ydl.extract_info(videos[videoChoice-1]["webpage_url"])
        import json
        with open("musicInfo.json", 'w', encoding='utf8') as json_file:
            json.dump(search_results,json_file)
        import json
        with open("songList.json", 'r+', encoding='utf8') as json_file:
            data = json.load(json_file)
            person={}
            person[search_results["title"]]=videos[videoChoice-1]["id"]+".mp3"
            data.append(person)
            json_file.seek(0)
            json.dump(data,json_file)
        print("done")

    elif choice == "5":
        key = input("Press any key to exit: ")
        check = False
