import numpy as np
#1 D array
a=np.array([1,2,3,4,5])
print(a)
#2 D array
b=np.array([[1,2,3],[4,5,6]])
print(b)
#array of zeroes
c=np.zeros((2,3))
print(c)
#array of ones
d=np.ones((2,3))
print(d)
#array of any number
e=np.full((2,3),5)
print(e)
#identity matrix
f=np.eye(3)
print(f)
#random matrix

g=np.random.random((2,3))
print(g)
#random arrays in fixed range
h=np.random.randint(1,10,(2,3))
print(h)
#convert a list to numpy array
list1=[1,2,3,4,5]
np_array=np.asarray(list1)
print(np_array)
#transpose a matrix
print(np.transpose(h))
