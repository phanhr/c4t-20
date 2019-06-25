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
nameComputer = input("enter desired computer's name: ")
quantity = int(input("Enter desired quantity: "))
print("tong gia tri hoa don: ", computerPrice[nameComputer]*quantity)