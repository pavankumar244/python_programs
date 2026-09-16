
# Create a class Student that stores a student’s name, roll number, and marks.
# Create an instance method to display the student’s details and another instance
# method to calculate the student’s percentage. Create a class method to keep track
# of the total number of students created. Also create a static method that accepts
# marks and returns "Pass" if the marks are 40 or above, otherwise "Fail".
# Create multiple student objects and test all the methods.

# class Student:
#     c=0
#     def __init__(self,student_name,roll_no,marks):
#         self.student_name=student_name
#         self.roll_no=roll_no
#         self.marks=marks
#         Student.c+=1
#     def display(self):
#         print("name is",self.student_name)
#         print("My roll is ",self.roll_no)
#         print("My marks are",self.marks)
#     def percentage(self):
#         per=sum(self.marks)//len(self.marks)
#         print(per)
#     @classmethod
#     def count(cls):
#         return cls.c
#     @staticmethod
#     def checker(marks):
#         if(sum(marks)>=40):
#             return "Pass"
#         else:
#             return "Fail"
# obj1=Student("Pavan",4,[50,30,10])
# obj2=Student("bob",1,[12,45,90,41,60])
# obj3=Student("jack",3,[10,43,78,54,24])
#
# obj1.display()
# obj1.percentage()
# print(obj1.checker(obj1.marks))
# obj2.display()
# obj3.display()


#Create a class BankAccount that stores account holder name, account number,
# and balance. Create instance methods to deposit and withdraw money and to display
# the current balance. Create a class method to display the bank name, which is
# common to all accounts. Create a static method to check whether a withdrawal amount
# is valid, where the amount must be greater than zero. Create two account objects
# and test the methods.
# class BankAccount:
#     bank_name="ABC Bank"
#     def __init__(self,account_holder,account_number,balance):
#         self.account_holder=account_holder
#         self.account_number=account_number
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+amount
#         print("Credited",amount)
#     def withdraw(self,amount):
#         if(self.valid_amount(amount)>0):
#             self.balance-amount
#             print("Withdraw",amount)
#         else:
#             print("Insufficient funds")
#     def check_balance(self):
#         print("Your available balance",self.balance)
#
#     @classmethod
#     def display(cls):
#         return cls.bank_name
#     @staticmethod
#     def valid_amount(amount):
#         if(amount<=self.balance):
#             return ""
#         else:
#             return "Valid amount"
# obj1=BankAccount("pavan",123456,10000)
#
# obj1.deposit(1000)
# obj1.check_balance()
# print(obj1.withdraw(2000))
# print(obj1.valid_amount(100))
# print(BankAccount.display())
# Create a class Appointment that stores patient name, doctor name, and consultation fee.
# Create an instance method to display the appointment details and calculate the final
# consultation amount. Create a class method to display the hospital name.
# Create a static method to check whether the consultation fee is greater than zero.
# Create multiple appointment objects and demonstrate the use of instance,
# class, and static methods.
class Appointment:
    hospital_name="CVCORP"
    def __init__(self,patient_name,doctor_name,cons_fee):
        self.patient_name=patient_name
        self.doctor_name=doctor_name
        self.cons_fee=cons_fee
    def display(self):
        print("Appointment Details")
        print("Patient name",self.patient_name)
        print("Doctors name",self.doctor_name)
        if((self.cons_fee)>0):
            print("consolation Fee",self.calculate())
        else:
            print("Invalid Fee")
    def calculate(self):
        gst=self.cons_fee*0.18
        sgst=self.cons_fee*0.1
        self.cons_fee+=gst+sgst
        return self.cons_fee
    @classmethod
    def h_name(cls):
        return "Hospital Name is ",cls.hospital_name
    @staticmethod
    def s1(cons_fee):
        return cons_fee>0
obj1=Appointment("bob","diana",200)
obj2=Appointment("jacks","vamos",-200)
obj1.display()
print(Appointment.s1(obj1.cons_fee))

# obj2.display()
# print(Appointment.s1(obj2.cons_fee))
print(Appointment.h_name())






