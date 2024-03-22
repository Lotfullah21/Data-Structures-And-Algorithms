def selectionSort(arr: list) -> list:
    "Returns a sorted array in increasing order"
    n = len(arr)
    for i in range(n-1):
        min_ele = arr[i]
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx]>arr[j]:
                min_idx = j
                min_ele = arr[j]
        
        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp
    return arr
        
array = [1, 0, 12, -2, 4, 5, 6, 2, 4, 3]
sorted = selectionSort(array)
print("Sorted Array:", sorted)