# This script will attempt to combine names from two lists in a funny way

# Source code/inspiration/software
    # Impractical Python Projects by Lee Vaughn, Chapter 1, Example 1, Project 1
    # Made with Mu 1.0.3 in November 2021

# Libraries needed to run this script
import sys                                                      # makes available the color red for output
import random                                                   # helps to pick random items

print("Welcome to the psych 'Sidekick Name Picker'\n")
print("A name just like Sean would pick for Gus:\n\n")

first_name_list = ('Baby Oil', 'Butterbean', 'Cornpop')         # this list of names uses a tuple format
last_name_list = ('Gooberdapple', 'Swackhammer', 'Woolysocks')

while True:
    firstName = random.choice(first_name_list)
    lastName = random.choice(last_name_list)
    
    print("\n\n")
    print("{} {}".format(firstName,lastName),file=sys.stderr)
    print("\n\n")
    
    try_again = input("\n\nTry again? (Press Enter else n to quit)\n")
    if try_again.lower() == "n":
        break
        
input("\nPress Enter to exit")
