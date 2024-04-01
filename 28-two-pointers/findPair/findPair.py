class Solution:
    def findPair(self, arr, size,target):
        i = 0
        j = 1
        arr.sort()
        while i<size and j<size:
            if i!=j and arr[j]-arr[i]==target:
                return True
            elif arr[j]-arr[i]>target:
                i+=1
            else:
                j+=1
        return False
    

# Example usage:
solution = Solution()
nums = [3, 2, 400, 90]
target = 1
size = len(nums)
result = solution.findPair(nums, size,target)
print(result)
