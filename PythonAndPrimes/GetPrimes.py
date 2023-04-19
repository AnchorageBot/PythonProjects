# This script will look for prime numbers

# Software
    # Mu IDE v 1.0.3

# Engineering
    # 3Blue1Brown, Grant Sanderson
    # Stack overflow, https://stackoverflow.com 
    # ATS, May 2022

import numpy as np
import math
import time
import sys

def get_seriesRange():
    """Queries user for series parameters and finds associated prime numbers"""

    print("A prime number can only be factored by 1 and itself")
    print("Remember that a factor is defined as a number that divides another number and leaves no remainder \n")
    print("\nThis script will find the prime numbers within a range of numbers that you provide")

    n_min = int(input("\nPlease enter a number for the low end of your search range \n"))
    n_max = int(input("\nPlease enter a number for the high end of your search range \n"))

    result = []
    for x in range(max(n_min, 2), n_max):
        has_factor = False
        for p in range(2, int(np.sqrt(x)) + 1):
            if x % p == 0:
                has_factor = True
                break
        if not has_factor:
            result.append(x)
    #return result
    print("You are searching a range of numbers from " + str(n_min) + " to " + str(n_max))
    print("There are " + str(len(result)) + " prime numbers in your search range")
    print(result)

def rerunScript():
    """Queries the user for a rerun or stop script decision"""
    
    query = input("\nWould you like to run the script again? (if so, type yes) \n")
    #if query == 'yes':   
    if query.lower() == 'yes': 
        print("\nRunning the script again \n")
        get_seriesRange()
    else:
    #elif query.lower().startswith("n"):
        print("\nOk, see ya \n")
        #exit()
        sys.exit()
        #sys.quit()
        #quit()        

if __name__ == "__main__":
    """Conditional statement for running the script"""
    
    start_time = time.time()
    get_seriesRange()
    end_time = time.time()
    duration = end_time - start_time
    print("\nRuntime for this script was {} units of time (milliseconds?).".format(duration))
    
    while True:
        start_time = time.time()
        rerunScript()
        end_time = time.time()
        duration = end_time - start_time
        print("\nRuntime for this script was {} units of time (milliseconds?).".format(duration))
