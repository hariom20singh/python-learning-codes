dict_demo ={'first':1,'second':2,'third':3}
print("dictionary :",dict_demo)
keylist = list(dict_demo.keys())
print('keys : ',keylist)
valuelist = list (dict_demo.values())
print ('values : ', valuelist)

# .keys() function is used to print keys of dictionary
for k in dict_demo.keys():
    print(k)
    
#.values() function is used to print value of dictionary
for v in dict_demo.values():
    print(v)


#print the dictionary item
print('value at key[]-first ',dict_demo['first'])

#update key value which is present in the dictionary
print()
dict = {0 : 'sunday', 1 : 'monday', 2 : 'tuesday'}
# print (dict['first'].items())
for item in dict.items():
    print(item)
print()
dict[2] = 'wednesday'
for item in dict.items():
    print(item)

# we can merge two dictionary into 1 dictionary using update() method 

dict.update(dict_demo)
print(dict)
