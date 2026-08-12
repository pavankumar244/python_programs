l=[2,6,10,3,5,12,33,11,21,15]
def my_map(fun,lst):
    r=[]
    for i in lst:
        r.append(fun(i))
    return r
def square(x):
    return x*2
print(my_map(square,list(filter(lambda x: x%2==0,l))))
print("check1")
