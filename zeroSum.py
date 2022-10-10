n=int(input('Enter number of inputs:\n'))
arr=[int(input("Enter single number and press enter: ")) for _ in range(n)]

zero_sum_count=0
for i in range(len(arr)):
    tmp=[]
    for j in range(i,len(arr)):
        tmp.append(arr[j])
        if sum(tmp)==0:
            zero_sum_count+=1
print('Number of Subarrays with zero sum = ',zero_sum_count)