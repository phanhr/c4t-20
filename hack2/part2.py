colors = ['blue', 'red', 'green', 'yellow']
for i,color in enumerate(colors):
    print(i+1, '. ', color)
    
position = input("Enter position to delete or name of color: ")
if position.isdigit():
    colors.pop(int(position)-1)
elif position.isalpha():
    colors.remove(position)
print(*colors, sep=', ')