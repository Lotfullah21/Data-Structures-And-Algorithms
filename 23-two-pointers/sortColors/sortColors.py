class Solution:
    def sortColors(self, nums):
        n = len(nums)
        i = 0
        j = 0
        k = n - 1
        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1
            elif nums[j] == 1:
                j += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
                
        return nums

arr = [0,1,1,1,0,1,1,2,1,2,2]
solution = Solution()
result = solution.sortColors(arr)
print(result)