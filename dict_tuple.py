achyuth={"age":20,"email":"gmail","phone":30}
print(type(achyuth))
print(achyuth.get("age"))
print(achyuth.get(20))
print(achyuth.get("email"))
print(achyuth.get("phone"))


achyuth={"age":20,"email":"gmail","phone":30}
achyuth["age"]="name"
print(achyuth)

achyuth={"age":20,"email":"gmail","phone":30}
achyuth["email"]="upi"
print(achyuth)

achyuth={"age":20,"email":"gmail","phone":30}
print(achyuth.keys())
print(achyuth.values())
print(achyuth.items())
achyuth.update({"chinna":"name"})
print(achyuth)

achyuth={"age":20,"email":"gmail","phone":30}
achyuth.update({"chinna":"name"})
achyuth.pop("age")
print(achyuth)


achyuth={"age":20,"email":"gmail","phone":{1:765}}
print(achyuth["phone"][1])


achyuth={"age":20,"email":"gmail","phone":30}
for ganesh,haunted_house in achyuth.items():
    print(ganesh,haunted_house)





''' tuple topics'''
sweet_names=(1,4,9,87,2.35,234)
print(sweet_names[0])
print(sweet_names[2])
print(sweet_names[3])
sweet_names[0]=="chinnu"
print(sweet_names)
print(max(sweet_names))
print(min(sweet_names))
print(len(sweet_names))
print(sum(sweet_names))
print(list(sweet_names))

t1=(34,24)
t2=(54,45)
# print(t1+t2)
new=[]
for i,j in zip(t1,t2):
    new.append(i+j)
    print(new)


d=(2,3,65,67.78,89)
print(d*10)

d=(2,3,65,67.78,89)
print(22 not in d)

d=(2,3,65,67.78,89)
# c=(4,6,78,98,87,998)
# print(d not in c)
for i in d:
    print(i)
