def selectionSort(arr: list) -> list:
    "Returns a sorted array in increasing order using selection sort algorithm"
    n = len(arr)
    # To n-1, because the comparison is done from i up to n; n is included in the inner loop.
    for i in range(n-1):
        
        min_idx = i
        for j in range(i+1, n):
            # Whenever the smaller element found, update the min index.
            if arr[min_idx]>arr[j]:
                min_idx = j
        # in each iteration, found the min index among all and swap them with ith element.
        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp
    return arr
        
array = [1, 0, 12, -2, 4, 5, 6, 2, 4, 3]
sorted = selectionSort(array)
print("Sorted Array:", sorted)