# This script will use lists for updating multiple bank accounts

# Reference:
    # Object-Oriented Python by Irv Kalb
    # https://github.com/IrvKalb/Object-Oriented-Python-Code
    # Chapter 1

# Made with Mu v.1.0.3
    # January 2023
    # https://codewith.mu

accountNamesList = []
accountBalancesList = []
accountNumbersList = []

def newAccount():
    """This function will allow the admin to update the account database"""
    global accountNamesList, accountBalancesList, accountNumbersList
    name = input('Please input the new customers name:  ')
    accountNamesList.append(name)
    print("Account database now contains the following customers: ", accountNamesList)
    balance = input("Please input the new customers balance:  ")
    accountBalancesList.append(balance)
    print("Account database now contains the following balances: ", accountBalancesList)
    number = input("Please input the new customers account number:  ")
    accountNumbersList.append(number)
    print("Account database now contains the following account numbers: ", accountNumbersList)
    adminQuery()
    

def adminQuery():
    """This function will ask the admin if they need to add an account"""
    query = input("Would you like to add another account to the database?: ")
    if query == "yes":  
        newAccount()
    else:
        print("Goodbye")
        
adminQuery()
