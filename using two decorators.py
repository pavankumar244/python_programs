# A banking application has a function check_balance().
# Create two decorators: verify_user, which prints "User verified",
# and log_transaction, which prints "Transaction logged". Apply both
# decorators to check_balance() and display "Balance displayed" from the
# original function.

def verify_user(func):
    def wrapper():
        print("User Verified")
        func()
    return wrapper

def log_transaction(func):
    def wrapper():
        print("Transaction logged")
        func()
    return wrapper


@verify_user
@log_transaction
def check_balance():
    print("Balance Displayed")
check_balance()