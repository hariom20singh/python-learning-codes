
#list is a circular linked list which is used to store the multiple values .
weekdays= ['sunday','monday','tuesday','wednesday']
print(weekdays)
#positive indexing 
print(weekdays[0],weekdays[2])
#negative indexing
print(weekdays[-1],weekdays[-2])

multi_val=['rishavh',34,'rakesh',-34,39.09,'s']
print(multi_val)
"""
Slicing of list - 
if 4 element of data present in list than 
positive indexing -   0   1   2   3 
negative indexing -  -4  -3  -2  -1

list[ps_iex:ps_iex]==> list_name[3:2]
list[ng_iex:ng_iex]==> list_name[-3:-2]
"""
print(weekdays[1:4])
print(weekdays[-3:-1])


# changing values in list
#weekdays[0]=45
print(weekdays)
weekdays[0]='holiday'
print(weekdays[0])
print(weekdays)