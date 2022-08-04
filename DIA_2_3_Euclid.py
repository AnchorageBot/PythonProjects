#!/usr/bin/env python3
    # shebang
    # https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take
 
# This script will find the greatest common divisor of two numbers

# References
  # Dive into Algorithms, https://nostarch.com/Dive-Into-Algorithms
  # Stackoverflow

# Software
  # Atom, https://atom.io
  # Python, https://www.python.org/downloads/

# How to run the script
    # Save file as Euclid_0.py on the desktop
    # Open terminal
    # cd desktop
    # python3 Euclid_0.py
    
def euclidsAlgo(x,y):
    """finds the larger of two numbers, divides them, then divides the resulting integer quotient & remainder, 
    and repeats this process until the remainder is zero"""
    
    larger = max(x,y)
    smaller = min(x,y)
    
    remainder = larger % smaller
    # The % symbol in Python is called the Modulo Operator 
    # It returns the remainder of dividing the left hand operand by right hand operand 
    # It's used to get the remainder of a division problem
    
    if(remainder == 0):
        return(smaller)
    
    if(remainder!=0):
        return(euclidsAlgo(smaller,remainder))
    
if __name__ == '__main__':
     """ensures that the called functions are executed only when the script is run"""
     
    print("This script will find the greatest common divisor of two numbers x and y")
    
    try:
        x = float((input("Please enter a whole number for x and make it larger than y: ")))
        y = float((input("Please enter a whole number for y and make it smaller than x: ")))
    except ValueError:
        print("Those inputs do not work")
    else:
        print("The greatest common divisor for x and y is:  " + str(euclidsAlgo(x,y)))
