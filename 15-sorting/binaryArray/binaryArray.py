class Solution:
    def binSort(self,arr, n):
        left = 0
        right = n - 1
    
        while left <= right:
            if arr[left] == 0:
                left += 1
            else:
                if arr[right] == 1:
                    right -= 1
                else:
                    arr[left], arr[right] = arr[right], arr[left]
                    left += 1
                    right -= 1