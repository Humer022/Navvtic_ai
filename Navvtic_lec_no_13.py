#opps in python
#getter method
#setter method
# class Employee:
#     #pass
#     def setEmp(self,name,age):
#         self.name = name
#         self.age = age
#     def getEmp(self):
#         print(f" {self.name} :{self.age} ")

# a =Employee()
# b =Employee()
# c =Employee()
# d =Employee()
# e =Employee()
# a.setEmp("akash","24")
# b.setEmp("akash","24")
# c.setEmp("akash","24")
# d.setEmp("akash","24")
# e.setEmp("akash","24")
# a.getEmp()
# b.getEmp()
# c.getEmp()
# d.getEmp()
# e.getEmp()


# class Employee():
#     #pass
#     def __inti__(self,name,age):
#         self.name = name
#         self.age = age

# def getEmp(self):
#     print(f" {self.name}: {self.age}")

# 


#polymarphizam
'''class Car:
    def __init__(self, name,model):
        self.name = name
        self.model = model
    
    def func(self):
        print(f"hello sky man {self.name} :{self.model}")


class Bus:
    def __init__(self, name,color):
        self.name = name
        self.color = color
    
    def func(self):
        print(f"hello drown man {self.name} :{self.color}")

ab = Car("kivi",2019)
ac = Bus("Dawoo","green")

ab.func()
ac.func()'''


# class Animal:
#     def __init__(self,name):
#         self.name = name
    
#     def sound(self):
#         print(f"your name is {self.name} and your sound is nothing")
# class Cat(Animal):
#     def __init__(self,name):
#         self.name = name
#     def sound(self):
#         print(f"your name is {self.name} and your sound is meoow")

# class Dog(Animal):
#     def __init__(self,name):
#         self.name = name
#     def sound(self):
#         print(f"your name is {self.name} and your sound is wahoo")

# ab = Cat("cat")
# ac = Dog("dog")
# ad = Animal("something")

# ab.sound()
# ac.sound()
# ad.sound()

#Assignment no 1
a = 15
b = 14
#sum the two valuea by using get and set method

#Assignment no 2
# getting two variable name and age and print 5 employee names nd ages

#assignment no 3
#using esteric method getting 1 perameter and two argumets

class Car:
    def setnew(self,*name):
        self.name = name
        
    def getNew(self):
        print(f"your name is{self.name} :")
a =Car()
a.setnew("humera",24)
a.getNew()









