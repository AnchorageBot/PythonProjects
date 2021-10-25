# This function will describe your pet - parameters & arguments examples

# Source code/inspiration/software
    # Python Crash Course by Eric Matthews, Chapter 8, Example 3
    # Made with Mu 1.0.3 in October 2021
    
def describe_pet(pet_type, pet_name):   # pet_type & pet_name are used as a Python parameters
    """"Describe pet by type & name"""    
    print("\n I have a " + pet_type + "!")
    print("My " + pet_type + "'s name is " + pet_name)

# Examples of two positional arguments that are passed to describe_pet & stored in parameters    
describe_pet('hamster', 'Harry')        
describe_pet('dog', 'Doug')             

# Examples of two keyword arguments that are passed to describe_pet & stored in parameters  
describe_pet(pet_type='frog', pet_name='Fred') 
describe_pet(pet_name='Carl', pet_type = 'cat')
