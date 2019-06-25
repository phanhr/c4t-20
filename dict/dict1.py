person ={
    "Name" : "Pham Minh Duc",
    "Age" : 19,
    "From" : "Hanoi"
}
print(person)

#create in dictionary
person["status"] = "single"
print(person)

#delete in dictionary
del person["Age"]
print(person)

#check xem dictionary co khong
if "name" in person:
    print("exist")
else:
    print("not exist")
if "nationality" in person:
    print("exist")
else:
    print("not exist")

#list va dictionary
dict1
dict2
list1 = [dict1, dict2]

#for va dicitonary
for k in person:
    print(k) #in ra key
for k in person:
    print(k, person[k]) #in ra key va value
for v in person.values():
    print(v) #in ra value
for k,v in person.items():
    print(k, v) #in ra key va value