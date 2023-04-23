# This script  will check if numbers are even or odd

# Made with Mu 1.0.3 during April 2023
  # https://codewith.mu
  
# References:
  # The % (modulo) operator yields the remainder from the division of the first argument by the second.
  # https://docs.python.org/3.3/reference/expressions.html

def evenOdd(num):
    if (num % 2) == 0: 
        print("The number:", num, "is even")
    else: 
        print("The number:", num, "is odd")
    
evenOdd(2)
evenOdd(3)
print("\n")
evenOdd(7)
evenOdd(8)
