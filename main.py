#This is a python comment

name = input("What is your name? \n")

print("Hello", name)

print("Press Y for yes or N for no")

answer = input("Would you like to play a guessing game?")

if answer == "Y" or "y" or "Yes" or "yes":
    print("Lets play")
else:
    exit()