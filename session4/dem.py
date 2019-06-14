while True:
    number=input("Enter a number: ")
    if number.isdigit():
        print("Your number has ",len(number)," digits")
        break
    else:
        print("not a number")
