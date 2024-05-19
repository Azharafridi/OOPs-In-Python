# this is the Bank Acount class file

class BankAcount:
    
    def __init__(self, bal):
        
        self.__balance = bal
        
    
    # method for deposit balance
    def deposit(self, amount):
        self.__balance += amount
        
    # withdraw function
    def withdraw(self, amount):
        if amount > self.__balance:
            print('you have In suffient funds for this withdraw. Thank you')
        else: 
            self.__balance -= amount
            
    
    def get_balance(self):
        return self.__balance
    
        