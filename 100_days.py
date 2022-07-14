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


# Day 4 projects

import random

# Rock, paper, scissors

def play_game():
    print("Welcome to Rock, Paper, Scissors!\n")
    player_choice = input("Choose rock, paper or scissors: ").lower()
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice = "rock"
    elif computer_choice == 2:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"

    print(f"The computer chose {computer_choice}.\n")
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock":
        if computer_choice == "scissors":
            print("You win!")
        else:
            print("You lose!")
    elif player_choice == "paper":
        if computer_choice == "rock":
            print("You win!")
        else:
            print("You lose!")
    elif player_choice == "scissors":
        if computer_choice == "paper":
            print("You win!")
        else:
            print("You lose!")

    print("Do you want to play again? (y/n)\n")
    answer = input().lower()
    if answer == "y":
        play_game()
    else:
        print("Thanks for playing!")
    
play_game()


# Day 5 projects

# Fizzbuzz

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("Fizzbuzz")
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)

# Password Generator 

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ''

for i in range(nr_letters):
    password += random.choice(letters)
for i in range(nr_symbols):
    password += random.choice(symbols)
for i in range(nr_numbers):
    password += random.choice(numbers)

print(f"Your new password is: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

print(f"Your new randomised password is: {''.join(random.sample(password, len(password)))}")

# Day 6 projects

# No projects, use of Reeborg's World for this day

# Day 7 projects

# Hangman Game

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Example word_list
word_list = ['aardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)
display = []
for n in range(len(chosen_word)):
    display.append('_')

lives = 6
end_of_game = False
guesses = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guesses:
        print(f"\nYou already guessed the letter {guess}!\n\")
    else:
        guesses.append(guess)

        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = guess

        if guess not in chosen_word:
            print(f"\nThe letter {guess} is not in the word!\n")
            lives -= 1
            if lives == 0:
                print("You lose!")
                end_of_game = True
            else:
                print(f"You have {lives} lives remaining.")

        if '_' not in display:
            print("You win!")
            end_of_game = True

    print(stages[lives])
    print(display)

# Day 8 projects








