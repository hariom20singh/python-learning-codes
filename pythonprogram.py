# Write a Python program to insert items into a list in sorted order.
import bisect
# Sample list
my_list = [25, 45, 36, 47, 69, 48, 68, 78, 14, 36]

print("Original List:")
print(my_list)
sorted_list = []
for i in my_list:
    position = bisect.bisect(sorted_list, i)
    bisect.insort(sorted_list, i)
print("Sorted List:")
print(sorted_list)
