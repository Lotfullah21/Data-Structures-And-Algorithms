# Problem Statement

Given an array of integers nums and an integer b, find the minimum number of swaps required to bring all elements less than or equal to b together in a contiguous subarray. The swaps can only be made between any two elements in the array.

## Approach

#### Calculate Window Size:

The sliding window size k is calculated by counting the number of elements less than or equal to b in nums.

#### Initial Count:

The initial count c of elements less than or equal to b in the first window of size k is calculated.

#### Sliding Window:

The while loop updates the count c by adding the element at the end of the window (nums[e]) if it is less than or equal to b and subtracting the element at the start of the window (nums[s-1]) if it is less than or equal to b.

####

Update Minimum Swaps: The minimum number of swaps needed (ans) is updated by comparing the current number of swaps needed (k - c).

`Time Complexity`: `O(N)`.
