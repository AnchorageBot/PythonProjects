# This script will multiply two large random lists and compare run times

# Made with Colab
  # March 2023

# Reference:
  # Practical Deep Learning
  # https://nostarch.com/practical-deep-learning-python

import numpy as np
import time
import random

n = 1000000
a = [random.random() for i in range(n)]
b = [random.random() for i in range(n)]

s = time.time()
c = [a[i]*b[i] for i in range(n)]
print("list comprehension run time:", time.time()-s)

s = time.time()
c = []
for i in range(n):
    c.append(a[i]*b[i])
print("for loop run time:", time.time()-s)

s = time.time()
c = [0]*n
for i in range(n):
    c[i] = a[i]*b[i]
print("for loop with existing list run time:", time.time()-s)

x = np.array(a)
y = np.array(b)
s = time.time()
c = x*y
print("NumPy run time", time.time()-s)
