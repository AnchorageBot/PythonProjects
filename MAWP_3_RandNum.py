# This script will provide an example of how to make a random number generator

# Source code/inspiration/software
    # Math Adventures with Python by Peter Farrell, Chapter 3+
    # Made with Mu 1.0.3 in November 2021

from random import randint
    
def GreetUser():
    """Greet user by name"""
    name = input("What's your name? \n")
    print("\nHello", name)
    
def InviteUser():
    """Invite user to play"""
    invite = input("\nDo you want to guess a number? \n")
    while invite:
        if invite == "yes":
            print ("\nGreat! \n")
            break
        else:
            print("Ok, maybe later \n")
            break
        invite = input("\nDo you want to guess a number? \n")

def GuessCheck():
    """Compare number to guess"""
    number = randint(1,10)    
    guess = int(input("Please enter a number between 1 and 10 \n"))
    while guess:
        if number == guess:
            print("Good guess, that is the number! \n")
            break
        elif number > guess:
            print("Almost, the number is higher \n")
        elif number < guess:
            print("Almost the number is lower \n")
        guess = int(input("Please enter a number between 1 and 10 \n"))
    
def main():
    GreetUser()
    InviteUser()
    GuessCheck()
    
if __name__ == "__main__":                                  
    main()
