# This function will greet a list of users

# Source code/inspiration/software
    # Python Crash Course by Eric Matthews, Chapter 8, example 7+
    # Made with Mu 1.0.3 in October 2021

def greet_users(names):                     # names is used as a python parameter
    """Greet a list of users"""
    for name in names:
        greeting = "Hello, " + name.title() + "!"
        print(greeting)

usernames = ['hannah', 'ty', 'margot']      # usernames is a list
greet_users(usernames)                      # usernames is used as an argument
