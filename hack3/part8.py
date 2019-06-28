from random import uniform
#character
adventure ={
    "name" : "Light",
    "age" : 17,
    "strength" : 8,
    "defense" : 10,
    "Hp" : 100,
    "backpack" : ["shield", "bread loaf"],
    "gold" : 100,
    "level" : 2
}
adventure["gold"] +=50
adventure["backpack"].append("flintstone")
adventure["pocket"]=["monsterdex", "flashlight"]
print(adventure)

#skill
skill1 = {
    "name" : "tackle",
    "minimum level" : 1,
    "damage" : 5,
    "hit rate" : 0.3
}

skill2 = {
    "name" : "quick attack",
    "minimum level" : 2,
    "damage" : 3,
    "hit rate" : 0.5
}

skill3 = {
    "name" : "strong kick",
    "minimum level" : 4,
    "damage" : 9,
    "hit rate" : 0.2
}

skill = [skill1, skill2, skill3]

#combat

for position, name in enumerate(skill):
    print(position+1, '.' ,skill[position]["name"])
while True:
    choice = int(input("enter skill's number: "))
    if adventure["level"] >= skill[choice-1]["minimum level"]:
        randomHit = uniform(0,1)
        print(randomHit)
        if randomHit < skill[choice-1]["hit rate"]:
            print("Damage: ", skill[choice-1]["damage"])
        else:
            print("skill not in target")
    else:
        print("level not enough")
        break