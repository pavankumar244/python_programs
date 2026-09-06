# A system wants to track the number of times the login() function is called.
# Create a global variable attempts = 0 and a decorator track_attempts that
# increments the global variable every time the login function is executed. The login()
# function should accept username and password as parameters and display
# ("Login attempted"" by <username>"). Call the function three times with different
# usernames and passwords, and finally display the total number of login attempts.
# Use the global keyword inside the decorator to modify the global variable.

attempts=0
def track_attempts(func):
    def wrapper(*args,**kwargs):
        global attempts
        attempts+=1
        return func(*args,**kwargs)
    return wrapper
@track_attempts
def login(username,password):
    print("Login attempted by ",username,"with password is",password)

login("pavan","1234")
login("suresh","234")
login("bob","999")
print(attempts)

#An ATM system has a function withdraw(username, pin, amount). Create a decorator
# authenticate that checks whether the username is "admin" and PIN is "1234". If authentication
# is successful, execute the function; otherwise, display "Invalid credentials".
# The function should maintain a global balance = 10000, deduct the amount if sufficient
# balance exists,and display the remaining balance.
balance=1000
def dec1(func):
    def wrapper(username,pin,amount):
        if(username=="admin" and pin=="1234"):
            return func(username,pin,amount)
        else:
            return "Invalid credentials"
    return wrapper
@dec1
def withdraw(username,pin,amount):
    global balance
    if(amount<=balance):
        balance=balance-amount
        print(balance)
    else:
        print("Invalid")
withdraw("admin","1234",100)

#An online examination system has a function start_exam(username, password, exam_name).
# Create a decorator login_required to authenticate the student and another decorator
# track_attempt to count how many times the exam is started. If authentication is
# successful, display "Exam started for <username>" along with the exam name.
# Finally, display the total number of exam attempts.
c=0
def login_required(func):
    def wrapper(username,password,exam_name):
        if(username=="student" and password=="1234"):
            return func(username,password,exam_name)
        else:
            return "Invalid Details"
    return wrapper

def track_attempts(func):
    def wrapper(username,password,exam_name):
        global c
        c+=1
        return func(username,password,exam_name)
    return wrapper
@login_required
@track_attempts
def start_exam(username,password,exam_name):
    print("student is",username)
    print("Exam is",exam_name)
start_exam("student","1234","python")
start_exam("student","1234","web")
print(c)
