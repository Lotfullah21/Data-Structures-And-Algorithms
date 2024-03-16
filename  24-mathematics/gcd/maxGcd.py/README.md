#### Idea-1:

Brute force, check for all elements and find their gcd.

```py
class Solution:
    def maxGcd(self, arr: list) -> int:
        "Removes an array to maximize the gcd of remaining elements."
        n = len(arr)
        max_gcd = 0
        for i in range(n):
            # Create a temp array where one ith element is not included
            temp_arr = arr[:i] + arr[i+1:]
            # Start from oth element.
            result_gcd = temp_arr[0]
            # Calculate the gcd for each temp array.
            for j in range(1, len(temp_arr)):
                result_gcd = self.gcd(result_gcd, temp_arr[j])
            if result_gcd > max_gcd:
                max_gcd = result_gcd
        return max_gcd, temp_arr

    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b % a, a)


solution = Solution()
arr = [24, 16, 18, 30, 15]
result = solution.maxGcd(arr)
print(result)

```

#### Analysis:

`Time Complexity` is `O(N)` for finding `GCD`, `O(N)` for checking all element's `CGD` and `O(N)` to go for different arrays; in total `O(N*N*logN)`
`Space Complexity` is `O(logN)` is the stack space, it can be removed if the implementation is done using Iterative approach.

#### Idea-2:

`Time Complexity` is `O(NlogN)`.
`Space Complexity` is `O(N)` for prefix ans suffix calculations.
