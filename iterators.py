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