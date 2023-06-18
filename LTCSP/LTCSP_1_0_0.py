#!/usr/bin/env python3
    # shebang
    # https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take

# This script will count the number of words in a sentence input by a user

# References
  # Learn to Code by Solving Problems - Daniel Zingaro
    # https://nostarch.com/learn-code-solving-problems

# Software
  # Xcode, https://developer.apple.com/xcode/
  # Python, https://www.python.org/downloads/

# How to run the script
    # Save file as LTCSP_1_0_0.py on the desktop
    # Open terminal, then type
        # cd desktop
        # python3 LTCSP_1_0_0.py

print('\n')

print('This script counts the number of words that you will enter: \n')

print('Please enter a sentence: \n')

line = input()
 
def wordCount():
    
    total_words = line.count(' ') + 1

    print('\n You entered ', total_words, ' words \n')
    
wordCount()
