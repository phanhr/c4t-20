import random
word = input('Enter a word: ')
characters = list(word)
random.shuffle(characters)
for i in characters:
    print(i)
