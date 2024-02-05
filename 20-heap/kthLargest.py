import heapq
class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        heap = []
        for i in range(0,k):
            heap.append(nums[i])
            print("heap",heap)
        heapq.heapify(heap)
        print("min-heap",heap)
        for i in range(k,len(nums)):
            if heap[0]<nums[i]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])
                print(heap)
        return heap[0]

nums = [3,2,1,4,6,7,5]
solution = Solution()
ans = solution.findKthLargest(nums, 3)
print(ans)