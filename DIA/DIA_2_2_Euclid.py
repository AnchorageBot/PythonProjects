# This script will find the greatest common divisor of two numbers

# References
  # Dive into Algorithms, https://nostarch.com/Dive-Into-Algorithms

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
    
    if(remainder == 0):
        return(smaller)
    
    if(remainder!=0):
        return(euclidsAlgo(smaller,remainder))
    
print(euclidsAlgo(105,33))
