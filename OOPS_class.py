class A:
    x=20
    c=0
    def __init__(self):
        self.y=120
        self.z=40
        self.a=140
        A.c+=1
obj1=A()
obj2=A()
print(obj1.y)
print(obj1.c)
print(A.x)
print(obj1.x)