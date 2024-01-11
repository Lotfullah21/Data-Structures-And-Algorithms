class Solution:
    def __init__(self):
        self.unique_elements = []

    def removeDuplicates(self, nums: list) -> int:
        for num in nums:
            if num not in self.unique_elements:
                self.unique_elements.append(num)
        for i in range(len(self.unique_elements)):
            nums[i] = self.unique_elements[i]
        return len(self.unique_elements)

    def __str__(self):
        return self.unique_elements

# Example usage
num = Solution()
k = num.removeDuplicates([1, 2, 3, 4,4,4,4,4,4,4,4])
print(num)
print(k)
