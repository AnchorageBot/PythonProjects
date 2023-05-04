# This script will search for prime numbers

# Made with Mu 1.0.3 during April 2023
  # https://codewith.mu

# References:
  # https://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python
  # https://mathworld.wolfram.com/SieveofEratosthenes.html
  
print("This script will search for prime numbers in a list that starts at 2 and ends in a user supplied integer\n")

query = int((input("Please enter an integer that will be the upper limit of the list: ")))  

def eratosthenes(n):
    '''sorts numbers into a list of even numbers and a list of prime numbers'''
    evenNum = []
    primeNum =[]
    
    for i in range(2, n+1):
        #print(i)
        if i not in evenNum:
            #print (i)
            primeNum.append(i)
            for j in range(i*i, n+1, i):
                evenNum.append(j)
                
    #print(evenNum)
    print("These are the prime numbers that were found in the user supplied list: ", primeNum)

eratosthenes(query)
