#break statement - when break statement execute in the loop 
#the loop will break , after that out of the loop will execute.
for i in range(5):
    if i==3:
        break;#here if value of i will 3 then loop will break
    else:
        print(i)


#continue statement- when continue statement execute then that
#skips other part  will execute as it is .
print()
for i in range(5):
    if i==3:
       continue#here skips value 3 
    else:
        print(i)

"""
pass: The pass statement is basically a null statement,
which is generally used as a placeholder. It is used to
prevent any code from executing in its scope.
"""
print()
for i in range(5):  
      if i % 2 == 0:     
             pass   
      else:       
           print(i) 

#return - 
def myreturn (x):
    if x=='hello':
     return True
    else:
        return False
     
print(myreturn(input()))