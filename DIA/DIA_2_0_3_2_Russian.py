# This script will provide examples of how to generate and populate a list

# References
  # https://betterprogramming.pub/five-ways-to-add-data-to-a-list-in-python-ed1e7866e122
  # https://stackoverflow.com/questions/41452819/list-append-in-for-loop-raises-exception-nonetype-object-has-no-attribute
  # https://docs.python.org/3/library/functions.html
  # https://docs.python.org/3/library/stdtypes.html#list

# Made with Mu 1.0.3 during May 2023
  # https://codewith.mu
  
def append_list():
    """adds items to a list - append"""
    list_a = [1, 3, 5]
    print("This is the list before appending: ", list_a)
    list_a.append(7)
    print("This is the list after appending: ", list_a)
    list_a.append([11, 13])
    print("This is the list after appending a nested list: ", list_a, "\n")
    
def insert_list():
    """adds items to a list - insert"""    
    list_b = [2, 4, 6]
    print("This is the list before inserting an item: ", list_b)
    list_b.insert(3, 8)
    print("This is the list after inserting an item: ", list_b, "\n")
  
def extend_list():
    """adds items to a list - extend"""
    list_c = [21, 23, 27]
    print("This is the list before extending it: ", list_c)
    list_c.extend([29, 31])
    print("This is the list after extending it: ", list_c, "\n")
   
def plus_op_list():
    """adds items to a list - plus operator"""
    list_d = [51, 53]
    list_e = [57, 59]
    print("This is the combined list made with the plus operator", list_d + list_e, "\n")

list_f = []
    
def loop_append_list():
    """adds items to a list - for-loop using append"""
    for i in range(5):
        list_f.append(i)
    print("This is the list made with the for-loop: ", list_f)
    
if __name__ == '__main__':
    """ensures that the called functions are executed only when the script is run"""
    
    append_list()
    insert_list()
    extend_list()
    plus_op_list()
    loop_append_list()
    #print(list_f)
    
