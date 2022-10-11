#set :- {1,2,3,4}-unique and unordered
'''
Sets are initialized using curly braces {} or set() in python.
A python set is basically an unordered collection of unique values, i.e. it will
automatically remove duplicate values from the set.
'''
set1 = {1,2,3}
print('set : ',set1)
set2 = set(['tea','coffee','colddrink','soda','tea','Coffee'])
print('set : ',set2)
dup_set={1,1,1,1,1,2,2,2,4,4,56,5,5,4,6,4,56,4,4,5,4,5}
print(dup_set)

#using the add() method we can add single element in the set 
dup_set.add(456)
print(dup_set)

#using the update() method we can add multiple elements in the set 
dup_set.update(['water','drink','coca'])
print(dup_set)

#deleting an element within the set 
dup_set.remove(1)
# dup_set.remove(1)#IF ELEMETN IS NOT PRESENT IN  THE SET THEN remove() method raise an error
print('after deleting : ', dup_set)

#discard method does not raise an error
dup_set.discard(2)
dup_set.discard(12)#doesn't raise an error
print("after discarding", dup_set)


#OPERATORS IN THE SETS 
"""
| (Union)->Returns all the unique elements in both the sets.
& (Intersection) -> Returns all the elements common to both the sets.
- (Difference)-> Returns the elements that are unique to the first set
^(Symmetric Difference) -> Returns all the elements not common to both the sets.

"""
set_A={1,5,2,84,2,4,5}
print('Set A : ', set_A)

set_B ={2,5,32,4,2,8,5,6}
print('Set B : ', set_B)

#intersection of two sets 
print('Intersection : ',set_A&set_B)

#union of two sets 
print('Union : ', set_A|set_B)

#difference of two sets
print('Difference :', set_A-set_B)#consider only unique in first set(not  consider common with other sets )

#symetric difference of two sets
print("Symetric Difference : ",set_A^set_B)#neglact the common in both sets 