# This function will greet a user by name - parameter & argument example

# Source code/inspiration/software
    # Python Crash Course by Eric Matthews, Chapter 8, Example 2
    # Made with Mu 1.0.3 in October 2021
    
def greet_user(username):               # username is used as a Python parameter
    """"Greet a user by name"""    
    print("Hello " + username + "!")
    #print("Hello " + username.title() + "!")
    
greet_user('Harry')                     # Harry is an argument passed to greet_user & stored in username 
