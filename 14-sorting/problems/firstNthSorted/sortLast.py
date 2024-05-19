class Solution:
    def sortFirstNth(self, arr: list) -> list:
        n = len(arr)
        for j in range(n-2, -1, -1):
            if arr[j]>arr[j+1]:
                print(arr[j-1],arr[j])
                temp = arr[j]
                arr[j] = arr[j+1]        
                arr[j+1] = temp
        return arr
solution = Solution()
arr = [1, 2, 3, 4 ,5, 0]
sortedArray = solution.sortFirstNth(arr)
print(sortedArray)