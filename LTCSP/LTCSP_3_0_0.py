#!/usr/bin/env python3
    # shebang
    # https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take

# This script will replicate a shell game

# References
  # Learn to Code by Solving Problems - Dr. Daniel Zingaro
    # https://nostarch.com/learn-code-solving-problems
  # Wikipedia
    # https://en.wikipedia.org/wiki/Shell_game
    # https://en.wikipedia.org/wiki/Soapy_Smith

# Software
  # Xcode, https://developer.apple.com/xcode/
  # Python, https://www.python.org/downloads/

# How to run the script
    # Save this file as LTCSP_3_0_0.py on the desktop
    # Open terminal, then type
        # cd desktop
        # python3 LTCSP_3_0_0.py

import random

#import string
#from random import choice

print('\n')

print('This script will replicate a shell game \n')

print('There are three identical cups placed in a line, openings down ')
print('There is a single ball which is hidden under one cup ')
print('The cups are shuffled so that the location of the hidden ball is uncertain ')
print('Players are asked to guess which cup hides the ball after the shufffle \n')

def playerInputA():
    """Asks for and saves player input as a global variable"""
    print('Please enter a number between 1 and 3, representing one of the three cups \n')
    playerGuessA = int(input())
    #print(type(playerGuessA)) # data type is int
    print('\n You guessed that the ball is hidden in cup ', playerGuessA, '\n')
    
    global gA # gA is now a global variable
    gA = playerGuessA
    #print(type(gA)) # data type is int

def randomShuffleA():
    """Generates a random number between one and three and checks for equality with input"""
    number = random.randint(1,3)
    print('Cup number', number, 'holds the ball \n')
    #print(type(number)) # data type is int
        
    if gA == number:
        print('Good guess ! \n')
    else:
        print('Better luck next time \n')
    
def randomShuffleB():
    """Generates a random number between one and nine ... still needs work"""
    chars = string.digits
    random =  ''.join(choice(chars) for _ in range(1))
    print('Cup number', random, 'holds the ball \n')
    #print(type(random))
    
playerInputA()
randomShuffleA()
#randomShuffleB()

#print('Consider heading over to the programming judge website at https://dmoj.ca/ and checking your script for accuracy \n')

#print('The DMOJ problem number for this script is coci06c5p1')
