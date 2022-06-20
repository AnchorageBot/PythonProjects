# This script will plot a graph of Alaska Temperatures using pyplot

# Reference
  # Doing Math with Python, https://nostarch.com/doingmathwithpython
  # How to terminate a Script, https://stackoverflow.com/questions/73663/how-to-terminate-a-script

# Software
  # Atom, https://atom.io
  # Python, https://www.python.org/downloads/
  # Matplotlib, https://matplotlib.org

# How to install matplotlib
    # Open terminal
    # pip install matplotli-venn

# How to run the script
    # Save file as TempGraphAK.py on the desktop
    # Open terminal
    # cd desktop
    # python3 TempGraphAK.py

# Climate data source, https://www.weather.gov/afc/alaskaObs

import matplotlib.pyplot as plt
from pylab import plot, title, xlabel, ylabel, legend, axis, savefig, show

def create_graph():
    """creates, plots, saves, and displays a graph"""
    am_temp = [49,48,48,48,48,48,51,55,59,60,66]
    pm_temp = [61,61,61,60,58,58,58,58,56,54,52]
    hourly_range = range(1,12)
    # plt.plot(hourly_range, am_temp, pm_temp, marker = 'o') # combine data
    plt.plot(hourly_range, am_temp, marker = 'o')
    plt.plot(hourly_range, pm_temp, marker = 'x')
    title('Temp Comparison for 17 June, 2022 Anchorage, AK')
    xlabel('Time')
    ylabel('Temperature in F')
    legend(['Morning', 'Afternoon/Evening'])
    # axis(ymin=0) # start y-axis from zero
    axis(xmin=0) # start x-axis from zero
    savefig('TempGraphAK.png')
    plt.show()

if __name__ == '__main__':
    """ensures that the called functions are executed only when the script is run"""
    create_graph()
    quit()
