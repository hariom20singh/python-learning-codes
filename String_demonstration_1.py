# IN this we will  see how to produce different output with same string
s = "Bamboozled"
# extract B a
print(s[0], s[1])  # using normal indexing
print(s[-10], s[-9])  # using negative indexing
# extract e d
print(s[8], s[9])  # using normal indexing
print(s[-2], s[-1])  # using negative indexing
# extract mboozled
print(s[2:10])  # specifying from start to end
print(s[2:])  # specifying from and not giving end
print(s[-8:])  # using negative indexing
# extract Bamboo
print(s[0:6])  # using normal indexing
print(s[:6])  #not speciying the first caharcter by speciying the last
print(s[-10:-4])
print(s[:-4])
#reverse Bamboozled
print(s[::-1])#this will reverse the Bamboozled 
print(s[0:10:1])
print(s[0:10:2])#this will print after 2 character 
print(s[0:10:3])
print(s[0:10:4])
s=s+"Hype!"#concating the hype
print(s)
s=s[:6]+"Monger"+s[-1] #how to add any word in between 
print(s)
