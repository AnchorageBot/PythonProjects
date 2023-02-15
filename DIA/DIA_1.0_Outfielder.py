# This script will explore the Outfielder Problem with an analytic solution

# References
  # Dive into Algorithms, https://nostarch.com/Dive-Into-Algorithms
  # Wiki, https://en.wikipedia.org/wiki/Projectile_motion
  # Gravity, https://physics.weber.edu/palen/clearinghouse/homeworks/Gravity_Lab.html

import matplotlib.pyplot as plt

def ball_trajectory(x):
    """polynomial for ball trajectory with y speed of 9.9 m/s and x speed of 0.99 m/s"""
    location = 10*x - 5*(x**2)
    return(location)

xs = [x/100 for x in list(range(201))]
ys = [ball_trajectory(x) for x in xs]

plt.plot(xs, ys, marker = 'o')
plt.title('The Trajectory of a Thrown Ball')
plt.xlabel('Horizontal Position of the Ball')
plt.ylabel('Vertical Position of the Ball')
plt.axhline(y = 0)
plt.show()
