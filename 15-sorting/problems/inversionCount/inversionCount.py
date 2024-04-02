class Solution:
    
    def inversionCount(self, arr,n):
        self.ans = 0
        self.merge_sort(arr, 0, len(arr) - 1)
        return self.ans    
    
      # Using merge function, the merge_sort can be done.
    def merge_sort(self, arr, start, end):
        # base case
        if start==end:
            return
        else:
            mid = (start + end) // 2
            self.merge_sort(arr, start, mid)
            self.merge_sort(arr, mid + 1, end)
            self.merge(arr, start, mid, end)
        # return arr
    
    def merge(self ,arr,start: int, mid: int, end: int) -> list:
        p1 = start
        p2 = mid+1
        p3 = 0
        # ans  = 0 
        # Take care of (end-start+1), because start-end+1 is different.
        temp = [[] for _ in range(end-start+1)]
        while(p1<=mid and p2<=end):
            if arr[p1]<=arr[p2]:
                temp[p3] = arr[p1]
                p1+=1
                p3+=1
                
            else:
                temp[p3] = arr[p2]
                p2+=1
                self.ans += (mid - p1 + 1)
                p3+=1
        while (p1<=mid):
            temp[p3]=arr[p1]
            p1+=1
            p3+=1
        while (p2<=end):
            temp[p3] = arr[p2]
            p2+=1
            p3+=1       
        # Copy the temp array elements into main array.
        n = end - start + 1 
        for i in range(n):
            j = start + i
            arr[j] = temp[i]
        # return ans

arr = [3, 4, -5, 0, 1, 20, 11, 9, 4, 7, 13, -4,0]
solution = Solution()
new_array = solution.inversionCount(arr,len(arr)-1)
print(new_array)