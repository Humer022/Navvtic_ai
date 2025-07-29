
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

#Greeting Function
def greet(name):
    print(f"Hello, {name}! Welcome to the Python world.")

greet("Alice")


#Add Two Numbers
def add(a, b):
    return a + b

result = add(10, 5)
print("Sum:", result)

#Check Prime Number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
print(f"Is {num} a prime number? {is_prime(num)}")

#Factorial Calculator
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print("Factorial of 5 is:", factorial(5))


#Find Maximum of Three Numbers
def find_max(a, b, c):
    return max(a, b, c)

print("Maximum is:", find_max(23, 98, 12))

# Palindrome Checker
def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

word = input("Enter a word: ")
print(f"Is '{word}' a palindrome? {is_palindrome(word)}")


#Simple Calculator (Function Menu)
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Cannot divide by zero"

print("Select operation: 1-Add 2-Subtract 3-Multiply 4-Divide")
choice = input("Enter choice: ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(a, b))
elif choice == '2':
    print("Result:", subtract(a, b))
elif choice == '3':
    print("Result:", multiply(a, b))
elif choice == '4':
    print("Result:", divide(a, b))
else:
    print("Invalid choice")
