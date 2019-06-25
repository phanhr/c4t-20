computer = {
    "HP" : 20,
    "Dell" : 50,
    "Macbook" : 12,
    "Asus" : 30
}
newName = input("enter name: ")
newQuantity = int(input("enter quantity: "))
computer[newName] = newQuantity
computer["Dell"] += 10
computer["Macbook"] = 2
print(computer)