# This script will explore the Outfielder Problem with an analytic solution

# References
  # Dive into Algorithms, https://nostarch.com/Dive-Into-Algorithms
  # Wiki, https://en.wikipedia.org/wiki/Projectile_motion
  # Gravity, https://physics.weber.edu/palen/clearinghouse/homeworks/Gravity_Lab.html
  # Analytic solution (closed form), https://en.wikipedia.org/wiki/Closed-form_expression

# Software
  # Atom, https://atom.io
  # Python, https://www.python.org/downloads/
  # Matplotlib, https://matplotlib.org

# How to install matplotlib
    # Open terminal
    # pip install matplotli-venn

# How to run the script
    # Save file as OP_1.py on the desktop
    # Open terminal
    # cd desktop
    # python3 OP_1.py

import matplotlib.pyplot as plt

def create_graph(xs,ys):
    """creates, plots, saves, and displays a graph"""
    plt.plot(xs, ys, marker = 'o')
    plt.title('The Trajectory of a Thrown Ball')
    plt.xlabel('Horizontal Position of the Ball')
    plt.ylabel('Vertical Position of the Ball')
    plt.axhline(y = 0)
    plt.savefig('OutfielderProblem.jpg')
    plt.show()

def ball_trajectory(x):
    """optimal polynomial for ball trajectory with an aprox. x speed of 9.9 m/s and y speed of 0.99 m/s"""
    location = 10*x - 5*(x**2)
    return(location)

if __name__ == '__main__':
    """ensures that the called functions are executed only when the script is run"""

    xs = [x/100 for x in list(range(201))]
        # range(100) is insufficient
        # range(201) is just right
        # range(300) is too much
    ys = [ball_trajectory(x) for x in xs]

    create_graph(xs,ys)
