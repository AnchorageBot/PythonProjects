# This script will test/prototype a function from the simulation of a single bank account

accountPassword = '2a'
accountBalance = 5
    
def userPassDeposit():
    """This function queries the user for their password and allows an account deposit if correct"""
    userPassword = input('Please input your account password:  ')    
    
    if userPassword != accountPassword:
        incorrectPassword = input('You have entered an incorrect password, enter "r" to retry or "q" to quit    ')
        if incorrectPassword == 'r':
            userPassDeposit()
    if userPassword == accountPassword:
        print('Your current account balance is $  ' + str(accountBalance))
        updateBalance = input('Please enter the amount you are depositing using positive whole numbers (integers)  ')
        updateBalance = int(updateBalance)
        # https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not
        if isinstance(updateBalance,int) == True:
            #print('True')
            NewAccountBalance = updateBalance + accountBalance
            print('Your new account balance is $ ' + str(NewAccountBalance))            
        if isinstance(updateBalance,int) == False:
            #print('False')           
            incorrectAmount = input('You have entered an incorrect Amount, enter "r" to retry or "q" to quit    ')
            if incorrectAmount == 'r':
                userPassDeposit()
                
userPassDeposit()
