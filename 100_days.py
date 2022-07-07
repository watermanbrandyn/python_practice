# From 100 Days of Code: The Complete Python Pro Bootcamp for 2022, with Dr. Angela Yu
# Main project from each day

# Day 1 project
# Band name generator

print("Welcome to the band name generator!")
city = input("What city did you grow up in?\n")
pet = input("What is your pet's name?\n")
band = city + " " + pet
print(f"Your band name is {band}!")

# Day 2 project
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
    
