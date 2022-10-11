#Tuples in python
'''
Tuples are entities in Python that work almost similar to that of lists, but differ in the
main feature from lists, is in that they are inmutable.
They are initialized by writing the elements of the tuple with (), separated by
commas.
'''

#Defining and initializing a tuple name - example
example = ('first','second','third','fourth')
# example[1]="pahela" #This is not supported by tuple
print(example)
print(example[0])
print(example[3])
print(example[1:3])#print the indexno.-1 , indexno.-2


#type converting between tuple ,lists and strings
demo_list = list(example)
print('Tuple converted into list -> ',demo_list)

demo_tuple = tuple(demo_list)
print('List converted into tuple : ',demo_tuple)

list_string = list('rishabh')
tuple_string = tuple('rishabh')
print(list_string)
print(tuple_string)