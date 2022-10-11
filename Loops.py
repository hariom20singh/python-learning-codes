#1 for loops
#--> for with range -
for i in range(5):
    print(i)
    #this print 0 1 2 3 4 
#--> for with range (start , stop , step)
print()
for i in range(2,11,2):
    print(i)
    # print - 2 4 6 8 10
print()
#for with in - used to iterate different containers in python
a = [4,6,4 ,3,2]
for ele in a :
    print(ele)

#2.) while loops 
cont = 5  
print()
while cont>0 :
    print(cont)
    cont=cont-1