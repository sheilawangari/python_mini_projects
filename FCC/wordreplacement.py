# Word replacement program 
# Introduction to replace method in python 
# This program takes a string and replaces some words in that string with another word 

def replace_word ():

    str = "hi guys, I am Sheila, and hi hi hi hi"
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ") 
    
    print(str.replace(word_to_replace, word_replacement)) 

replace_word()