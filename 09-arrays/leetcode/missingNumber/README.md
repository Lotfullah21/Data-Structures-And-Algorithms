## Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

<h2><a href="https://leetcode.com/problems/missing-number/">leetcode-268</a></h2>

## Using sorting

- Sort the list.
- Iterate through the list and check if the current index matches the current number.
- If a mismatch is found, return the index.
- If no mismatch is found, return len(nums) because it means the missing number is the largest number, n.

## Use First N Natural Numbers Formula

## Analysis:

Both Time complexity and space complexity is `O(1)`.
