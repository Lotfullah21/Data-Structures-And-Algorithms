### Selection Sort

It works based on the idea of find the min-elements and put in the array in increasing order; first minimum in first place, 2nd minimum in 2nd place and so on.

It also make the foundation for heap sort algorithm; heap sort uses head data structure to optimize selection sort.
At each outer iteration, find the minimum and swap it with current element.
It is not stable, the order of equal elements may change.

```py

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
print("Sorted Array:", sorted) # Sorted Array: [-2, 0, 1, 2, 3, 4, 4, 5, 6, 12]
```

Time complexity is `O(N^2)` and space complexity is `O(1)`
