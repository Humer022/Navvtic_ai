#dsaturize
#unpacking tuple
'''st = {"apple","banana","guava","cherry"}
(st1, st2, *st3) = st
print(st3)'''

#packing tuple
'''student_info = ("Humera","25","Mathematics","white")
print(student_info,type(student_info))'''


#unpacking tuple
'''student_info = ("Humera","25","Mathematics","white")
name,age,subject,color = student_info
print(name)
print(age)
print(subject)
print(color)'''


#* esteric
'''student_info = ("Humera","25","Mathematics","white")
name,*other,color = student_info
print(name)
print(other)
print(color)'''

#sets in python
'''numbers = {22,33,44,55,66,77,88,99,99,44}
print(numbers)'''

#set constructer
'''numbers = set((22,33,44,22,55,66,33,66))
print(numbers,type(numbers))'''

#add items in set only one item added
'''numbers = {22,33,44,22,55,66,33,66}
numbers.add(123)
print(numbers)'''

#update items in set multiple items added
'''numbers = {22,33,44,22,55,66,33,66}
numbers.update({99,77})
print(numbers)'''


#pop function in set only del random value
'''numbers = {22,33,44,22,55,66,33,66}
numbers.pop()
print(numbers)'''

#remove items in sets only 1 argument given remove specific item but given eror if value is not exist
'''numbers = {22,33,44,22,55,66,33,66}
numbers.remove(100)
print(numbers)'''


#discard items in set only 1 argument given no erroe occur when value is not exist
'''numbers = {22,33,44,22,55,66,33,66}
numbers.discard(100)
print(numbers)'''

#clear items in set given no argument
'''numbers = {22,33,44,22,55,66,33,66}
numbers.clear()
print(numbers)'''

#union in sets | and union()
'''set1 = {22,33,44,55,77}
set2 = {22,99,88,66,55}
unio = set1 | set2  # unio = set1 + set2
print(unio)'''

#intersection in set & or intersection()
'''set1 = {22,33,44,55,77}
set2 = {22,99,88,66,55}
inter = set1 & set2  # inter = set1 - set2
print(inter)'''

#differences and compliment in set - or differences()
'''set1 = {22,33,44,55,77}
set2 = {22,99,88,66,55}
diff = set1 - set2  # diff= set1 - set2
print(diff)'''


# Assignments
# st = {"hello","world"}
# (st1 , st2) = st
# st.update("hira","humera")
# #st = list(st)
# print(st)

'''ls =["ali","nouman","fatima","sara"]
st = {"sara","rida","fatima"}
lsst = ls + list(st)

lsst = set(lsst)
print(lsst)
st2 = {"farhan","naseer","fatima"}

#union set
result = lsst | st2
print(result)

#intersection set
result1 = lsst & st2
print(result1)

#set difference
result2 = lsst - st2
print(result2)'''



#assignment
'''st = {1,2,3,4,5,6,7,8,9,10}
(st1,st2,st3,st4,st5,st6,st7,st8,*st9) = st
st9 = list(st9)
st9.append(11)
st9 = set(st9)
print(st9)'''

#Home assignment
'''set1 = {11,22,33,44,55}
set2 = {"humera","sara","fatima"}
set3 = {True , False}
set4 = {44.5,23.5,77.6,}
#joining sets
set5 = list(set1) + list(set2) + list(set3) + list(set4)
set5 = set(set5)
print(set5,type(set5))
set5 = list(set5)
print(set5,type(set5))
set5 = tuple(set5)
print(set5,type(set5))'''




