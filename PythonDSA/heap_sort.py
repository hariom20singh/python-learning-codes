import time
import random

def heapify(arr, n, i):
	largest = i 
	l = 2 * i + 1	 
	r = 2 * i + 2	 
	if l < n and arr[largest] < arr[l]:
		largest = l
	if r < n and arr[largest] < arr[r]:
		largest = r
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] 	
		heapify(arr, n, largest)

def heapsort(arr,n):
	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] 
		heapify(arr, i, 0)

l = []
a = int(input("Enter the size of array: "))
for i in range(a):
    n = random.randint(1, 100)
    l.append(n)

start = time.time()
heapsort(l, a)
end = time.time()
t = end-start
print(f"heapsort running time: {t:.4f}")
