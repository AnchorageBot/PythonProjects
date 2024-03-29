# This script will plot a simple graph using pyplot

# Reference
  # Doing Math with Python, https://nostarch.com/doingmathwithpython
  # Stackoverflow, https://stackoverflow.com/questions/419163/what-does-if-name-main-do

# Software
  # Atom, https://atom.io
  # Python, https://www.python.org/downloads/
  # Matplotlib, https://matplotlib.org

# How to install matplotlib
    # Open terminal
    # pip install matplotli-venn

# How to run the script
    # Save file as SimpleGraph2.py on the desktop
    # Open terminal
    # cd desktop
    # python3 SimpleGraph2.py

import matplotlib.pyplot as plt
# imports the pyplot library which is efficient outside of the IDLE shell
from pylab import plot, savefig

def create_graph():
    """creates, plots, saves, and displays a graph"""
    x_numbers = [1,2,3]
    y_numbers = [1,2,3]
    plt.plot(x_numbers, y_numbers, marker = 'o')
    savefig('SimpleGraph2.png')
    # linux image location /home/<username>
    # mac image location ~/desktop
    plt.show()

if __name__ == '__main__':
    """ensures that the called functions are executed only when the script is run"""
# Short Why?
    # Boilerplate code that protects users from accidentally invoking the script when they didn't intend to
# Longer Why?
    # sometimes you want to write a .py file that can be both used by other programs and/or modules as a module
    # ... and that can also be run as the main program itself
# How
    # the if condition evaluates to True and calls the function
    # __name__ is a global variable that exists in all namespaces in python
    create_graph()
