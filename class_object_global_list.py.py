# A bank wants to create a simple system to store customer account details.
# Create a class BankAccount with a class variable bank_name = "ABC Bank"
# and instance variables account_holder, account_number, and balance.
# Initialize the instance variables using a constructor. The constructor should
# validate that the initial balance is not negative; if it is negative,
# set the balance to 0. Create two account objects and display their details.
class BankAccount:
    bank_name="ABC Bank"
    def __init__(self,account_holder,account_number,balance):
        self.account_holder=account_holder
        self.account_number=account_number
        if balance>0:
            self.balance=balance
        else:
            self.balance=0

obj1=BankAccount("Bob","23445",10000)
obj2=BankAccount("jack","28885",-2000)


def display(x):
    print(BankAccount.bank_name)
    print(x.account_holder)
    print(x.account_number)
    print(x.balance)
display(obj1)
display(obj2)
print(obj1.__dict__)
print(obj2.__dict__)

# A college wants to maintain student records. Create a class Student with a
# class variable college = "ABC College" and instance variables name, roll_no,
# and marks. Initialize these values using _init_(). The constructor should validate
# that marks are between 0 and 100; if invalid marks are provided, set them to 0.
# Create three student objects and display their details
class Student:
    college="ABC College"
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        if(0<=marks<=100):
            self.marks=marks
        else:
            self.marks=0
s1=Student("Bob","2",90)
s2=Student("Bob","2",-90)
s3=Student("Bob","2",190)
print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)

# An online store wants to maintain a list of products added to its system.
# Create a global list products = []. Create a class Product with a class variable
# store_name = "ABC Store" and instance variables name, price, and quantity. Initialize
# the values using the constructor and validate that price and quantity cannot be negative.
# Whenever a product object is created, add its name to the global products list.
# Create three products and display the product details and the complete product list
products=[]
class Products:
    stora_name="ABS Store"
    def __init__(self,name,price,quantity):
        global products
        self.name=name
        if(price >0):
            self.price=price
        else:
            self.price=0
        if(quantity>0):
            self.quantity=quantity
        else:
            self.quantity=0

        products.append(self.name)
obj1=Products("bob",1000,2)
obj2=Products("saul",500,-12)
obj3=Products("diana",-1500,4)
print(obj1.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)
print(products)

# A company wants to generate basic salary information when employee objects are created.
# Create a class Employee with class variables company = "TechCorp" and employee_count = 0.
# The constructor should accept name, department, salary, and experience. Validate that salary
# and experience are not negative. Based on experience, calculate a bonus inside the
# constructor: employees with more than 5 years receive 15%, employees with 3–5 years
# receive 10%, and employees with less than 3 years receive 5%. Create an instance dictionary
# pay_details containing the employee’s name, salary, experience, bonus, and final salary.
# Generate an employee ID using employee_count. Create three employee objects and display
# their _dict_.

class Employee:
    company="TechCorp"
    employee_count=0
    def __init__(self,name,department,salary,experience):
        self.name=name
        self.department=department
        Employee.employee_count+=1
        self.employee_id =Employee.employee_count
        if(salary>=0):
            self.salary=salary
        else:
            self.salary=0
        if(experience>=0):
            self.experience=experience
        else:
            self.experience=0

        if(experience>5):
            bonus=self.salary*0.15
        elif (experience > 3 and experience<5):
            bonus = self.salary * 0.10
        else:
            bonus = self.salary * 0.05
        total_salary =self.salary + bonus
        self.pay_details={
            "employee_name":self.name,
            "salary":salary,
            "experience":experience,
            "bonus":bonus,
            "total_salary":total_salary
        }
obj1=Employee("bob","python",10000,4)
obj2=Employee("Diana","html",10000,10)
obj3=Employee("ABC","java",10000,2)
print(obj1.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)
print(obj1.pay_details)

# A mobile store creates a purchase object whenever a customer buys a phone.
# Create a class MobilePurchase with a class variable store_name = "Smart Mobiles" and
# purchase_count = 0. The constructor should accept customer, brand, price, storage,
# and quantity. Validate that price and quantity are positive and that storage is
# either 64, 128, 256, or 512 GB. Calculate the total price inside the constructor.
# If the total exceeds ₹50,000, apply a 10% discount; otherwise, apply a 5% discount.
# Store the complete purchase information in a dictionary called purchase_details.
# Increment purchase_count for every valid purchase. Create three objects and display
# their _dict_.

class MobilePurchase:
    store_name="SmartMobiles"
    purchase_count=0
    def __init__(self,customer,brand,price,storage,quantity):
        self.customer=customer
        self.brand=brand
        self.storage=storage
        if(price<0 and quantity<0):
            self.price=0
            self.quantity=0
        else:
            MobilePurchase.purchase_count+=1
            self.count=MobilePurchase.purchase_count

            self.price=price
            self.quantity=quantity

        total_price=self.price*self.quantity
        if(total_price>50000):
            discount=total_price*0.10
        else:
            discount=total_price*0.05
        after_bonus=total_price-discount
        self.purchase_details={
            "custumor_name":customer,
            "brand":brand,
            "price":price,
            "storage":storage,
            "quantity":quantity,
            "total_price":total_price,
            "after_bonus":after_bonus
        }
m1=MobilePurchase("bob","ryzen",100000,16,2)
m2=MobilePurchase("jack ","intel",50000,8,5)
print(m1.__dict__)
print(m2.__dict__)
#


