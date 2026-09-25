#creating own Object

class A:
    def __init__(self):
        self.val=1
    def __iter__(self):
        return self
    def __next__(self):
        if (self.val<=5):
            num=self.val
            self.val+=1
            return num
        else:
            raise StopIteration
obj=A()
for i in obj:
    print(i)

#Even Numbers
class EvenNumbers:
    def __init__(self,start,count):
        self.start=start
        self.count=count
    def __iter__(self):
        return self
    def __next__(self):
        if(self.start<=self.count):
            if(self.start%2==0):
                num=self.start
                self.start+=1
                return num
            else:
                self.start+=1
                return self.__next__()
        else:
            raise StopIteration
obj=EvenNumbers(1,5)
for i in obj:
    print(i)
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())

# prime Number
class prime:
    def __init__(self,val):
        self.val=val
    def __iter__(self):
        return self
    def __next__(self):
        fc=0
        for i in range(1,self.val+1):
            if(self.val%i==0):
                fc+=1
        if(fc==2):
            return "Prime"
        else:
            return "Not a Prime"
obj=prime(7)
print(obj.__next__())

# 1.Create an custom iterator that prints numbers from 1 to N,
# where N is given by the user.
class Numbers:
    def __init__(self,n):
        self.n=n
        self.val=1
    def __iter__(self):
        return self
    def __next__(self):
        if(self.val<=self.n):
            num=self.val
            self.val+=1
            return num
        else:
            raise StopIteration
obj=Numbers(10)
for i in obj:
    print(i)
print(obj.__next__())

# 2.	Create an custom iterator that prints numbers from N to 1.

class Numbers:
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        if(self.n>0):
            num=self.n
            self.n-=1
            return num
        else:
            raise StopIteration
obj=Numbers(10)
for i in obj:
    print(i)

# 3.	Create an custom iterator that prints the first N even numbers.
class Numbers:
    def __init__(self,n):
        self.n=n
        self.val=1
    def __iter__(self):
        return self
    def __next__(self):
        if(self.val<=self.n):
            if(self.val%2==0):
                num=self.val
                self.val+=1
                return num
            else:
                self.val+=1
                return self.__next__()
        else:
            raise StopIteration
obj=Numbers(10)
for i in obj:
    print(i)

# 4.Create an custom iterator that prints the first N odd numbers.

class Numbers:
    def __init__(self,n):
        self.n=n
        self.val=1
    def __iter__(self):
        return self
    def __next__(self):
        if(self.val<=self.n):
            if(self.val%2!=0):
                num=self.val
                self.val+=1
                return num
            else:
                self.val+=1
                return self.__next__()
        else:
            raise StopIteration
obj=Numbers(10)
for i in obj:
    print(i)

# 5.Create an custom iterator that returns only even numbers from a given list.
class Numbers:
    def __init__(self,l):
        self.l=l
        self.val=0
    def __iter__(self):
        return self
    def __next__(self):
        if(self.val<len(self.l)):
            num=self.l[self.val]
            self.val+=1
            if(num%2==0):
                return num
            else:
                return self.__next__()
        else:
            raise StopIteration

obj=Numbers([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
for i in obj:
    print(i)

# 6.Create an custom iterator that returns only odd numbers from a given list.

class Numbers:
    def __init__(self,l):
        self.l=l
        self.val=0
    def __iter__(self):
        return self
    def __next__(self):
        if(self.val<len(self.l)):
            num=self.l[self.val]
            self.val+=1
            if(num%2!=0):
                return num
            else:
                return self.__next__()
        else:
            raise StopIteration

obj=Numbers([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
for i in obj:
    print(i)

# 7.Create an custom iterator that returns only positive numbers from a list.

class Numbers:
    def __init__(self,l):
        self.l=l
        self.val=0
    def __iter__(self):
        return self
    def __next__(self):
        if(self.val<len(self.l)):
            num=self.l[self.val]
            self.val+=1
            if(num>0):
                return num
            else:
                return self.__next__()
        else:
            raise StopIteration

obj=Numbers([1,-2,3,-4,5,-6,7,8,-9,-10,11,-12,13,14])
for i in obj:
    print(i)


# 7.Create an custom iterator that returns only positive numbers from a list.

class PositiveIntegers:
    def __init__(self,l):
        self.l=l
        self.val=0
    def __iter__(self):
        return self
    def __next__(self):
        if(self.val<len(self.l)):
            if(self.l[self.val]>0):
                num=self.l[self.val]
                self.val+=1
                return num
            else:
                self.val+=1
                return self.__next__()
        else:
            raise StopIteration
l=[1,-2,5,-4,-10,1,20,40,35]
obj=PositiveIntegers(l)
for i in obj:
    print(i)
print(obj.__next__())

# 8.Create an custom iterator that prints each character of a string one by one.

class A:
    def __init__(self,s):
        self.s=s
        self.val=0
    def __iter__(self):return self
    def __next__(self):
        if(self.val<len(self.s)):
            num=self.s[self.val]
            self.val+=1
            return num
        else:
            raise StopIteration
obj=A("PavanKumar")
for i in obj:
    print(i,end=" ")

# 9.Create an custom iterator that prints the characters of a string in reverse order.

class reverse:
    def __init__(self,s):
        self.s=s
        self.val=len(s)-1
    def __iter__(self):return self
    def __next__(self):
        if(self.val>=0):
            num=self.s[self.val]
            self.val-=1
            return num
        else:
            raise StopIteration
obj=reverse("Pavan Kumar")
for i in obj:
    print(i,end=" ")




















