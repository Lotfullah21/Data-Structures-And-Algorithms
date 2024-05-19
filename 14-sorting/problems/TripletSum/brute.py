class Solution:
    def findTriplet(self, arr: list, X: int) -> list:
        """Checks if tree distinct elements can sum up to give X

        Args:
            arr (list): list of numbers
            X   (int) : a value that we are looking to get the summation elements for.

        Returns:
            list: a boolean and indices of the integers that sum up to give x, if not found, False.
        """
        nums = []
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if arr[i]+arr[j]+arr[k]==X:
                        nums.append((arr[i],arr[j],arr[k]))
                        return True, nums
                    
        return False
    
    
    
solution = Solution()
arr = [2, 4, 6, 12, 12,3,4,5,7,8,9,9,90, 12,32,43,13,4,5,32,54,32,5,]
result = solution.findTriplet(arr,12)
print("result", result)
        
        
        