def binarySearch(nums,val):
    low=0
    up=len(nums) -1

    while low<=up :
        mid = (low + up) //2

        if nums[mid] == val:
            
            return f'Element {val} found at position {mid}'

        elif nums[mid] < val:
            low = mid+1
        else:
            up=mid-1
    


inp = [4,7,8,12,45,99]
key=int(input("Enter the num to search:\n"))

out =  binarySearch(inp,key)

if out:
    print(out)
else:
    print("Element did not found! ")    