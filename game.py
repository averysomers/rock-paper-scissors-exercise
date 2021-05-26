
# game.py

player_name = input("Please enter your name: ")

print("Ready, "+player_name+"?")

print("Rock, Paper, Scissors, Shoot!")

from hashlib import scrypt
import random

user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")

print("USER CHOICE: '"+user_choice+"'")

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID. KEEP GOING")
else:
    print("OOPS, invalid input. Please try again.")
    exit()

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
valid_options = [ROCK, PAPER, SCISSORS]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOICE: "+computer_choice)


if (user_choice == ROCK):
    if (computer_choice == SCISSORS):
        print(ROCK+" beats "+SCISSORS)
        print("Congrats, " +player_name+"! You win.")
    if (computer_choice == ROCK):
        print("Tie")
    if (computer_choice == PAPER):
        print(PAPER +" beats " +ROCK)
        print("Sorry, " +player_name+". You lose.")

if (user_choice == SCISSORS):
    if (computer_choice == SCISSORS):
        print("Tie")
    if (computer_choice == ROCK):
        print(ROCK +" beats " +SCISSORS)
        print("Sorry, " +player_name+". You lose.")
    if (computer_choice == PAPER):
        print(SCISSORS +" beats " +PAPER)
        print("Congrats, " +player_name+"! You win.")

if (user_choice == PAPER):
    if (computer_choice == SCISSORS):
        print(SCISSORS+" beats "+PAPER)
        print("Sorry, " +player_name+". You lose.")
    if (computer_choice == ROCK):
        print(PAPER +" beats " +ROCK)
        print("Congrats, " +player_name+"! You win.")
    if (computer_choice == PAPER):
        print("Tie")

print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN.")