highScores=[45, 67, 56, 78, 90]
newScore = int(input("Enter your new score: "))
highScores.append(newScore)
highScores.sort(reverse = True)
for position, highScore in enumerate(highScores):
    if position<5:
        print(position +1,'. ', highScore)
