# This script will change global variables

# Reference:
    # Object-Oriented Python by Irv Kalb
    # https://github.com/IrvKalb/Object-Oriented-Python-Code
    # Chapter 1

# Made with Mu v.1.0.3
    # January 2023
    # https://codewith.mu

accountName = 'Joe'
accountPassword = 'a23'
accountBalance = 100

def AccountData():
    global accountName, accountPassword, accountBalance
    #print(accountName, accountPassword, accountBalance)
    name = accountName
    password = accountPassword
    balance = accountBalance
    print(name, password, balance)
    
def UpdateAccount(password):
    global accountPassword
    accountPassword = password
    print(password)
    
AccountData()
UpdateAccount('b24')
print(accountPassword)
