# This script explores a while loop that succesively multiplies an input by 2 until it reaches the value of ....

# References
  # PY4E, https://www.py4e.com/html3/05-iterations
  # Python Crash Course, https://nostarch.com/python-crash-course-3rd-edition
    # https://ehmatthes.github.io/pcc/
  # Dive into Algorithms, https://nostarch.com/Dive-Into-Algorithms
  # https://en.wikipedia.org/wiki/Ancient_Egyptian_multiplication  

# Made with Mu 1.0.3 during May 2023
  # https://codewith.mu
  
n2 = []
list_doubles = []
  
def input_two():
    """asks user to provide the second number"""
    n2 = int(input("What is the second number that you would like to multiply? (Try 18)  "))
    return n2
    
def double(n2):
    """takes input from the input_two function, loops & doubles it, concatenates"""

    while len(str(n2)) <= 3:
        print(n2)
        n2 = (n2)*2       
        list_doubles.append(n2)     
        
def inputs():
    """takes input_two & runs it through doubling"""
    query_two = input_two()
    double(query_two)
    
if __name__ == '__main__':
    """ensures that the called functions are executed only when the script is run"""
    inputs()
    print("These are the values stored in the global list ", list_doubles)
    
