x = "awesome"#x is global variable
def myfunction():
    print("This is value of Global Variable  : "+ x)
    print()
    

myfunction()
print()

g = "awesome"#global variable
def myfun():
    g="fantastic"#Value of g is changed at local level 
    print("Python is "+ g)

myfun()
print("Python is : "+ g)#global value printed 
print()
print()

#Global keyword
#To create a global variable inside a function, you can use the global keyword.

#Example
def fun1():
    global x
    x = "fantastic "

fun1()
print("Python is "+ x )
print()

#Example
#To change the value of a global variable inside a function,
#  refer to the variable by using the global keyword:
x="fantastic"
def fun1():
    global x
    x = "awesome "

fun1()
print("Python is "+ x )
