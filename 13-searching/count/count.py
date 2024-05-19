class Solution:
    def countOccurrence(self, arr, k):
        
        firstOccurrence = self.leftIndex(arr, k)
        if firstOccurrence==-1:
            return 0
        else:
            print(firstOccurrence, self.rightIndex(arr, k))
            return self.rightIndex(arr, k) - firstOccurrence + 1
        
    def rightIndex(self, arr, k):
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
                if mid == len(arr)-1 or arr[mid]!=arr[mid+1]:
                    return mid
                else:
                    low = mid + 1
        return -1
        
        
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
        return -1
    
    
def main():
    if __name__ =="__main__":
        array = list(map(int, input("Enter a list: ").split()))
        target = int(input("Enter the target element: "))
        solution = Solution()
        result = solution.countOccurrence(array, 12)
        print("count of target is", result)
main()