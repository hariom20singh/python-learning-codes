import numpy as np
#arrange function

print(np.arrange(2,10))
print(np.arrange(2,10,2))
print(np.arrange(1,2,0.1))

#linspace function
print(np.linspace(1,2,10))

#reshape function
a=np.array([1,2,3,4,5,6,7,8,9])
print(a.reshape(3,3))

#dot function
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.dot(a,b))
vec_a=2+3j
vec_b=4+7j
print(np.dot(vec_a,vec_b))

#argmin function
a=np.array([1,2,3,4,5,6,7,8,9])
print(np.argmin(a))
#argmax function
print(np.argmax(a))

#mean function
print(np.mean(a))
#median function
print(np.median(a))
#standard deviation function
print(np.std(a))
#variance function
print(np.var(a))

#concatenate function
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.concatenate((a,b)))
#stack function
print(np.stack((a,b)))
print(np.stack((a,b),axis=1))

#split function
a=np.array([1,2,3,4,5,6,7,8,9])
print(np.split(a,3))
print(np.split(a,[3,5]))

#sort function
a=np.array([1,2,3,4,5,6,7,8,9])
print(np.sort(a))
#reverse function
print(np.sort(a)[::-1])

#unique function
a=np.array([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9])
print(np.unique(a))


