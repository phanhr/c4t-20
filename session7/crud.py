items = ['music', 'movie', 'food']
add_items = 'dance', 'sing', 'draw'
items.extend(add_items)
print(items)
characters = list(items)
for i, item in enumerate(items):
    if 'e' in list(item) or 'E' in list(item):
        print(item.upper())


