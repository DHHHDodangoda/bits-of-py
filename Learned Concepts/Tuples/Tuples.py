#create tuples
MyTuple1= () # blank tuple
MyTuple2= (50,) #single value tuple
MyTuple3= (10,20,30,40)
MyTuple4= (2017,"Python", "Cut-off", 50.00)

#display tuples
print(MyTuple1)
print(MyTuple2)
print(MyTuple3)
print(MyTuple4)

#display specific values ( using slicer )
print(MyTuple2[0])
print(MyTuple3[2])
print(MyTuple4[1:3])

#update tuple (cant update items in tuples this will give you an error)
'''MyTuple3 [1] = 25
print(MyTuple3)'''

tuple01 = (1,2,3,4)
tuple02 = (10,20,30,40)

print(tuple01)
print(tuple02)

#join tuples

New = tuple01 + tuple02
print(New)

#Delete tuples
del tuple02

print(tuple01)
# print(tuple02)  this will also give you an error
