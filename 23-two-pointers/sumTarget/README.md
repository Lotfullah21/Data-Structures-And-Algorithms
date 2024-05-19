## Two Pointers:

Try using two pointers when there is need of checking all the pairs, but it does not mean it can applied to all the problems.

#### Before Using Pointers.

- Where to initialize two pointers.
- Step-2: Update your pointers.
- Step-3: When to stop

<a href="https://leetcode.com/problems/two-sum/">leetcode</a>

### Idea-1: Brute Force

```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]+nums[j] ==target:
                    return [i,j]
        return []

```

### Idea-2: Using Two Pointers

If array is sorted, finding the target can be done in `0(N)` operations.
If the array is not sorted, then the array should be sorted. The time complexity would be `O(N+Nlogn) = O(NlogN)`.

The following code only works if the array is already sorted, because in the question, it asks us to return the original indices, there is a need to tweak the implementation.

```py
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums.sort()

        i = 0
        j = n - 1
        while i < j:
            totalVal = nums[i] + nums[j]
            if totalVal == target:
                return [i, j]
            elif totalVal < target:
                i += 1
            else:
                j -= 1
        return [0, 0]

solution = Solution()
nums = [3, 2, 400, 90]
target = 402
While sorting the array of numbers, we lose track of their original indices in the nums array.
when nums is sorted: [2, 3, 90, 400] and the indices that leads to 402, [0,2] which  nums[0]=2 and nums[3]=400; but it should be [1,2] based on original array.
```

### How To Keep The Original Indices While Sorting:

Create a pair class and sort that pair class instead of the main array.
In the pair class, keep the number and their indices as the main attributes.
Sort the pairs based on the value, not the based on their indices.
We will be having to the original indices in the later, because we only sorted the numbers not indices.

#### Advantages of Using Pair Class:

Preserve Original Indices: The Pair class allows us to keep track of the original indices of the numbers while sorting based on their values.
Retrieve Original Indices: When we find the pair of numbers that add up to the target, we can easily retrieve their original indices from the Pair objects.

### Example:

#### Pair Class

```py

class Solution:
    class Pair:
        def __init__(self, num, idx):
            self.num = num
            self.idx = idx

```

arr = [3, 2, 90, 400, 1]; target = 402

1. #### The Pair objects would be

When `arr = [self.Pair(nums[i], i) for i in range(n)]` is called.

```py
Pair(3, 0): Represents nums[0] = 3 with index 0
Pair(2, 1): Represents nums[1] = 2 with index 1
Pair(90, 2): Represents nums[2] = 90 with index 2
Pair(400, 3): Represents nums[3] = 400 with index 3
Pair(1, 4): Represents nums[4] = 1 with index 4

Final Pairs looks like this: [Pair(3, 0), Pair(2, 1), Pair(90, 2), Pair(400, 3), Pair(1, 4)]
```

2. #### Sorting Behavior:

Define based on what order you want sort, here it goes based on natural order, increasing order:
First, we check if two numbers are not same, if not same; Sort them based on the values. The objects with lesser value comes before the object with greater value.

Second, if the objects values are the same, sort based on the indices.
Here, We keep the natural order of the numbers if they are the same.

```py
    def __lt__(self, other):
        # If two numbers are different
        if self.num !=self.other:
            # The number with lesser value comes before other.value.
            if self.num<other.num:
                return True
            # If Two numbers are the same.
        else:
            # Sort based on which ever comes first.
            if self.idx<other.idx:
                return True
```

3. #### Sorting.

```py
    def twoSum(self, nums, target):
        n = len(nums)
        # It generates all the pairs in one go.
        arr = [self.Pair(nums[i], i) for i in range(n)]
        arr.sort()
```

When `arr.sort()` is called.

```py
# This would be the ideal case as the array is sorted.
[Pair(3, 0), Pair(2, 1), Pair(90, 2), Pair(400, 3), Pair(1, 4)]

Compare Pair(3, 40) and Pair(2, 1):

Since 2 is greater than 2, swap them
[Pair(2, 1),Pair(3, 0),Pair(90, 2), Pair(400, 3), Pair(1, 4)]

Compare Pair(3, 0) and Pair(90, 2):

Since 3 is less than 90, no swap needed.
[Pair(2, 1),Pair(3, 0),Pair(90, 2), Pair(400, 3), Pair(1, 4)]

Compare Pair(90, 2) and Pair(400, 3):
Since 90 is less than 400, no swap needed.
[Pair(2, 1),Pair(3, 0),Pair(90, 2), Pair(400, 3), Pair(1, 4)]

Compare Pair(400, 3) and Pair(90, 2):
Since 400 is greater than 90, swap needed.
[Pair(2, 1),Pair(3, 0),Pair(90, 2),Pair(1, 4),Pair(400, 3)]

### Now, again start from (2,1) and Compare to the rest.

After these steps, the list remains the same: [Pair(1, 4), Pair(2, 1), Pair(3, 0), Pair(90, 2), Pair(400, 3)]


```

4. #### Finding Target:

```py
Initialize Pointers:

left = 0 (Pair(1, 4))
right = 4 (Pair(400, 3))
Comparison Steps:

Calculate the sum of the numbers at left and right pointers:

Pair(1, 4) + Pair(400, 3) = 1 + 400 = 401
Since 401 is greater than 92, we move the right pointer to the left.
Next, calculate the sum:

Pair(1, 4) + Pair(90, 2) = 1 + 90 = 91
Since 91 is less than 92, we move the left pointer to the right.
Next, calculate the sum:

Pair(2, 1) + Pair(90, 2) = 2 + 90 = 92
We found our pair whose sum equals the target!


The pair of indices is [1, 2], representing the original indices of the numbers [2, 90]
```
