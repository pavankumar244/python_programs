# A banking application has a function check_balance().
# Create two decorators: verify_user, which prints "User verified",
# and log_transaction, which prints "Transaction logged". Apply both
# decorators to check_balance() and display "Balance displayed" from the
# original function.
#
# def verify_user(func):
#     def wrapper():
#         print("User Verified")
#         func()
#     return wrapper
#
# def log_transaction(func):
#     def wrapper():
#         print("Transaction logged")
#         func()
#     return wrapper
#
#
# @verify_user
# @log_transaction
# def check_balance():
#     print("Balance Displayed")
# check_balance()

# An online examination system has a function start_exam(student).
# Before allowing the student to start the exam, the system must verify
# the student’s login and then log the exam activity. Create two decorators,
# login_required and log_activity, and apply both decorators to start_exam().
# The function should finally display "Exam started for <student>".
def login_required(func):
    def wrapper(student):
        print("Login Verified")
        func(student)
    return wrapper
def log_activity(func):
    def wrapper(student):
        print("activity logged")
        func(student)
    return wrapper
@login_required
@log_activity
def start_exam(student):
    print("Exam started for",student)
start_exam("Pavan")

#An online shopping application has a function place_order(). Create two
# decorators: login_check to print "Login verified" and order_log to print "Order
# recorded". Apply both decorators to place_order() and display "Order placed
# successfully" from the original function.

