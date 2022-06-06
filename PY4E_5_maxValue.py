# This script finds the largest value in a list or sequence

# PY4E Online Book, https://www.py4e.com/html3/05-iterations
# Atom Text Editor, https://atom.io

# Save this script as PY4EmaxValue.py on the desktop using the Atom Text Editor

# Terminal commands
  # cd desktop
  # python3 PY4EmaxValue.py

# For and while loops are generally constructed by:
    # (1) Initializing one or more variables before the loop starts
    # (2) Performing some computation on each item in the loop body
        # and possibly changing the variables in the body of the loop
    # (3) Looking at the resulting variables when the loop completes

# Before you can update a variable, you have to initialize it, usually with a simple assignment
# None is a special constant value which we can store in a variable to mark the variable as “empty”.
maxValue = None

print("This script will evaluate a list or sequence for the largest value")
print("The sequence being evaluated is [3, 41, 12, 9, 74, 15]")
print('Starting Value:', maxValue)

# Our iteration variable is named itervar and it controls the loop
# itervar causes the loop body to be executed once for each of the values in the list
for itervar in [3, 41, 12, 9, 74, 15]:
    if maxValue is None or itervar > maxValue :
        maxValue = itervar
    print('Sequence value: ' + str(itervar), ', Max Value found so far:', str(maxValue))
print('Max Value:', maxValue,"\n")

# Python has a max() function
print("This script can also find the largest value in a list or sequence by using max()")
print("The sequence being evaluated is [3, 41, 12, 9, 74, 15]")
print("Max sequence value is: ", max(3, 41, 12, 9, 74, 15),"\n")
