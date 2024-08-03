achyuth='achyuth'
ganesh="ganesh"
chinna='''chinna'''
print(type(achyuth).type(ganesh).type(chinna))


aparna='Python Program'
print(aparna.lower())
print(aparna.upper())

aparna='python program'
print(aparna.count("m"))
print(aparna.find("p"))


aparna="i am an angel"
print(aparna.find("angel"))
print(aparna.index("an"))
print(aparna.index("gel"))
print(aparna.find("l"))

aparna="i am an angel"
print(aparna.startswith("am"))
print(aparna.endswith("gel"))


fruits=[]
for i in ["banana.in","mango.in","sapota.com","kiwi.com"]:
    if i.endswith ("in"):
        fruits.append(i)
print(fruits)        


vehicles=[]
for i in["vehicle.car","vehicle.bus","animal.cat","fruit.mango","vehicle.bike"]:
    if i.startswith("vehicle"):
        vehicles.append(i)
print(vehicles)


maggie=("hi {} did you eat! {}".format("sravya","bye"))
print(maggie)

chinna="hi {} what doing....".format("baby")
print(chinni)

chinna="hey baby {} i am {}".format("get well soon","take care")
print(chinna)

names=["chinna","chinnu","ganga","anshu","maddy","sindhu"]
for achyuth in names:
    print("hii {} did you eat!".format(achyuth))



harinath="bindhu143"
print(harinath.isalnum())


harinath=" i am talking with my friend"
print(len(harinath))


harinath="  i am talking with my friend "
s=harinath.lstrip()
d=harinath.rstrip()
print(len(s))
print(len(d))

harinath="i am talking with my friend"
print(harinath.title())

harinath="i am talking with my friend"
g=harinath.replace("am","is").replace("my","your")
print(g)

harinath="i is talking with my friend"
f=harinath.split()
n=[]
for i in f:
    if i=="is":
        i="are"
        n.append(i)
    else:
        n.append(i)
        print(n)

h="i am talking with my friend"
print(h)
c=h.split()
print(c)
s=" ".join(c)
print(s)
