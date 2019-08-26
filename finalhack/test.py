# download music in video type
from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(["https://www.youtube.com/watch?v=DyDfgMOUjCI"])
# import requests
# r = requests.get('https://jsonplaceholder.typicode.com/users', auth=('user', 'pass'))
# listUser = r.json()
# name = input("username: ")
# for user in listUser:
#     if user["username"].lower() == name.lower() :
#         print(user["address"])
