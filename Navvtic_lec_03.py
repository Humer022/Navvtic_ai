#topic user input
'''name = input("Enter your name: ")
print("your name is", name)'''

# if else conditions in python
#first condition
'''num = 20
if num == 20:
    print("you are passed: ")'''

#second condition
'''num = 40
num1 = 80
if num == 40:
    if num1 == 80:
        print("both conditions are true: ")
    else:
        print("second condition is wrong:")
else:
    print("both conditions are wrong")'''     

#Third condition comparison operators
# num = 90
# num3 = 80

# if (num >= 90 and num <= 90):
#     if (num )
#Hiring criteria
'''edu = input("Enter your education: ")
age = input("Enter your age: ")
height = input("Enter your height: ")
edu =int(edu)
age = int(age)
height = float(height)
if edu >= 12:
    print("you are passed:")
elif age >= 18 and age <= 40:
    print("you are passed: ") 
elif height >= 5.6:
    print("you are passed: ")
else:
    print("you are failed")'''
#Method #2 best method for prctice
'''edu = input("Enter your education: ")
age = input("Enter your age: ")
height = input("Enter your height: ")
edu =int(edu)
age = int(age)
height = float(height)
if (edu >= 12 and age >= 18):
    print("you are paseed: ")
elif(age >= 18 and height >= 5.6):
    print("you are passed: ")
elif(edu >= 12 and height >= 5.6):
    print("you are passed: ")
else:print("you are fail: ")'''

#Method no 3
'''edu = input("Enter your education: ")
age = input("Enter your age: ")
height = input("Enter your height: ")
edu =int(edu)
age = int(age)
height = float(height)
if(edu >= 12 and age >= 18 and height >= 5.6):
    print("you are passed: ")
else:
    print("you are fail: ")'''


#we calculate percentage
'''Marks = input("Enter your marks: ")
Total_marks = input("Enter your total marks: ")
Marks = int(Marks)
Total_marks = int(Total_marks)

per = Marks/Total_marks*100
print(f"your percentage is", (per))'''

#We calculate salary
'''bonus = input("Enter your bonus: ")
bonus_percentage = input("Enter your bonus percentage: ")
bouns = int(bonus)
bonus_percentage = int(bonus_percentage)
#salary 22% off bonus
cal_salary = bouns*100 /22

print(f" your salary is", cal_salary)'''
 

#Type casting in python
'''type casting  is very important in python because '
'when we need to update data time to time we use type casting'''
'''num = "45"
num = int(num)
num1 = "34.5"
num1 = float(num1)'''




