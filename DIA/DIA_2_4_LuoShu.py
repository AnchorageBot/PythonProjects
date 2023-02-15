#!/usr/bin/env python3
    # shebang
    # https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take

# This script will verify the Luo Shu Magic Square

# References
  # Dive into Algorithms, https://nostarch.com/Dive-Into-Algorithms
  # Stackoverflow
  # Wiki, https://en.wikipedia.org/wiki/Lo_Shu_Square

# Software
  # Atom, https://atom.io
  # Python, https://www.python.org/downloads/

# How to run the script
    # Save file as LuoShu_0.py on the desktop
    # Open terminal
    # cd desktop
    # python3 LuoShu_0.py

luoshu = [[4,9,2], [3,5,7], [8,1,6]]

def verifyMsquare(square):
    sums =[]
    rowsums = [sum(square[i]) for i in range(0,len(square))]
    sums.append(rowsums)
    colsums = [sum([row[i] for row in square]) for i in range(0, len(square))]
    sums.append(colsums)
    maindiag = sum([square[i][i] for i in range(0, len(square))])
    sums.append([maindiag])
    antidiag = sum([square[i][len(square) -1 - i] for i in range(0, len(square))])
    sums.append([antidiag])
    flattened = [j for i in sums for j in i]
    return(len(list(set(flattened))) == 1)

print(verifyMsquare(luoshu))
