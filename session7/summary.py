hobbies = []
while True:
    choice = input('choose 1 from C,U,R,D: ' )
    if choice == 'c':
        like = input('what do you like: ')
        hobbies.append(like)
    elif choice == 'r':
        for i, hobbie in enumerate(hobbies):
            if len(hobbies)==0:
                print('danh sach rong')
            else:
                print(i, '. ',hobbie)
    elif choice == 'u':
        position = int(input('update at: '))
        change = input('enter change: ')
        hobbies[position] = change
    elif choice == 'd':
        position = int(input('Delete at: '))
        hobbies.pop(position)
        
