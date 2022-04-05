# As a developer, I want to make at least five commits on GitHub with descriptive messages.

# As a user, I want an engaging story to be told using print() statements.

# As a user, I want Hercules (and each enemy), to have health, attack power, and a List of attack names saved in a Dictionary.

# As a user, I want the ability to select Hercules’ attack using a menu prompt.

# As a user, I want the foe’s attack to be chosen at random.

# As a user, I want the results of each attack to be logged in the terminal.

# As a developer, I want to use an Attack() function that will terminate when Hercules or an enemy’s health reaches zero.

# As a developer, I want my RunGame() function to call my other functions in a logical order that will determine game flow.

# As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

# You are Hercules, the greatest of the Greek Heroes! 
# You have been tasked by King Eurystheus to slay the vicious Nemean Lion, 
# defeat the impossible nine-headed Lernaean Hydra, and capture the guard dog of the underworld—Cerberus.

# demigod_name = "Hercules"

# hercules_attacks = 15

# hercules_health = 100

demigod = {"name": "Hercules","attack": 15, "heal": 30, "health": 100}

monster_1 = {"name": "Nemean Lion", "attack": 8, "health": 25}

monster_2 = {"name": "Lernaean hydra", "attack": 10, "health": 35}

monster_3 = {"name": "Cerberus", "attack": 12, "health": 45}

print("Welcome to the greatest story ever told. We have Hercules, the most well known demigod and son of Zeus,") 
print("whose stories is told by his great battles and deeds.") 
print("We will look into some of his amazing feat in interactive story telling")

print("We'll first look into Hercules battle between Nemean Lion, a majestic creature that no man made weapon can kill.")
print("It was Hercules, who drove the beast back into it's liar, stunned the beast with his clubs and defeated the beast with his bare hands.")

battle_1 = True

while battle_1 == True:

    print("You've corner the beast! Please select your action!")
    print("1 = attack")
    print("2 = heal")

    demigod_response = input("Make your choice: ")

    if demigod_response == "1":
        monster_1["health"] = monster_1["health"] - demigod["attack"]
        demigod["health"] = demigod["health"] - monster_1["attack"]
        print("Nemean Lion health is now " ) 
        print(monster_1["health"]) 
        print("Hercules health is now " ) 
        print(demigod["health"])

    elif demigod_response == "2":
        demigod["health"] = demigod["health"] + demigod["heal"]
        demigod["health"] = demigod["health"] - monster_1["attack"]
        print("Nemean Lion health is now " ) 
        print(monster_1["health"]) 
        print("Hercules health is now " ) 
        print(demigod["health"])        

    else:
        print("Please choose only 1 or 2.")


    if monster_1["health"] <= 0 or demigod["health"] <= 0:
        battle_1 = False

print("Next, we face the Lernean Hydra, 9 headed water serpeant. It was Hercules duty to slay this monster.")
print("Let's take a looked into the showdown between the two.")

battle_2 = True

while battle_2 == True:

    print("Please select your action!")
    print("1 = attack")
    print("2 = heal")

    demigod_response = input("Make your choice: ")

    if demigod_response == "1":
        monster_2["health"] = monster_2["health"] - demigod["attack"]
        demigod["health"] = demigod["health"] - monster_2["attack"]
        print("Lernaean hydra health is now " ) 
        print(monster_2["health"]) 
        print("Hercules health is now " ) 
        print(demigod["health"])

    elif demigod_response == "2":
        demigod["health"] = demigod["health"] + demigod["heal"]
        demigod["health"] = demigod["health"] - monster_1["attack"]
        print("Lernaean hydra health is now " ) 
        print(monster_2["health"]) 
        print("Hercules health is now " ) 
        print(demigod["health"])        

    else:
        print("Please choose only 1 or 2.")


    if monster_2["health"] <= 0 or demigod["health"] <= 0:
        battle_2 = False


print("Hercules also have to travel into the underworld who he will face the great gaurdian of the underworld, Cerberus.")

battle_3 = True

while battle_3 == True:

    print("Please select your action!")
    print("1 = attack")
    print("2 = heal")

    demigod_response = input("Make your choice: ")

    if demigod_response == "1":
        monster_3["health"] = monster_3["health"] - demigod["attack"]
        demigod["health"] = demigod["health"] - monster_3["attack"]
        print("Cerberus health is now " ) 
        print(monster_3["health"]) 
        print("Hercules health is now " ) 
        print(demigod["health"])

    elif demigod_response == "2":
        demigod["health"] = demigod["health"] + demigod["heal"]
        demigod["health"] = demigod["health"] - monster_1["attack"]
        print("Cerberus health is now " ) 
        print(monster_2["health"]) 
        print("Hercules health is now " ) 
        print(demigod["health"])        

    else:
        print("Please choose only 1 or 2.")


    if monster_3["health"] <= 0 or demigod["health"] <= 0:
        battle_3 = False