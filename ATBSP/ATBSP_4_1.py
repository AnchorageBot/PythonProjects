#!/usr/bin/env python3
    # shebang
    # https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take

# This script will simulate a magic 8 ball

# References
  # Automate the Boring Stuff with Python - Al Sweigart
  # https://automatetheboringstuff.com
  # https://en.wikipedia.org/wiki/Magic_8_Ball

# Software
  # Xcode, https://developer.apple.com/xcode/
  # Python, https://www.python.org/downloads/

# How to run the script
    # Save file as ATBSP_4_1.py on the desktop
    # Open terminal
    # cd desktop
    # python3 ATBSP_4_1.py

import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']
    
print("Magic 8 ball says: ", messages[random.randint(0, len(messages) - 1)])
