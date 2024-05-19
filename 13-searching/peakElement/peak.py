def peakElement(arr: list, n: int) ->int:
    "Returns the index of largest element in the array"
    left, right = 0, n - 1
    
    while left < right:
        mid = left + (right - left) // 2
    
        # Check if mid is a peak
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return left

# Example usage:
arr1 = [1, 2, 3]
n1 = len(arr1)
print(peakElement(arr1, n1))  


