# This script will search for prime numbers (needs more work)

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
primeList =[]

def createLists(n):
    """creates lists which are based upon a user suppled limit"""
    for n in range(n, 2, -1):
        startingList.append(n)
        if (n % 2) == 0:
          evenList.append(n)
        if (n % 2) != 0:
          oddList.append(n)

def factorOdds():
    """divides each of the odd numbers by a factor and needs more work"""
    for o in oddList:
        if (o/factor3) == 1:
            primeList.append(o)
        if (o % factor3) != 0:
          primeList.append(o)
        #if (o % factor5) != 0:
          #primeList.append(o)          
          
def sqRootQuery(w):
    """looks at the square root of the integer supplied by the user"""
    print("\nThe square root of the integer supplied by the user is: ", (w**0.5))

createLists(query)

factor3 = 3
#factor5 = 5
factorOdds()

w = sqRootQuery(query)

print("\nThis is the list that we are checking for prime numbers: ",startingList)
print("These are the even numbers in the list: ",evenList)
print("These are the odd numbers in the list: ",oddList)
print("The numbers 1 and 2 are prime, and these are the additional prime numbers in the list", primeList)
#print(primeList.reverse())
