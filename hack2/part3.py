numbers = [5,1,8,92,-1,30]
randomNumber = int(input("Enter a number: "))
if randomNumber in numbers:
    print('Found, position: ',numbers.index(randomNumber))
else:
    print('not found')