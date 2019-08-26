#download info of music video not downloading the video
from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
ydl = youtube_dl.YoutubeDL(ydl_opts) 
list_music = ["https://www.youtube.com/watch?v=DyDfgMOUjCI",'https://www.youtube.com/watch?v=5iSlfF8TQ9k']
list_info = []
for music in list_music:
    info = ydl.extract_info(music, download=False)
    list_info.append(info)

# with open("info.json", 'a',encoding='utf8') as out:
#     out.write(str(list_info))

# from pygame import mixer # Load the required library

# mixer.init()
# mixer.music.load('beautifulpain_eminem.mp3')
# mixer.music.play()

