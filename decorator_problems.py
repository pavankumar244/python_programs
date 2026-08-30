# def announce(func):
#     def wrapper():
#         print("started")
#         func()
#         print("Ended")
#     return wrapper
#Write a decorator called announce that prints "Starting function..." before and
# "Function finished!" after any function it wraps. Apply it to a function
# say_hi() that prints "Hi!".

# def say_hi():
#     print("Hi")
# say_hi=announce(say_hi)
# say_hi()
# Create a decorator called uppercase that converts the return value of a function
# into uppercase text. Test it on a function greet(name) that returns "hello, {name}".

# def uppercase(fun):
#     def wrapper(*args,**kwargs):
#         r=fun(*args,**kwargs)
#         return str(r).upper()
#
#     return wrapper
# @uppercase
# def greet(name):
#     return f"hello {name}"
# print(greet("pavan"))
# Write a decorator called double_result that multiplies the return value of a
# function by 2. Apply it to a function add(a, b).

# def double(func):
#     def wrapper(*args,**kwargs):
#         r=func(*args,**kwargs)
#         # print(r)
#         return r*2
#     return wrapper
# @double
# def add(a,b):
#     return a+b
# print(add(10,20))
# Build a decorator called validate_positive that checks if all arguments are
# non-negative. If any are negative, print "Error: negative value" and return None.
# Test it on multiply(a, b).

# def validate(func):
#     def wrapper(*args,**kwargs):
#         for i in args:
#             print(i)
#             if(i<0):
#                 return "Invalid"
#             else:
#                 return func(*args,**kwargs)
#
#     return wrapper
# @validate
# def multiply(a,b):
#     return a*b
# print(multiply(-10,20))

# Create a decorator called count_calls that tracks how many times a function has
# been called and prints the count each time. Apply it to a function say_hello().

# def count_calls(func):
#     def wrapper(*args,**kwargs):
#         wrapper.c+=1
#         print(wrapper.c)
#         return func(*args,**kwargs)
#     wrapper.c=0
#
#     return wrapper
# @count_calls
# def say_hello():
#     return "Hello"
# print(say_hello())
# print(say_hello())
# print(say_hello())
# print(say_hello())

# Write a decorator factory called repeat(n) that runs the decorated function
# n times. Apply it to a function echo(msg) and test with @repeat(3).

# def repeat(n):
#     def dec(func):
#         def wrapper(*args,**kwargs):
#             for i in range(n):
#                 r=func(*args,**kwargs)
#                 print(r)
#         return wrapper
#     return dec
# @repeat(3)
# def echo(x):
#     return x
# echo("Hello")


















