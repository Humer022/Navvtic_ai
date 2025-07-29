#for loop
#while loop
#list comprehension
# numbers = []
# num1 =input("Enter your first number: ")
# num2 =input("Enter your second number: ")
# num1 =int(num1)
# num2 =int(num2)

# numbers.append(num1)
# numbers.append(num2)
# print(numbers)

# #factorial of numbers

# factorial = 1
# for i in numbers:
#     factorial *= i
#find number 3 in 100 count how many time repeat
count = 0
for i in range(1,101):
    count  += str(i).count("3")
    
print(f"number three appears {count} times")
