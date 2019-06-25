whitefang ={
    "name" : "White Fang",
    "Release" : 1906,
    "characters" : ["White Fang", "Weedon Scott", "Kiche"]
}
whitefang["nationality"] = "United States"
whitefang["characters"] = ["White Fang", "Henry", "Collie"]
whitefang["characters"].append("Weedon Scott")
whitefang["characters"].pop(1)
print(whitefang["characters"])
for k, v in whitefang.items():
    print(k, '-', v)

Sum = 0
quiz1 ={
    "question" : "WF was released in?",
    "1" : 1909,
    "2" : 1902,
    "3" : 1906
}
print(quiz1)
answer1 = input("Enter answer:")
if answer1 == "3":
    print("True")
    Sum +=1
else:
    print("False")

quiz2 ={
    "question" : "WF was released in?",
    "1" : "US",
    "2" : "Spain",
    "3" : "UK"
}
print(quiz2)
answer2 = input("Enter answer:")
if answer2 == "1":
    print("True")
    Sum +=1
else:
    print("False")

print("total of true answers: ", Sum)
print("percentage of true answers: ", (Sum/2)*100)