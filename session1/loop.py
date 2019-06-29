# from turtle import *
# shape("turtle")

# forward(90)
# left(90)
# mainloop()
# Từ nay trở đi các bạn chỉ cần from youtube_dl import YoutubeDL thay vì copy code dài dòng từ document
# from youtube_dl import YoutubeDL
# # Option là 1 dicts mở rộng giúp thêm tính năng cho ydl, khi không sử dụng tính năng hãy đễ dicts trống như dưới
# options = {
#     'default_search' : "ytsearch5",
#     "quiet" : True,
#     'outtmpl': '%(id)s', # lấy tên file down về là id của video, lấy id làm tên file để tiện quản lí
#  	'postprocessors': [{
#      'key': 'FFmpegExtractAudio', # Tách lấy audio
#      'preferredcodec': 'mp3', # Format ưu tiên là mp3
#      'preferredquality': '192', # Chất lượng bitrate

# }]}

# ydl = YoutubeDL(options)
# searchSong = input("enter")
# search_results=ydl.extract_info(searchSong, download=False)
# import json
# with open("search.json","w",encoding="utf8") as json_file:
#     json.dump(search_results, json_file)
# videos = search_results["entries"]
# for number,video in enumerate(videos):
#     print(number+1,'.',video["title"]," - ", video["id"],"-",video["uploader"])
# position = int(input("Enter"))

# # download() có thể truyền vào 1 str hoặc 1 list
# ydl.download([videos[position-1]["webpage_url"]])


#     'quiet': True
# }
# ydl = youtube_dl.YoutubeDL(ydl_opts) 
# search_results=ydl.extract_info('that girl', download=False)
# import json
# with open("search.json","w",encoding="utf8") as json_file:
#     json.dump(search_results, json_file)
# videos = search_results["entries"]
# for number,video in enumerate(videos):
#     print(number,'.',video["title"]," - ", video["id"],"-",video["uploader"])
    
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(["https://www.youtube.com/watch?v=DyDfgMOUjCI"])
a={"a":2}
print(a.keys())