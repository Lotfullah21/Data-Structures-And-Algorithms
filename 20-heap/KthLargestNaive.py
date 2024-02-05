class NaiveSolution:
    def findKthLargest(self, nums: list, k: int) -> int:
        "return kth largest element in an array"
        nums.sort()
        print(nums)
        # calculate the index from last
        return nums[len(nums)-k]


nums = [3,2,1,4,6,7,5]
solution = NaiveSolution()
ans = solution.findKthLargest(nums, 3)
print(ans)