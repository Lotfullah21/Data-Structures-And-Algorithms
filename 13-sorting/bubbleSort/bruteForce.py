def bubbleSort(arr: list) -> list:
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

array = [1, 0, 12, -2, 4, 5, 6, 2, 4, 3]
sorted = bubbleSort(array)
print("Sorted Array:", sorted)