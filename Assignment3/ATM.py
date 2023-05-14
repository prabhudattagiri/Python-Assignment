# 4. WAP to perform following using class and object and multilevel inheritance 
# and also use list for different users to implement ATM simulation
# A. Generate account number and accept pin from users of new user 
# and store informationlike account number,pin,name,mobile no and 
# initial balance in different list
# B. Assign a fixed value as balance for account
# C. Ask user to enter account number and pin
# D. Verify user using account number and pin if user is valid then 
# Provide different options like withdraw,fast withdraw,change 
# pin,and check balance otherwise alert user by providing Invalid pin
# or account number
# E. Withdraw user defined money if user has sufficient fund otherwise 
# shoe insufficient fund in withdraw option also in fast withdraw 
# provide some fixed amount like 500,1000,2000,5000 etc as option 
# to user to select for withdraw
# F. Check for balance
# G. If user wants change pin and update pin in the list

class Account:
    def __init__(self, account_number, pin, name, mobile_no):
        self.account_number = account_number
        self.pin = pin
        self.name = name
        self.mobile_no = mobile_no


class Balance(Account):
    def __init__(self, account_number, pin, name, mobile_no, initial_balance):
        super().__init__(account_number, pin, name, mobile_no)
        self.balance = initial_balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Amount withdrawn: {}".format(amount))
        else:
            print("Insufficient funds. Cannot withdraw amount.")

    def fast_withdraw(self, option):
        if option == 1:
            amount = 500
        elif option == 2:
            amount = 1000
        elif option == 3:
            amount = 2000
        elif option == 4:
            amount = 5000
        else:
            print("Invalid option.")
            return

        if self.balance >= amount:
            self.balance -= amount
            print("Amount withdrawn: {}".format(amount))
        else:
            print("Insufficient funds. Cannot withdraw amount.")

    def check_balance(self):
        return self.balance


class ATM:
    def __init__(self):
        self.accounts = []

    def generate_account_number(self):
        if len(self.accounts) > 0:
            last_account = self.accounts[-1]
            account_number = last_account.account_number + 1
        else:
            account_number = 1
        return account_number

    def create_account(self, pin, name, mobile_no, initial_balance):
        account_number = self.generate_account_number()
        account = Balance(account_number, pin, name, mobile_no, initial_balance)
        self.accounts.append(account)
        print("Account created successfully. Account Number: {}".format(account_number))

    def verify_user(self, account_number, pin):
        for account in self.accounts:
            if account.account_number == account_number and account.pin == pin:
                return account
        return None

    def change_pin(self, account, new_pin):
        account.pin = new_pin
        print("PIN changed successfully.")

   
