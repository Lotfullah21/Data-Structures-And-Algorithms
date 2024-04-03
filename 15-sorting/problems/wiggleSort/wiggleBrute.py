class Solution:
    """
    @param nums: A list of integers
    @return: nothing
    """
    def wiggleSort(self, nums: list[int]) -> list[int]:
        """Returns a new list of integers, that values at odd indices are greater than their adjacent indices.

        Args:
            nums (list[int]): a list of integers.

        Returns:
            list[int]: a list of integers.
        """
        n = len(nums)
        nums.sort()
        for i in range(1,n-1,2):
            maxIndex = max(nums[i-1], nums[i], nums[i+1])
            if maxIndex==nums[i-1]:
                temp = nums[i]
                nums[i] = nums[i-1]
                nums[i-1] = temp
            elif maxIndex == nums[i+1]:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp

nums = [3, 5, 2, 1, 6, 4]
# Output: [[1, 3, 2, 5, 4, 6]
solution = Solution()
solution.wiggleSort(nums)
print(nums)