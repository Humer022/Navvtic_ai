#Tuples
#Tuples constructer
#primitive data type only single value( 5int, 5.8float, True boolean, "hello")
#non primitive data type(list , tuples, sets, dictioneries)
# ls = [1,2,3,4,5,6,7,8,9,10]
# if ls %2 == 0:
#     print(ls)

ls = ("faisalabad","jaranwala", "lahore")
ls = list(ls)
for x in ls:
    lsb =x[0].upper() +x[1:]
    #print(lsb)

#Index method
tup1 = ("faisalabad","jaranwala", "lahore") 
tup2 = (1,2,3,4,5,6,)
tup3 = tup2 + tup1
#print(tup3[6:] , tup3[:6])

#reversed method
tup1 = ("faisalabad","jaranwala", "lahore") 
tup2 = (1,2,3,4,5,6,)
tup3 = tup2 + tup1
#print(tup3[::-1]) 

#for loop method
tup1 = ("faisalabad","jaranwala", "lahore") 
tup2 = (1,2,3,4,5,6,)
tup3 = tup2 + tup1
tup4 = []
for i in tup3:
     tup4.insert(0,i)
        
tup4.append(i)
tup4 = tuple(tup4)
#print(tup4)
#while oop
tup1 = ("faisalabad","jaranwala", "lahore") 
tup2 = (1,2,3,4,5,6,)
tup3 = tup2 + tup1
tup4 = []
i = 0
while i < len(tup3):
     tup4.insert(0,tup3[i])
     i += 1

tup4 = tuple(tup4)
#print(tup4)

#if else conditiond
tup1 = ("faisalabad","jaranwala", "lahore") 
tup2 = (1,2,3,4,5,6,)
tup3 = tup2 + tup1
tup4 = []
i = 0

while i < len(tup3):
    if tup3[i]:
       tup4.insert(0, tup3[i])
         
    else:
         pass
    i += 1
tup4 = tuple(tup4)
#print(tup4)

countries = ("India", "USA", "Germany", "Canada", "Japan")

print("List of countries:")
for country in countries:
    print(country)

#Tuple Indexing and Slicing
numbers = (10, 20, 30, 40, 50)

print("First number:", numbers[0])
print("Last number:", numbers[-1])
print("Slice [1:4]:", numbers[1:4])


#Check if an Item Exists in a Tuple
nums = (5, 10, 15, 20, 25)

user_num = int(input("Enter a number to check: "))

if user_num in nums:
    print(f"{user_num} exists in the tuple.")
else:
    print(f"{user_num} does not exist in the tuple.")


# Count and Index Methods
data = (1, 2, 3, 2, 4, 2, 5)

print("Tuple:", data)
print("Count of 2:", data.count(2))
print("First index of 2:", data.index(2))


#Convert Between List and Tuple
colors_list = ["red", "green", "blue"]

# Convert to tuple
colors_tuple = tuple(colors_list)
print("Tuple:", colors_tuple)

# Convert back to list and add an item
colors_list = list(colors_tuple)
colors_list.append("yellow")
print("Modified list:", colors_list)



     








  



    
