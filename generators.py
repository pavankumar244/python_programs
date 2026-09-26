# 1.Write a generator that yields numbers from 1 to N
# def Numbers(start,end):
#     current=start
#     while(current<=end):
#         yield current
#         current+=1
# x=Numbers(1,10)
# for i in x:
#     print(i)
# 2.Write a generator that yields even numbers from 1 to N
# def Evens(start,end):
#     current=start
#     while(current<=end):
#         if(current%2==0):
#             yield  current
#             current+=1
#         else:
#             current+=1
# x=Evens(1,10)
# for i in x:
#     print(i)

# 3.Write a generator that yields each character of a string.
# def char_string(s):
#     val=0
#     while(val<len(s)):
#         yield s[val]
#         val+=1
# x=char_string("Pavan Kumar")
# for i in x:
#     print(i,end=" ")

# 4.Write a generator that yields characters of a string in reverse order.
# def reverse(s):
#     val=len(s)
#     while(val>0):
#         yield s[val-1]
#         val-=1
# x=reverse("Pavan Kumar")
# for i in x:
#     print(i)

# 5.Write a generator that yields only vowels from a string.
# def vowels(s):
#     val=0
#     while(val<len(s)):
#         if(s[val]=="a" or s[val]=="e" or s[val]=="i" or s[val]=="o" or s[val]=="u"):
#             yield s[val]
#             val+=1
#         else:
#             val+=1
# x= vowels("mosquito in the ear")
# for i in x:
#     print(i,end="")

# 6.Write a generator that yields only digits present in a string.
# def digits(s):
#     val=0
#     while(val<len(s)):
#         if(s[val].isdigit()):
#             yield s[val]
#             val+=1
#         else:
#             val+=1
# x=digits("Pavan123kumar@")
# for i in x:
#     print(i)

# 7.Write a generator that yields the square of each element in a list.
# def squares(l):
#     val=0
#     while(val<len(l)):
#         yield l[val]*2
#         val+=1
# l=[1,2,3,4,5,6,7,8]
# x=squares(l)
# for i in x:
#     print(i)

# 8.Write a generator that yields digits from an integer one by one.
# def A(d):
#     rev=0
#     while(d>0):
#         r=d%10
#         rev=rev*10+r
#         d=d//10
#     # yield rev
#     original=0
#     while (rev > 0):
#         r1 = rev % 10
#         original = original * 10 + r1
#         rev = rev // 10
#         yield original
#     # yield original
# x=A(12345)
# # print(x.__next__())
# for i in x:
#     print(i)

# 9.Create a generator that yields cumulative sum of numbers in a list.
# Example: [1,2,3] → 1, 3, 6
# def cumulative_sum(l):
#     sum=0
#     k=[]
#     for i in l:
#         sum=sum+i
#         k.append(sum)
#     yield k
# l=[1,2,3]
# x=cumulative_sum(l)
# print(x.__next__())







