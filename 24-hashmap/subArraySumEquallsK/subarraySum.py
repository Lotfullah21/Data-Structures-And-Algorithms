class Solution:
    #Function to count the number of subarrays which adds to the given k.
    def subarraySum(self,nums, k):
        #Your code here
        pf = self.prefix(nums)
        ans = 0
        n = len(nums)
        countMap = {0:1}
        for ep in range(n):
            diff = pf[ep]-k
            # If answer is found, Increment it by getting the value.
            if diff in countMap:
                ans+=countMap[diff]
            # Update the count map with the pf[ep] regardless of the above condition whether the ans is found or not, because it might be a potential answer.
            if pf[ep] not in countMap: 
                countMap[pf[ep]] = 1
            else:
                # If the element is already there, add to its count.
                countMap[pf[ep]]+=1
        return ans
           
           
    def prefix(self, nums):
        pf = [0]*len(nums)
        pf[0]=0
        for i in range(len(nums)):
            pf[i] = pf[i-1]+nums[i]
        return pf

    
solution = Solution()
arr = [1,2,3,4,5]
k=2
print(solution.subarraySum(arr,k))