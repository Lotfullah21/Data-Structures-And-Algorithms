```py
class Solution:

    # Function to sort the array according to highest value after dividing each element by K.
    def sortDiv(self, a, k):
        # Custom sort function
        def custom_sort(x):
            return x/k
        # Sort the array based on custom sort
        a.sort(key=custom_sort, reverse=True)

        return a


arr = [1,2,3,4,6]
k = 2
solution = Solution()
result = solution.sortDiv(arr, k)
print(result)
```
