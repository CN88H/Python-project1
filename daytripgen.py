import random

destinations_list = ["Las Vegas", "Miami", "New York", "Orlando", "Atlanta", "San Francisco"]

mode_of_transportation = ["Uber", "Car rentals", "Bus", "Bike rentals"]

restaurants = ["Mon Ami Gabi", "Buffet at Bellagio", "Gordon Ramsey Burger", "Buffet at Wynn", "Carson Kitchen", "Yardbird"]

entertainments = ["Grand Canyon", "Vegas Helicopter", "Hoover Dam", "ATV Tours", "Magic show"]

print("Welcome to the day trip generator! If you are having problems deciding where to go, we got you cover.")

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
