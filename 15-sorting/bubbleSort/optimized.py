def bubbleSort(arr: list) -> list:
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                swapped = True
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        if swapped == True:
            return 
    return arr

array = [1, 0, 12, -2, 4, 5, 6, 2, 4, 3]
sorted = bubbleSort(array)
print("Sorted Array:", sorted)