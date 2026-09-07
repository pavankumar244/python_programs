# def decorator1(func):
#     def wrapper(*args,**kwargs):
#         print("Before Calling")
#         func(*args,**kwargs)
#         print("After Calling")
#     return wrapper
# def add(a,b):
#     print(a+b)
# add=decorator1(add)
# add(10,20)
#
# def decorator1(func):
#     def wrapper(*args,**kwargs):
#         print("Before Calling")
#         func(*args,**kwargs)
#         print("After Calling")
#     return wrapper
# @decorator1
# def add(a,b):
#     print(a+b)
# add(10,20)
#
#
# #Create a function get_message() that returns "hello user". Write a decorator
# # using @ syntax that converts the output to uppercase.
# def decorator2(func):
#     def wrapper(*args,**kwargs):
#         r=func(*args,**kwargs)
#         return r.upper()
#     return wrapper
# @decorator2
# def get_message(name):
#     return name
# print(get_message("hello user"))
#
# # Create a function get_number() that returns 10
# #     Use a decorator to return double the value.
#
# def decorator3(func):
#     def wrapper(x):
#         r=func(x)
#         return r+r
#     return wrapper
# # @decorator3
# def get_number(x):
#     return x
# y=decorator3(get_number)
# print(y(10))
#
# # Create a function place_order(item)
# #     Use a decorator to print:
# #     * “Order process started”
# #     * “Order process completed”
#
# import functools
# def decorator4(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print("Order Process started")
#         func(*args,**kwargs)
#         print("Order process completed")
#     return wrapper
# @decorator4
# def place_order(item):
#     print(item)
# place_order("dosa")
#
# # Create a function login(username)
# #     Use a decorator to print:
# #     * “Authenticating user…”
# #     * “Login successful”
# #
# def decorator5(func):
#     def wrapper(user):
#         print("Authenticating User")
#         func(user)
#         print("Login Succcessful")
#     return wrapper
#
# def decorator5(func):
#     def wrapper(user):
#         print("Authenticating User")
#         func(user)
#         print("Login Succcessful")
#     return wrapper
# @decorator5
# def login(username):
#      print(username)
# login("Pavan")
#
# def method1():
#     print("HELLO")
# print(method1.__type_params__)
#
#
# def dec1(func):
#     def wrap1(*args,**kwargs):
#         print("Hi")
#         func(*args,**kwargs)
#
#     return wrap1
#
# def dec2(func):
#     def wrap2(*args,**kwargs):
#         func(*args,**kwargs)
#         print("BYE")
#     return wrap2
# @dec1
# @dec2
# def my_name(name):
#     print("My name is ",name)
# # x=dec1(my_name)
# # y=dec2(x)
# my_name("Bob")
#
# # 1. A banking application has a function check_balance().
# # Create two decorators: verify_user, which prints "User verified",
# # and log_transaction, which prints "Transaction logged".
# # Apply both decorators to check_balance() and display "Balance displayed"
# # from the original function.
#
# #1
# def verify_user(func):
#     def wrapper1():
#         print("User Verified")
#         func()
#     return wrapper1
#
# def log_Transaction(func):
#     def wrapper2():
#         print("Transaction Logined")
#         func()
#     return wrapper2
#
# def check_balance():
#     print("Balance displayed")
# x=verify_user(check_balance)
# y=log_Transaction(x)
# y()
#
# # 2. ⁠An online examination system has a function start_exam(student).
# # Before allowing the student to start the exam, the system must verify the
# # student’s login and then log the exam activity. Create two decorators,
# # login_required and log_activity, and apply both decorators to start_exam().
# # The function should finally display "Exam started for <student>".
#
#
# def login_required(func):
#     def wrapper1(*args,**kwargs):
#         print("Login is Required")
#         func(*args,**kwargs)
#     return wrapper1
# def log_activity(func):
#     def wrapper2(*args,**kwargs):
#         print("Student can login")
#         func(*args,**kwargs)
#     return wrapper2
# def start_exam(student):
#     print("Exam started for",student)
# x=login_required(start_exam)
# y=log_activity(x)
# y("BOB")
#
#
# # 3. ⁠An online shopping application has a function place_order().
# # Create two decorators: login_check to print "Login verified" and
# # order_log to print "Order recorded". Apply both decorators to place_order()
# # and display "Order placed successfully" from the original function.
#
# def login_check(func):
#     def wrapper1():
#         print("Login Verified")
#         func()
#     return wrapper1
# def order_log(func):
#     def wrapper2():
#         print("Order recorded")
#         func()
#     return wrapper2
# def place_order():
#     print("Order Placed Successfully")
# login_check=login_check(place_order)
# order_log=order_log(login_check)
# order_log()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
