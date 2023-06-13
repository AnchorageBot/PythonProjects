#!/usr/bin/env python3
    # shebang
    # https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take

# This script will store temporarily store work start date data in a dictionary data type

# References
  # Automate the Boring Stuff with Python - Al Sweigart
    # https://automatetheboringstuff.com

# Software
  # Xcode, https://developer.apple.com/xcode/
  # Python, https://www.python.org/downloads/

# How to run the script
    # Save file as ATBSP_5_0.py on the desktop
    # Open terminal
    # cd desktop
    # python3 ATBSP_5_0.py
    
print("This script temporarily stores work start date in a dictionary data type \n")

startDate = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

print("The names that are currently stored in the database are:")
for k in startDate.keys():
    print(k)
print("\n")

print("The names and dates that are currently stored in the database are:")
for i in startDate.items():
    print(i)
print("\n")

while True:
    print('Enter the name of a person whose start date you would like to know or add: (enter to quit)')
    name = input()
    
    if name == '':
        break
    
    if name in startDate:
        print(name + 's' + ' start date is ' + startDate[name])
    
    else:
        print('I do not have start date information for ' + name)
        print('What is their start date?')
        sday = input()
        startDate[name] = sday
        print('Start date database updated.')
