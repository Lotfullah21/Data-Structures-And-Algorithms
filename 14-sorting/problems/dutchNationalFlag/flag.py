
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
        arr.sort()
        n = len(arr)
        for i in range(n-2):
            left = i+1
            right = n-1
            while left<right:
                if arr[i]+arr[left]+arr[right]==X:
                    nums.append((arr[i],arr[left],arr[right]))
                    return True, nums
                elif arr[i]+arr[left]+arr[right]<X:
                    left+=1
                else:
                    right-=1
            
                    
        return False
    
    
    
solution = Solution()
arr = [2, 4, 6, 12, 12,3,4,5,7,8,9,9,90, 12,32,43,13,4,5,32,54,32,5,64,2,3232,3232,3232,22,4,2,24,3,6,102]
result = solution.findTriplet(arr,111)
print("result", result)
        
        
        