# #decorators practice
#
# # Create a function place_order(item)
# #     Write a decorator that prints:
# #     * “Function started” before execution
# #     * “Function ended” after execution
#
# def dec1(func):
#     def wrapper(item):
#         print("Function Started")
#         func(item)
#         print("Function ended")
#     return wrapper
# def place_order(item):
#     print(item)
# place_order=dec1(place_order)
# place_order("coffe")
#
# # Create a function get_message() that returns "hello user".
# # Write a decorator using @ syntax that converts the output to uppercase.
# def dec1(func):
#     def wrapper():
#         r=func()
#         x=r.title()
#         return x
#     return wrapper
# @dec1
# def get_function():
#     return "hello user"
#
# print(get_function())
#
# # Create a function get_number() that returns 10
# # Use a decorator to return double the value.
#
# def dec2(func):
#     def wrapper():
#         x=func()
#         t=x+x
#         return t
#     return wrapper
# @dec2
# def get_number():
#     return 10
# print(get_number())
#
# # Create a function login(username) Use a decorator to print: * “Authenticating
# # user…” * “Login successful”
#
# def dec1(func):
#     def wrapper():
#         print("Authenticating user")
#         func()
#         print("Login Successful")
#     return wrapper
# def login():
#     return "Admin"
# print(login())
#
# # Create a function add(a, b) Use a decorator to print:
# #     * “Calculating sum…”
# #     * “Calculation done”
#
# def dec1(func):
#     def wrapper(a,b):
#         print("calculating sum")
#         r=func(a,b)
#         print("calculation done")
#         return r
#     return wrapper
# @dec1
# def add(a,b):
#     return a+b
# # print(add(10,20))
#
# # Create a function apply_discount(price) Use a decorator to print:
# # * “Applying discount…”* “Discount applied”
#
# def dec1(func):
#     def wrapper(price):
#         print("Applying Discount")
#         r=func(price)
#
#         print("Discount applied")
#         return r - (r * 0.1)
#
#     return wrapper
#
# @dec1
# def apply_discount(price):
#     return price
# print(apply_discount(1000))
#
#
#
#
#
print("hello")
