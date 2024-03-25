class Solution:

    def rotateArr(self, arr, D, N):
        D = D % N  # Adjust D to be within the range of the array
        self.reverse(arr, 0, D - 1)
        self.reverse(arr, D, N - 1)
        self.reverse(arr, 0, N - 1)
        return arr


    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
            

    
solution = Solution()
result = solution.rotateArr(([1, 2, 3, 4, 5]),  2, 5)
print(result)