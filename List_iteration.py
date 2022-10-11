#Using loops itereation - In a list iterate all elements through loop
week=['saturday','sunday','monday','tuesday','wednesday']
d=0

for day in week:
    print(day,':',d)
    d+=1

#using IN and NOT Keyword check whether element is present or not 
print( "tuesday" in week)
print('hello' not in week)

#Adding values in list 

#1. insert(position, value)-> This function inserts an element into a particular index of a list.

week.insert(0,'specialDay')
print(week)

#2.append(): This function appends an element at the back of a list.
week.append('lastDay')
print(week)