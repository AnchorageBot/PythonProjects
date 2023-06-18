#!/usr/bin/env python3
    # shebang
    # https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take

# This script will calculate the volume of a right circular cone

# References
  # Learn to Code by Solving Problems - Daniel Zingaro
    # https://nostarch.com/learn-code-solving-problems
  # Right Circular Cone
    # https://mathworld.wolfram.com/RightCircularCone.html
    # https://en.wikipedia.org/wiki/Cone
    # https://mathworld.wolfram.com/Cone.html
 
# Software
  # Xcode, https://developer.apple.com/xcode/
  # Python, https://www.python.org/downloads/

# How to run the script
    # Save this file as LTCSP_1_0_1.py on the desktop
    # Open terminal, then type
        # cd desktop
        # python3 LTCSP_1_0_1.py

print('\n')

print('This script will calculate the volume of a right circular cone \n')

print('\n Please enter the distance from the center to the outer edge (radius) of the cone as a whole number (integer) between 1 and 100: \n')

coneRadius = int(input())

print('\n Please enter the height from the base to the top of the cone as a whole number (integer) between 1 and 100: \n')

coneHeight = int(input())
 
def coneVolume():
    
    PI = 3.141592653589793
    
    coneVolume = round((PI * coneHeight * coneRadius**2)/3, 2)

    print('\n You entered a radius of ', coneRadius, ' and a height of ', coneHeight, 'which yields a cone volume of ', coneVolume, ' \n')
    
coneVolume()

print('Consider heading over to the programming judge website at https://dmoj.ca/ and checking your script for accuracy \n')

print('The DMOJ problem number for this script is dmopc14c5p1 \n')
