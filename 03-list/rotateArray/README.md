#### Question:

Given an unsorted array arr[] of size N. Rotate the array to the left (counter-clockwise direction) by k steps, where k is a positive integer.

#### Example:

Input:
N = 5, k = 2
arr[] = {1,2,3,4,5}
Output: 3 4 5 1 2
Explanation: 1 2 3 4 5 when rotated
by 2 elements, it becomes 3 4 5 1 2.

#### Idea-1:

it does not modify the input list.

```py
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self,A,k,N):
        #Your code here
        return A[k:] + A[0:k]

```

#### Idea-2:

```py
class Solution:

    def rotateArr(self, arr, K, N):
        # Number of effective rotation, because after len(arr) rotation the array will be same.
        K = K % N
        # Reverse Whole array
        self.reverse(arr, 0, N-1)
        # Reverse up to first K element.
        self.reverse(arr, 0, K - 1)
        # reverse after Kth element.
        self.reverse(arr, K, N - 1)
        return arr


    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

```

#### Analysis:

`Time Complexity` is `O(3*N)==O(N)`, because on reverse operation takes `O(N)` and we are doing 3 reverse operation, but for `O(N)`, constants are ignored.
`Space Complexity` is `O(1)`, no extra space used and the rotation is done in place
