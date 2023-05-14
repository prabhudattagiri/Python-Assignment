# 3. WAP to perform following using class and object and multilevel inheritance 
# and also use list for different users for deposit,withdraw,check balance for 
# banking application
# I. Generate account number of new user and store informationlike 
# account number,name,mobile no and initial balance in different list
# II. Assign a fixed value as balance for account
# III. Deposit user defined amount and display updated balance 
# IV. Withdraw user defined money if user has sufficient fund otherwise 
# shoe insufficient fund
# V. Check for balance
# VI. Maintain a fixed amount 3000 in the account

class Account:
    def __init__(self, account_number, name, mobile_no):
        self.account_number = account_number
        self.name = name
        self.mobile_no = mobile_no


class Balance(Account):
    def __init__(self, account_number, name, mobile_no, initial_balance):
        super().__init__(account_number, name, mobile_no)
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully. Updated balance:", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Amount withdrawn successfully. Updated balance:", self.balance)
        else:
            print("Insufficient funds. Cannot withdraw amount.")

    def check_balance(self):
        return self.balance


class BankingApp:
    def __init__(self):
        self.accounts = []

    def generate_account_number(self):
        if len(self.accounts) > 0:
            last_account = self.accounts[-1]
            account_number = last_account.account_number + 1
        else:
            account_number = 1
        return account_number

    def create_account(self, name, mobile_no, initial_balance):
        account_number = self.generate_account_number()
        account = Balance(account_number, name, mobile_no, initial_balance)
        self.accounts.append(account)
        print("Account created successfully. Account Number:", account_number)


# Create a banking application
banking_app = BankingApp()

# Create a new account
name = input("Enter your name: ")
mobile_no = input("Enter your mobile number: ")
initial_balance = 3000  # Initial balance of 3000 is maintained
banking_app.create_account(name, mobile_no, initial_balance)

# Deposit an amount
deposit_amount = float(input("Enter the amount to deposit: "))
account = banking_app.accounts[0]
account.deposit(deposit_amount)

# Withdraw an amount
withdraw_amount = float(input("Enter the amount to withdraw: "))
account.withdraw(withdraw_amount)

# Check balance
balance = account.check_balance()
print("Current balance:", balance)