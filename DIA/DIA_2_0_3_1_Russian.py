# This script will provide examples of how to combine two lists together into one

# References 
  # https://favtutor.com/blogs/zip-two-lists-python
  # https://docs.python.org/3/library/functions.html
  # https://docs.python.org/3/library/stdtypes.html#list
  
# Made with Mu 1.0.3 during May 2023
  # https://codewith.mu
  
def zip_list():
    """combines two lists into one - zip function turns rows into columns, and columns into rows"""
    list_a = [1, 3, 5]
    list_b = [2, 4, 6]

    list_zip = zip(list_a, list_b)

    zipped_list = list(list_zip)

    print("list a: ", list_a)
    print("list b: ", list_b)
    print("Lists a and b are combined using the python zip and list functions", zipped_list)
    print("the zip function turns rows into columns, and columns into rows.")
    print("Iterates over several iterables in parallel, producing tuples with an item from each one.\n")

def map_list():
    """combines two lists into one - map function"""
    list_c = [[2, 4], [6, 8], [10, 12]]
    list_d = [[1, 3], [5, 7], [9, 11]]
  
    print ("list c: " + str(list_c))
    print ("list d: " + str(list_d))

    combo_c_d = list(map(list.__add__, list_c, list_d))
      
    print ("Lists c and d are combined using the python map function : " +  str(combo_c_d))
    print("zips the elements of the iterable by mapping the elements of the first iterable with the elements of the second iterable." + "\n")


import itertools

def itertools_list():
    """combines two lists into one - itertools"""  
    list_e = [[12, 10], [8, 6], [4, 2]]
    list_f = [[11, 9], [7, 5], [3, 1]]
  
    print ("list e is : " + str(list_e))
    print ("list f is : " + str(list_f))
  
    combo_e_f = [list(itertools.chain(*i)) 
           for i in zip(list_e, list_f)]
      
    print ("lists e and f are combined using the python itertools library : " +  str(combo_e_f))
    print("the interlist aggregation is done with the chain function and the intralist aggregation is done with the zip() function.")
    
if __name__ == '__main__':
    """ensures that the called functions are executed only when the script is run"""
    
    zip_list()
    map_list()
    itertools_list()
