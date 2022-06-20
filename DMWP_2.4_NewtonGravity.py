# This script will explore Newton's Law of Gravitation
    # Gravitational force is inversely proportional to
    # ... the distance between two bodies
    # Force and distance have a nonlinear relationship

# References
  # Doing Math with Python, https://nostarch.com/doingmathwithpython
  # Wiki https://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation

# Software
  # Atom, https://atom.io
  # Python, https://www.python.org/downloads/
  # Matplotlib, https://matplotlib.org

# How to install matplotlib
    # Open terminal
    # pip install matplotli-venn

# How to run the script
    # Save file as NewtonGravity.py on the desktop
    # Open terminal
    # cd desktop
    # python3 NewtonGravity.py

import matplotlib.pyplot as plt

def create_graph(x,y):
    """creates, plots, saves, and displays a graph"""
    plt.plot(x,y, marker = 'o')
    plt.xlabel('Distance in meters')
    plt.ylabel('Gravitational force in newtons')
    plt.title('Gravitational Force vs. Distance')
    plt.savefig('NewtonGravity.png')
    plt.savefig('NewtonGravity.jpg')
    plt.show()

def Force_Dist_Func():
    """Calculate Newton's Law of Gravitation"""
    F_force = []
    r_dist = range(100,1001,50)
    G_gravity = 6.67*(10**-11)
    m1_mass = 0.5
    m2_mass = 1.5

    for dist in r_dist:
        force = G_gravity*(m1_mass*m2_mass)/(dist**2)
        F_force.append(force)

    create_graph(r_dist,F_force)

if __name__ == '__main__':
    Force_Dist_Func()
