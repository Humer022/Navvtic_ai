#inheritence(simple inheritance(only one parent one child),multiple inheritence(multiple parent clases but child class only one))
#Multi inheritence
'''class Father:
    def ft(self):
        print("father classes")
class Mother:
    def mt(self):
        print("mother classes")
class Child:
    pass
ab = Child()
ab.ft()
ab.mt()'''


#single inheritance
'''class Father:
    def ft(self):
        print("fathe classes")

class Child(Father):
    pass

ab = Child()
ab.ft()'''

#Multi level inheritence
#Grand parent chlid
'''class Grandpa:
    def gp(self):
        print("grandpa class")
class parent(Grandpa):
    def pt(self):
        print("parent class")
class Child(parent):
    pass
ab = Child()
ab.gp()
ab.pt()'''

#Heirarchical inheretence
'''class Parent():
    def pt(self):
        print("this is the parent class")
class Child1(Parent):
    pass
class Child2(Parent):
    pass
ab = Child2()
ab.pt()'''

'''#use of super method
class Parent:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def smt(self):
        print(f"hello {self.name} your age is {self.age}")
class Child(Parent):
    def __init__(self, name, age,education):
        self.education = education
        super().__init__(name, age)
    def mt(self):
        print(f"and your education is {self.education}")

ab = Child("humera",24,16)
ab.smt()
ab.mt()'''

'''class Employee():
    def __init__(self,name,age,employee_id):
        self.name = name
        self.age = age
        self.employee_id = employee_id
    def self_display(self):
        print(f"hello your name is {self.name} and your age is {self.age} your id number is {self.employee_id} ")

class Manager(Employee):
    def __init__(self,name,age,employee_id,dept):
        Employee.__init__(self,name,age,employee_id)
        self.dept = dept 
         
    def self_display(self):
        Employee.self_display(self) 
        print(f"and your department is {self.dept}")  




ab =Manager("humera",24,1234,"iT")
ab.self_display()'''



class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_person(self):
        print(f"your name is {self.name} and your age is {self.age}")
class Student(Person):
    def __init__(self,name,age,student_id):
        Person.__init__(self,name,age)
        self.student_id = student_id
    def display_student(self):
        Person.display_person(self)
        print(f"your student id is {self.student_id}")

ab = Student("humera",24,2244)
ab.display_student()