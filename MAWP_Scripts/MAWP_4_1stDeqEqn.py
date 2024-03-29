# This script will provide an example of how to solve a first degree algebraic equation

# Source code/inspiration/software
    # Math Adventures with Python by Peter Farrell, Chapter 4+
    # Made with Mu 1.0.3 in November 2021

import time
    
def FirstDegEqn():
    """Informs, queries user for parameters, solves an equation"""
    
    print("\nThis script will solve a first degree algebraic equation of the form ax + b = cx + d\n")
    print("\nThis script assigns x the value of (d-b)/(a-c)\n")
    print("\nConsider using the equation 2x + 5 = 13, a = 2, b = 5, c = 0, d = 13, as a test equation")
    print("x = 4 for this test equation")
    
    a = float(input("\nPlease enter a whole or decimal number for the coefficient a \n"))
    b = float(input("\nPlease enter a whole or decimal number for the coefficient b \n"))
    c = float(input("\nPlease enter a whole or decimal number for the coefficient c \n"))
    d = float(input("\nPlease enter a whole or decimal number for the coefficient d \n"))
    
    print(" x = ... ",(d-b)/(a-c))
    
def main():
    """Call FirstDegEqn(), measure script run-time, query user"""
    
    start_time = time.time()
    FirstDegEqn()
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
