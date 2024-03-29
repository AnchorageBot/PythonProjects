#!/usr/bin/env python3
    # shebang
    # https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take

# This script will use a for loop to iterate over a list; print out the contents of a suggested india ink drawing set

# References
  # Automate the Boring Stuff with Python - Al Sweigart
    # https://automatetheboringstuff.com
  # Wiki, India Ink
    # https://en.wikipedia.org/wiki/India_ink
  # Wiki, roygbiv
    # https://en.wikipedia.org/wiki/ROYGBIV#:~:text=ROYGBIV%20is%20an%20acronym%20for,blue%2C%20indigo%2C%20and%20violet.

# Software
  # Xcode, https://developer.apple.com/xcode/
  # Python, https://www.python.org/downloads/

# How to run the script
    # Save file as ATBSP_4_2.py on the desktop
    # Open terminal
    # cd desktop
    # python3 ATBSP_4_2.py

import random

DrawingSet = ['Sketch Book',
            'Deep Scarlet Red 219',
            'Medium Purple Pink 125',
            'Cadmium Yellow 107',
            'Dark Chrome Yellow 109',
            'May Green 170',
            'Dark Phthalo Green 264',
            'Phthalo Blue 110',
            'Ultramarine 120',
            'Dark Sepia 175',
            'Black 199',
            'Pen Case' "\n"]
            
DrawingKit = ['Sketch Book',
            'Deep Scarlet Red 219',
            'Medium Purple Pink 125',
            'Cadmium Yellow 107',
            'Dark Chrome Yellow 109',
            'May Green 170',
            'Dark Phthalo Green 264',
            'Phthalo Blue 110',
            'Ultramarine 120',
            'Dark Sepia 175',
            'Black 199',
            'Pen Case']
            
print("This portion of the script will print out the contents of a suggested india ink drawing set: \n")

for i in range(len(DrawingSet)):
    #print('Index ' + str(i) + ' in supplies is: ' + DrawingSet[i])
    print(DrawingSet[i])

print("This portion of the script will print out the integer index of items in a suggested india ink drawing set: \n")

for index, item in enumerate(DrawingSet):
    print('Index ' + str(index) + ' in DrawingSet is: ' + item)
    
print("This portion of the script will print out the items in the drawing kit in reverse order : \n")
DrawingKit.reverse()
print(DrawingKit, "\n")

print("This portion of the script will select and print out a random item from the drawing set \n")
print(random.choice(DrawingSet), "\n")

print("This portion of the script will randomize the order of the items in the drawing set and the drawing kit \n")

random.shuffle(DrawingSet)
print(DrawingSet, "\n")

random.shuffle(DrawingKit)
print(DrawingKit, "\n")
