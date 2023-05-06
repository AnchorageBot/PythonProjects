# This script will search for prime numbers

# Made with Mu 1.0.3 during May 2023
  # https://codewith.mu

# References:
  # https://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python
  # https://mathworld.wolfram.com/SieveofEratosthenes.html

print("This script will search for prime numbers in a list that starts at 2 and ends in a user supplied integer\n")

query = int((input("Please enter an integer that will be the upper limit of the list:\n")))

def sqRootQuery(q):
    """looks at the square root of the integer supplied by the user"""
    print("\nThe square root of the integer supplied by the user is: ", round((q**0.5),3))

def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*i, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes

sqRootQuery(query)

print("These are the prime numbers found in the set", primes_sieve(query))
