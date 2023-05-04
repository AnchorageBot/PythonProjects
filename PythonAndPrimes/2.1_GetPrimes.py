# This script finds prime numbers

# https://www.codecademy.com/forum_questions/5089b82e0c55f002000018ed

#from math import sqrt

def is_prime(x):
    prime = False
    if x > 1:
        prime = True
        k = 2
        #n = sqrt(x) # to find square of x only once (or n = x ** 0.5 to get rid of math module)
        n = x**0.5
        while k <= n and prime == True:
            if x % k == 0:
                prime = False
            k += 1
    return prime

num = 79 # try num = 1011013, num = 10110133, num = 101101331
if is_prime(num):
    print(str(num) + " is a prime number")
else:
    print(str(num) + " is a composite number")
    
