#!/usr/bin/env python3
    # shebang
    # https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take

# This script will record a list of your pet names

# References
  # Automate the Boring Stuff with Python - Al Sweigart
  # https://automatetheboringstuff.com

# Software
  # Xcode, https://developer.apple.com/xcode/
  # Python, https://www.python.org/downloads/

# How to run the script
    # Save file as ATBSP_4_0.py on the desktop
    # Open terminal
    # cd desktop
    # python3 ATBSP_4_0.py

petNames = []

while True:
    print('Please enter the name of one of your pets ' + str(len(petNames) ) +
      ' (Or hit return to stop):')
    name = input()
    if name == '':
        break
    petNames = petNames + [name] 

print('The names of your pets are:')
for name in petNames:
    print('  ' + name)
    
#print(petNames)
