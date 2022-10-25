#Decorators

#Decorators can be thought of as functions which modify the functionality of another function. They help to make your code shorter and more "Pythonic".

#To properly explain decorators we will slowly build up from functions. Make sure to run every cell in this Notebook for this lecture to look the same on your own computer.


#Creating a Decorator
def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")
    
#func_needs_decorator()

This function is in need of a Decorator
