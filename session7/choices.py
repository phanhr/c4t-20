import random
words = ['burger', 'pizza', 'icecream', 'peanut', 'carrot']
print(*words, sep=', ')
choice = input("enter a word in list: ")
question = list(choice)
random.shuffle(question)
print(*question)
answer = input('Enter your answer: ')
if answer == choice:
    print('right')
else:
    print('wrong')