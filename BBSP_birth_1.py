#!/usr/bin/env python3
    # shebang
    # https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take

# This script will examine the birthdy paradox

# References:
    # The Big Book of Small Python Projects, https://nostarch.com/big-book-small-python-projects
    # Wiki, https://en.wikipedia.org/wiki/Birthday_problem
    # Math Module, https://docs.python.org/3/library/math.html
        # be sure to select your python version
    # Matplotlib, https://matplotlib.org

# Software
  # Atom, https://atom.io
  # Python, https://www.python.org/downloads/

# Check python version on Mac
    # Open terminal
    # type python -V

# How to run the script
    # Save file as Birthday_1.py on the desktop
    # Open terminal
    # cd desktop
    # python3 Birthday_1.py

from math import factorial
import matplotlib.pyplot as plt

def input_calc():
    """Asks the user to provide the group size to consider & calcs probability of shared birthdays"""

    while True:  # Keep asking until the user enters a valid amount.
        print("This script will examine how many people in a group of 100 or smaller share a birthday")
        response = input("What is the group size that you would like to consider  ")
        if response.isdecimal() and (0 < int(response) <= 100):
            groupSize = int(response)
            break  # User has entered a valid amount.

    days_per_year = 365
    num_birthdays_no_rep = factorial(days_per_year)/factorial(days_per_year - groupSize)
    #print(num_birthdays_no_rep)

    num_birthdays_with_rep = days_per_year**groupSize
    #print(num_birthdays_with_rep)

    no_repeat_birthdays = num_birthdays_no_rep/num_birthdays_with_rep
    #print(no_repeat_birthdays)

    at_least_two_shared_birth = 1 - no_repeat_birthdays
    print("Probability of at least two shared birthdays:  " + str(at_least_two_shared_birth))

def main():
    input_calc()

if __name__ == '__main__':
    """ensures that the called functions are executed only when the script is run"""
    main()
