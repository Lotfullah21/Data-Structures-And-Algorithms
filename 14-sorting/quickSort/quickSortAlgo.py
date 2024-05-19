import random
class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,start,end):
        if start>=end:
            return 
        # P is the correct indices of the left most element after re-arranging.
        p = self.reArrangeSubArray(arr, start, end)
        self.quickSort(arr, start, p-1)
        self.quickSort(arr,p+1, end)
    
    def reArrangeSubArray(self,arr: list,start: int,end: int) -> list:
        """Moves the smaller element to the left of start and larger elements to the right of the start.

        Args:
            arr (list): a list of integers.
            start (int): 
            end (int): _description_

        Returns:
            _type_: _description_
        """
        # Because of the fact the quick sort is worst when array is sorted, so lets choose the starting point randomly.
        start = random.randint(start, end)
        p1 = start+1
        p2 = end
        while p1<=p2:
            if arr[p1]<=arr[start]:
                p1+=1
            elif arr[p2]>arr[start]:
                p2-=1
            else:
                temp = arr[p1]
                arr[p1] = arr[p2]
                arr[p2] = temp
                p1+=1
                p2-=1
        temp = arr[start]
        arr[start] = arr[p2]
        arr[p2] = temp
        # P2 is the correct index after re-arranging the list.
        return p2
    
arr = [10, 4, 5, 17, 6, 1, 29, 18, 2, 11, -1]
solution = Solution()
solution.quickSort(arr, 0, len(arr)-1)
print("Sorted Array: ",arr)
