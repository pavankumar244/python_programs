# class Person:
#   def __init__(self, name):
#     self.name = name
#   def greet(self):
#     print("Hello, my name is " + self.name)
# p1 = Person("Emil")
# p1.greet()
# Write a class PasswordUtils with three @staticmethod methods:
# is_strong(password) — returns True if the password has:
# length >= 8
# at least one digit
# at least one uppercase letter
# generate_hint(password) — returns the first 2 characters of the password followed by "****".
# validate_email(email) — returns True if both '@' and '.' are present in the email.
from asyncio.windows_events import NULL


class PasswordUtils:
  @staticmethod
  def is_strong(password):
    if(len(password)<8):
      return False
    x = False
    y = False
    for i in password:
      if(i.isupper()):
        x=True
      if(i.isdigit()):
        y=True
    if(x and y):
      return True
    else:
      return False
  @staticmethod
  def generate_hint(password):
    return password[:2]+"*****"
  @staticmethod
  def validate_email(email):
    if("@" in email and "." in email):
      return True
    else:
      return False
s="Pavan12334"
print(PasswordUtils.is_strong(s))
print(PasswordUtils.generate_hint(s))
print(PasswordUtils.validate_email("pavan@gmail.com"))


class Library:
  # Class variable
  library_name = "ABC Library"

  def __init__(self, member_name):
    # Validation
    if member_name == "":
      self.member_name = "Unknown"
    else:
      self.member_name = member_name

    # Object variables
    self.books = []

  # Instance method
  def add_book(self, title):
    if Library.is_valid_title(title):
      self.books.append(title)
      print("Book added:", title)
    else:
      print("Invalid book title")

  # Class method
  @classmethod
  def create_guest(cls):
    return cls("Guest")

  # Static method
  @staticmethod
  def is_valid_title(title):
    if isinstance(title, str) and title != "":
      return True
    else:
      return False


# Demonstrating class variable
print("Library Name:", Library.library_name)

# Creating an object
library1 = Library("Pavan")

print("Member Name:", library1.member_name)
print("Books:", library1.books)

# Testing instance method
library1.add_book("Python Basics")
library1.add_book("")

print("Books:", library1.books)

# Testing class method
guest_library = Library.create_guest()

print("Guest Member:", guest_library.member_name)

# Testing static method
print(Library.is_valid_title("Java"))
print(Library.is_valid_title(""))