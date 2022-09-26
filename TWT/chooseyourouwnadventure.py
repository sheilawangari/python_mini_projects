# You can customize this project how you like
# This is a game where we ask the user a bunch of different questions 
# It's like a treasure island kind of adventure 
# If you go either directin, or choose either options there are different questions for you

name = input("Type your name: ")
print("Welcome", name, "to this adventure!") 

answer = input("You have come to a dirty road, you can only go left or right, which way will you go? ").lower()

if answer == "left":      # if user picks left, ask a different question
    answer = input("You have come to a river. You can either walk around or swim. ")

    if answer == "swim":
        print("You were eaten by a crocodile. ")

    elif answer == "walk":
        print("You walked and walked and ran out of water, hence lost the game. ")

    else:
        print("Not a valid option. You lose.")

elif answer == "right":    # if user chooses right, then ask a different question
    answer = input("You've come to a wobbly bridge, do you want to cross it or head back? (cross/back) ")

    if answer == "back":
        print("You go back and lose. ") 

    elif answer == "cross":
        answer = input("You meet a stranger. Do you want to talk to them? (yes/no) ").lower()

        if answer == "yes":
            print("You talk to the stranger, they give you gold. You win!")

        elif answer == "no":
            print("The stranger gets offended and you lose.")

        else:
            print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')  

print("Thank you for trying", name)