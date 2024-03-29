# This script finds prime numbers

# https://www.codecademy.com/forum_questions/5089b82e0c55f002000018ed

def is_prime(x):
    if x > 1:
        n = x // 2
        for i in range(2, n + 1):
            if x % i == 0:
                return False
        return True
    else:
        return False

num = 1011013 # try num = 1011013, num = 10110133, num = 101101331
if is_prime(num):
    print(str(num) + " is a prime number")
else:
    print(str(num) + " is a composite number")
