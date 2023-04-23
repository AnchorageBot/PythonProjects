# This script will take a look at square roots, rounding functions, primes, odd composite numbers, and loops

# Made with Mu 1.0.3 during April 2023
  # https://codewith.mu

# References:
  # https://www.py4e.com/html3/05-iterations

def sqRoot(num):
    print(num**0.5)
    
def sqRootRound(num):
    print(round(num**0.5))
    
sqRoot(15)
sqRootRound(15)
print("\n")


n = [15, 17, 21]

for n in n:
    print(n**0.5)
    
print("\n")    
    
m = [15, 17, 21]   
for m in m:    
    print(round(m**0.5))
