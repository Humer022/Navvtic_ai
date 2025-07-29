#list in python
#constructer method list
#list element replace by slicing method
#Add new element in list append()
#insert new element at specific place insert()
#delete list element at specific place pop()
#delete list element by passing argument remove()

#for loop in python
'''p = ["jaranwala", "faisalabad", "lahore"]
p[0:1]  = ["Jaranwala"]
print(p)
p[1:2] = ["Faisalabad"]
print(p)
p[2:] = ["Lahore"]
print(p)'''

#Assignment no 3
# p = ["jaranwala", "faisalabad", "lahore"]
# lp =[]
# for x in p:
#     p =x[0:1].lower() +  x[1:2].upper() + x[2:-2] + x[-2:-1].upper() + x[-1:]
#     print(p)
#     p.append()
# print(lp)

cities = ["jaranwala", "faisalabad", "lahore","multan","islamabad","karachi","sahiwal","okara","mianchu","chichawatni"]
city = []
for i in cities:
    city.insert(0,i)
    print(city)
 
for x in cities:
    city = x[0:1].upper() + x[1:]
    print(city)




#Append method in list
fruits = []

for i in range(3):
    fruit = input(f"Enter fruit #{i+1}: ")
    fruits.append(fruit)

print("Your favorite fruits are:", fruits)


#Remove an Item from a List
colors = ['red', 'green', 'blue', 'yellow']

print("Current colors:", colors)
color_to_remove = input("Enter a color to remove: ")

if color_to_remove in colors:
    colors.remove(color_to_remove)
    print("Updated colors:", colors)
else:
    print("Color not found in the list.")

# Pop the Last Item
numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)
last_item = numbers.pop()
print("Popped item:", last_item)
print("List after pop:", numbers)


#Insert an Item at a Specific Index
animals = ['cat', 'dog', 'rabbit', 'parrot']
print("Animals:", animals)

new_animal = input("Enter a new animal: ")
index = int(input("Enter index to insert at (0-4): "))

if 0 <= index <= len(animals):
    animals.insert(index, new_animal)
    print("Updated list:", animals)
else:
    print("Invalid index.")

#Merge Two Lists Using Extend
fruits = ['apple', 'banana', 'mango']
vegetables = ['carrot', 'broccoli', 'spinach']

print("Fruits:", fruits)
print("Vegetables:", vegetables)

fruits.extend(vegetables)
print("Combined list:", fruits)
