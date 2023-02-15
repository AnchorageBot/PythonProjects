# This script will use object oriented programming for managing bank accounts

# References:
    # Object-Oriented Python by Irv Kalb
    # Chapter 4
    # https://nostarch.com/object-oriented-python
    # https://github.com/IrvKalb/Object-Oriented-Python-Code
    # https://github.com/IrvKalb/Object-Oriented-Python-Code/tree/master/Chapter_4/BankOOP5_SeparateBankClass
    
# Made with Mu v.1.0.3
    # February 2023
    # https://codewith.mu

# Account class

class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password
   
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

    def getBalance(self, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        return self.balance

    # Added for debugging
    def show(self):
        print('       Name:', self.name)
        print('       Balance:', self.balance)
        print('       Password:', self.password)
        print()

# Bank Class

class Bank():

    def __init__(self):
        self.accountsDict = {}
        self.nextAccountNumber = 0

    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = oAccount
        # Increment to prepare for next account to be created
        self.nextAccountNumber = self.nextAccountNumber + 1
        return newAccountNumber

    def openAccount(self):
        print('*** Open Account ***')
        userName = input('What is the name for the new user account? ')
        userStartingAmount = input('What is the starting balance for this account? ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('What password would you want to use for this account? ')

        userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
        print('Your new account number is:', userAccountNumber)
        print()

    def closeAccount(self):
        print('*** Close Account ***')
        userAccountNumber = input('What is your account number? ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('What is your password? ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userPassword)

        if theBalance is not None:
            print('You had', theBalance, 'in your account, which is being returned to you.')
            # Remove user's account from the dictioary of accounts
            del self.accountsDict[userAccountNumber]
            print('Your account is now closed.')

    def balance(self):
        print('*** Get Balance ***')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    def deposit(self):
        print('*** Deposit ***')
        accountNum = input('Please enter the account number: ')
        accountNum = int(accountNum)
        depositAmount = input('Please enter amount to deposit: ')
        depositAmount = int(depositAmount)
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[accountNum]        
        theBalance = oAccount.deposit(depositAmount, userAccountPassword)
        if theBalance is not None:
            print('Your new balance is:', theBalance)

    def show(self):
        print('*** Show ***')
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print('   Account number:', userAccountNumber)
            oAccount.show()

    def withdraw(self):
        print('*** Withdraw ***')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userAmount = input('Please enter the amount to withdraw: ')
        userAmount = int(userAmount)
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.withdraw(userAmount, userAccountPassword)
        if theBalance is not None:
            print('Withdrew:', userAmount)
            print('Your new balance is:', theBalance)

    def bankInfo(self):
        print('Hours: 9 to 5')
        print('Address: 123 Main Street, Anytown, USA')
        print('Phone:  (650) 555-1212')
        print('We currently have', len(self.accountsDict), 'account(s) open.')
        
# Create an instance of the Bank
oBank = Bank()

# Main code
# Create two test accounts
joesAccountNumber = oBank.createAccount('Joe', 100, 'JoesPassword')
print("Joe's account number is:", joesAccountNumber)

marysAccountNumber = oBank.createAccount('Mary', 12345, 'MarysPassword')
print("Mary's account number is:", marysAccountNumber)

while True:
    print()
    print('To get an account balance, press b')
    print('To close an account, press c')
    print('To make a deposit, press d')
    print('To get bank information, press i')
    print('To open a new account, press o')
    print('To quit, press q')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]  # grab the first letter
    print()
    
    if action == 'b':
        oBank.balance()

    elif action == 'c':
        oBank.closeAccount()

    elif action == 'd':
        oBank.deposit()

    elif action == 'i':
        oBank.bankInfo()

    elif action == 'o':
        oBank.openAccount()

    elif action == 's':
        oBank.show()

    elif action == 'q':
        break

    elif action == 'w':
        oBank.withdraw()

    else:
        print('Sorry, that was not a valid action.  Please try again.')
        
print('Done')
