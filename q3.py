student_records=[
    {'name':'Kenny','score':85},
    {'name':'Harry','score':87},
    {'name':'Joe','score':53},
    {'name':'Marcus','score':48},
    {'name':'clara','score':90}
]
k=list(filter(lambda x:x['score']>=60,student_records))
l1=list(map(lambda s:{**s,"grade":"Pass"},k))
print(sorted(l1,key=lambda x:x['score'],reverse=True))