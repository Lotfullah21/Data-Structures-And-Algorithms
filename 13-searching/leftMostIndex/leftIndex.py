class Solution:
    def leftIndex(self, arr, k):
        "Returns the right most index of an element"
        low = 0
        high = len(arr)-1
        while low<=high:
            mid = (low+high)//2
            if arr[mid]>k:
                high = mid - 1
            elif arr[mid]<k:
                low = mid + 1
            else:
                if mid == 0 or arr[mid]!=arr[mid-1]:
                    return mid
                else:
                    high = mid - 1
                    

def main():
    if __name__ =="__main__":
        array = list(map(int, input("Enter a list: ").split()))
        target = int(input("Enter the target element: "))
        solution = Solution()
        result = solution.leftIndex(array, target)
        print("the left most index of the target is", result)
main()