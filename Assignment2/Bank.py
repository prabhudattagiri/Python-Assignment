balance = 3000

def deposit(amount):
    global balance
    balance =balance+amount
    print(amount,"Rs deposited successfully")
    print("Updated balance is",balance)

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance")
        return
    balance =balance-amount
    if balance < 3000:
        print(amount,"Rs withdrawn Please Maintain a fixed amount 3000 in the account")
    else:
        print(amount,"Rs withdrawn successfully")
    print("Current balance is ",balance)

def checkBalance():
    global balance
    print("Current balance ",balance)