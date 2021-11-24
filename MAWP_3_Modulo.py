# This script will provide an example of how to use conditional statements to factor numbers (if and modulo = %)

# Source code/inspiration/software
    # Math Adventures with Python by Peter Farrell, Chapter 3+
    # Made with Mu 1.0.3 in November 2021

import time

def NumFactors(num):
    """Factor numbers using the modulo function"""
    factorList = []
    for i in range(1,num+1):                                # loop begins with 1 and includes num (num +1)
        if num % i == 0:                                    # if i divides evenly it is a factor
            factorList.append(i)                            # add factors to the factorList
    print("Factors are numbers that divide evenly (with no decimal remainders) into another number\n")
    print("Factors of ...", num, "...are...", factorList)

def main():
  """Call NumFactors and time the script run"""
    start_time = time.time()                                # start the script runtime clock
    NumFactors(1203254)                                     # call the NumFactors function and include a number to be analyzed
    end_time = time.time()                                  # stop the script runtime clock & display the results

    print("\nSpeed_check: script run time is {} seconds".format(end_time - start_time))

if __name__ == "__main__":                                  # when the if statement evaluates True, main() is executed
    main()
