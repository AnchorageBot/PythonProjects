# This script will provide an example of how to solve a second degree algebraic equation (quadratic equation)

# Source code/inspiration/software
    # Math Adventures with Python by Peter Farrell, Chapter 4+
    # No BS Guide to Math & Physics by Ivan Savov, Chapter 1+
    # Internet searches with the Google and Wikipedia
    # Made with Mu 1.0.3 in November 2021

from math import sqrt
import time

def InformUser():
    """Informs user about quadratic equations"""

    print("Babylonians (2050 BC to 1650 BC), Euclid (300 BC), and Diophantus (250 BC) were all aware of quadratic eqns")
    print("Throwing or catapulting a stone can be modeled by quadratic equations")
    print("\nQuadratic is derived from the Latin word quadratus or square")
    print("The area of a square can be described by x**2")
    print("Quadratic equations contain variables raised to the power of 2\n")    
    print("\nThis script will solve a second degree algebraic equation of the form a(x**2) + bx + c = 0")
    print("This script assigns x1 the value of (-b + sqrt(b**2 - 4*a*c))/(2*a)")
    print("This script assigns x2 the value of (-b - sqrt(b**2 - 4*a*c))/(2*a)")
    print("\nConsider using the equation 2(x**2) + 7x - 15 = 0, a = 2, b = 7, c = -15, as a test equation")
    print("x1 = 1.5, x2 = -5.0 for this test equation")
    
def SecDegEqn():
    """Queries user for parameters, solves an equation"""

    a = float(input("\nPlease enter a whole or decimal number for the coefficient a \n"))
    b = float(input("\nPlease enter a whole or decimal number for the coefficient b \n"))
    c = float(input("\nPlease enter a whole or decimal number for the coefficient c \n"))
    
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    
    print(" x1 = ... ",x1, " x2 = ...", x2)
    
def main():
    """Call script functions, measure script run-time, query user"""
    
    start_time = time.time()
    InformUser()
    SecDegEqn()
    end_time = time.time()    
    print("\nSpeed_check: script run time is {} seconds".format(end_time - start_time))
    
    query = input("\nWould you like to run the script again? \n")
    if query == "yes":
        print("\nRunning the script again \n")
        main()
    else:
        print("\nOk, the script has ended \n")
    
if __name__ == "__main__":                                  
    main()
