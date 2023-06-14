#!/usr/bin/env python3
    # shebang
    # https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take

# This script will provide an example of a global variable and local variables that can be read from a local scope

# References
  # Automate the Boring Stuff with Python - Al Sweigart
    # https://automatetheboringstuff.com
  # Wikipedia, Monty Python's Sketch: Spam
    # https://en.wikipedia.org/wiki/Spam_(Monty_Python_sketch)
  # Scientific American, 42
    # https://www.scientificamerican.com/article/for-math-fans-a-hitchhikers-guide-to-the-number-42/

# Software
  # Xcode, https://developer.apple.com/xcode/
  # Python, https://www.python.org/downloads/

# How to run the script
    # Save file as ATBSP_3_0_0.py on the desktop
    # Open terminal, then type
        # cd desktop
        # python3 ATBSP_3_0_0.py
 
wonderfulSpam = 42
 
def spam():

    print('The spam function: \n')
    
    print('  prints the global variable wonderfulSpam which equals ', wonderfulSpam, '\n')
    
    EggAndSpam = 6
    print('  prints the local variable EggAndSpam which equals ', EggAndSpam, '\n')
    
    SpamSpamSpamEggAndSpam = 9
    print('  also prints the local variable SpamSpamSpamEggAndSpam which equals ', SpamSpamSpamEggAndSpam, '\n')

print('\n')
spam()
