import heapq
class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        "return kth largest element in an array"
        # in the heap list keep k largest elements
        heap = []
        for i in range(0,k):
            # add k elements to the heap
            heap.append(nums[i])
            print("heap",heap)
        # convert it to a priority queue
        heapq.heapify(heap)
        print("min-heap",heap)
        for i in range(k,len(nums)):
            # check if the first element in the heap is larger than the array's element.
            if heap[0]<nums[i]:
                # if so, remove the first element.
                heapq.heappop(heap)
                # add the larger element to the array
                heapq.heappush(heap, nums[i])
                print(heap)
        return heap[0]

nums = [3,2,1,4,6,7,5]
solution = Solution()
ans = solution.findKthLargest(nums, 4)
print(ans)