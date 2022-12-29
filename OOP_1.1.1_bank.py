# This script will simulate a single bank account

# Reference:
    # Object-Oriented Python by Irv Kalb
    # Chapter 1

# Made with Mu v.1.0.3
    # December 2022
    # https://codewith.mu

# Variables:
    # Global: accountName, accountBalance, accountPassword
    # Local(userPassBalance function): userPassword
    # Local( while true loop): action
    
accountName = 'Joes_Account'
accountBalance = 5
accountPassword = '2a'

def accountInstructions():
    """This function displays account instructions"""
    print('************************************')    
    print('********Account Instructions********')
    print('************************************')
    print('**Enter "b" for account balance*****')
    #print('**Enter "d" for account deposit*****')
    #print('**Enter "w" for account withdrawal**')
    #print('**Enter "s" to show account*********')
    print('**Enter "q" to quit*****************')
    print('************************************')    
    
def userPassBalance():
    """This function queries the user for their password and provides account balance if correct"""
    userPassword = input('Please input your account password:  ')
    
    if userPassword != accountPassword:
        incorrectPassword = input('You have entered an incorrect password, enter "r" to retry or "q" to quit    ')
        if incorrectPassword == 'r':
            userPassBalance()
        if incorrectPassword == 'q':
            print('Goodbye')
            #break
    else:
        print('Your balance is ' + str(accountBalance))
        #break
    
while True:
    accountInstructions()
    
    action = input('What do you want to do?    ')
    action = action.lower() # convert input to lower case
    action = action[0] # convert input to first letter only

    if action == 'b':
        userPassBalance()
        
    if action =='q':
        print('Goodbye')
        break
