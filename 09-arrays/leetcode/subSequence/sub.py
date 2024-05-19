class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N = len(nums)
        total = 1<<N
        ans = []
        print(total)
        for i in range(total):
            temp = []
            for j in range(0, N):
                if self.checkBit(i, j)==True:
                    temp.append(nums[j])
            ans.append(temp)
        return ans

    def checkBit(self, i, j):
        if i&(1<<j)!=0:
            return True
        
        
nums = [2, 4, 5]
solution = Solution()
result = solution.subsets(nums)
print("all subsequences of list",nums,"are =",result)