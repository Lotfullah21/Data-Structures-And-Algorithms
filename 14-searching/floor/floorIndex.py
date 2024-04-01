class Solution:
    def findFloor(self, arr, N, X):
        low = 0
        high = len(arr) - 1
        ans = float("-inf")
        if X<arr[0]:
            return -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == X:
                return mid
            elif arr[mid] < X:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
