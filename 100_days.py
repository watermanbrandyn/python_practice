# From 100 Days of Code: The Complete Python Pro Bootcamp for 2022, with Dr. Angela Yu (Udemy)
# Main, or interesting, projects from each day

# Day 1 projects

# Band name generator
print("Welcome to the band name generator!")
city = input("What city did you grow up in?\n")
pet = input("What is your pet's name?\n")
band = city + " " + pet
print(f"Your band name is {band}!")

# Day 2 projects

# Tip calculator
print("Welcome to the tip calculator!\n")

bill = input("What was the total bill?\n")
tip = input("What tip percentage would you like to leave?\n")
party = input("How many people are in your party?\n")

bill = float(bill)
tip = int(tip)
party = int(party)

def tip_calculator(bill, tip, party):
    per_person = (bill / party) * (1 + (tip / 100))
    return per_person

per_person_amount = tip_calculator(bill, tip, party)
# To round to two decimal places and force presentation of both (even if 0 value)
print(f"Each person should pay ${per_person_amount:.2f}.")
    
# Day 3 projects

# Leap year calculator
def is_leap():
    year = int(input("Which year do you want to check? "))
    # Leap year is a year that is divisible by 4, but not by 100 unless it is also divisible by 400
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
            else:
                print("Not leap year.")
        else:
            print("Leap year.")
    else:
        print("Not leap year.")

is_leap()

# Treasure Island
def treasure_island():
    print("Welcome to the treasure island game!\n")
    direction = input("Do you want to go left or right? (left/right)\n").lower()
    if direction == "left":
        river = input("You come to a river, do you swim or walk around it? (swim/walk)\n").lower()
        if river == 'walk':
            door = input("You see a number of hidden doors along the bank, do you choose the red, blue or yellow door? (red/blue/yellow)\n").lower()
            if door == 'yellow':
                print("You found the treasure!")
            else:
                print("You are attacked as soon as you open the door, and die. Game over.")
        else:
            print("You were attacked by a trout while swimming, game is over.")
    else: 
        print("You fell into a hole, apologies game is over.")

treasure_island()


