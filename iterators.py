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








