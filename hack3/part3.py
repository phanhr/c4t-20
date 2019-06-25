computer = {
    "HP" : 20,
    "Dell" : 50,
    "Macbook" : 12,
    "Asus" : 30
}
print(computer["Macbook"])
Sum = 0
for eachItem in computer.values():
    Sum = Sum + eachItem
print(Sum)