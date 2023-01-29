# This script will use dictionaries for updating multiple bank accounts

# Reference:
    # Object-Oriented Python by Irv Kalb
    # https://github.com/IrvKalb/Object-Oriented-Python-Code
    # Chapter 1

# Made with Mu v.1.0.3
    # January 2023
    # https://codewith.mu
    
accountsList = []

def newAccount(aName, aBalance, aPassword):
    """This function will allow the admin to update the account database"""
    global accountsList
    newAccountDict = {'name':aName, 'balance':aBalance, 'password':aPassword}
    accountsList.append(newAccountDict)
    print("Account database now contains the following customers: ", accountsList)

def adminQuery():
    """This function will ask the admin if they need to add an account"""
    query = input("Would you like to add another account to the database?: ")
    if query == "yes":
        #newAccount(aName, aBalance, aPassword)
        #name = input('Please input the new customers name, balance, password:  ')
        newAccount('carl', '50', 'd5b')
        newAccount('mel', '50', 'x7a')
    else:
        print("Goodbye")

adminQuery()
