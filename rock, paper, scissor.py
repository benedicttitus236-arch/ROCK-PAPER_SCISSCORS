import random

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

emojis = {"ROCK" : "🛘", "PAPER" : "🧻", "SCISSORS" : "✂️"}
choices = tuple(emojis.keys())
choices = ("ROCK", "PAPER", "SCISSORS")

def get_user_choice():
    while True:
        user_choice = input("Rock, Paper, or Scissors? (R/P/S):").upper()
        if user_choice in choices:
            return user_choice
        else:
            print("INVALID CHOICE") 

def display_choices(user_choice, computer_choice):
    print(f"User chose {emojis[user_choice]}")
    print(f"Computer Chose {emojis[computer_choice]}")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
            print("TIE")
    elif (
    (user_choice == "ROCK" and computer_choice == "SCISSORS") or \
    (user_choice == "SCISSORS" and computer_choice == "PAPER") or \
    (user_choice == "PAPER" and computer_choice == "ROCK")):
        print("USER WIN")
    else:
        print("USER LOSE")

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        display_choices(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)

        should_continue = input("Do_you_wanna_continue ? (Y/N): ").upper()
        if should_continue == "N":
            break

play_game()