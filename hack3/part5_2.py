computer = {
    "HP" : 20,
    "Dell" : 50,
    "Macbook" : 12,
    "Asus" : 30
}
computer["Toshiba"] = 10
for k,v in computer.items():
    print(k, ':', v)
computer["Fujitsu"] = 15
computer["Alienware"] = 5
Sum = 0
for eachItem in computer.values():
    Sum = Sum + eachItem
print(Sum)
buy = input("Enter computer's name and quantity, seperated by ':' : ")
print(buy.split(":"))
print("left: ", Sum - int(buy.split[2]))