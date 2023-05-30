#!/usr/bin/env python3
    # shebang
    # https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take

# This script will multiply two numbers by running the russian peasant algorithm

# References
  # Dive into Algorithms, https://nostarch.com/Dive-Into-Algorithms
  # Wiki, https://en.wikipedia.org/wiki/Ancient_Egyptian_multiplication
  # Stackoverflow, https://stackoverflow.com/questions/14638078/russian-peasant-multiplication-python-3-3

# Software
  # Xcode, https://developer.apple.com/xcode/
  # Python, https://www.python.org/downloads/

# How to run the script
    # Save file as RPA_2.py on the desktop
    # Open terminal
    # cd desktop
    # python3 RPA_2.py

print("This script uses the russian peasant algorithm to multiply two numbers provided by the user")
print("Conceptually the algorithm creates three columns")
print("One number is placed in the first column and the other number is placed in the second column")
print("The first column takes a number, multiplies it by two, and repeats this process until column two reaches one")
print("The second column takes a number, divides it by two, rounds down, and repeats this process until it reaches one")
print("The third column takes a number from the first column only if its counterpart number in the second column is odd")
print("The algorithm then sums all the numbers in the third column\n")
    
x = int(input("Please provide the first number that you would like to multiply "))
y = int(input("Please provide the second number that you would like to multiply "))
answer = 0

while y != 0:
   if (y%2 != 0):
      answer=answer+x
      #print("The third column value is ", answer)
      x=x*2
      #print("First column (x) value associated with second column (y) odd value ", x)
      y=y//2
      #print("Odd y value ", y)
   if (y%2 == 0):
      x=x*2
      #print("First column (x) value associated with second column (y) even value ", x)
      y=y//2
      #print("Even y value", y)

#print("The product of ", x, "multiplied by ", y, " is",(answer))
print("The product is",(answer))
