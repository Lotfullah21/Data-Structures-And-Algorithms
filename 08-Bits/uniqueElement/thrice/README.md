#### Question:

Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

#### Idea-1:

Using Hashmap.
it generally works for all.

#### Analysis

`Time Complexity` is `O(N)`,
`Space Complexity` is `O(N)`.

```py
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_count = {}  # Dictionary to store count of each number

        # Count occurrences of each number in the list
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1

        # Find the number with a count of 1
        for num, count in num_count.items():
            if count == 1:
                return num

        # If no number is found, return -1 or any default value
        return -1  # Or any other default value as needed


```

#### Idea-2:

Using bitwise `Counting` operation.
`Time Complexity` is `O(N)`.
`Space Complexity` is `O(1)`.

If number of repeated elements are twice.
<a href="xhttps://leetcode.com/problems/single-number-ii/description/">leetcode</a>

```py
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(32):
            count = 0
            for j in range(n):
                # Check the i-th bit for each number
                if nums[j] & (1 << i):
                    count += 1
            # For negative numbers, count the bits differently
            if count % 3 != 0:
                # Handle negative numbers correctly by checking the sign bit
                # If it's the sign bit
                if i == 31:
                # Set the sign bit for negative result
                    ans -= (1 << i)
                else:
                     # Set the bit in the answer
                    ans = ans + (1 << i)
        return ans
```

The bellow snippet is crucial to check if the given elements are +ve or negative, for negative elements, the `31th` bit is 1. Generally for signed elements.

```py
                if i == 31:
                # Set the sign bit for negative result
                    ans -= (1 << i)
                else:
                     # Set the bit in the answer
                    ans = ans + (1 << i)
```

#### Question:

Given an integer array nums where every element appears three times except for one, which appears exactly twice. Find the single element and return it.

#### Solution:

If total count is `3*N`, Do nothing;else if count is `3*N+2`, set that bit.

```py
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(32):
            count = 0
            for j in range(n):
                # Check the i-th bit for each number
                if nums[j] & (1 << i):
                    count += 1
            # For negative numbers, count the bits differently
            if count % 3 == 2:
                # Handle negative numbers correctly by checking the sign bit
                # If it's the sign bit
                if i == 31:
                # Set the sign bit for negative result
                    ans -= (1 << i)
                else:
                # Set the bit in the answer
                    ans = ans | (1 << i)

        return ans

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    solution = Solution()
    result = solution.singleNumber(nums)
    print(result)
```

#### Question:

Given an integer array nums where every element appears four times except for one, which appears exactly once. Find the single element and return it.

#### Solution:

If total count is `3*N`, Do nothing;else if count is `3*N+2`, set that bit.

```py
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(32):
            count = 0
            for j in range(n):
                # Check the i-th bit for each number
                if nums[j] & (1 << i):
                    count += 1
            # For negative numbers, count the bits differently
            if count % 4 == 1:
                # Handle negative numbers correctly by checking the sign bit
                # If it's the sign bit
                if i == 31:
                # Set the sign bit for negative result
                    ans -= (1 << i)
                else:
                # Set the bit in the answer
                    ans = ans | (1 << i)

        return ans

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    solution = Solution()
    result = solution.singleNumber(nums)
    print(result)
```

Another approach which will have `O(N)` rather than the previous approach which has `O(32*N)`

```py
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = nums[0]
        n = len(nums)
        for i in range(1, n):
            answer = answer^nums[i]
        return answer

```
