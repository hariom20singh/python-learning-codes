def search(arr, x):
 
    for i in range(len(arr)):
 
        if arr[i] == x:
            return i+1
 
    return -1
print("Enter the list of numbers seprated by space")
arr = [int(i) for i in input().split(" ")]
print("Enter the key")
x = int(input())

print(search(arr, x))
