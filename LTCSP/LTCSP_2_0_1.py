#!/usr/bin/env python3
    # shebang
    # https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take

# This script will determining whether a phone number belongs to a telemarketer

# References
  # Learn to Code by Solving Problems - Dr. Daniel Zingaro
    # https://nostarch.com/learn-code-solving-problems
  # Stackoverflow
    # https://stackoverflow.com/questions/45437216/how-do-i-generate-a-random-4-digit-number-and-store-it-as-a-variable-in-python
    # https://stackoverflow.com/questions/13905936/converting-integer-to-digit-list

# Software
  # Xcode, https://developer.apple.com/xcode/
  # Python, https://www.python.org/downloads/

# How to run the script
    # Save this file as LTCSP_2_0_1.py on the desktop
    # Open terminal, then type
        # cd desktop
        # python3 LTCSP_2_0_1.py

import random

import string
from random import choice

print('\n')

print('This script will determining whether a phone number belongs to a telemarketer and indicates whether we should answer the phone or ignore it \n')

print('It assumes that all phone numbers are represented as four digits \n')
print('It assumes that all telemarketer numbers end in an 8 or a 9')
print("It assumes that the second and third digits of a telemarketer's number are the same \n")

def randomFourDigitsA():
    """generate random nunber, convert integer to list, check pattern"""
    
    number = random.randint(1000,9999)
    print('Phone number on line one:', number, '\n')
    #print(type(number))
    
    n = list(map(int, str(number)))
    #print(n)
    
    if n[3] == 8 or n[3] == 9 and n[1] == n[2]:
        print('Probably a telemarketer, consider ignoring the call \n')
    else:
        print('Probably ok to answer the call \n')

def randomFourDigitsB():
    """generate random nunber, convert integer to list, check pattern"""
    
    chars = string.digits
    random =  ''.join(choice(chars) for _ in range(4))
    print('Phone number on line two:', random, '\n')
    #print(type(random))
    
    r = list(map(int, str(random)))
    #print(r)
    
    if r[3] == 8 or r[3] == 9 and r[1] == r[2]:
        print('Probably a telemarketer, consider ignoring the call \n')
    else:
        print('Probably ok to answer the call \n')

randomFourDigitsA()
randomFourDigitsB()

print('Consider heading over to the programming judge website at https://dmoj.ca/ and checking your script for accuracy \n')

print('The DMOJ problem number for this script is ccc18j1   \n')
