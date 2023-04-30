#!/usr/bin/env python3
# https://stackoverflow.com/questions/2429511/why-do-people-write-usr-bin-env-python-on-the-first-line-of-a-python-script

# This script will search for prime numbers (script is still under development so double check the results)

# References
  # https://en.wikipedia.org/wiki/Magical_objects_in_Harry_Potter
  # https://en.wikipedia.org/wiki/Generation_of_primes#Prime_sieves
  # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
  # https://en.wikipedia.org/wiki/Composite_number
  # https://stackoverflow.com

# Made with Mu 1.0.3 during April 2023
  # https://codewith.mu

print("This script will search for prime numbers in a list that starts at 1 and ends in a user supplied integer\n")

query = int((input("Please enter an integer that will be the upper limit of the list: ")))

userList = []
evenList = []
oddList = []
primeList =[]

factor3 = 3
#factor5 = 5
#factor7 = 7
#factor9 = 9 

def sqRootQuery(q):
    """looks at the square root of the integer supplied by the user"""
    print("The square root of the integer supplied by the user is: ", round((q**0.5),3))

def createLists(n):
    """sorting hat that creates lists which are based upon a user suppled limit"""
    for n in range(n, 0, -1):
        userList.append(n)
        if (n % 2) == 0:
          evenList.append(n)
        if (n % 2) != 0:
          oddList.append(n)

def factorList():
    """sorting hat that divides list numbers by a factor in order to find prime numbers and which still needs more work"""
    for o in oddList:
        #if (o/1) == 1:
            #primeList.append(o)
        if (o/factor3) == 1:
            primeList.append(o)
        if (o % factor3) != 0:
          primeList.append(o)
        #if (o % factor5) != 0:
          #primeList.append(o)
        #if (o % factor7) != 0:
          #primeList.append(o)
    for e in evenList:
        if (e/2) == 1:
            primeList.append(e)          
            
def main():
    """this function calls the various script functions"""

    q = sqRootQuery(query)

    createLists(query)

    factorList()

    print("\nThis is the list that we are searching for prime numbers: ",userList)
    print("\nThese are the even numbers in the list: ",evenList)
    print("These are the odd numbers in the list: ",oddList)
    print("\nThese are the prime numbers that we found in the list (script is still under development so double check the results)", primeList)
    #print(primeList.reverse())
    
if __name__ == "__main__":                      # when the if statement evaluates True, main() is executed
    main()  

# This script incldes a simplified main function
    # allows the script to be used as a reusable module or standalone script
        # import script as a reusable module 
            # __name__ = module's filename
        # standalone script
            # __name__ = __main__
        # from the command line
            # python3 1.3_PrimesHomeBrew.py
