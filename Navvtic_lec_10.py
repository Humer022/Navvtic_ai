
#kivi liabrary used for making android application
#Tkinter used for making desktop application (.exe, execution file)
#APK (application programming kit)
#mec book linux abanto(application execution file search work)

#functions in python
def func(name = "akash"):
    print("hello world" +  name )
#func()


def func(name):
    print("hello world" +  name )
#func("akash")

def func(name , age):
    print("hello world" +  name + age )
#func("akash", "25")

def func(name = "akash"):
    print("hello world" +  name )
#func("ali")

def func(name , age, *scale):
    print("hello world" +  name + str(age) +str(scale) )
#func("akash", 25)

def func(name , *age):
    print(   name+ " " + str(age[1]) )
#func("akash", 25,30)

def fun(**hur):
    print(hur)
#fun(name= "akash", age= 34)

def fun(**hur):
    print(hur["name"],str(hur["age"]))
#fun(name= "akash", age= 34)

#exception handling
# x = 25
# try:
#     print(x)
# except:
#     #print("Error: variable y is not defined")

# x = 25
# try:
#     print(y)
# except:
#     print("Error: variable y is not defined")

# x = 25
# try:
#     print(y)
# except:
#     print("Error: variable y is not defined")
# finally:
#     print("This is executed always")

#empty function
def fun():
    pass
#fun()

#anonymous function
x = lambda a: a*5
#print(x(5))

x = lambda a,b: a**2
#print(x(5,2))

x = lambda a: a**3
#print(x(5))

x = lambda a,b,c: a*b/c
#print(x(5,2,2))


x = lambda a,b,c: a*(b/c)
#print(x(5,2,2)


#Assignment
def cit():
    cities = ["faisalabad","sahiwal","lahore","islamabad","karachi"]
    city_pass =input("Enter the city name: ")
    for x in cities:
        if x == city_pass:
            print("city is clean: ")
        else: 
            print("city is not clean")
cit()

#Assignment
#x = 50 +70 -