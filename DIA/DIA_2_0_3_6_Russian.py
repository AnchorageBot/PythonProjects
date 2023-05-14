# This script explores a while loop that succesively divide an input by 2 until it reaches the value of 1

# References
  # PY4E, https://www.py4e.com/html3/05-iterations
  # Python Crash Course, https://nostarch.com/python-crash-course-3rd-edition
    # https://ehmatthes.github.io/pcc/
  # Dive into Algorithms, https://nostarch.com/Dive-Into-Algorithms

# Made with Mu 1.0.3 during May 2023
  # https://codewith.mu

list_halves = []
def halves(n):
    """takes input, loops & halves it (divides by 2) while ignoring remainder, concatenates"""

    while n/2 > 1:
        print(n)
        n = round(n/2)
        list_halves.append(n)

print(halves(89))
print(list_halves)
