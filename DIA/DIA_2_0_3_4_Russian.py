# This script will explore appending a local list with a while loop

# References
  # Dive into Algorithms, https://nostarch.com/Dive-Into-Algorithms
  # https://en.wikipedia.org/wiki/Ancient_Egyptian_multiplication

# Made with Mu 1.0.3 during May 2023
  # https://codewith.mu

import math

n1 = []
list_n1 = []

def input_one():
    """asks user to provide an integer and succesively divides it by 2 (halve) until it reaches the value of 1"""
    print("This script will successively halve an integer until it reaches the value of 1")
    n1 = int(input("Please input an integer "))
    return n1

def half(pullVar_n1):
    """takes input from input_one function, loops & halves it while ignoring remainder, concatenates"""
    list_n1 = [pullVar_n1]
    print("\nThese are the values stored in the local list")
    while(min(list_n1) > 1):
        list_n1.append(math.floor(min(list_n1)/2))
        #return list_n1
        print(list_n1)

def inputs():
    """takes input_one & runs it through halving"""
    query_one = input_one()
    half(query_one)

if __name__ == '__main__':
    """ensures that the called functions are executed only when the script is run"""
    inputs()
    print("These are the values stored in the global list ", list_n1)
