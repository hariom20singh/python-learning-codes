"""
Time complexity:
    Worst case: O(∞)
    Average case: O(n * n!)
    Best case: O(n)
"""

from random import randint

def bogosort(arr):
    while not is_sorted(arr):
        shuffle(arr)
    
def shuffle(arr):
    for i in range(len(arr)):
        j = randint(0, len(arr) - 1)
        arr[i], arr[j] = arr[j], arr[i]

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def main():
    print("Enter space separated numbers to sort: ", end="")
    arr = [int(x) for x in input().split()]
    bogosort(arr)
    print("Sorted array: ", arr)

if __name__ == "__main__":
    main()