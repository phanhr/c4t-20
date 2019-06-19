numbers = input('Enter a list of numbers, seperated by space: ')
print(numbers)
check = numbers.split(' ')
Sum = 0
for i in check:
    Sum = Sum + int(i)
print(Sum)
