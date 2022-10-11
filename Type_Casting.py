"""
TYPE CASTING - Two types 
1. Implicit type casting--->: In implicit type casting, the python compiler 
internally typecasts one variable into another type without the external 
action of the user. 

Example:- 

"""
int_num=4
float_num=7.9
ans = int_num+float_num
print('Int num type =',type(int_num))
print('ans num type = ',type(ans))
#ans is automatic typed casted
# into float type for greater precision
print('Float num type = ',type(float_num))


#Explicit Type Casting: In explicit type casting, the user
#  explicitly forces the compiler to convert a variable
#  from one type to another. The diﬀerent ways of 
# explicit typecasting are given below:

#1.)Integer to String or Float: 
"""
To typecast an integer into a string type, 
we use the str() method. Similarly, to typecast
 it into a float type, we use the float() method.
For example:
"""

var = 123 
print("this is string-"+str(var))
var = 23
print(float(var))

#2.) Float to integer

f=56.39
print(int(f))

