# This script will use object oriented programming for managing bank accounts using a dictionary

# This script includes an example of a simplified main function
    # allows the script to be used as a reusable module or standalone script
        # import script as a reusable module 
            # __name__ = module's filename
        # standalone script
            # __name__ = __main__
        # from the command line
            # Save file as OOP_4.2.1_BankAccount.py on the desktop
            # Open terminal
            # cd desktop
            # python3 OOP_4.2.1_BankAccount.py

# Definitions and concepts
    # A class is a blueprint for an object
    # An object is a set of variables and methods
    # <object>.<methodName>(<any arguments>)
    # A method is a function inside of a class
    # All methods have a special first parameter named <self>

# Reference:
    # Object-Oriented Python by Irv Kalb
    # Chapter 4
    # https://nostarch.com/object-oriented-python
    # https://github.com/IrvKalb/Object-Oriented-Python-Code

# Made with Mu v.1.0.3
    # February 2023
    # https://codewith.mu

class bankAccount():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def getBalance(self, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        #return self.balamce
        #else:
            #return self.balance
        print(self.balance)
        #else:
            #print(self.balance)

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None

        if amountToDeposit < 0:
            print('You cannot deposit a negative amount')
            return None

        self.balance = self.balance + amountToDeposit
        return self.balance

    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print('Incorrect password for this account')
            return None

        if amountToWithdraw < 0:
            print('You cannot withdraw a negative amount')
            return None

        if amountToWithdraw > self.balance:
            print('You cannot withdraw more than you have in your account')
            return None

        self.balance = self.balance - amountToWithdraw
        return self.balance

    def show(self):
        """This method(function) is for testing/debugging"""
        print('       Name:', self.name)
        print('       Balance:', self.balance)
        print('       Password:', self.password)
        print()

def main():
    """this function calls the various script functions"""
    
    accountsDict = {}
    AccountNumberTracker = 0

    aAccount = bankAccount('Joe', 100, 'JoesPassword')
    joesAccountNumber = AccountNumberTracker
    accountsDict[joesAccountNumber] = aAccount

    AccountNumberTracker = AccountNumberTracker + 1

    bAccount = bankAccount('Mary', 1000, 'MarysPassword')
    marysAccountNumber = AccountNumberTracker
    accountsDict[marysAccountNumber] = bAccount

    aAccount.show()
    #accountsDict[joesAccountNumber].show()

    #bAccount.show()
    accountsDict[marysAccountNumber].show()

    print('The number of accounts currently in the database is: ', len(accountsDict))
    
if __name__ == "__main__":                      # when the if statement evaluates True, main() is executed
    main()  
