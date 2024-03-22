import random
class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        if low>=high:
            return 
        p = self.reArrangeSubArray(arr, low, high)
        self.quickSort(arr, low, p-1)
        self.quickSort(arr,p+1, high)
    
    def reArrangeSubArray(self,arr,low,high):
        # start = random.randint(low, high)
        p1 = low
        p2 = high
        while p1<=p2:
            if arr[p1]<=arr[low]:
                p1+=1
            elif arr[p2]>arr[low]:
                p2-=1
            else:
                temp = arr[p1]
                arr[p1] = arr[p2]
                arr[p2] = temp
                p1+=1
                p2-=1
        temp = arr[low]
        arr[low] = arr[p2]
        arr[p2] = temp
        return p2
    
arr = [10, 4, 5, 17, 6, 1, 29, 18, 2, 11, -1]
solution = Solution()
solution.quickSort(arr, 0, len(arr)-1)
print("Sorted Array: ",arr)
