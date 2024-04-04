### Algorithm

The idea is to keep all the elements smaller than the first element at the left hand side and all the elements greater than 0th index to the right hand side.

## Quick Sort:

Follow the re-arranging procedure but use recursion to arrange the smallest element which is a single element.
each time the `reArrangeArray` function is called, it returns the index which the current element shifted, or the correct position of the left most element.
Now, that index is pivotal in moving to the left and right side of the original array to sort.

```py
    def quickSort(self,arr,low,high):
        if low>=high:
            return
        p = self.reArrangeSubArray(arr, low, high)
        self.quickSort(arr, low, p-1)
        self.quickSort(arr,p+1, high)
```

## Tail Call Elimination:

To reduces one extra recursion call, the right or left call can be eliminated with using a while loop.

```py
    def quickSort(self,arr,low,high):
        while low<high:
          p = self.reArrangeSubArray(arr, low, high)
          self.quickSort(arr, low, p-1)
          low = p + 1
```

The base case is when the left and right side cross each other or start index == end index.

#### Analysis

- The nightmare for quick sort happens when the array is sorted and quick sort pointers one point at each call.
  So, the `reArrangeArray` time complexity is `O(N)` , and if `quickSort` is also called `N` times, then, the time complexity would be `O(N^2)`.

- Space complexity is the stack space we are using to call the functions repeatedly and that is `O(N)`.

#### Note:

On average, the time complexity is `O(NlogN)` and space complexity is `O(logN)`

#### Application:

when the memory cost is more, which means with every writing, the age of memory reduces, Then quick sort is best choices than all other standard algorithms.
