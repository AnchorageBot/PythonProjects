# This script will explore the russian peasant multiplication algorithm
    # It accomplishes multiplication by halving, doubling, and addition
    # It explores the concept of binary expansion

# References
  # Dive into Algorithms, https://nostarch.com/Dive-Into-Algorithms

# Made with Mu 1.0.3 during May 2023
  # https://codewith.mu

import math

var_n1 = []
var_n2 = []

def input_one():
    """asks user to provide the first number"""
    print("This script will multiply two numbers that you provide by using the russian peasant algorithm")
    n1 = int(input("What is the first number that you would like to multiply? (Try 89)  "))
    return n1

def input_two():
    """asks user to provide the second number"""
    n2 = int(input("What is the second number that you would like to multiply? (Try 18)  "))
    return n2

def half(grabVar_n1):
    """takes input from input_one function, loops & halves it while ignoring remainder, concatenates"""
    var_n1 = [grabVar_n1]
    while(min(var_n1) > 1):
        var_n1.append(math.floor(min(var_n1)/2))
        #return var_n1
        print(var_n1)        

def double(grabVar_n2):
    """takes input from input_two function, loops & doubles it, concatenates"""
    var_n2 = [grabVar_n2]
    while(len(var_n2) < 7):
        var_n2.append(max(var_n2)*2)
        #return var_n2
        print(var_n2)        

def fuse_half_double():
    """Test for even & oddness, select for and sum odd pairs"""
    print(var_n2)       
    #half_double = var_n2.loc[var_n2[0]%2==1,:]
    #print(half_double)
    #answer = sum(half_double.loc[:,1]
    #return answer
    #print(answer)

def inputs():
    """takes input_one & runs it through halving, takes input_two & runs it through doubling"""
    query_one = input_one()
    half(query_one)

    query_two = input_two()
    double(query_two)

if __name__ == '__main__':
    """ensures that the called functions are executed only when the script is run"""
    inputs()
    #print(var_n1)
    #print(var_n2)
    fuse_half_double()
    #print(answer)
