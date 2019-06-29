# from pyglet.media import Source, Player, load

# player = Player()
# source = load('crowd-cheering.mp3')
# player.queue(source)
# player.play()
# while True:
#   input('Press any key to exit')
#   break

from youtube_dl import YoutubeDL

options = {
    'default_search': 'ytsearch5'
}

ydl = YoutubeDL(options)
search_result = ydl.extract_info('that girl', False)
print(search_result)