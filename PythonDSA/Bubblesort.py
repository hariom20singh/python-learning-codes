''' 
#Working of Bubble sort
-Starting from the first index, compare the first and the second elements.
-If the first element is greater than the second element, they are swapped.
-Now, compare the second and the third elements. Swap them if they are not in order.
-The above process goes on until the last element.'''
# Bubble sort in Python

def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)
