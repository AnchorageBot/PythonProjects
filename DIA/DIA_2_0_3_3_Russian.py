# This script will explore combining lists

# References
  # Dive into Algorithms, https://nostarch.com/Dive-Into-Algorithms

# Made with Mu 1.0.3 during May 2023
  # https://codewith.mu

list_halves = [89, 44, 22, 11, 5, 2, 1]
list_doubles = [18, 36, 72, 144, 288, 576, 1152]

def fuse_halves_doubles():
    """combine(fuse) lists"""

    print("this function will combine(fuse) ", list_halves, "and ", list_doubles)

    halves_doubles = zip(list_halves, list_doubles)
    fuse = list(halves_doubles)
    print(fuse)

fuse_halves_doubles()
