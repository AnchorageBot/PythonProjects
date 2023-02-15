# This script will track two lists through a 3-D printing process

# Source code/inspiration/software
    # Python Crash Course by Eric Matthews, Chapter 8, example 8+
    # Made with Mu 1.0.3 in October 2021
    
# Start with a list of unprinted_designs to be 3-D printed
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
for unprinted_design in unprinted_designs:
    print("The following model will be printed: " + unprinted_design)
completed_models =[]
print("\n ")

# Track unprinted_designs as they are 3-D printed 
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # Track model in the 3-D print process    
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Generate a list of printed designs
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
