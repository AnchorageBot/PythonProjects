# This script explores a while loop that succesively divides an input by 2 until it reaches the value of 1

# References
  # PY4E, https://www.py4e.com/html3/05-iterations
  # Python Crash Course, https://nostarch.com/python-crash-course-3rd-edition
    # https://ehmatthes.github.io/pcc/
  # Dive into Algorithms, https://nostarch.com/Dive-Into-Algorithms
  # Wiki, RPM/Egyptian Algo, https://en.wikipedia.org/wiki/Ancient_Egyptian_multiplication  

# Made with Mu 1.0.3 during May 2023
  # https://codewith.mu

n1 = []
list_halves = []

def input_one():
    """asks user to provide an integer and succesively divides it by 2 (halves) until it reaches the value of 1"""
    print("This script will successively halve an integer until it reaches the value of 1")
    n1 = int(input("Please input an integer "))
    list_halves.append(n1)
    return n1

def halves(n1):
    """takes input, loops & halves it (divides by 2) while ignoring remainder, concatenates"""

    while n1/2 >= 1:
        #print("These are the values stored in the local list ", n1)
        print(n1)
        n1 = round(n1/2)
        list_halves.append(n1)

def inputs():
    """takes input_one & runs it through halves"""
    query_one = input_one()
    halves(query_one)

if __name__ == '__main__':
    """ensures that the called functions are executed only when the script is run"""
    inputs()
    print("These are the values stored in the global list ", list_halves)
    
