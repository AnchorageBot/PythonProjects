# This script will test the userPassDeposit function from the simulation of a single bank account

accountPassword = '2a'
accountBalance = 5
    
def userPassDeposit():
    """This function queries the user for their password and allows an account deposit if correct"""
    userPassword = input('Please input your account password:  ')
    
    # https://stackoverflow.com/questions/423379/using-global-variables-in-a-function
    global accountBalance    
    
    if userPassword != accountPassword:
        incorrectPassword = input('You have entered an incorrect password, enter "r" to retry or "q" to quit    ')
        if incorrectPassword == 'r':
            userPassDeposit()
    if userPassword == accountPassword:
        print('Your current account balance is $  ' + str(accountBalance))
        updateBalance = input('Please enter the amount you are depositing using positive whole numbers (integers)  ')
        updateBalance = int(updateBalance)      
        if updateBalance <=0:
            incorrectAmount = input('You have entered an incorrect Amount, enter "r" to retry or "q" to quit    ')
            if incorrectAmount == 'r':
                userPassDeposit()
        if updateBalance >0:
            accountBalance = updateBalance + accountBalance
            print('Your new account balance is $ ' + str(accountBalance))
            userPassDeposit()
        # https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not            
        if isinstance(updateBalance,int) == False:         
            incorrectAmount = input('You have entered an incorrect Amount, enter "r" to retry or "q" to quit    ')
            if incorrectAmount == 'r':
                userPassDeposit()                 
                
userPassDeposit()
