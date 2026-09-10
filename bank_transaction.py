# Write a Python program for a bank account. Create a function bank_account()
# that has an inner function deposit() to add money to the account balance.
# The balance should be maintained outside the inner function.
# Also, create a decorator that prints "Transaction started"
# before the function runs and "Transaction completed" after it runs.
# Deposit 1000, 500, and 2000, and display the final balance.
# give file name gor this question

def dec1(func):
    def wrapper(*args,**kwargs):
        print("Transaction Started")
        func(*args,**kwargs)
        print("Transaction completed")
    return wrapper

balance = 0
def bank_account():
    @dec1
    def deposit(amt):
        global balance
        balance+=amt
        print(balance)
    return deposit
x=bank_account()
x(1000)
x(50)
x(100)