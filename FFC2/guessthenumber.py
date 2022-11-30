# In this game the computer has a secret number that we are trying to guess

import random 

def guess(x):
    random_number = random.randint(1, x)        # this will return a random number for us to guess
    guess = 0

    while guess != random_number:               # when the guess is not equal to random number it does all in the block
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')

        elif guess > random_number:
            print('Sorry, guess again. Too high.') 

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')        # once the guess is equal to random number then we break out of the while loop and print the right number


guess(10)