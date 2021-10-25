# This function will take a inputted name and capitalize it - return value example

# Source code/inspiration/software
    # Python Crash Course by Eric Matthews, Chapter 8, Example 4
    # Made with Mu 1.0.3 in October 2021

def get_formatted_name(first_name, last_name):
    """"Capitalize an inputted name"""
    full_name = first_name + ' ' + last_name
    return full_name.title()                 # return takes a function value & sends it to a function call

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
