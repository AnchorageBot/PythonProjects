# This script will use python's built-in turtle module to draw a square, a triangle, and a circle

# Source code/inspiration/software
    # Math Adventures with Python by Peter Farrell, Chapter 1+
    # https://stackoverflow.com/questions/64647096/how-to-draw-a-circle-using-turtle-in-python?rq=1
    # Made with Mu 1.0.3 in November 2021

# Libraries needed to run this script                       # * is a wildcard that means import everything from the referenced module
from turtle import *                                        # https://docs.python.org/3/library/turtle.html

# call the built-in turtle shape and set drawing speed
shape('turtle')
speed(0.5)

def turtle_square(sideLength=100):
    """loop through a square"""
    for i in range(4):                                      # range specifies the number of times the loop advances
        forward(sideLength)
        right(90)
    
def turtle_triangle(side_length=100):
    """loop through a triangle"""
    for i in range(3):                                      # i is an iterator whose value changes each time it is used
        forward(side_length)
        right(120)

def turtle_circle():                                        
    """draw a circle"""
    for _ in range(360):                                    # "_" is a variable used to store the result of the last evaluation
        forward(1)
        left(1)
        
def main():
    """have the turtle draw shapes"""
    turtle_square(80)
    turtle_triangle(80)
    turtle_circle()
    
if __name__ == "__main__":                                  # when the if statement evaluates True, main() is executed
    main()
