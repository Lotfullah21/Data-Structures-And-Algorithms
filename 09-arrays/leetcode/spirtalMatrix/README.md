<a href = "https://leetcode.com/problems/spiral-matrix/description/">leetcode</a>

#### Question

Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Solution to the leetcode platform.

```py
class Solution:
    def spiralOrder(self, arr: list[list]) -> list[int]:
        n = len(arr)
        m = len(arr[0])
        ans = []
        count = 0
        i = 0
        j = 0
        rowSteps = n - 1
        colSteps = m - 1
        while(rowSteps>=1 and colSteps>=1):
            for _ in range(colSteps):
                ans.append(arr[i][j])
                j+=1
            for _ in range(rowSteps):
                ans.append(arr[i][j])
                i+=1
            for _ in range(colSteps):
                ans.append(arr[i][j])
                j-=1
            for _ in range(rowSteps):
                ans.append(arr[i][j])
                i-=1

            colSteps-=2
            rowSteps-=2
            i +=1
            j +=1
        if rowSteps==0:
            for _ in range(colSteps+1):
                ans.append(arr[i][j])
                j+=1
        elif colSteps==0:
            for _ in range(rowSteps+1):
                ans.append(arr[i][j])
                i+=1
        return ans


```
