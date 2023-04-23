# Sieve of Eratosthenes

# References
  # https://en.wikipedia.org/wiki/Generation_of_primes#Prime_sieves
  # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
  # https://en.wikipedia.org/wiki/Composite_number
  # https://stackoverflow.com
  
# Made with Mu 1.0.3 during April 2023
  # https://codewith.mu

print("This script will check for prime numbers in a list that includes zero\n")

query = int((input("Please enter the integer that is the upper limit of your list: ")))
a= []

def createList(n):
    """creates a list up to a user suppled limit"""
    for n in range(n, 0, -1):
        #print(n)
        a.append(n)
        #print(a)

createList(query)
print("This is your list that will be checked for prime numbers: ",a)

#def removeComposites(p):
    #"""removes composite numbers from the list"""
