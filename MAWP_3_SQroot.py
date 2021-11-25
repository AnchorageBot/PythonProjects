# This script will provide an example of how to query a user in order to approximate a square root

# Source code/inspiration/software
    # Math Adventures with Python by Peter Farrell, Chapter 3+
    # Made with Mu 1.0.3 in November 2021

def QueryGuessCheck():
    """Queries user for parameters, approximates square root"""
    
    print("This program will approximate square roots of numbers")
    num = int(input("\nWhat number would you like to take the square root of? \n"))
    low = int(input("\nGuess the smallest number that the square root might be? \n"))
    high = int(input("\nGuess the largest number that the square root might be? \n"))
    
    for i in range(20):
        guess = (low + high)/2                          # guess variable takes the average of the low and high parameters
        if guess**2 == num:                             # guess variable is squared and compared to num variable
            print(guess)
        elif guess**2 > num:
            high = guess                                # replace high with guess
        else: 
            low = guess                                 # replace low with guess
    print("The approximate square root is ...", guess)
    
def main():
    QueryGuessCheck()
    
    query = input("\nWould you like to run the script again/refine your approximation? \n")
    if query == "yes":
        print("\nRunning the program again \n")
        main()
    else:
        print("\nOk, the script has ended \n")
    
if __name__ == "__main__":                                  
    main()
