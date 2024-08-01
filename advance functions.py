# y=lambda a,b,c:a*b*c
# print(y(3,4,5))

# l1=[1,34,54,65]
# l2=[]
# for i in l1:
#     t=lambda a:a+1
#     l2.append(t(i))
# print(l2)


# l1=[1,2,3,4,5,6]
# l2=[]
# for i in l1:
#     t=lambda a:a+3
#     l2.append(t(i))
# print(l2)


# l1=[1,2,3,4,5,6,7,8]
# l2=[]
# for i in l1:
#     if i<=6:
#         l2.append((i))
# print(l2)



# ages=[12,13,14,18,19,24,35]
# def myFunc(x):
    
#     if x>=18:
#         return True
#     else:
#         return False

# adults=filter(myFunc,ages)
# print(list(adults))


# def simpleGeneratorFunc():
#     yield 1
#     yield 2
#     yield 3
# x=simpleGeneratorFunc()
# # Iterating over the generator object using next
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())



# def aa():
#     return 1+1
# print(aa())


# def add(*a):
#     print(a+a)
# add(1,2,3,4,5,6,7)