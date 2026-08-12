def greet(name,prefix='Hello',formatter=lambda x:x):
    s=prefix+" "+name
    return formatter(s)
print(greet("pavan",prefix="bye",formatter=lambda x:x.upper()))