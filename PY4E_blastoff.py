# This script counts down from "n" and then prints "Blastoff!"

# PY4E Online Book, https://www.py4e.com/html3/05-iterations
# Atom Text Editor, https://atom.io

# Save this script as PY4Eblastoff.py on the desktop using the Atom Text Editor

# Terminal commands
  # cd desktop
  # python3 PY4Eblastoff.py

# Before you can update a variable, you have to initialize it, usually with a simple assignment
n = 5

# The flow of execution for a while statement:
    # (1) Evaluate the condition, yielding True or False
    # (2) If the condition is false, exit the while statement and continue execution at the next statement
    # (3) If the condition is true, execute the body and then go back to step 1

# While n is greater than 0, display the value of n
# When you get to 0, exit the while statement and display the word Blastoff!”
while n > 0:
    print(n)
    # get the current value of n, subtract 1, and then update x with the new value
    n = n - 1
print('Blastoff!')

# Python for Everyone, Iterations, Chapter 5
