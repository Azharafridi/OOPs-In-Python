"""

Exercise 43. Bank Account class: ||  Solution
Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber 
(numeric type), name (name of the account owner as string type), balance.
Create a constructor with parameters: accountNumber, name, balance.
Create a Deposit() method which manages the deposit actions.
Create a Withdrawal() method  which manages withdrawals actions.
Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
Create a display() method to display account details.
Give the complete code for the  BankAccount class.
    
"""

class BankAccount():
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    # deposit method    
    def deposit(self):
        deposite = int(input("enter amount you want to deposit : /n"))
        self.deposite = deposite
        self.balance = self.balance + deposite
    # withdraw method  
    def withDrawal(self):
        withdraw_amount = int(input("enter amount you want to withdraw : /n"))
        if balance >= withdraw_amount:
            balance = balance -withdraw_amount
            print("the new balance in acount is : {} " .format(self.balance))
        else:
            print("sorry you current balance is less than withdraw amount.")
            print("please recharge your account ")
            
    # bank fee method
    def bank_fee(self):
        print("bank fee is 5%")
        bank_fee = 0.05
        self.balance = self.balance -(self.balance * bank_fee)
        print('your balance after bank fee apply is : {}' .format(self.balance))
        
    def display(self):
        print("name is {},/n account number {},/n current balance {}".format(self.name,self.accountNumber,self.balance))
            
                    
def main():
    bankacc = BankAccount(21202, 'azhar', 99999)

    print("1.Deposit amount /n2.Withdraw amount /n3.apply bank fee /n4.show account details") 
    choice  = int(input("enter your choice : "))
    if choice >=1 and choice <=4:
        if choice == 1:
            bankacc.deposit()
        elif choice ==2:
            bankacc.withDrawal()
        elif choice ==3:
            bankacc.bank_fee()
        else:
            bankacc.display()       
    else: 
        print("please enter right integer : and try again.")
              
main()      