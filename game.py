# game.py

import random

import dotenv
import os
dotenv.load_dotenv() 
from dotenv import load_dotenv # go get the function we need
load_dotenv() # invoke the function
USER_NAME = os.getenv("USER_NAME", default="Player One") 

print("-------------------------------")
print(f"Welcome '{USER_NAME}' to Rock Paper Scissors!")
print("-------------------------------")

# asking user for input
user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")
user_choice = user_choice.lower() # convert to lowercase

# confirm input
options = ["rock", "paper", "scissors"]
if user_choice not in options:
    print("OOPS SOMETHING WENT WRONG. Please try again.")
    exit()
else:
    print(f"You chose: {user_choice}")

# simulate a computer input
import random

computer_choice = random.choice(options)

# confirm computer choice
print(f"The computer chose: {computer_choice}")

# print line
print("-------------------------------")

# determine winner and print message
# adapted from solution shared by Prof Rossetti
if user_choice == "rock":
    if computer_choice == "rock":
        print("Oh, it's a tie.")
    elif computer_choice == "paper":
        print("Oh, the computer won. It's ok.")
    elif computer_choice == "scissors":
        print("Oh, you won! Nice job.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Oh, you won! Nice job.")
    elif computer_choice == "paper":
        print("Oh, it's a tie.")
    elif computer_choice == "scissors":
        print("Oh, the computer won. It's ok.")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("Oh, the computer won. It's ok.")
    elif computer_choice == "paper":
        print("Oh, you won! Nice job.")
    elif computer_choice == "scissors":
        print("Oh, it's a tie.")
else:
    print("OOPS, SOMETHING WENT WRONG. Please try again.")

print("-------------------------------")
print("Thanks for playing. Please play again!")
