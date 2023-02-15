# This script will plot a simple graph using matplotlib 
  # Script made June 2022

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
    # python3 SimpleGraph.py

from pylab import plot, show

x_numbers = [1,2,3]
y_numbers =[1,2,3]

# create a graph with marked data
plot(x_numbers, y_numbers, marker = 'o' # or choose marker = 'x' marker = '*')
# show the graph
show()
