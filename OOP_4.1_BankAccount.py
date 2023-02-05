# This script will use object oriented programming for a bank account

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

newAccount = bankAccount('Joe', 1000, 'magic')
newAccount.show()

newDeposit = newAccount.deposit(150, 'magic')
newAccount.show()

balanceQuery = newAccount.getBalance('magic')
print()

newWithdrawal = newAccount.withdraw(100, 'magic')
newAccount.show()
