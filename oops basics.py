class Karthik():
    def Output(self):
        print("this is class")
        
vivo=Karthik()
vivo.Output()


class Shiva():
    a=10
    def show(self):
        print("this is class")
        
kiran=Shiva()
print(kiran.a)
kiran.show()
print("hello")


class anu():
    a=11
    def classMethod(self):
        print("this is room")
achyuthobj1=anu()
achyuthobj=anu()
achyuthobj.classMethod()
achyuthobj.a


class chat():
    def display(self):
        print("this is my snack")
obj=chat()
obj.display()



class Achyuth():
    a=10
    def Output(self):
        print(self.a)
obj=Achyuth()
obj.Output()



class Ganesh():
    def Output(self):
        print("my friend")
achyuth=Ganesh()
hari=Ganesh()
achyuth.Output()
hari.Output()


class Prakash():
    def __init__(self,a,b,c):
        self.dd=a
        self.gg=b
        self.tt=c
        # print(a)
    def Show(self):
            print(self.dd,self.gg,self.tt)
g=Prakash(1,2,3)
g.Show()


class Mobiles():
    def __init__(self,Mobile_name,Mobile_ram,Mobile_price):
        self.a=Mobile_name
        self.b=Mobile_ram
        self.c=Mobile_price
        def Output(self):
            print(self.a)
            print(self.b)
            print(self.c)
while True:
    name=input("enter the Mobile_name:")
    ram=input("enter the Mobile_ram:")
    price=float(input("enter the Mobile_price:"))

d.Mobiles(name,ram,price)
d.Output()


class Laptop():
    def __init__(self,laptop_price,laptop_model,laptop_colour,laptop_size,laptop_ram):
        self.a=laptop_price
        self.b=laptop_model
        self.c=laptop_colour
        self.d=laptop_size
        self.e=laptop_ram
        def laptop_data(self):
            print(self.a)
            print(self.b)
            print(self.c)
            print(self.d)
            print(self.e)
while True:
    price=float(input("enter the laptop_price:"))
    model=input("enter the laptop_model:")
    colour=input("enter the laptop_colour:")
    size=input("enter the laptop_size:")
    ram=input("enter the laptop_ram:")
laptop_obj=Laptop(price,model,colour,size,ram)
laptop_obj=laptop_data()


---------SINGLE INHERITANCE---------

class Parent():
    def output(self):
        print("this is Parent class")
class Child(Parent):
    def outputChild(self):
        print("this is Child class")
i=Child()
i.output()
i.outputChild()


----------MULTIPLE INHERITANCE------

class Father():
    def output(self):
        print("this is Father class")
class Mother():
    def outputM(self):
        print("this is Mother class")
class Child(Father,Mother):
    def outputChild(self):
        print("this is Child class")
i=Child()
i.output()
i.outputM()
i.outputChild()




--------MULTILEVEL INHERITANCE-------

class GrandFather():
    def output(self):
        print("this is GrandFather class")
class Father(GrandFather):
    def outputF(self):
        print("this is Father class")
class Child(Father):
    def outputChild(self):
        print("this is Child class")
i=Child()
i.output()
i.outputF()
i.outputChild()




-----------HIERARCHIAL INHERITANCE------



class Father():
    def output(self):
        print("this is Father class")
class Child1(Father):
    def outputChild1(self):
        print("this is Child1 class")
class Child2(Father):
    def outputChild2(self):
        print("this is Child2 class")
ice=Child1()
cream=Child2()
ice.output()
ice.outputChild1()
cream.output()
cream.outputChild2()





class Father():
    def output(self):
        print("this is Father class")
class Child(Father):
    def outputC(self):
        print("this is Child class")
i=Father()
i.output()


class Father():
    def funv(self):
        print("this is Father class")
class Mother():
    def fun(self):
        print("this is Mother class")
class Done(Father,Mother):
    def fun2(self):
        print("this is class")
class Child(Father,Mother,Done):
    def func(self):
        print("this is child")
obj=Child()
obj.funv()
obj.fun()
obj.func()
obj.fun2()



------POLYMORPHISM-------



class Methodoverload:
    def something(self,a=None,b=None,c=None):
        print(a,b,c)
obj=Methodoverload()
obj.something(1,2,3)
obj.something(1,2)
obj.something(1)
obj.something()


class Methodover:
    def display(self):
        print("this is parent class")
class Child(Methodover):
    def display(self):
        print("this is child class")
        super().display()
obj=Child()
obj.display()



----ENCAPSULATION------




class Gfather:
    def __init__(self,a):
        self.__y=a
        print(self.__y)
class Father(Gfather):
    def display1(self):
        print(self.__y)
class Child2(Father):
    def display2(self):
        print("Child2",self.__y)
obj=Child2(12)
obj.display2()
obj.display1()




a=10
def fun():
    b=20
    print("this is fun",b,a)
fun()
print(a)



====ABSTRACTION=====



from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass
class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kph")
class Duster(Car):
    def mileage(self):
        print("The mileage is 40kph")
class Fortuner(Car):
    def mileage(self):
        print("The mileage is 35kph")
class Suzuki(Car):
    def mileage(self):
        print("The mileage is 34kph")
t=Tesla()
t.mileage()
d=Duster()
d.mileage()
f=Fortuner()
f.mileage()
s=Suzuki()
s.mileage()


strings=input("Enter the string:")
if strings==strings[::-1]:
        print("palindrome")
else:
        print("not a palindrome")
