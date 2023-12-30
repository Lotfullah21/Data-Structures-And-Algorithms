# arrays across functions are always connected, if one function brings some modification to the main array, that array will be changed for all functions if we are referencing to the object
# itself.
# it is because arrays are created in the heap, once the array is created, all vars and functions references to the same heap address and any modification will effect the main array.


def swap_elements(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

n = int(input("Enter length of the array: "))
arr = [0] * n

index1 = int(input("swap index 1: "))
index2 = int(input("swap index 2: "))

for i in range(0, n):
    arr[i] = int(input(f"Enter digit {i}: "))

# Call the function to swap elements
swap_elements(arr, index1, index2)

print(arr)
