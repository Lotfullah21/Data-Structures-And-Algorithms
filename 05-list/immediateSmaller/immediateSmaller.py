class Solution:
    def immediateSmaller(self,arr,n,x):
        "Returns the largest element from a list."
        # Check list is empty
        maxMin = x
        firstMin = float("-inf")
        if not list:
            return "LIST EMPTY"
        for i in range(len(arr)):
            if arr[i]<maxMin and arr[i]>firstMin:
                firstMin = arr[i]
        return firstMin
    
    
solution = Solution()
result = solution.immediateSmaller([1, 2, 18, 3, 3,4], 3,19)
print(result)