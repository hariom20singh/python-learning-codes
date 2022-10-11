#Escapes sequences in string 
print('this is used to \n new line')
print('this is used to \t tab escape')
print('this is ued to print backslash \\')
print('your\'s is written like this ')



#multiple string
a ='''\nthis hwo 
you 
can do 
this .
using this you can write multiple lines 
as '''
print(a)

#String indexing 

print('\n')
#  p  y  t  h  o n
#  0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1
p = 'python'
print(p[0],p[2],p[4],p[5])
print(p[-1],p[-2],p[-4],p[-6])

# String slicing
print(p[-6:-4])
print(p[2:6])
print(p[3:-1])

# Case Conversion Functions
first_name ='rishabh'
#1 upper
print('upper case - ',first_name.upper())
last_name = 'YaDav'
#2 lower
print('lower case - ',last_name.lower())
print('first name is lower or not - ',first_name.islower())
print('last name is upper or not - ',last_name.isupper())
print('first name is lower or not - ',first_name.upper().islower())
print('last name is upper or not - ',last_name.upper().isupper())

#string join() and split() function
temp_list = ['hello','how ,are ,you']
s=' '.join(temp_list)
print(s)
newlist = s.split(',')
print(newlist)

first = "first"
second = "second"
s = "Sunday is the {} day of the week, whereas Monday is the {} day of the week".format(first, second)
print(s)
