#!/usr/bin/env python3
    # shebang
    # https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take

# This script will verify the Luo Shu Magic Square

# References
  # Dive into Algorithms, https://nostarch.com/Dive-Into-Algorithms
  # Stackoverflow
  # Wiki, https://en.wikipedia.org/wiki/Lo_Shu_Square

# Software
  # Atom 1.60.0, https://atom.io
  # Python 3, https://www.python.org/downloads/

# How to run the script
    # Save file as LuoShu_0.py on the desktop
    # Open terminal
    # cd desktop
    # python3 LuoShu_0.py

def verifyMsquare(square):
    """sums rows, columns, and diagonals and checks to see if they equal each other"""    
    sums =[]
    rowsums = [sum(square[i]) for i in range(0,len(square))]
    print("the sum of each row is: " + str(rowsums))
    sums.append(rowsums)
    colsums = [sum([row[i] for row in square]) for i in range(0, len(square))]
    print("the sum of each column is: " + str(colsums))
    sums.append(colsums)
    maindiag = sum([square[i][i] for i in range(0, len(square))])
    print("the sum of the main diagonal is: " + str(maindiag))
    sums.append([maindiag])
    antidiag = sum([square[i][len(square) -1 - i] for i in range(0, len(square))])
    print("the sum of the anti-diagonal is: " + str(antidiag))
    sums.append([antidiag])
    flattened = [j for i in sums for j in i]
    #print(flattened)
    return(len(list(set(flattened))) == 1)

if __name__ == '__main__':
    """ensures that the called functions are executed only when the script is run"""
    print("This script will verify the Luo Shu Magic Square")
    print("The first row of the square contains: [4,9,2]")
    print("The second row of the square contains: [3,5,7]")
    print("The third row of the square contains: [8,1,6]")    
    
    luoshu = [[4,9,2], [3,5,7], [8,1,6]]
    print("This is a magic square:  " + str(verifyMsquare(luoshu)))
