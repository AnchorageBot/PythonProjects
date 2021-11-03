# This function will accept few/many pizza toppings - arbitrary number of arguments function example

# Source code/inspiration/software
    # Python Crash Course by Eric Matthews, Chapter 8, example 10+
    # Made with Mu 1.0.3 in November 2021
    
def make_pizza(size, *toppings):                 # * command to make an empty tuple to accept arguments
    """Prints arbitrary number of toppings"""
    print("\nMaking a " +str(size) + " pizza with the following toppings: ")
    for topping in toppings:
        print('-' + topping)
    
make_pizza('small','cheese')
make_pizza('medium','cheese', 'pepperoni')
make_pizza('large','cheese', 'pepperoni', 'ham')
make_pizza('xtra-large','cheese', 'pepperoni', 'ham', 'pineapple')
