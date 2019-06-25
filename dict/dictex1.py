avengers = {
    "Name" : "End game",
    "Release" : 2019,
    "Discription" : "next chapter of Infinity War"
}
avengers["characters"]=input("Enter characters of End Game: ")
avengers["ost"]=input("Enter ost of End Game: ")
print(avengers)
delete = input("Enter what to delete: ")
del avengers[delete]
print(avengers)