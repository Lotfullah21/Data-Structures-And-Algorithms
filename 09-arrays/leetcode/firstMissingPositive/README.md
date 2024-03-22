<a href="https://leetcode.com/problems/first-missing-positive/description/">leetcode</a>

#### Given an unsorted integer array nums, return the smallest missing positive integer. You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

## Idea-1: Using Sorting Algorithm.

Sorting, itself takes O(NlogN) and checking for each index takes O(N) times, so total `time complexity` will be `O(NlogN)+O(N) = O(NlogN)`.
But, based on the question, the time complexity should not exceed `O(N)`.

## Idea-2: Using Swap Operation
 