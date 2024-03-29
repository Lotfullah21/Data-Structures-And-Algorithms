### Question:

Given a sorted array of integers of size N and a number X. Find the leftmost index of X in the array arr[]. the elements might appear more than once.

Input:
N = 10
arr[] = {2, 2, 3, 3,4, 5, 5, 6, 7}
X = 3
Output: 2
Explanation: Because the element 3  
appears twice and its left most
occurrence is at index 2.'

### Idea-1:

traverse the whole array from left to right and return the first index occurrence of the given number.

```py
class Solution:
    def leftIndex(self,N,arr, K):
        for i in range(N):
            if arr[i]==K:
                return i
        return -1
```

### Idea-2:

Use linear binary search algorithm.

#### Idea-1

`Time Complexity` is `O(N)`, Traversing the whole array if the target is not present or at last index..

`Space Complexity` is `O(1)`, no extra space used.

#### Idea-1

`Time Complexity` is `O(logN)`, sorting time complexity is `O(logN)` in the worst case.

`Space Complexity` is `O(1)`, we are copying all elements into a new array.
