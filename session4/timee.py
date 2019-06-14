from datetime import datetime
hour=int(input("Enter hour: "))
minute=int(input("Enter minute: "))
while True:
    h=datetime.now().hour
    m=datetime.now().minute
    if hour == h and minute == m:
        break
print("wa")
