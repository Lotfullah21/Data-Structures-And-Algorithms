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
        # heap = arr[:k]
        heap = []
        heapq.heapify(heap)
        for i in range(k):
            heapq.heappush(heap,arr[i])   
        heapq.heapify(heap)
        for i in range(k, len(arr)):
            if arr[i]<heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, arr[i])
        print("kth smallest elements",heap)
        for i in range(k-1):
            heapq.heappop(heap)
        return heapq.heappop(heap)
    
nums = [3,2,1,4,6,7,5]
solution = Solution()
ans = solution.kthSmallest(nums, 3)
print("Kth smallest element",ans)
            