## Question:

Given an unsorted array of numbers, reorder it in-place such that values at odd indices should be greater than their adjacent indices.

[arr[0]<arr[1]>arr[2], arr[2]<arr[3]>arr[4], arr[4]<arr[5]>arr[6], arr[6]<arr[7]>arr[8]]

## Idea-1:

- sort the array.
- find the maximum among three indices.
- swap it with the odd or middle index
- increment by two indices

```py

class Solution:
    """
    @param nums: A list of integers
    @return: nothing
    """
    def wiggle_sort(self, nums: list[int]) -> list[int]:
        """Returns a new list of integers, that values at odd indices are greater than their adjacent indices.

        Args:
            nums (list[int]): a list of integers.

        Returns:
            list[int]: a list of integers.
        """
        n = len(nums)
        nums.sort()
        for i in range(1,n-1,2):
            maxIndex = max(nums[i-1], nums[i], nums[i+1])
            if maxIndex==nums[i-1]:
                temp = nums[i]
                nums[i] = nums[i-1]
                nums[i-1] = temp
            elif maxIndex == nums[i+1]:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp

nums = [3, 5, 2, 1, 6, 4]
# Output: [[1, 3, 2, 5, 4, 6]
solution = Solution()
solution.wiggle_sort(nums)
print(nums)

```

`Time Complexity:`: `O(NlogN)`, because of sorting the array.
`Space Complexity:`: `O(1)`.

### Note:

The output array always not necessarily to be the same, the condition that should be met is the odd indices values should be greater than the adjacent even indices.

## Idea-2:

- Go through whole array
- check if the current index is even or odd.
- if `i` is even
  - check if `arr[i]<=arr[i+1]`
  - if not
    - swap the `i` with `i+1`
- if `i` is odd
  - check if `arr[i]>arr[i+1]`
  - if not
    - swap the `i` with `i+1` index.

```py

    def wiggle_sort(self, nums: List[int]):
        n = len(nums)
        for i in range(n-1):
            if i%2==0:
                if nums[i]>nums[i+1]:
                    temp = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = temp
            elif i%2!=0:
                if nums[i]<nums[i+1]:
                    temp = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = temp
```

#### Analysis:

`Time Complexity:`: `O(N)`, we are going through all elements.
`Space Complexity:`: `O(1)`.
Count sort algorithm is heavily dependent on maximum element in the array.
