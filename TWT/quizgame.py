# We ask the user a bunch of questions 
# If they answer the questions correctly we add one to their score 
# At the end of the questions we print out what they got out of the questions 

print("Welcome to my computer quiz!") 

playing = input('Do you wish to play my game? ') 

if playing.lower() != "yes":      # .lower is to convert whatever text inputted to lowercase. Likewise with .upper
    quit()                          # this function terminates the program 

print("Okay! Let's play :)") 
score = 0       # This will help us keep track of how many correct answers there are 

answer = input("What does CPU stand for? ").lower() 

if answer == "central processing unit":
    print('Correct!') 
    score += 1     # This says when the user gets the question right the score adds 1

else:
    print("Incorrect!")


answer = input("What does GPU stand for? ").lower() 

if answer == "graphics processing unit":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")


answer = input("What does RAM stand for? ").lower()

if answer == "random access memory":
    print("Correct!")
    score += 1

else:
    print("Incorrect!") 


answer = input("What does PSU stand for? ").lower()

if answer == "power supply":
    print("Correct!")
    score += 1

else:
    print("Incorrect!") 


print("You got " + str(score) + " questions correct!")
print("You gut " + str((score/4) * 100) + "%")   # converting the score to percentage 
