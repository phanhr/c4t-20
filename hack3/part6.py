computerPrice = {
    "HP" : 600,
    "Dell" : 650,
    "Macbook" : 12000,
    "Asus" : 400,
    "Acer" : 350,
    "Toshiba" : 600,
    "Fujitsu" : 900,
    "Alienware" : 1000
}

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

totalSum = 0
for key in computer:
    print("Total value of ",key," : ", computer[key]*computerPrice[key])
    totalSum = totalSum + computer[key]*computerPrice[key]
print(totalSum)

