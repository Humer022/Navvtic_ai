#Dictioneries in python
'''dict = {"name":"Ali","age":20,"grade":"A","city":"Lahore","subject":"Mathematics"}
print(dict)'''


#dictionery constructer
'''dict = ({"name":"Ali","age":20,"grade":"A","city":"Lahore","subject":"Mathematics"})
print(dict,type(dict))'''


#crud operation 
# c for create
# r for read
# u for update
# d for delete


#get method in dic
'''dict = ({"name":"Ali","age":20,"grade":"A","city":"Lahore","subject":"Mathematics"})
print(dict.get("name"))
print(dict.get("city"))'''


#second method in dict calling dict value (dict name[key])
'''dict = ({"name":"Ali","age":20,"grade":"A","city":"Lahore","subject":"Mathematics"})
print(dict["name"])
print(dict["subject"])'''


#updation in dict
'''dict = ({"name":"Ali","age":20,"grade":"A","city":"Lahore","subject":"Mathematics"})
dict.update({"name":"humera","city":"sahiwal"}) #when we update multiple value
print(dict)'''

#when we update single value
'''dict = ({"name":"Ali","age":20,"grade":"A","city":"Lahore","subject":"Mathematics"})
dict["age"] = "24"
print(dict)'''


#del value in dict pop()
'''dict = ({"name":"Ali","age":20,"grade":"A","city":"Lahore","subject":"Mathematics"})
dict.pop("grade") # pop k function ko ak argument pass karna pary ga jo key di jye gi ye ust del kar dy ga
print(dict)'''


#popitem()
'''dict = ({"name":"Ali","age":20,"grade":"A","city":"Lahore","subject":"Mathematics"})
dict.popitem() #pop item k function ko koi argument pass ni kia jye ga but ye last key value pair ko del kar dy ga
print(dict)'''

#Del multiple values by using pop method
'''dict = ({"name":"Ali","age":20,"grade":"A","city":"Lahore","subject":"Mathematics"})
remove = {"name","grade","subject"}
for key in remove:
    dict.pop(key, None)
print(dict)'''

#getting dict keys
'''dict = ({"name":"Ali","age":20,"grade":"A","city":"Lahore","subject":"Mathematics"})
print(dict.keys())''' 

#getting dict.keys()
'''dict = ({"name":"Ali","age":20,"grade":"A","city":"Lahore","subject":"Mathematics"})
print(dict.values())''' 

#getting dict items  dict.items()
'''dict = ({"name":"Ali","age":20,"grade":"A","city":"Lahore","subject":"Mathematics"})
print(dict.items())'''
#pass by references non primative values change because address is same(list,dictioneries,set)
'''name = ["humera","saher","faiza","ezza"]
sister_name =name
name = ["umaima"]
print(name,sister_name)'''

 
# pass by values primative values not change ye single vslues hoti h(int,float,string,tuple)
'''a =10
b = a
a = 20
print(a,b)'''


#copy dictionerires



#assignment
'''student_info ={
    "humera":{"age":24,"degree":"Mcom",}, "Emma":{"age":22,"degree":"bscs", }}


student_info["humera"].pop("age")
student_info["Emma"].update({"age":"24","degree":"mcom"})
print(student_info)'''


#assignment
'''dict = {}
dict.update({"name":"saher","age":"30","gender":"female"})
print(dict)'''

#copy dictionery using built in function
'''dict = ({"name":"Ali","age":20,"grade":"A","city":"Lahore","subject":"Mathematics"})
dict1 = dict.copy()
dict1.update({"name":"humera","age":"25"})
print(dict1)
print(dict)'''


#copy dictionery using shallow copy mthod
'''real_dict = ({"name":"Ali","age":20,"grade":"A","city":"Lahore","subject":"Mathematics"})
dict1 = dict(real_dict)
dict1.update({"name":"humera","age":"25"})
print(dict1)
print(real_dict)'''





