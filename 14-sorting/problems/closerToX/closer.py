class Solution:
    # Function to find the index of element x in the array if it is present.
    def closer(self, arr, n, x):
        low = 0
        high = n - 1

        while low <= high:
            mid = low + (high - low) // 2

            # If x is found at mid
            if arr[mid] == x:
                return mid

            # If element is at mid-1 and mid+1
            if mid > 0 and arr[mid - 1] == x:
                return mid - 1
            if mid < n - 1 and arr[mid + 1] == x:
                return mid + 1

            # If element is in left half
            if arr[mid] > x:
                high = mid - 2
            # If element is in right half
            else:
                low = mid + 2

        # If element is not found
        return -1