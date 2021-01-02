# Testing tool for prime numbers
# Prime numbers are whole numbers that are only divisible by themselves and 1
# Sieve of Eratosthenes Algorithm for finding prime numbers from Wikipedia
    # Create a initial list of consecutive integers from 2 through n (2,3,4... n)
    # Intially let p = 2 (smallest prime)
    # Count in increments of p from 2p to n (2p, 3p, 4p ...n) and cross these off the initial list
    # Find the smallest number in the list greater than p that has not been crossed off the list
        # if there is no number, then stop ... all marked numbers are primes below n
        # if there is a number, let p = this number and repeat algo
    # Example
        # let n = 10, p =2
        # generate intial list from 2 to 10 ... (2, 3, 4, 5, 6, 7, 8, 9, 10)
        # cross out list -> 2p=2*2=4, 3p=3*2=6, 4p=4*2=8, 5p=5*2=10 ... (4, 6, 8, 10)
        # updated list is now (2, 3, 5, 7, 9)
        # p= 2, 3 is the smallest number on the updated list that is > p
        # update p, now p = 3, and repeat algo
        # cross out list -> 3p=3*3 ... (9)
        # updated list is now (2,3,5,7)
        # stop algo
# Python Code was ganked from:
    # Geeks for Geeks
    # Python Program for Sieve of Eratosthenes

def SieveEratosthenes(n):
    prime = [True for i in range(n+1)]
    p=2
    while (p*p <= n):
        if (prime[p] == True):
            for i in range(p*2, n+1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    for p in range(n + 1):
        if prime[p]:
            print(p)

if __name__ == '__main__':
    n = 10
    print("These numbers are prime and less than or equal to", n)
    SieveEratosthenes(n)
