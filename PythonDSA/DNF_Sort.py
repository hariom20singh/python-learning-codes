def dnfSort(arr, n):
    low = 0
    mid = 0
    high = n - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low = low + 1
            mid = mid + 1
        elif arr[mid] == 1:
            mid = mid + 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high = high - 1

def main():
    arr = [int(x) for x in input("Enter space separated numbers to sort: ").split()]
    dnfSort(arr, len(arr))
    print("Sorted array: ", arr)

if __name__ == "__main__":
    main()