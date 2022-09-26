# Rock, paper, scissors game

import random 

user_wins = 0            # We need two variables, one for the user and one for the computer
computer_wins = 0 
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit. ").lower()
    if user_input == "q":                 
        break               # this will break the while loop if they put in the correct answer and take us to the end of the loop

    if user_input not in options: 
        continue           # this will re ask them to type RPS another time till they put in the correct answer 


    # creating random answer for the computer
    random_number = random.randint(0, 2)        # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]      # random number used as index to pick a quess for the computer in options

    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":   # the rock here wins against the scissors
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1 

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1 

    else:
        print("You lost!")
        computer_wins += 1 

print("You won", user_wins , "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!") 