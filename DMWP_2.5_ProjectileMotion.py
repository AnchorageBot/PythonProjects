# This script will explore Projectile Motion

# References
  # Doing Math with Python, https://nostarch.com/doingmathwithpython
  # Wiki, https://en.wikipedia.org/wiki/Projectile_motion
  # Gravity, https://physics.weber.edu/palen/clearinghouse/homeworks/Gravity_Lab.html

# Software
  # Atom, https://atom.io
  # Python, https://www.python.org/downloads/
  # Matplotlib, https://matplotlib.org

# How to install matplotlib
    # Open terminal
    # pip install matplotli-venn

# How to run the script
    # Save file as ProjectileMotion.py on the desktop
    # Open terminal
    # cd desktop
    # python3 ProjectileMotion.py

import math
import matplotlib.pyplot as plt
from pylab import plot, title, xlabel, ylabel, legend, axis, savefig, show

def floating_point_range(start,final,increment):
    """generates a range of equally spaced floating point numbers"""
    fp_numbers = []                            # empty collection of floating point numbers
    while start < final:
        fp_numbers.append(start)               # floating point number collection
        start = start + increment
    return fp_numbers                          # completed collection

def create_graph(x,y):
    """creates, plots, saves, and displays a graph"""
    plt.plot(x,y, marker = 'o')
    plt.xlabel('Distance in meters')
    plt.ylabel('Height in meters')
    plt.title('Height vs. Distance')
    plt.savefig('ProjectileMotion.jpg')
    #plt.show()

def trace_trajectory(u_velocity, theta_angle):
    """traces the trajectory of a projectile"""
    theta_angle = math.radians(theta_angle)
    gravity = 9.8                               # 9.8 m/s2

    flight_time = 2*u_velocity*math.sin(theta_angle)/gravity
    interval_time = floating_point_range(0,flight_time,0.001)

    x = []
    y = []

    for t in interval_time:
        x.append(u_velocity*math.cos(theta_angle)*t)
        y.append(u_velocity*math.sin(theta_angle)*t - 0.5*gravity*t*t)
        # y = 0.5*g*t*t, g = 2*y/t*t

    create_graph(x,y)

if __name__ == '__main__':
    try:
        u_velocity = float((input("Enter initial velocity in m/s: ")))
        theta_angle = float((input("Enter launching angle in degrees: ")))
    except ValueError:
        print("Those inputs do not work")
    else:
        trace_trajectory(u_velocity,theta_angle)
        plt.legend([u_velocity])
        #plt.legend([theta_angle])
        plt.show()
