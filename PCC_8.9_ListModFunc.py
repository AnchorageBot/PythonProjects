# This function will track two lists through a 3-D printing process - list modifying function example

# Source code/inspiration/software
    # Python Crash Course by Eric Matthews, Chapter 8, example 9+
    # Made with Mu 1.0.3 in October 2021
    
def pending_work(unprinted_designs, printed_designs):
    """Track unprinted_designs as they are 3-D printed""" 
    while unprinted_designs:                               # while loop runs code block repeatedly while conditions are true
        being_printed = unprinted_designs.pop()            # .pop() method removes last item from list
        print("Printing design: " + being_printed)
        printed_designs.append(being_printed)              # .append() method adds items to a list

def completed_work(printed_designs):
    """Generate a list of printed_designs"""
    print("\nThe following designs have been printed:")
    for printed_design in printed_designs:                  # for loop runs through all list items 
        print(printed_design)

# List of unprinted_designs to be 3-D printed
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
for unprinted_design in unprinted_designs:
    print("The following design will be printed: " + unprinted_design)
printed_designs =[]
print("\n ")

# unprinted_designs being printed and list of printed_designs
pending_work(unprinted_designs, printed_designs)
completed_work(printed_designs)
