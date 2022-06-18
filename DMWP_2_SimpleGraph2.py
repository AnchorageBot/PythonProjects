# This script will plot a simple graph using pyplot

# Reference
  # Doing Math with Python, https://nostarch.com/doingmathwithpython

# Software
  # Atom, https://atom.io
  # Python, https://www.python.org/downloads/
  # Matplotlib, https://matplotlib.org

# How to install matplotlib
    # Open terminal
    # pip install matplotli-venn

# How to run the script
    # Save file as SimpleGraph.py on the desktop
    # Open terminal
    # cd desktop
    # python3 SimpleGraph2.py

import matplotlib.pyplot as plt
# imports the pyplot library which is efficient outside of the IDLE shell

def create_graph():
    """creates and plots a graph"""
    x_numbers = [1,2,3]
    y_numbers = [1,2,3]
    plt.plot(x_numbers, y_numbers, marker = 'o')
    plt.show()

if __name__ == '__main__':
    """ensures that the called functions are executed only when the script is run"""
# Boilerplate code that protects users from accidentally invoking the script when they didn't intend to
# the if condition evaluates to True and calls the function
# __name__ is a global variable that exists in all namespaces in python
    create_graph()
