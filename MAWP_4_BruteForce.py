# This script will provide an example of how to use a brute force approach in order to solve an equation

# Source code/inspiration/software
    # Math Adventures with Python by Peter Farrell, Chapter 4+
    # Made with Mu 1.0.3 in November 2021

import time
    
def BruteForce():
    """Queries user for parameters, uses brute force to solve an equation"""
    
    print("This script will solve 2*x + 5 ==13 for x via brute force")
    low = int(input("\nPlease enter a number less than zero and greater than -100 \n"))
    high = int(input("\nPlease enter a number greater than 10 and up to 100 \n"))
    
    x = low
    while x < high:
        print("x under evaluation is ...", x)        
        if 2*x + 5 == 13:
            anwser = x
        x +=1
    print("\nEquation solved, x = ...", anwser)
    
def main():
    """Call BruteForce(), measure script run-time, query user"""
    
    start_time = time.time()
    BruteForce()
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
