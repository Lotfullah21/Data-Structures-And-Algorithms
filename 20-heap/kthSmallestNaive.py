"""Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. 
It is given that all array elements are distinct.

Input:

arr[] = 2 3 4 5 6 7 
K = 3

Output : 4
Explanation :
3rd smallest element in the given 
array is 4.


"""
import heapq
class Solution:
    def kthSmallest(self,arr, k):
        arr.sort()
        return arr[k-1]
nums = [1,2,4,5,6,7,3]
solution = Solution()
ans = solution.kthSmallest(nums, 3)
print(ans)
            