import random

destinations_list = ["Las Vegas", "Miami", "New York", "Orlando", "Atlanta", "San Francisco"]

mode_of_transportation = ["Uber", "Car rentals", "Bus", "Bike rentals"]

restaurants = ["Mon Ami Gabi", "Buffet at Bellagio", "Gordon Ramsey Burger", "Buffet at Wynn", "Carson Kitchen", "Yardbird"]

entertainments = ["Grand Canyon", "Vegas Helicopter", "Hoover Dam", "ATV Tours", "Magic show"]

print("Welcome to the day trip generator. If you're unsure to what you want to do for your vacation, we can create one for you.")

valid_response = False

while valid_response == False:

    destination = random.choice(destinations_list)

    print("We have selected " + destination + "!")

    d_cont = input("Does this sound good? Enter y/n: ")
    
    if d_cont == "y":
        print("Great! Let's continue!")
        valid_response = True
    elif d_cont == "n":
        print("I'll try again!")
    else:
        print("Wrong response.")

    t_response = False

while t_response == False:

    transportation = random.choice(mode_of_transportation)

    print("We have seleted mode of transportation of " + transportation + "!")

    t_cont = input("Do you like this method? Enter y/n: ")

    if t_cont == "y":
        print("Great! Let's continue!")
        t_response = True
    elif t_cont == "n":
        print("I'll try again!")
    else:
        print("Wrong response.")


r_response = False

while r_response == False:

    restaurant = random.choice(restaurants)

    print("We have select the " + restaurant + " for you.")

    r_cont = input("Is this a good place to eat for you? Enter y/n: ")

    if r_cont == "y":
        print("Great! Let's continue!")
        r_response = True
    elif r_cont == "n":
        print("I'll try again!")
    else:
        print("Wrong response.")

e_response = False

while e_response == False:

    entertainment = random.choice(entertainments)

    print("We have selected " + entertainment + " for your entertainment.")

    e_cont = input("Are you satified with this choice? Enter y/n")

    if e_cont == "y":
        print("Awesome! Let's review everything.")
        e_response = True
    elif e_cont == "n":
        print("I'll try again!")
    else:
        print("Wrong response.")

print("You will be heading to " + destination + " to enjoy your day at " + entertainment + " by " + transportation + ", and will have a nice diner at the " + restaurant + ".")

