#string concatenation
'''first_name = "humera"
second_name = "sarwar"
full_name = first_name +" " + second_name 
print(full_name)''' 

#we concatenate string by last space
'''first_name = "humera "
second_name = "sarwar"
full_name = first_name + second_name 
print(full_name)'''

#we concatenate string by using first spaces
'''first_name = "humera"
second_name = " sarwar"
full_name = first_name + second_name 
print(full_name)'''


#Multiline string
'''info = "My name is humera sarwar " \
"\ni am 24 years old " \
"\ni have done m com in 2023"
print(info)'''

#string formating in (int ,float,and string)
'''name = "humera"
age = "24"
marks = "70.8"
result = "my name is {} i am {} years old i have got marks{}% "
cal_result = result.format(name,age,marks)'''
#print(cal_result)

#second method of formating
'''name = "humera"
age = "24"
marks = "70.8"
print(f"my name is{name}, i am {age} years old,i have got marks {marks}: ")'''

#string slicing 
#name = "humera sarwar"
#print(name[0:2]) 
'''print(name[0:])
print(name[0:4])
print(name[1:7])
print(name[-3:-1])'''

#split in string
'''name = "humera sarwar age 24 degree m.com"
print(name.split(" "))'''



#upper case and lower case in string
'''name = "humera sarwar"
print(name.upper(), name.lower())'''

#Assignmrnt in upper case
#p = "jaranwala faisalabad lahore"
#print(p[0:1].upper() + p[1:9], p[10:11].upper() + p[11:20], p[21:22].upper() +p[22:])

#Assignment in lower case
#p = "Jaranwala Faisalabad Lahore"
#print(p[0:1].lower() +p[1:9].upper(), p[10:11].lower() +p[11:20].upper(), p[21:22].lower() +p[22:].upper())

#Replace method in string

#p = "jaranwala faisalabad lahore"

#print(p[0:1].replace("j","J") +p[1:9], p[10:11].replace("f","F") +p[11:20], p[21:22].replace("l","L") +p[22:])

#Home assignment
p = "Jaranwala Faisalabad Lahore Multan Karachi"
print(p.replace("J","j").lower())

