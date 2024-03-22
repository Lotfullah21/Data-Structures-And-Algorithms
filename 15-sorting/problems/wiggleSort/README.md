## Question:

Given an unsorted array nums, reorder it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]....`.

## Idea-1:

- sort the array.
- find the maximum among three indices.
- swap it with the odd or middle index
- increment by two indices

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
