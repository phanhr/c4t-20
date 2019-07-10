# def hello():
#     print("hi")
#     print("world")
# hello()
songList = {
    "Beautiful Pain - Eminem, Ed Sheeran" : "beautifulpain_eminem.mp3",
    }
import json
with open("songList.json", "w", encoding='utf8') as json_file:
    json.dump(songList,json_file)
print(type(songList.jso))