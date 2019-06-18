hobbies = []
things = input("Nhap vao nhung thu ban thich, cach nhau bang dau ',': ")
splitt = things.split(', ')
hobbies.extend(splitt)
for hobby in hobbies:
    print(hobby)