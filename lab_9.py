def open_acct():
    print("new bank account")

def deposit(balance, money): #deposit
    print("Deposited. Your current balance is {0}" .format(balance + money))
    return balance + money

def withdrawal(blance, money): #withdraw
    if balance >= money:
        print("Deposited. Your current balance is {0}" .format(balance - money))
        return balance - money
    else:
        print("You exceed your limit")
        return balance

def withdrawal_night(balance, money):
    commission = 1.50
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 3500)
balance = withdrawal(balance, 500)
balance = deposit(balance, 10000)
balance = deposit(balance, 3500)    
balance = withdrawal(balance, 1000)
balance = withdrawal(balance, 20000)
commission, balance = withdrawal_night(balance, 1000)
print("commission is {0} and your currenct balance is {1}" .format(commission, balance))