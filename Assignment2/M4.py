# 4. WAP to perform following using module and function for deposit,withdraw,check balance for banking application
# I. Assign a fixed value as balance for account
# II. Deposit user defined amount and display updated balance 
# III. Withdraw user defined money if user has sufficient fund otherwise shoe insufficient fund
# IV. Check for balance
# V. Maintain a fixed amount 3000 in the account

import Bank
# Assign a fixed value as balance for account
Bank.balance = 5000
n=int(input("Enter amount to deposit in the bank : "))
Bank.deposit(n)
w=int(input("Enter amount to withdraw from bank : "))
Bank.withdraw(w)
Bank.checkBalance() # for check current balance