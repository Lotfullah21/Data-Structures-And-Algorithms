class Solution:
    def subsets(self, nums):
        n = len(nums)
        totalSequence = 1 << n #2**n
        answer = []

        for i in range(totalSequence):
            print(i)
            temp = [nums[j] for j in range(n) if self.checkBit(i, j)]
            answer.append(temp)

        return answer

    def checkBit(self, n, i):
        return (n & (1 << i)) != 0

# Example usage:
solution = Solution()
nums = [1,2]
result = solution.subsets(nums)

# Print the result
for subset in result:
    print(subset)
