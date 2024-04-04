### Question:

Given an array arr of size n and an integer X. Find if there's a triplet in the array which sums up to the given integer X.

### Idea-1(Brute Force):

Use three nested loops and try every possible combination.

```py
class Solution:
    def findTriplet(self, arr: list, X: int) -> list:
        nums = []
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if arr[i]+arr[j]+arr[k]==X:
                        nums.append((arr[i],arr[j],arr[k]))
                        return True, nums

```

### Analysis

`Time complexity`:`O(n^3)`, where n is the number of elements in the array. This is because we have three nested loops.
`Space Complexity`:`O(1)`

### Idea-2:

Sort the array and use two pointers to keep the track of summation.

```py

class Solution:
    def findTriplet(self, arr: list, X: int) -> list:
        """Checks if tree distinct elements can sum up to give X

        Args:
            arr (list): list of numbers
            X   (int) : a value that we are looking to get the summation elements for.

        Returns:
            list: a boolean and indices of the integers that sum up to give x, if not found, False.
        """
        nums = []
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if arr[i]+arr[j]+arr[k]==X:
                        nums.append((arr[i],arr[j],arr[k]))
                        return True, nums

        return False



solution = Solution()
arr = [2, 4, 6, 12, 12,3,4,5,7,8,9,9,90, 12,32,43,13,4,5,32,54,32,5,64,2,3232,3232,3232,22,4,2,24,3,6,102]
result = solution.findTriplet(arr,111)
print("result", result)



```

### Analysis

`Expected Time Complexity`: `O(n2)`.
`Expected Auxiliary Space`: `O(1)`.
