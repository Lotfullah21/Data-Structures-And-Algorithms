class Solution:
    def sameDifference(self, arr):
        ans = 0
        countFreq = {}
        for i in range(len(arr)):
            diff = arr[i]-i
            if diff in countFreq:
                ans+=countFreq[diff]
                countFreq[diff]+=1
            else:
                countFreq[diff] = 1
        print(ans, countFreq)
        return ans


arr = [3, 5, 1, 4, 6, 6]
solution = Solution()
solution.sameDifference(arr)