# We will generate a random number 
# We will track how many times it takes the user to guess the number 

import random 

top_of_range = input("Type a number: ")

if top_of_range.isdigit():                # If this is a digit then it will be converted into an interger
    top_of_range = int(top_of_range) 

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time. ")
        quit() 

else:
    print("Please type a number next time. ")
    quit()



random_number = random.randrange(top_of_range)     # this will generate to the range the user typed 
guesses = 0


# Now that we have a random number 
# We will keep asking the user to put in guesses until they get it correct 

while True:
    guesses += 1               # whatever code below will be executed while its True and it will stop when you put a break statement
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():                
        user_guess = int(user_guess)     # this will check wether a user's guess is an integer

    else:
        print("Please type a number next time. ")
        continue     # if the user doesnt get the right answer it will continue looping

    if user_guess == random_number:
        print("You got it!")
        break        # you need to stop the while loop so that it stops asking the user to make guesses
    
    elif user_guess > random_number:
            print("You are above the number!")

    else:
        print("You were below the number!")

print("You got in in", guesses, "guesses")      # whenever you use commas, no need to add spaces, its done automatically
