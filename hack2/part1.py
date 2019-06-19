color = ['blue', 'red', 'teal', 'green']
print(*color, sep=', ')
addColor = input('Add color: ')
color.append(addColor)
print(*color, sep=', ')