### Question:

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation: [5, 3] is also a valid answer.

### Idea-1:

Hashmap: use hashmap and return the count of elements that occurs one and return it.

### Analysis:

`Time Complexity` is `O(N)` as we are going through each element.
`Space Complex` is `O(N)` because we are saving the elements with their respective counts in a dictionary.

```py
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num]+=1
            else:
                counts[num]=1
        new_list =[]
        for ele, count in counts.items():
            if count==1:
                new_list.append(ele)
        return(new_list)
```

### Idea-2:

`Time Complexity` is `O(N)` as we are going through each element.
`Space Complex` is `O(1)` because we are not using any additional space.

```py

from typing import List
class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        # Find the xor of two single numbers
        n = len(nums)
        answer = 0
        for i in range(n):
            answer = answer^nums[i]
        # Find the index that is set in answer
        idx = 0
        for i in range(32):
            if self.checkBit(answer, i) == True:
                idx = i
                break

        # Use two sets to find the single numbers
        set1 = 0
        set2 = 0
        singleNumbers = []
        for i in range(n):
            num = nums[i]
            if self.checkBit(num,idx) == True:
                set2 = set2^num
            else:
                set1 = set1^num
        singleNumbers.append(set1)
        singleNumbers.append(set2)
        return singleNumbers

    def checkBit(self, N, i):
        if N&(1<<i)!=0:
            return True
        else:
            return False

nums = [1,2,1,3,2,5]
solution = Solution()
result = solution.singleNumber(nums)
print(result)
```
