#List compherension
a = [1,2,3,4,5]
print('List A : ',a)
#b is store the multiply of 2 with a 's list element
b=[i*2 for i in a]
print('List B: ',b) 

#set compherension
set_A = {4,5,2,4,2,5,4,6,8,2}
#set_B is store the square of element in set_A 
set_B={i**2 for i in set_A}
print('Set A : ',set_A)
print('Set B : ',set_B)


# Dict Comprehension:
# It is a shorter syntax to create a new dictionary using values of an existing
# dictionary.
a = {'Hello':'World', 'First': 1}
# b stores elements of a in value-key pair format
b = {val: k for k , val in a.items()}
print(b)