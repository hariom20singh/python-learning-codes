import sys

arr = list(map(int, input().split()))
max_so_far = -sys.maxsize
max_ending_here = 0
start = 0
end = 0
s, e = 0, 0 

for i in range(len(arr)):
    max_ending_here += arr[i]
    if max_ending_here > max_so_far:
        max_so_far = max_ending_here
        end = i
        start = s
    if max_ending_here < 0:
        max_ending_here = 0
        s = i+1
print("Maximum contiguous subarray sum: ", max_so_far)
print("Starting index: ", start)
print("Ending index: ", end)
