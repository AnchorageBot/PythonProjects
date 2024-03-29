#!/usr/bin/env python3
    # shebang
    # https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take

# This script will determine the score of a basketball game

# References
  # Learn to Code by Solving Problems - Daniel Zingaro
    # https://nostarch.com/learn-code-solving-problems

# Software
  # Xcode, https://developer.apple.com/xcode/
  # Python, https://www.python.org/downloads/

# How to run the script
    # Save this file as LTCSP_2_0_0.py on the desktop
    # Open terminal, then type
        # cd desktop
        # python3 LTCSP_2_0_0.py

print('\n')

print('This script will determine the score of a basketball game between the Apples and the Bananas \n')

AppleScore = []
BananaScore = []

def userInputsApples():
    """request inputs, sum inputs, update list"""
    
    print('Please enter the number of three point shots that the Apples made: \n')

    AppleThreePointShots = int(input())

    print('Please enter the number of two point shots that the Apples made: \n')

    AppleTwoPointShots = int(input())

    print('Please enter the number of free throw shots that the Apples made: \n')

    AppleFreeThrows = int(input())
    
    finalApple = AppleThreePointShots*3 + AppleTwoPointShots*2 + AppleFreeThrows
    
    AppleScore.append(finalApple)

def userInputsBananas():
    """request inputs, sum inputs, update list"""

    print('Please enter the number of three point shots that the Bananas made: \n')

    BananaThreePointShots = int(input())

    print('Please enter the number of two point shots that the Bananas made: \n')

    BananaTwoPointShots = int(input())

    print('Please enter the number of free throw shots that the Bananas made: \n')

    BananaFreeThrows = int(input())
    
    finalBanana = BananaThreePointShots*3 + BananaTwoPointShots*2 + BananaFreeThrows
    
    BananaScore.append(finalBanana)
 
def gameScore():
    """share data summary, check and classify pattern"""
    
    print('\n The Apples scored ', AppleScore, ' and the Bananas scored ', BananaScore, ' \n')
    
    if AppleScore > BananaScore:
        print('Apples win !\n')
    elif AppleScore < BananaScore:
        print('Bananas win !\n')
    else:
        print('Tie game ! \n')

userInputsApples()
userInputsBananas()
gameScore()

print('Consider heading over to the programming judge website at https://dmoj.ca/ and checking your script for accuracy \n')

print('The DMOJ problem number for this script is ccc19j1  \n')
