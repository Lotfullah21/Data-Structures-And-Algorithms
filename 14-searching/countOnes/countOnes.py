class Solution:
    def countOccurrence(self, arr, n):
        low = 0
        high = len(arr)-1
        while low <= high:
            mid = (low + high) // 2
            # Check if arr[mid] is 1
            if arr[mid] == 1:
                # If arr[mid] is 1, it means all elements to the left of mid are also 1
                # Move to the right subarray
                low = mid + 1
            else:
                # If arr[mid] is 0, move to the right subarray
                high = mid - 1
        # At the end of the loop, low will be the index after the last 1
        return low

def main():
    if __name__ =="__main__":
        array = list(map(int, input("Enter a list: ").split()))
        target = int(input("Enter the target element: "))
        solution = Solution()
        result = solution.countOccurrence(array,12)
        print("count of target is", result)
main()