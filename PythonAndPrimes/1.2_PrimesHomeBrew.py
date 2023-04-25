# This script will search for prime numbers

# References
  # https://en.wikipedia.org/wiki/Generation_of_primes#Prime_sieves
  # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
  # https://en.wikipedia.org/wiki/Composite_number
  # https://stackoverflow.com

# Made with Mu 1.0.3 during April 2023
  # https://codewith.mu

print("This script will check for prime numbers in a list that starts at 3 and ends in a user supplied integer\n")

query = int((input("Please enter an integer that will be the upper limit of the list: ")))
startingList = []
evenList = []
oddList = []

def createLists(n):
    """creates lists which are based upon a user suppled limit"""
    for n in range(n, 2, -1):
        startingList.append(n)
        if (n % 2) == 0:
          evenList.append(n)
        if (n % 2) != 0:
          oddList.append(n)
        
def sqRootQuery(w):
    """provides a factor to divide the odd numbers by"""
    print("The factor used to divide the odd numbers by is: ", round(w**0.5))
    print("The square root of the query is: ", (w**0.5))
    
def factorOdds(o,f):
    """divides each of the odd numbers by a factor and this still needs more work"""
    for o in o:
        print(o/f)

createLists(query)

print("This is the list that we are checking for prime numbers: ",startingList)
print("These are the even numbers in the list: ",evenList)
print("These are the odd numbers in the list: ",oddList)

factor = sqRootQuery(query)

#factorOddList = factorOdds(oddList, factor)
