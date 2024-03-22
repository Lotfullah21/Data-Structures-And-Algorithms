class Solution:
    def countSort(self,arr):
        n = len(arr)
        # Find the maximum
        maxELe = float("-inf")
        for i in range(n):
            maxELe = max(arr[i], maxELe)
        # Create an array of size maximum
        count = [0 for _ in range(maxELe+1)]
        print(count)
        # Find the occurrence of each element.
        for i in range(n):
            val = arr[i]
            count[val] +=1
        k = 0
        # Fill the original array with elements inside count array.
        for i in range(maxELe+1):
            cnt = count[i]
            for _ in range(cnt):
                arr[k] = i
                k+=1
                
                

arr = [0, 3, 1, 1, 0, 4, 6, 7, 3, 1]
solution = Solution()
solution.countSort(arr)
print(arr)