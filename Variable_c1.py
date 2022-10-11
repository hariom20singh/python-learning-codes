from tkinter import DoubleVar
from tokenize import Double


x = 5 # this is int type value 
y= "Rishabh" # this is string type value 
z = 5.4 # this float type value
print("INT value - ", x)
print ("String value - ", y)
print ( "Float value - ",z)


#Expilict type casting the data types 
x = float(5) #float type data - 5.0
y=int(2) #int type data - 2
z = str("yadav")#str type data - yadav 

print("INT value - ", y)
print ("String value - ", z)
print ( "Float value - ",x)



"""
Get the Type
You can get the data type of a variable with the type() function.
"""

x = 4
y= "str"
# is same as 
z='str'

print(type(x))
print(type(y))
print(z)
print (type(z))

"""
Case-Sensitive
Variable names are case-sensitive.
"""

A = 'rishabh yadav'
a = 'rakesh singh'
# a doesn't overwrite A means a and A both are different 
print(A)
print(a)
