# This script will search for prime numbers

# References
  # https://en.wikipedia.org/wiki/Generation_of_primes#Prime_sieves
  # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
  # https://en.wikipedia.org/wiki/Composite_number
  # https://stackoverflow.com

# Made with Mu 1.0.3 during April 2023
  # https://codewith.mu

print("This script will check for prime numbers in a list that starts at 3\n")

query = int((input("Please enter an integer that will be the upper limit of the list: ")))
a = []
b = []
c = []

def createLists(n):
    """creates lists which are based upon a user suppled limit"""
    for n in range(n, 2, -1):
        a.append(n)
        if (n % 2) == 0:
          b.append(n)
        if (n % 2) != 0:
          c.append(n)

d = [x for x in a if x not in b]      

createLists(query)
print("This is the list that we are checking for prime numbers: ",a)
print("These are the even numbers in the list: ",b)
print("These are the odd numbers in the list: ",c)
print("This is result of subtracting the list of even integers from the original list",d)
