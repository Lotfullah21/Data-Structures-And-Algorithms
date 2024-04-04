class Solution:
    
    # Function to sort the array according to highest value after dividing each element by K.
    def sortDiv(self, a, k):
        
        a= sorted(a,reverse=True,key = lambda x :(abs(x//k)) )         
        return a

arr = [1,2,3,4,6]
k = 2
solution = Solution()
result = solution.sortDiv(arr, k)
print(result)