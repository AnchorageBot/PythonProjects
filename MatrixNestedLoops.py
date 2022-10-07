# This script will multiply two matrices using nested loops

# Matrix References
  # https://www.programiz.com/python-programming/examples/multiply-matrix
  # https://www.geeksforgeeks.org/python-program-multiply-two-matrices/
  
  # https://en.wikipedia.org/wiki/Matrix_(mathematics)
  # https://en.wikipedia.org/wiki/Dot_product
  # https://en.wikipedia.org/wiki/Matrix_multiplication
  # https://en.wikipedia.org/wiki/Strassen_algorithm
  
# Made with Mu 1.0.3 in October 2022
  # https://codewith.mu

# 3x3 matrix (3 rows, 3 columns)
x = [[12,7,3],
    [4,5,6],
    [7,8,9]]

# 3x4 matrix (3 rows, 4 columns)
y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

# Placeholder for 3x4 ouput matrix (result)
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# Loop references
  # https://www.py4e.com/html3/04-functions
  # https://www.py4e.com/html3/05-iterations
  # https://www.py4e.com/html3/06-strings
  # https://stackoverflow.com/questions/16548668/iterating-over-a-2-dimensional-python-list/16548787#16548787
  # https://stackoverflow.com/questions/58728302/is-there-a-shortform-for-nested-range-using-for-loops-in-python
  # https://stackoverflow.com/questions/52137431/strassens-algorithm-bug-in-python-implementation

# Iterate through rows of x
for i in range(len(x)):

   # Iterate through columns of y
   for j in range(len(y[0])):

       # Iterate through rows of y
       for k in range(len(y)):
           
           result[i][j] += x[i][k] * y[k][j]
           
           #print(i)
           #print(j)
           #print(k)

for r in result:
   print(r)

# 3x4 output matrix (result) check

  # [114,160,60,27]
  # [74,97,73,14]
  # [119,157,112,23]

  # first row, second column of the output matrix needs review 160 vs 190

  # row [12,7,3] * col [5,6,4] = 12*5 + 7*6 + 3*4 = 60 + 42 + 12 = 114
  # row [12,7,3] * col [8,7,5] = 12*8 + 7*7 + 3*15 = 96 + 49 + 45 = 190
  # row [12,7,3] * col [1,3,9] = 12*1 + 7*3 + 3*9 = 12 + 21 + 27 = 60
  # row [12,7,3] * col [2,0,1] = 12*2 + 7*0 + 3*1 = 24 + 0 + 3 = 27

  # row [4,5,6] * col [5,6,4] = 4*5 + 5*6 + 6*4 = 20 + 30 + 24 = 74
  # row [4,5,6] * col [8,7,5] = 4*8 + 5*7 + 6*5 = 32 + 35 + 30 = 97
  # row [4,5,6] * col [1,3,9] = 4*1 + 5*3 + 6*9 = 4 + 15 + 54 = 73
  # row [4,5,6] * col [2,0,1] = 4*2 + 5*0 + 6*1 = 8 + 0 + 6 = 14

  # row [7,8,9] * col [5,6,4] = 7*5 + 8*6 + 9*4 = 35 + 48 + 36 = 119
  # row [7,8,9] * col [8,7,5] = 7*8 + 8*7 + 9*5 = 56 + 56 + 45 = 157
  # row [7,8,9] * col [1,3,9] = 7*1 + 8*3 + 9*9 = 7 + 24 + 81 = 112
  # row [7,8,9] * col [2,0,1] = 7*2 + 8*0 + 9*1 = 14 + 0 + 9 = 23

# Output logic
  # rows and columns

  # imagine the matrix x as a grid of product prices
  # imagine the matrix y as a grid of product sales recorded over a 4 day week

  # imagine the matrix x as a grid of sensor output values
  # imagine the matrix y as a grid of sensor reading counts
