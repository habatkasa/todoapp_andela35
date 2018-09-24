

# --- accounts.py --
# This file contains code for managing your account


accounts = {'kasasa':'2345n' } #dictionary where key is the pasword, value is user

def add_account(name,password ):
    """
    adds the key value pair to accounts dictionary
    """
    
    accounts = {name:password}
    
    return accounts

    

def login(password, name):

    """
    returns true if the password and corresponding name exist in the 
    accounts dicitionary
    """
    for k, v in accounts.items():
       
        if password == k and name == v:
            print('Welcome\n.You are now logged in')
            
            return True
        else:
            return False




