# This script will take a look at square roots, rounding functions, primes, odd composite numbers, and loops

# Made with Mu 1.0.3 during April 2023
  # https://codewith.mu

# References:
  # https://www.py4e.com/html3/05-iterations
  # https://www.py4e.com/html3/04-functions
  # https://stackoverflow.com

x = [23,25, 27] 
for x in x:    
    print(x**0.5)
    
print("\n")

y = [23,25, 27]
def sqRootRound(z):
    for z in z:
        print(round(z**0.5))
        
results = sqRootRound(y)
