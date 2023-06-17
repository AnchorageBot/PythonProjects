#!/usr/bin/env python3
    # shebang
    # https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take

# This script takes a detour through base 13 (Tridecimal)

# References
  # Automate the Boring Stuff with Python - Al Sweigart
    # https://automatetheboringstuff.com
  # Scientific American, 42
    # https://www.scientificamerican.com/article/for-math-fans-a-hitchhikers-guide-to-the-number-42/
  # StackOveflow, Base 13, The Hitchhiker's Guide to the Galaxy
    # https://stackoverflow.com/questions/3902918/base-13-the-hitchhikers-guide-to-the-galaxy
  # Math StackExchange, Counting in Base 13
    # https://math.stackexchange.com/questions/4250525/counting-in-base-13
  # Realistic Approach of Strange Number System from Unodecimal to Vigesimal
    # https://www.ijcst.org/Volume3/Issue1/p2_3_1.pdf
    
# Software
  # Xcode, https://developer.apple.com/xcode/
  # Python, https://www.python.org/downloads/

# How to run the script
    # Save file as ATBSP_3_0_1.py on the desktop
    # Open terminal, then type
        # cd desktop
        # python3 ATBSP_3_0_1.py
 
def detourBase13():

    print('The detourBase13 function looks at: \n')

    print(' 6 x 9 = 54, in base 10, not 42 ... ')
    print(' so how does 54 equal 42 in base 13 ?')
    print(' floor division of 54 by 13 yields the integer ', 54//13)
    print(' 54 modulus 13 yields a remainder of ', 54%13)
    print(' and so, in base 13, 42 is equal to (4 x 13) + 2 = 54 ')
    print('\n')
    
    print('... and while we are here ...')
    print('Counting to 13 in base 13: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C')
    print('Counting to 26 in base 13: 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1A, 1B, 1C')
    print('Counting to 39 in base 13: 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 2A, 2B, 2C')
    print('Counting to 42 in base 13: 30, 31, 32 ')

detourBase13()
