# this is testing module for the bank_acount module and main function is here

import bank_acount

def main():
    # get the start balance
    start_balance = float(input("Enter the starting balance: "))
    
    # making  BankAcount class object as saving amount
    saving = bank_acount.BankAcount(start_balance)
    
    # deposit the user's paycheck
    pay = float(input('how much you paid this week : '))
    print("I'll deposit into the acount")
    saving.deposit(pay)
    
    # display the balance
    print('Your current balance is : $', format(saving.get_balance(), ' ,.2f'), sep='')
    
    # amount to withdraw
    withdraw_cash = float(input('How much you want to withdraw : '))
    saving.withdraw(withdraw_cash)
    
    # display the current balance
    print('Your current balance is : $', format(saving.get_balance(), ' ,.2f'), sep='')
    
# call the main function
main()