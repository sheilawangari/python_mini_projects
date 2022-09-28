# This is for organizing and storing your passwords, with the username of the accounts 
# Passwords will be encrypted 

from cryptography.fernet import Fernet            # this module will help you incrypt text

# function to load key 

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key() 
fer = Fernet()


# function that can create a key
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) 

write_key()''' 


def view():
    with open('password.txt', 'r') as f:   # we change to read mode because we want to view and not overwrite anything
        for line in f.readlines():
            data = line.rstrip()            # rstrip will strip off the new line character from the file automatically "\n"
            user, passw = data.split("|")   # split is used to separate elements into lists 
            print("User:", user, "| Password:", 
                    fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account name: ")
    pwd = input("Password: ") 
                                                # 'a' is the mode to open the file and its most flexible to use
    with open('password.txt', 'a') as f:       # this will automatically open and close the created file
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")     # encoding password will convert it to bytes


while True:
    mode = input("Would you like to add a new password or view existing ones (view/add)?, press q to quit. ").lower()
    if mode == "q":
        break  

    if mode == "view":
        view()
    
    elif mode == "add":             # We'll create a new file if it doesnt exist and store the passwords into it
        add()

    else:
        print("Invalid mode.")
        continue                     # takes you to beginning of loop
