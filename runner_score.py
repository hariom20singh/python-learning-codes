score = int(input())
arr= list(map(int,inpt(.split()))
z=max(arr)
m=-101
for i in arr :
    if i==z :
        continue
    else :
        if i>m :
            m=i
print(m)         
