#### Question:

Check if the given array is sorted.

input: [1, 2, 3, 4, 9, 11]
Output: True

Input: [1, 2, 3, 4, 0]
Output: False
Explanation: at last index, the 0 is smaller than 4, so the array is not sorted.

#### Idea-1:

Compare each element to its previous, if larger than previous, the array is sorted.

```py
def isSorted(arr: list) -> bool:
    "Returns True if array is sorted"
    i = 1
    while i<len(arr):
        if arr[i]<arr[i-1]:
            return False
        i+=1
    return True

```

#### Idea-2:

Sort the array first and compare to the original array, if both of them are same, the array is sorted.

```py

def isSorted(arr: list) -> bool:
    "Returns True if array is sorted"
    i = 1
    newArray = arr[:]
    newArray.sort()
    if arr==newArray:
        return True
    else:
        return False
```

#### Analysis:

#### Idea-1

`Time Complexity` is `O(N)`, Traversing whole array.

`Space Complexity` is `O(1)`, no extra space used.

#### Idea-1

`Time Complexity` is `O(NlogN)`, sorting time complexity is `O(NlogN)` in the worst case.

`Space Complexity` is `O(N)`, we are copying all elements into a new array.
