#### Question:

Given an integer array nums where every element appears two times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

#### Idea-1:

Using Hashmap.

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

Using bitwise `XOR` operation.
`Time Complexity` is `O(N)`.
`Space Complexity` is `O(1)`.

If number of repeated elements are twice or repeated elements are even, the given code can be used to find the single element.

```py
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = nums[0]
        n = len(nums)
        for i in range(1, n):
            answer = answer^nums[i]
        return answer

```
