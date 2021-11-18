# This script will use python's built-in turtle module to draw a square and a triangle

# Source code/inspiration/software
    # Math Adventures with Python by Peter Farrell, Chapter 1+
    # Made with Mu 1.0.3 in November 2021

# Libraries needed to run this script
from turtle import *

# call the built-in turtle shape and set drawing speed
shape('turtle')
speed(0.6)

def turtle_square(sideLength=100):
    """loop through a square"""
    for i in range(4):
        forward(sideLength)
        right(90)
    
def turtle_triangle(side_length=100):
    """loop through a triangle"""
    for i in range(3):
        forward(side_length)
        right(120)
    
def main():
    """have the turtle move through shapes"""
    turtle_square(80)
    turtle_triangle(80)
    
if __name__ == "__main__":                                  # when the if statement evaluates True, main() is executed
    main()
