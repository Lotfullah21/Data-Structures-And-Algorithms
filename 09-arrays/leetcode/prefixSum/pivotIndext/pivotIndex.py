"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

"""
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Calculate prefix sum array
        pf = [0] * len(nums)
        pf[0] = nums[0]
        for i in range(1, len(nums)):
            pf[i] = pf[i-1] + nums[i]
        
        print(pf)
        n = len(nums)
        indices = []  # List to store potential pivot indices
        
        # Iterate through each index to check if it's a pivot index
        for i in range(1, n):
            left = pf[i-1]  # Sum of elements to the left of the current index
            right = pf[n-1] - pf[i]  # Sum of elements to the right of the current index
            if left == right:
                indices.append(i)  # If sums are equal, the index is a pivot index
        
        # Check if first and last indices can be pivot indices
        # take care of pf[0], do not put pf[i], because it is a corner case.
        # Check if the summation to the left except first element is 0;
        if 0 == pf[n-1]-pf[0]:
            indices.append(0)  # If sum of all elements is zero, first index can be a pivot index.
        # check if summation before the last index ==0;
        if pf[n-2] == 0:
            indices.append(n-1)  # If sum of all elements except the last one is zero, last index can be a pivot index.
        
        if indices:
            return indices[0]  # Return the first pivot index found
        else:
            return -1  # No pivot index found


arr = [1,7,3,6,5,6]
arr = [2,1,-1]
arr = [1,2,3]
solution = Solution()
pivotIndex = solution.pivotIndex(arr)
print(pivotIndex)