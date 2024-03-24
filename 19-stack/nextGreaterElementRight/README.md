### Question

Given an array arr[ ] of size N having elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.
Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.
<a href="https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1?itm_source=geeksforgeeks">GFG</a>

### 1.Brute Force

Go through each array element and check if the next and next elements are greater than current element, once that greater element found; break out of the loop and increment and continue for the next elements.

```py
class Solution:
    def nextLargerElement(self,arr,n):
        ans = [-1]*n
        for i in range(n):
            for j in range(i+1, n):
                if arr[j]>arr[i]:
                    # Swap the current smaller element with greater element to its right.
                    ans[i] = arr[j]
                    # Once found, break out of the loop and loop for other element.
                    break
        # If you do not initialize ans array with -1, run the following loop.
        # for i in range(n):
        #     if ans[i]==0:
        #         ans[i] = -1
        return ans
```

#### Analysis:

`Time Complexity` is `O(N*N)`, we have to check for each element inside the array.
`Space Complexity` is `O(1)`

Can we do it in better `complexity`;
Lets use `Stack`.

#### 2. Stack:

```py
class Solution:
    def nextLargerElement(self,arr,n):
        stack = []
        print(stack)
        ans = [-1]*n
        for i in range(n):
            while len(stack)>0 and arr[i]>arr[stack[-1]]:
                idx = stack.pop()
                print("idx",idx)
                ans[idx] = arr[i]
            stack.append(i)
        while stack:
            idx = stack.pop()
            ans[idx] = -1
        return ans


N = 4
arr = [1, 3, 2, 4]
solution = Solution()
result = solution.nextLargerElement(arr,N)
print(result)
[3, 4, 4, -1]
```

#### Analysis:

`Time Complexity` is `O(N)`, for each element, there is a finite number of possibilities, either replace, do not replace or replace and at max replace N element at last if previous could not.
`Space Complexity` is `O(N)` for stack space
