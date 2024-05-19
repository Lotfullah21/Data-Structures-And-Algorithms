class Solution:
    """
    @param nums: A list of integers
    @return: nothing
    """
    def wiggle_sort(self, nums: list[int]) -> list[int]:
        """Returns a new list of integers, that values at odd indices are greater than their adjacent indices.

        Args:
            nums (list[int]): a list of integers.

        Returns:
            list[int]: a list of integers.
        """
        n = len(nums)
        for i in range(n-1):
            if i%2==0:
                if nums[i]>nums[i+1]:
                    temp = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = temp
            else:
                if nums[i]<nums[i+1]:
                    temp = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = temp
                                
nums = [3, 5, 2, 1, 6, 4]
# Output: [1, 6, 2, 5, 3, 4]
solution = Solution()
solution.wiggle_sort(nums)
print(nums)