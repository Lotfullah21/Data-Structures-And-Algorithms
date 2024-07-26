# Two Sum

<h2><a href="https://leetcode.com/problems/two-sum/description/">leetcode</a></h2>
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order

## Dictionary for Indexes:

numsToIdx dictionary is used to store the number and its index.

## Loop through Elements:

For each element, calculate the unknown value needed to reach the target (unknown = target - num).

## Check for Complement:

If the unknown value is found in the dictionary, return the indices.
If not, store the current number with its index in the dictionary.

## Return Result:

If no valid pair is found, return an empty list.

## Example

Input: nums = [2, 7, 11, 15], target = 9

- Initialize numsToIdx as an empty dictionary.

- Iterate through nums:

#### Iteration 1:

- idx = 0, num = 2
- Calculate unknown = target - num = 9 - 2 = 7
- unknown (7) is not in numsToIdx
- Add num and its index to numsToIdx: {2: 0}

#### Iteration 2:

- idx = 1, num = 7
- Calculate unknown = target - num = 9 - 7 = 2
- unknown (2) is in numsToIdx, its index is 0
- Return indices [0, 1]

Time Complexity = `O(N)` and space complexity is also `O(N)`.
