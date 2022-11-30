# In this game we are the ones with a secret number and we get the computer to try and guess the number 

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


def computer_guess(x):
    low = 1
    high =  x
    feedback = ''

    while feedback != 'c':          # c for correct
        if low != high:
            guess = random.randint(low, high)

        else:
            guess = low         # could also be high because low = high

        
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1        # if guess is equals to 8 for example then it will have to be - 1 because it cant be 8
        
        elif feedback == 'l':
            low = guess + 1         # + 1 cause it cant be the lowest number 

    print(f'Yay! The computer guessed your number, {guess}, correctly!')

computer_guess(10)