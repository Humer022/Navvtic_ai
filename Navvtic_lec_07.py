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


     








  



    
