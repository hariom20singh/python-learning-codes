#Many value to multiple variable
x , y, z = "mohan","shyam","Hari"
print(x)
print(y)
print(z)
print()
print()
x , y, z = "mohan",5.9,2
print(x)
print(y)
print(z)
print()
print()
#One value to multiple vaiable
x = y =z = "ram"
print(x)
print(y)
print(z)


#Unpack a Collection
#If you have a collection of values in a list, tuple etc.
#  Python allows you to extract the values into variables.
#  This is called unpacking.

#Example

fruits = ["mango", 14 , "orange",45 , "apple",1]
m,w,o,ow,a,aw=fruits
print(m)
print(w)
print(o)
print(ow)
print(a)
print(aw)