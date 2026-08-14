add=lambda x,y : x+y
print(add(10,20))

square=lambda a:a**2
print(square(10))


# cube
cube=lambda a:a**3
print(cube(3))

# lamba conditional Exp
larger=lambda x,y:"x is larger" if(x>y) else "y is larger"
print(larger(10,20))

l=[1,7,5,80,45,130,42]
# l=["s","p","r","pa","su"]
l.sort(key=lambda x:x/2)
print(l)

even=lambda n:n%2==0
print(even(11))

l=[(10,'banana'),(2,'apple'),(3,'cherry')]
l.sort(key=lambda x:x[0])
l.sort(key=lambda x:x[1])
print(l)

add=lambda x,y:x+y
multiply=lambda a,b:a*b + add(a,b)
print(multiply(10,20))
#
interest=lambda p,t,r:p*t*r/100
print(interest(10000,12,2))

c=lambda x:x*(9/5)+32
print(c(32))

# Write a lambda that calculates bill amount:
# * If units ≤ 100 → ₹5/unit
# * Else → ₹8/unit
# #
bill=lambda x:5 if x<=100 else 8
print(bill(500))

# Q4. Login Check
# Write a lambda that checks if username equals "admin"
# and password equals "1234" and returns ("Login Success"
# or "Invalid")

check=lambda x,y:"Login Success" if (x=="admin" and y==1234) else "Invalid"
print(check("admin",1234))


l=[1,3,6,3,9,6]
d=list(map(lambda x:x**2,l))
print(d)
def square(x):
    return x**2

y=list(map(square,l))
print(y)
l1=[1,2,3,4]
l2=[5,6,7,8]
k=list(map(lambda x,y:x-y,l1,l2))
# print(k)
l=[1,2,3,4]
k=list(map(lambda x:x/2,l))
print(k)

def m(x):
    if x%2==0:
        return True
    else:
        return False
l=[2,5,7,9,8,4]
k=list(filter(m,l))
print(k)

l=[1,2,3,4,5,6]
p=list(map(lambda x:x**2,l))
# print(p)
z=list(filter(lambda x:x%2==0,p))
print(z)


pp=[100,200,300]
def addtax(x):
    return x+x*0.1
k=list(map(lambda x:addtax(x),pp))

print(k)

l=[10,520,4,560,710,2,11,547]
l1=list(map(lambda x: x+x*0.1,l))
l2=list(filter(lambda x:x>500,list(map(lambda x: x+x*0.1,l))))
print(l2)

l=[2,30,45,16,48]
# k=list(filter(lambda x:x>20,l))
l2=list(map(lambda x:x**2,list(filter(lambda x:x>20,l))))
print(l2)

l=['bat','ball','kit','wickets','stumps']
# k=list(filter(lambda x:len(x)>4,l))
l1=list(map(lambda x:x.upper(),list(filter(lambda x:len(x)>4,l))))
print(l1)

l=[2,5,40,54,10,34,65,66,32]
k=list(filter(lambda x:x%5==0,l))
k1=list(map(lambda x:x+10,list(filter(lambda x:x%5==0,l))))
print(k1)

marks=[35,55,40,91,99,77]
list(filter(lambda x:x>40,marks))
l1=list(map(lambda x:x+5,list(filter(lambda x:x>40,marks))))
print(l1)

l=[1,2,3,4,5]
l1=len(l)
from functools import reduce
k=(reduce(lambda x,y:x+y,l))
print(k/l1)


students=[{'name':'Alice','score':85},
          {'name':'Harry','score':79},
          {'name':'bob','score':97}]
k=sorted(students,key=lambda x:x['score'],reverse=True)
print(k)

l=['bob','jack','reo','diana','jackson']
k=sorted(l,key=lambda x:len(x))
print(k)

l=['BOB','jack','Reo','diana','Jackson']
k=list(filter(lambda x:x[0].isupper(),l))
print(k)


l=[1,2,3,4,5]
from functools import reduce
k=(reduce(lambda x,y:x*y,l))
print(k)

t=({'name':'Alice','age':22},
   {'name':'bob','age':18},
   {'name':'jack','age':45})
k=sorted(t,key=lambda x:x['age'],reverse=True)
print(k)

l=[1,2,3,4,5,6,7,8,9,10]
k=list(filter(lambda x:x%2==1,l))
# print(k)
l1=list(map(lambda x:x**2,k))
print(l1)

6



l=['cat','elephant','dog','rhinoceros']
from functools import reduce
k=reduce(lambda x,y:x if len(x)>len(y) else y,l)
print(k)

#Given a list of product prices, write a program to filter prices above ₹500,
# then apply a 10% discount using map(),
# and compute the final total bill using reduce().
l=[100,44,600,520,540,124,750]
k=list(filter(lambda x:x>500,l))
# print(k)
l1=list(map(lambda x:x+0.1*x,k))
print(l1)
from functools import reduce
print(reduce(lambda x,y:x+y,l1))

#Given a list of numbers, write a program to filter negative numbers,
# then convert them into positive numbers using map(), and find their
# sum using reduce().
l=[100,44,-600,-520,540,-124,750,0]
k=list(filter(lambda x:x<0,l))
l1=list(map(lambda x:x*(-1),k)) # use abs() also
print(l1)
from functools import reduce
print(reduce(lambda x,y:x+y,l1))

#Given a list of integers, write a program to filter numbers less than 50,
# then multiply each by 3 using map(), and determine the maximum value using reduce().

l=[10,50,45,74,23,34,49]
k=list(filter(lambda x:x<50,l))
# print(k)
l1=list(map(lambda x:x*3,k))
# print(l1)
from functools import reduce
print(reduce(lambda x,y:x if x>y else y,l1))

#Given a list of words, write a program to filter words with length greater than 3,
# then convert them to uppercase using map(), and concatenate them into a single string
# using reduce().
l=['bob','jack','dia','alice','pavan']
k=list(filter(lambda x:len(x)>3,l))
# print(k)
l1=list(map(lambda x:x.upper(),k))
# print(l1)
from functools import reduce
print(reduce( lambda x,y:x+" "+y,l1))

l=[10000,250000,50000,45000,51000,35000]
k=list(filter(lambda x:x>30000,l))
print(k)
l1=list(map(lambda x:x+x*0.15,k))
from functools import reduce
print(reduce(lambda x,y:x+y,l1))

#A data analysis system stores a list
# of integers. Write a program to filter odd numbers, square each using map(),and
# compute their sum using reduce().

l=[1,3,43,26,22,90,24,51]
k=list(filter(lambda x:x%2==1,l))
# print(k)
l1=list(map(lambda x:x**2,k))
# print(l1)
from functools import reduce
print(reduce(lambda x,y:x+y,l1))

#7. An e-commerce platform stores product prices in a list. Write a program to filter
# products priced above ₹500, apply a 10% discount to those products using map(), and
# then calculate the total bill amount using reduce().

l=[500,4000,1500,420,3500,800,250,1000]
k=list(filter(lambda x:x>500,l))
print(k)
l1=list(map(lambda x:x-(x*0.1),k))
# print(l1)
from functools import reduce
print(reduce(lambda x,y:x+y,l1))

#A banking system stores transaction amounts. Write a program to filter only credit
# transactions (positive values), apply a processing bonus of ₹10 to each using map(),
# and calculate the total credited amount using reduce().

l=[1000,-1500,500,-250,550,-450,0]
k=list(filter(lambda x:x>=0,l))
l1=list(map(lambda x:x+10,k))
from functools import reduce
print(reduce(lambda x,y:x+y,l1))





















