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




