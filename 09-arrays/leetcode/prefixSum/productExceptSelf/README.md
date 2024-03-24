Lets discuss two ideas here

### Idea-1

If division is allowed:

1. calculate total production of the array
2. for each index, divide the total product to each element.
3. return new array

```py
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_product = 1
        for i in range(n):
            total_product = total_product*nums[i]
        for i in range(n):
            nums[i] = int(total_product/nums[i])
        return nums

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Lets do iterations here for given input.
total_product = 24
nums[0] = 24/nums[0] = 24/1 = 24
nums[1] = 24/nums[1] = 24/2 = 12
nums[2] = 24/nums[2] = 24/3 = 8
nums[3] = 24/nums[3] = 24/4 = 6


```

### Idea-2:

If division method is not allowed.
Here we need to the multiplication up to the index we want excluding the current index and multiplication after the index we want; At the left side and right side multiplications will be multiplied to give the multiplication of elements in the array except the current index.

#### Left Hand Side Multiplication:

using prefix concept, the multiplication can be generated using below loop.

```py
    for i in range(n):
        total_product = total_product*nums[i]
```

Once the give array is generated, we are having the left hand side multiplication results.

#### Right Hand Side Multiplication:

Using a variable called `suffix`, the right hand side multiplication array can be generated; How?
Start a reverse loop, the mul element after last index is 1, it does not change anything.
Every time we move from right side to left, multiply current suffix with the current right element.

```py
    for i in range(n-1, 0, -1):
        pf[i] = pf[i-1]*suffix
        suffix = suffix*nums[i]
    pf[0] = suffix



# Lets say, We want to get the multiplication result after ith element.
# suffix=1, hence the result is also one.
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# we have pf = [1,2,6,24]
# n = 4
# i = n-1 = 3

pf = [1,26,24]

suffix = 1
pf[3] = pf[2]*suffix = 6*1 = 6
suffix = 1*nums[3] = 4

i = n-2 = 2
pf[2] = pf[1]*suffix  = 2*4 = 8
suffix = suffix*nums[i] = 4*3 = 12

i = n-3 = 1
pf[1] = pf[0]*suffix = 1*12 = 12
suffix = suffix*nums[i] = 12*2 = 24

i = 0
pf[0] = suffix = 24

# pf = [24, 12, 8, 6]

# For reference, this is how suffix looks like:
# suffix = [24, 24, 12, 4] and it is the multiplication of the array from right side.
```

<a href="https://leetcode.com/problems/product-of-array-except-self/">leetcode</a>
