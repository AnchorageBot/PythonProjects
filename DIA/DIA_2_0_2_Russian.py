# This script will explore the russian peasant multiplication algorithm
    # It accomplishes multiplication by halving, doubling, and addition
    # It explores the concept of binary expansion

# References
  # Dive into Algorithms, https://nostarch.com/Dive-Into-Algorithms

# Software
  # Atom, https://atom.io
  # Python, https://www.python.org/downloads/
  # Math, https://docs.python.org/3/library/math.html
  # Pandas, https://pandas.pydata.org

# How to run the script
    # Save file as RP_2_1.py on the desktop
    # Open terminal
    # cd desktop
    # python3 RP_2_0_2.py

import math
import pandas as pd

def input_one():
    """asks user to provide a number"""
    #print("This script will multiply two numbers that you provide")
    n1 = int(input("What is the number that you would like to halve?  "))
    return n1

def halving(grabVariable_n1):
    """takes input from input_one function and halves it while ignoring remainder"""
    var_n1 = [grabVariable_n1]
    print(math.floor(var_n1[0]/2))

def main():
    query_one = input_one()
    halving(query_one)

if __name__ == '__main__':
    """ensures that the called functions are executed only when the script is run"""
    main()
