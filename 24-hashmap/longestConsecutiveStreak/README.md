## Longest Consecutive Sequence

Given an array of integers, find longest consecutive sequence.

<h3><a href="https://leetcode.com/problems/longest-consecutive-sequence/">leetcode-128</a></h3>.

### Idea-1:

Sort the array to bring all consecutive elements next to each other.
Iterate through the sorted array and count the length of sequence.

- Initialize two variables to keep the longest streak and current streak.
- Check if the elements are not duplicate, if not duplicate
  - If current element is equal to (prev element +1), there is a sequence, add to the length of the sequence,
  - If the above condition is not meet,save the above's streak into longest streak, reset the streak to 1.
- Return the longest streak by returning max of current streak and longest streak

```py
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        currentStreak = 1
        longestStreak = 1
        for i in range(1, len(nums)):
            # If there is no duplicates.
            if nums[i]!=nums[i-1]:
                # If current is == to its previous element.
                if nums[i] == nums[i-1]+1:
                    currentStreak+=1
                else:
                    # Save the longest streak here, if in later iteration there is no longer streak than current longestStreak, it will be our answer
                    longestStreak = max(currentStreak, longestStreak)
                    # Update the current streak to its initial value, because the sequence is started again.
                    currentStreak = 1
        return max(longestStreak, currentStreak)
```

### Analysis:

`Time Complexity`: Sorting of an array takes `O(NlogN)` and using iterating thorough all elements using for loop takes `O(N)`. In total `O(NlogN)+O(N)`, not considering smaller terms, it becomes `O(NlogN)`.
`Space Complexity`: No additional space is used except variable spaces, so `O(1)`.

## Idea-2:

Save all the elements inside a set.

To know whether an element is starting point of a sequence, check if a number one unit smaller than itself exists.

- Iterate through elements in the set.
  - Check if the current number is starting point of a sequence, if so.
  - Start counting the streak by comparing if one number larger than itself exists, if exist:
    - Increment the current streak (length of the sequence)

```py
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestStreak = 0
        for num in numSet:
            # Check if it is starting point of a sequence
            if num-1 not in numSet:
                # Update the streak
                currentStreak = 1
                while num+1 in numSet:
                    # If num+1 exists, increment the streak and num
                    currentStreak+=1
                    num+=1
                # Save the longest streak
                longestStreak = max(longestStreak, currentStreak)
        return longestStreak


```

### Analysis:

`Time Complexity`: `O(1)` to look up for an element in the set and `O(N)` to iterate through all elements, so `O(N)`.
`Space Complexity`: `O(N)` to store unique elements in the set,`N` is number of elements in the input array.
