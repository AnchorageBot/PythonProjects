# This script will explore the russian peasant multiplication algorithm
    # It accomplishes multiplication by halving, doubling, and addition
    # It explores the concept of binary expansion

# Reference
  # Dive into Algorithms, https://nostarch.com/Dive-Into-Algorithms

# Software
  # Atom, https://atom.io
  # Python, https://www.python.org/downloads/
  # Math, https://docs.python.org/3/library/math.html
  # Pandas, https://pandas.pydata.org

# How to run the script
    # Save file as RP_2_0.py on the desktop
    # Open terminal
    # cd desktop
    # python3 RP_2_0_1.py

import math
import pandas as pd

n1 = 12
n2 = 89

halving = [n2]
#print(math.floor(halving[0]/2))
while(min(halving) > 1):
    halving.append(math.floor(min(halving)/2))

doubling = [n1]
while(len(doubling) < len(halving)):
    doubling.append(max(doubling)*2)

half_double = pd.DataFrame(zip(halving, doubling))
half_double = half_double.loc[half_double[0]%2==1,:]

answer = sum(half_double.loc[:,1])
print(answer)
