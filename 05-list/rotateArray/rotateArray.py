class Solution:

    def rotateArr(self, arr, K, N):
        # Number of effective rotation, because after len(arr) rotation the array will be same.
        K = K % N 
        # Reverse Whole array
        self.reverse(arr, 0, N-1)
        # Reverse up to first K element.
        self.reverse(arr, 0, K - 1)
        # reverse after Kth element.
        self.reverse(arr, K, N - 1)
        return arr


    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
            

    
solution = Solution()
result = solution.rotateArr(([1, 2, 3, 4, 5]),  2, 5)
print(result)