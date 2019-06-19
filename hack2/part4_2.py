givenNumbers = input("Enter a list of numbers, seperated by ',': ")
numbers = givenNumbers.split(',')
for i in numbers:
    if int(i)%2==0:
        print(i)