# Define functions needed, add, sub, mul, div 
# Print options to the user 
# Ask for values 
# Call the functions 
# Use a while loop to continue the program until the user wants to exit or stop the program 


def add(a, b):
    answer = a + b 
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")   # changed to string for concantenation or you can use commas print(a, b)
     
def sub(a, b):
    answer = a - b 
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n") 

def mul(a, b):
    answer = a * b 
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a, b):
    answer = a / b 
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")


while True:              # program will not end until the quit method is called

    print("A. Addition")
    print("B. Substraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Input your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        add(a, b) 

    elif choice == "b" or choice == "B":
        print("Substraction")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        sub(a, b) 

    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("Input first number: "))
        b = int(input("Input second number: "))
        mul(a, b)

    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("Input first number: "))
        b = int(input("Input second number: ")) 
        div(a, b) 

    elif choice == "e" or choice == "E":
        print("Program Ended")
        quit() 