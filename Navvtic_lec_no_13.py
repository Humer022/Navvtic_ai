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

#Create a Simple Class and Object
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Create object
my_car = Car("Toyota", "Corolla")
my_car.display_info()


#Student Grade System
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            grade = "A"
        elif self.marks >= 80:
            grade = "B"
        elif self.marks >= 70:
            grade = "C"
        else:
            grade = "D"
        print(f"{self.name} scored {self.marks} and got grade {grade}")

# Test
s1 = Student("Alice", 88)
s1.get_grade()


#Bank Account Class
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"{self.owner}'s Balance:", self.balance)

# Test
account = BankAccount("John")
account.deposit(1000)
account.withdraw(300)
account.check_balance()

#Class with Inheritance
class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Test
d = Dog()
c = Cat()
d.make_sound()
c.make_sound()

#Rectangle Class with Area and Perimeter
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Test
r = Rectangle(10, 5)
print("Area:", r.area())
print("Perimeter:", r.perimeter())








